/* Ask Canary: the corner canary and its chat panel (Streamlit v2 component; data from canary.dashboard.chatbird).
   The DOM is built once; every data change re-renders its contents. Visitor and model text is only ever set with
   textContent. Python can't update mid-run, so on send the panel shows a local "thinking" state until data with
   a new nonce arrives. */
const SVGNS = 'http://www.w3.org/2000/svg';
const OPENED = 'canary-chat-opened';
const FIRST_GAP_MS = 4000;     // hop and tweet this often until the first open this visit
const LATER_GAP_MS = 60000;    // then about once a minute
const HOP_MS = 1000;
const WAIT_LIMIT_MS = 540000;  // give up the local thinking state if no answer ever arrives: 9 minutes, past
                               // the Python worst case of 2 attempts x 4 calls x the 60 s client timeout

function wasOpened() { try { return window.sessionStorage.getItem(OPENED) === '1'; } catch (e) { return false; } }
function rememberOpened() { try { window.sessionStorage.setItem(OPENED, '1'); } catch (e) { /* storage blocked */ } }
const calm = () => !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

const el = (tag, cls, text) => {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (text !== undefined) e.textContent = text;
  return e;
};

/* the pixel canary from the sprite grid; asleep, the eye pixel K becomes a 2-pixel navy line */
const birdSvg = (sprite, asleep) => {
  const grid = sprite.grid, pal = sprite.palette;
  const svg = document.createElementNS(SVGNS, 'svg');
  svg.setAttribute('viewBox', '0 0 ' + grid[0].length + ' ' + grid.length);
  svg.setAttribute('shape-rendering', 'crispEdges');
  svg.setAttribute('aria-hidden', 'true');
  svg.setAttribute('focusable', 'false');
  const px = (x, y, w, fill) => {
    const r = document.createElementNS(SVGNS, 'rect');
    r.setAttribute('x', x); r.setAttribute('y', y); r.setAttribute('width', w); r.setAttribute('height', 1);
    r.setAttribute('fill', fill); svg.appendChild(r);
  };
  let eye = null;
  grid.forEach((row, y) => [...row].forEach((ch, x) => {
    if (!pal[ch]) return;
    if (ch === 'K' && asleep) { eye = [x, y]; px(x, y, 1, pal.Y); } else px(x, y, 1, pal[ch]);
  }));
  if (eye) px(eye[0], eye[1], 2, pal.K);
  return svg;
};

const sig = (m) => JSON.stringify([m.who, m.text, m.source || '', m.lookups || []]);

function renderMessage(m, ctx) {
  const row = el('div', m.who === 'me' ? 'msg me' : 'msg');
  if (m.who !== 'me') {
    const av = el('span', 'av');
    av.appendChild(birdSvg(ctx.sprite, ctx.asleep));
    row.appendChild(av);
  }
  const box = el('div', 'text');
  box.appendChild(el('p', 'body', m.text));
  if (m.source) box.appendChild(el('span', 'cite', m.source));
  if (m.lookups && m.lookups.length) box.appendChild(el('span', 'looked', ctx.lookedUp + ': ' + m.lookups.join(' · ')));
  row.appendChild(box);
  return row;
}

const build = (parent) => {
  const root = el('div', 'cb');
  const panel = el('section', 'panel');
  panel.hidden = true;
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-labelledby', 'cb-title');
  const head = el('header', 'head');
  const hbird = el('span', 'hbird');
  const title = el('h2', 'title'); title.id = 'cb-title';
  const close = el('button', 'x', 'X'); close.type = 'button';
  head.append(hbird, title, close);
  const msgs = el('div', 'msgs');
  msgs.setAttribute('role', 'log');
  msgs.setAttribute('aria-live', 'polite');
  const form = el('form', 'ask');
  const label = el('label', 'sr'); label.htmlFor = 'cb-q';
  const input = el('input'); input.id = 'cb-q'; input.type = 'text'; input.autocomplete = 'off';
  const send = el('button', 'send'); send.type = 'submit';
  form.append(label, input, send);
  const foot = el('p', 'foot');
  panel.append(head, msgs, form, foot);

  const tweet = el('span', 'tweet');
  tweet.setAttribute('aria-hidden', 'true');
  const launch = el('button', 'launch'); launch.type = 'button';
  launch.setAttribute('aria-expanded', 'false');
  launch.setAttribute('aria-haspopup', 'dialog');
  const bubble = el('span', 'bubble');
  const word = el('span', 'word'), wordPhone = el('span', 'word-phone'), dot = el('span', 'dot');
  bubble.append(word, wordPhone, dot);
  const bird = el('span', 'bird'), sprite = el('span', 'sprite'), zs = el('span', 'zs');
  zs.setAttribute('aria-hidden', 'true');
  zs.append(el('i', 'z1', 'z'), el('i', 'z2', 'z'), el('i', 'z3', 'Z'));
  bird.append(sprite, zs);
  launch.append(bubble, bird);
  root.append(panel, tweet, launch);
  parent.appendChild(root);

  const S = { root, panel, hbird, title, close, msgs, form, label, input, send, foot, tweet, launch, word, wordPhone,
              sprite, open: false, thinking: null, data: null, api: null, sleepy: null,
              next: Date.now() + (wasOpened() ? LATER_GAP_MS : FIRST_GAP_MS) };
  root._cb = S;

  const openPanel = () => {
    S.open = true; panel.hidden = false; root.classList.add('open'); root.classList.remove('hop');
    launch.setAttribute('aria-expanded', 'true');
    rememberOpened();
    msgs.scrollTop = msgs.scrollHeight;
    (input.disabled ? close : input).focus();
  };
  const closePanel = () => {
    S.open = false; panel.hidden = true; root.classList.remove('open');
    launch.setAttribute('aria-expanded', 'false');
    S.next = Date.now() + LATER_GAP_MS;
    launch.focus();
  };
  const ask = (text) => {
    const q = (text || '').trim();
    if (!q || S.thinking || !S.data || !S.data.can_ask || !S.api) return;
    S.thinking = { question: q, nonce: S.data.nonce };
    S.thinking.timer = setTimeout(() => { S.thinking = null; render(S); }, WAIT_LIMIT_MS);
    input.value = '';
    render(S);
    S.api.setTriggerValue('question', q);
  };
  S.ask = ask;
  launch.addEventListener('click', () => (S.open ? closePanel() : openPanel()));
  close.addEventListener('click', closePanel);
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && S.open) { e.preventDefault(); e.stopPropagation(); closePanel(); }
  });
  form.addEventListener('submit', (e) => { e.preventDefault(); ask(input.value); });

  /* hop and tweet: often until the first open this visit, then about once a minute; never while open,
     asleep or under reduced motion */
  const tick = setInterval(() => {
    if (!root.isConnected) { clearInterval(tick); return; }
    if (S.open || calm() || !S.data || S.data.state !== 'awake' || Date.now() < S.next) return;
    S.next = Date.now() + (wasOpened() ? LATER_GAP_MS : FIRST_GAP_MS);
    root.classList.add('hop');
    setTimeout(() => root.classList.remove('hop'), HOP_MS);
  }, 500);
  return S;
};

