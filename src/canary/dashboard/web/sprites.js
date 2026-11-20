/* Canary pixel sprites (v6): grids drawn on canvas, never images. The two casts' looks live here;
   their names, badges and roles come from window.CANARY.team. */
const PAL = { k:'#1e2240', s:'#f4c29a', w:'#ffffff', y:'#ffd43b', o:'#f08c00', g:'#2f9e44', l:'#74c0fc', T:'#5c3a24' };
const BODY = ["....kkkkkk....","...kHHHHHHk...","..kHHHHHHHHk..","..kHHHHHHHHk..","..kFFFFFFFFk..","..kFkFFFFkFk..","..kFkFFFFkFk..","..kFFFFFFFFk..",
"...kkkkkkkk...","..kSSSSSSSSk..",".kSSSSSSSSSSk.",".kFSSSSSSSSFk.",".kkPPPPPPPPkk.","..kPPPkkPPPk..","..kPPk..kPPk..","..kkk....kkk.."];

function draw(rows, map) {
  const h = rows.length, w = Math.max(...rows.map(r => r.length));
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const x = c.getContext('2d');
  rows.forEach((r, j) => [...r].forEach((ch, i) => { if (ch !== '.') { x.fillStyle = map[ch] || '#f0f'; x.fillRect(i, j, 1, 1); } }));
  return c;
}

function person(o) {
  let rows = BODY.slice();
  if (o.hat) o.hat.forEach((r, i) => { if (r) rows[i] = r; });
  if (o.stripes) rows = rows.map((r, j) => j >= 9 && j <= 11 ? [...r].map((ch, i) => ch === 'S' && i % 2 === 0 ? 'Z' : ch).join('') : r);
  return draw(rows, { ...PAL, H:o.H, F:o.F || PAL.s, S:o.S, P:o.P, X:o.X || '#000', Z:'#1b1b1b' });
}

const HATS = {
  deerstalker:["...kkkkkkkk...","..kHHXHHXHHk..",".kHHHHHHHHHHk.",".kHkHHHHHHkHk."],
  fedora:[null,"...kHHHHHHk...","kkHHXXXXXXHHkk","kHHHHHHHHHHHHk"],
  beanie:["....kXkXkX....","...kHXHXHXk...","..kXHXHXHXHk..","..kHXHXHXHXk.."],
  glasses:[null,null,null,null,"..kFFFFFFFFk..","..kkkkFFkkkk.."],
};

const PROPS = {
  magnifier:["..kkk...",".kllk...","kllllk..",".kllk...","..kkkk..","....kTk.",".....kTk","......kk"],
  folder:["kkkk....","kyyykkkk","kyyyyyyk","kyyyyyyk","kyyyyyyk","kkkkkkkk"],
  notepad:["kkkkkk","kwwwwk","kwkkwk","kwwwwk","kwkkwk","kkkkkk"],
  whistle:["kkkk..","kyyyk.","kyyyyk",".kkkk."],
  ball:["..kkkk..",".kookok.","kooookok","kkkkkkkk","kokoookk","kooookok",".kookok.","..kkkk.."],
  stamp:["...kk...","..kTTk..","..kTTk..","...kk...",".kkkkkk.","kTTTTTTk","kkkkkkkk","kggggggk","kkkkkkkk"],
  check:["......kk",".....kgk","k...kgk.","kk.kgk..","kgkgk...",".kgk...."],
  bench:["kkkkkkkkkkkkkkkkkkkkkk","kTTTTTTTTTTTTTTTTTTTTk","kkkkkkkkkkkkkkkkkkkkkk","..kTk............kTk..","..kTk............kTk..","..kkk............kkk.."],
};
const prop = n => draw(PROPS[n], PAL);

