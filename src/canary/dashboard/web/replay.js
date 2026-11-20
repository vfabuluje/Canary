/* Canary report replay (v6 engine, data-driven). Reads window.CANARY (built by canary.dashboard.replay):
   screen 1 plays the six pipeline scenes, about 5.5 s each; screen 2 is the report with hover/tap tips. */
(function () {
  const C = window.CANARY;
  const MEMBERS = ['rule', 'trend', 'peer', 'check', 'lead'];
  const STAGE_W = 640, STAGE_H = 300, BORDER = 8;
  try { if (window.self !== window.top) document.documentElement.classList.add('embedded'); }
  catch (e) { document.documentElement.classList.add('embedded'); }

  const $ = id => document.getElementById(id);
  function el(tag, cls, text) { const e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function scaled(c, s) { c.style.width = (c.width * s) + 'px'; c.style.height = (c.height * s) + 'px'; return c; }
  // a member = its look (sprites.js) + its name, badge and role (payload)
  const T = {};
  MEMBERS.forEach(id => { T[id] = Object.assign({}, LOOKS[C.cast][id], C.team[id]); });
  function badge(m) { return el('span', 'tag ' + (m.badge === 'AI' ? 'ai' : 'rule'), m.badge); }

  /* ---------- scaling: the 640 x 300 stage fills whatever width the scene gets ---------- */
  const sceneBox = $('scene'), stage = $('stage');
  function fit() {
    const k = Math.max(sceneBox.clientWidth, 1) / STAGE_W;
    stage.style.transform = 'scale(' + k + ')';
    sceneBox.style.height = Math.round(STAGE_H * k + BORDER) + 'px';
  }
  window.addEventListener('resize', fit);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(sceneBox);

  /* ---------- scene pieces ---------- */
  let step = 0, timer = null, pending = [];
  function later(fn, ms) { pending.push(setTimeout(fn, ms)); }
  function clearPending() { pending.forEach(clearTimeout); pending = []; clearInterval(timer); }

  function actor(m, x, working) {
    const a = el('div', 'actor' + (working ? ' go' : '')); a.style.left = x + 'px';
    a.appendChild(scaled(avatar(m), m.bb ? 8 : 10));
    if (m.icon && m.icon !== 'stamp') {
      const t = el('div', 'prop tool'); t.appendChild(scaled(prop(m.icon), 5)); t.style.left = '118px'; t.style.top = '70px'; a.appendChild(t);
    }
    return a;
  }
  function ball(x, y, dribbling) { const b = el('div', 'ball' + (dribbling ? ' dribble' : '')); b.style.left = x + 'px'; b.style.top = y + 'px'; b.appendChild(prop('ball')); return b; }
  function bench(x) { // Peer sits this one out
    const b = el('div', 'prop'); b.appendChild(scaled(prop('bench'), 7)); b.style.left = (x - 8) + 'px'; b.style.bottom = '14px'; stage.appendChild(b);
    const p = actor(T.peer, x, false); p.style.bottom = '30px'; stage.appendChild(p);
    const s = el('div', 'sign', C.text.bench_sign); s.style.left = (x - 4) + 'px'; s.style.top = '28px'; stage.appendChild(s);
  }
  function checks(numbers, note, left) {
    const c = el('div', 'checks'); c.style.left = left + 'px';
    const rows = numbers.length ? numbers : [null];
    rows.forEach((n, i) => {
      const d = el('div');
      if (n === null) d.appendChild(el('b', '', C.text.checked_summary));
      else { d.appendChild(document.createTextNode(n + ' ')); d.appendChild(el('b', '', C.text.real)); }
      d.style.animationDelay = (0.3 + i * 0.45) + 's'; c.appendChild(d);
    });
    if (note) { const r = el('div', 'retry', '↩ ' + note); r.style.animationDelay = (0.3 + rows.length * 0.45) + 's'; c.appendChild(r); }
    return c;
  }

  const SCENES = {
    numbers() {
      const p = el('div', 'papers');
      C.papers.forEach((w, i) => { const sp = el('span', '', w); sp.style.animationDelay = (i * 0.25) + 's'; p.appendChild(sp); });
      stage.appendChild(p);
    },
    rule() {
      if (C.cast === 'detective') { const st = el('div', 'prop'); st.appendChild(scaled(prop('stamp'), 9)); st.style.left = '290px'; st.style.bottom = '30px'; stage.appendChild(st); }
      else stage.appendChild(actor(T.rule, 40, true));
      const b = el('div', 'bigstamp ' + C.stamp.kind, C.stamp.word);
      if (C.stamp.lines.length) { const l = el('div', 'lines'); C.stamp.lines.forEach(t => l.appendChild(el('div', '', t))); b.appendChild(l); }
      if (C.cast === 'basketball') b.style.marginLeft = '-90px';
      stage.appendChild(b); later(() => b.classList.add('show'), 700);
    },
    specialists() {
      stage.appendChild(actor(T.trend, 70, true));
      if (C.cast === 'basketball') stage.appendChild(ball(210, 190, true));
      if (C.bench) bench(400);
      else { stage.appendChild(actor(T.peer, 370, true)); if (C.cast === 'basketball') stage.appendChild(ball(338, 190, true)); }
    },
    check(s) {
      stage.appendChild(actor(T.check, 40, true));
      stage.appendChild(checks(C.checks.specialists, s.note, 200));
    },
    lead(s) { // the lead writes; then, in the same scene, the fact checker checks the summary
      const lead = actor(T.lead, 240, true); stage.appendChild(lead);
      const b = C.cast === 'basketball' ? ball(372, 190, true) : null; if (b) stage.appendChild(b);
      const paper = el('div', 'paper'); paper.style.left = '420px'; for (let i = 0; i < 4; i++) paper.appendChild(el('i'));
      if (C.cast === 'detective') stage.appendChild(paper);
      later(() => {
        if (b) b.remove(); paper.remove();
        lead.classList.remove('go'); lead.style.left = '470px';
        const chk = actor(T.check, 20, true); chk.classList.add('hide'); stage.appendChild(chk);
        later(() => chk.classList.remove('hide'), 30);
        stage.appendChild(checks(C.checks.summary, s.note, 170));
      }, Math.round(C.scene_ms * 0.45));
    },
    done() {
      if (C.cast === 'basketball') {
        stage.appendChild(actor(T.trend, 30, false)); stage.appendChild(actor(T.lead, 230, false));
        if (C.bench) bench(450); else stage.appendChild(actor(T.peer, 430, false));
        const h = el('div', 'hoop'); h.appendChild(scaled(hoop(), 6)); stage.appendChild(h);
        const sh = el('div', 'shot'); sh.style.setProperty('--x0', '360px'); sh.style.setProperty('--y0', '190px');
        sh.style.setProperty('--x1', (STAGE_W / 2 - 16) + 'px'); sh.appendChild(prop('ball')); stage.appendChild(sh);
        const sw = el('div', 'swish', C.text.swish); stage.appendChild(sw); later(() => sw.classList.add('show'), 1350);
      } else {
        stage.appendChild(actor(T.trend, 40, false)); stage.appendChild(actor(T.lead, 440, false));
        if (C.bench) bench(250); else stage.appendChild(actor(T.peer, 240, false));
      }
    },
  };

  function renderTeam(s) {
    const box = $('members'); box.textContent = '';
    MEMBERS.forEach(id => {
      const m = T[id], benched = C.bench && id === 'peer';
      const row = el('div', 'member' + (s.active.includes(id) ? ' active' : '') + (benched ? ' bench' : ''));
      row.appendChild(scaled(avatar(m), m.bb ? 2.4 : m.look ? 3 : 4));
      const info = el('div'); const name = el('div', 'mn', m.name); name.appendChild(badge(m)); info.appendChild(name);
      info.appendChild(el('div', 'md', m.role));
      const doing = s.doing && s.doing[id]; if (doing) info.appendChild(el('div', 'doing', doing));
      row.appendChild(info); box.appendChild(row);
    });
  }

  function show() {
    const s = C.scenes[step];
    stage.textContent = '';
    SCENES[s.key](s);
    $('now').textContent = s.now; $('who').textContent = s.who[C.cast]; $('noteline').textContent = s.note || '';
    [...$('bar').children].forEach((d, i) => { d.classList.toggle('done', i < step); d.classList.toggle('on', i === step); });
    renderTeam(s);
    $('see').style.visibility = 'hidden';
    if (step === C.scenes.length - 1) later(() => { $('see').style.visibility = 'visible'; }, C.cast === 'basketball' ? 1900 : 600);
  }
  function run() {
    clearPending(); step = 0; show();
    timer = setInterval(() => { if (step < C.scenes.length - 1) { step++; show(); } else clearInterval(timer); }, C.scene_ms);
  }
  function showReport() {
    clearPending(); hideTip(true);
    $('loading').style.display = 'none'; $('report').style.display = 'block';
    try { const f = window.frameElement; if (f && f.getBoundingClientRect().top < 0) f.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) { /* not embedded */ }
  }
  function replay() { hideTip(true); $('report').style.display = 'none'; $('loading').style.display = 'block'; fit(); run(); }

  /* ---------- screen 2: the report ---------- */
  const TIPS = [];
  function sentence(parent, s) { // the sentence as written, each cited number highlighted with its tip
    let pos = 0;
    s.numbers.forEach(n => {
      const at = s.text.indexOf(n.text, pos); if (at < 0) return;
      parent.appendChild(document.createTextNode(s.text.slice(pos, at)));
      const span = el('span', 'num', n.text); span.dataset.tip = String(TIPS.push(n) - 1); span.tabIndex = 0; parent.appendChild(span);
      pos = at + n.text.length;
    });
    parent.appendChild(document.createTextNode(s.text.slice(pos)));
  }
  function bold(parent, text) { text.split('**').forEach((part, i) => parent.appendChild(i % 2 ? el('b', '', part) : document.createTextNode(part))); }
  function buildReport() {
    const R = C.report;
    $('asof').textContent = R.as_of; $('headline').textContent = R.headline;
    sentence($('rankline'), R.rank);
    const after = $('after'); if (R.after) { after.appendChild(el('b', '', C.text.after_label + ' ')); after.appendChild(document.createTextNode(R.after)); }
    const g = $('grid');
    R.cards.forEach(card => {
      const m = T[card.member], f = el('div', 'finding' + (card.wide ? ' wide' : '')), top = el('div', 'top');
      top.appendChild(scaled(avatar(m), m.bb ? 3 : m.look ? 3.5 : 5));
      const head = el('div'); head.appendChild(el('h3', '', card.title));
      const by = el('div', 'byline', C.text.found_by + ' ' + m.name + ' '); by.appendChild(el('span', 'tag ' + (card.badge === 'AI' ? 'ai' : 'rule'), card.badge));
      head.appendChild(by); top.appendChild(head); f.appendChild(top);
      const p = el('p'); card.sentences.forEach((s, i) => { if (i) p.appendChild(document.createTextNode(' ')); sentence(p, s); }); f.appendChild(p);
      f.appendChild(el('div', 'checked', card.badge === 'AI' ? C.text.checked_ai : C.text.checked_rule));
      g.appendChild(f);
      if (card.member === 'trend' && C.bench) {
        const b = el('div', 'finding bench'), bt = el('div', 'top');
        bt.appendChild(scaled(avatar(T.peer), T.peer.bb ? 3 : 3.5)); bt.appendChild(el('p', '', T.peer.name + ' ' + C.text.bench_card));
        b.appendChild(bt); g.appendChild(b);
      }
    });
    bold($('foot'), C.text.foot);
  }

  /* ---------- tips: hover on a mouse, tap on a phone ---------- */
  const tip = $('tip'); let pinned = false;
  function showTip(n, x, y, pin) {
    tip.textContent = '';
    if (pin) { const x0 = el('button', 'x', '✕'); x0.setAttribute('aria-label', C.text.close); x0.addEventListener('click', ev => { ev.stopPropagation(); hideTip(true); }); tip.appendChild(x0); }
    tip.appendChild(el('b', '', n.text)); tip.appendChild(document.createTextNode(' ' + n.explain));
    tip.appendChild(el('div', 'src', n.label + (n.when ? ' · ' + n.when : '')));
    tip.style.display = 'block';
    const w = tip.offsetWidth, h = tip.offsetHeight;
    tip.style.left = Math.max(4, Math.min(x + 14, window.innerWidth - w - 8)) + 'px';
    tip.style.top = Math.max(4, Math.min(y + 14, window.innerHeight - h - 8)) + 'px';
    pinned = !!pin;
  }
  function hideTip(force) { if (pinned && !force) return; tip.style.display = 'none'; pinned = false; }
  const target = e => e.target instanceof Element ? e.target.closest('[data-tip]') : null;
  document.addEventListener('mouseover', e => { const t = target(e); if (t && !pinned) showTip(TIPS[+t.dataset.tip], e.clientX, e.clientY); });
  document.addEventListener('mouseout', e => { if (target(e)) hideTip(false); });
  document.addEventListener('click', e => {
    const t = target(e);
    if (t) showTip(TIPS[+t.dataset.tip], e.clientX, e.clientY, true);
    else if (!(e.target instanceof Element && e.target.closest('#tip'))) hideTip(true);
  });
  document.addEventListener('focusin', e => { const t = target(e); if (t) { const r = t.getBoundingClientRect(); showTip(TIPS[+t.dataset.tip], r.left, r.bottom, true); } });

  /* ---------- start ---------- */
  C.scenes.forEach(() => $('bar').appendChild(el('div')));
  $('see').addEventListener('click', showReport); $('skip').addEventListener('click', showReport); $('watch').addEventListener('click', replay);
  buildReport(); fit(); run();
})();