const render = (S) => {
  const d = S.data, t = d.text, asleep = d.state === 'asleep';
  if (S.thinking && d.nonce !== S.thinking.nonce) { clearTimeout(S.thinking.timer); S.thinking = null; }
  S.root.dataset.state = d.state;
  S.root.classList.toggle('thinking', !!S.thinking);
  if (S.sleepy !== asleep) {  // redraw the sprites only when the eye changes
    S.sleepy = asleep;
    S.sprite.replaceChildren(birdSvg(d.sprite, asleep));
    S.hbird.replaceChildren(birdSvg(d.sprite, asleep));
  }
  S.word.textContent = d.bubble;
  S.wordPhone.textContent = d.bubble_phone;
  S.tweet.textContent = t.tweet;
  S.title.textContent = t.title;
  S.launch.setAttribute('aria-label', asleep ? t.open_asleep : t.open);
  S.close.setAttribute('aria-label', t.close);
  S.label.textContent = t.label;
  S.input.placeholder = t.placeholder;
  S.input.maxLength = d.max_chars;
  S.send.textContent = t.button;
  S.foot.textContent = d.footer;
  const hadInput = !S.input.disabled;
  S.input.disabled = !d.can_ask;
  S.send.disabled = !d.can_ask || !!S.thinking;

  const ctx = { sprite: d.sprite, asleep, lookedUp: t.looked_up };
  if (S.sigs === undefined || S.drawnAsleep !== asleep) {  // first draw, or the avatars' eyes changed
    S.drawnAsleep = asleep; S.sigs = []; S.chipsKey = ''; S.msgs.replaceChildren();
  }
  /* the transcript only grows, so keep the rows already drawn and append the new ones: no aria-live
     re-announcing and no scroll jump when an unrelated rerun pushes the same data */
  const sigs = d.messages.map(sig);
  let keep = 0;
  while (keep < S.sigs.length && keep < sigs.length && S.sigs[keep] === sigs[keep]) keep++;
  const added = sigs.length - keep;
  const local = [...S.msgs.querySelectorAll('.local')];
  if (added > 0 || keep < S.sigs.length || !S.thinking) local.forEach((n) => n.remove());
  [...S.msgs.querySelectorAll('.msg:not(.local)')].slice(keep).forEach((n) => n.remove());
  d.messages.slice(keep).forEach((m) => S.msgs.appendChild(renderMessage(m, ctx)));
  S.sigs = sigs;
  let grew = added > 0;

  const chipsKey = S.thinking ? '' : JSON.stringify(d.starters);
  const first = S.msgs.querySelector('.msg:not(.local) .text');
  if (first && (chipsKey !== S.chipsKey || keep === 0)) {
    S.chipsKey = chipsKey;
    const old = first.querySelector('.chips');
    if (old) old.remove();
    if (d.starters.length && !S.thinking) {
      const chips = el('div', 'chips');
      d.starters.forEach((q) => {
        const c = el('button', 'chip', q); c.type = 'button';
        c.addEventListener('click', () => S.ask(q));
        chips.appendChild(c);
      });
      first.appendChild(chips);
    }
  }
  if (S.thinking && !S.msgs.querySelector('.local')) {
    const me = renderMessage({ who: 'me', text: S.thinking.question }, ctx);
    const wait = renderMessage({ who: 'bird', text: t.thinking }, ctx);
    me.classList.add('local'); wait.classList.add('local', 'wait');
    S.msgs.append(me, wait);
    grew = true;
  }
  if (grew) S.msgs.scrollTop = S.msgs.scrollHeight;
  if (S.open && hadInput && S.input.disabled) S.close.focus();  // keep focus in the panel when asking ends
};

export default function (component) {
  const { parentElement, data } = component;
  if (!data || !data.sprite) return;
  const S = (parentElement.querySelector('.cb') || {})._cb || build(parentElement);
  S.api = component;
  S.data = data;
  render(S);
}