const BB = [
".....kkkkkk.....","....kHHHHHHk....","...kHHHHHHHHk...","...kBBBBBBBBk...","...kFFFFFFFFk...","...kFkFFFFkFk...","...kFkFFFFkFk...","...kFFFFFFFFk...",
"....kkFFFFkk....","..kkJJJJJJJJkk..",".kFkJJJJJJJJkRk.",".kFkJJJJJJJJkRk.",".kFkJJJJJJJJkRk.",".kFkJJJJJJJJkRk.",".kkkLLLLLLLLkkk.","...kSSSSSSSSk...",
"...kSSSkkSSSk...","...kQQk..kGGk...","...kQQk..kGGk...","..kZZZk..kZZZk..","..kkkkk..kkkkk.."];
const DIG = { '1':[".L.","LL.",".L.",".L.","LLL"], '2':["LLL","..L","LLL","L..","LLL"], '3':["LLL","..L","LLL","..L","LLL"], '5':["LLL","L..","LLL","..L","LLL"] };

function baller(o) { // o: skin, hair, band, num, shoes, legSleeve, armSleeve
  const rows = BB.map(r => r.split(''));
  const digits = String(o.num).split(''), w = digits.length * 4 - 1, start = 4 + Math.floor((8 - w) / 2);
  digits.forEach((d, di) => DIG[d].forEach((r, ry) => [...r].forEach((ch, rx) => { if (ch === 'L') rows[9 + ry][start + di * 4 + rx] = 'N'; })));
  const map = { ...PAL, H:o.hair, B:o.band || o.hair, F:o.skin, J:'#f8f9fa', N:'#4dabf7', L:'#74c0fc', S:'#74c0fc',
    G:o.skin, Q:o.legSleeve || o.skin, R:o.armSleeve || o.skin, Z:o.shoes };
  return draw(rows.map(r => r.join('')), map);
}

const HOOP = ["eeeeeeeeeeeeeeee","ebbbbbbbbbbbbbbe","ebbbbbbbbbbbbbbe","ebbbbbkkkkbbbbbe","ebbbbbkbbkbbbbbe","eeeeeeeeeeeeeeee",
  "...rrrrrrrrrr...","...n.n.n.n.n.n..","....n.n.n.n.n...","....nnnnnnnn...."];
const hoop = () => draw(HOOP, { ...PAL, r:'#f03e3e', n:'#f8f9fa', b:'#f8f9fa', e:'#adb5bd' });

/* The casts (spec 4). Basketball: white jerseys, light-blue numbers and shorts; #5 brown skin with a black
   leg sleeve and black sneakers; #13 light skin, light-blue headband, white sneakers; #23 light skin,
   light-blue arm sleeve and sneakers; the striped Referee; Replay Review in glasses and a light-blue polo. */
const LOOKS = {
  detective: {
    rule:{ icon:'stamp' },
    trend:{ look:{ hat:HATS.deerstalker, H:'#8c5a3c', X:'#5c3a24', S:'#2b8a3e', P:'#495057' }, icon:'magnifier' },
    peer:{ look:{ hat:HATS.beanie, H:'#7048e8', X:'#b197fc', F:'#a0663f', S:'#e67700', P:'#364fc7' }, icon:'folder' },
    check:{ look:{ hat:HATS.glasses, H:'#212529', S:'#f8f9fa', P:'#212529' } },
    lead:{ look:{ hat:HATS.fedora, H:'#495057', X:'#212529', S:'#c9a96e', P:'#5c3a24' }, icon:'notepad' },
  },
  basketball: {
    rule:{ look:{ hat:[null,"...kHHHHHHk..."], H:'#212529', S:'#f8f9fa', P:'#212529', stripes:true }, icon:'whistle' },
    trend:{ bb:{ num:5, skin:'#7a4a2a', hair:'#1b1b1b', shoes:'#1b1b1b', legSleeve:'#1b1b1b' } },
    peer:{ bb:{ num:13, skin:'#c68a5a', hair:'#2b1d14', band:'#74c0fc', shoes:'#f8f9fa' } },
    check:{ look:{ hat:HATS.glasses, H:'#6b4423', S:'#4dabf7', P:'#343a40' } },
    lead:{ bb:{ num:23, skin:'#f6d3b3', hair:'#8a5a2b', shoes:'#74c0fc', armSleeve:'#74c0fc' } },
  },
};

function avatar(m) { return m.bb ? baller(m.bb) : m.look ? person(m.look) : prop(m.icon); }
