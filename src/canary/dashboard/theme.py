"""The v6 look for Streamlit pages: theme CSS, the theme picker, the footer and the pixel sprites.

The three themes change the page background (and the top bar); cards stay white with navy borders.
The CSS restyles Streamlit's own parts (header, top nav, buttons, inputs, popover) to match
dashboard/design/dashboard-mockup.html. Containers whose key starts with "box-" are drawn as v6 cards.
"""

import html
import re

import streamlit as st

from canary.dashboard import icons

THEMES = ("standard", "detective", "basketball")
THEME_LABELS = {"standard": "Standard", "detective": "🔍 Detectives", "basketball": "🏀 Basketball"}
FOOTER = "Research tool, not financial advice. Built from public FDIC data."

# ---------------------------------------------------------------------------------------------- sprites
BIRD = [".......YYY...", "......YYYYY..", "......YYKYYO.", "......YYYYY..", ".....YYYYYY..",
        "...YYYWWWYY..", "YYYYYYWWWWY..", "..YYYYYWWYY..", ".....YYYYY...", "......O.O....",
        "...BBBBBBBBB."]
CAGED_BIRD = [".YYY.", "YYKYO", "YYYY.", "YYWYY", ".YYY.", ".O.O."]
# Y yellow, W wing, K eye, O beak and feet, B perch, T tear, N navy (cage)
PALETTE = {"Y": "#ffd43b", "W": "#f59f00", "K": "#1e2240", "O": "#e8590c", "B": "#8a5a2b", "T": "#74c0fc",
           "N": "#1e2240"}


def _pixels(cells: list[tuple[int, int, int, int, str]], cols: int, rows: int, width: int, label: str) -> str:
    """An inline SVG of pixel rectangles (x, y, w, h, colour), scaled crisply to `width` px."""
    rects = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>' for x, y, w, h, c in cells)
    height = round(width * rows / cols)
    return (f'<svg class="pixel" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {cols} {rows}" width="{width}" '
            f'height="{height}" shape-rendering="crispEdges" role="img" aria-label="{label}">{rects}</svg>')


def _grid_cells(grid: list[str], dx: int = 0, dy: int = 0) -> list[tuple[int, int, int, int, str]]:
    return [(dx + i, dy + j, 1, 1, PALETTE[ch])
            for j, row in enumerate(grid) for i, ch in enumerate(row) if ch in PALETTE]


def bird_svg(width: int = 104, sad: bool = False) -> str:
    """The pixel canary on its perch; `sad` adds a tear."""
    cells = _grid_cells(BIRD) + ([(8, 3, 1, 2, PALETTE["T"])] if sad else [])
    return _pixels(cells, 13, 11, width, "A sad pixel canary" if sad else "A pixel canary on a perch")


def cage_svg(width: int = 136) -> str:
    """The pixel canary in a cage (Why Canary)."""
    n = PALETTE["N"]
    cells = [(7, 0, 3, 1, n), (8, 1, 1, 1, n), (4, 2, 9, 1, n), (2, 3, 13, 1, n), (1, 15, 15, 2, n)]
    cells += [(x, 3, 1, 12, n) for x in range(2, 15, 3)]
    cells += _grid_cells(CAGED_BIRD, dx=6, dy=8)
    return _pixels(cells, 17, 17, width, "A pixel canary in a cage")


def bold(text: str) -> str:
    """Fixed copy to HTML: escape it, then turn **bold** into <b>bold</b>."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(text, quote=False))


def html_block(markup: str) -> None:
    st.markdown(markup, unsafe_allow_html=True)


def on_background(text: str, bold: bool = False) -> None:
    """A line of plain text that sits on the page background, not in a card (a paper tag in the
    detective and basketball themes, so it stays readable on the cork board and the court)."""
    weight = " strong" if bold else ""
    html_block(f'<p class="on-bg{weight}">{html.escape(text)}</p>')


# ------------------------------------------------------------------------------------------------- CSS
BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
:root { --bg:#d5d7db; --navy:#1e2240; --yellow:#ffe066; --paper:#ffffff; --soft:#f1f3f5; --muted:#5c6178;
        --cream:#fff8db; --nav:#1e2240; --nav-edge:#000000; --pix:"Press Start 2P", ui-monospace, monospace; }
html, body { overflow-x:hidden; }
[data-testid="stAppViewContainer"] { background:var(--bg); color:var(--navy); }
[data-testid="stMainBlockContainer"] { max-width:1120px; padding:5.5rem 16px 60px; }
[data-testid="stElementContainer"]:has(> [data-testid="stMarkdown"] style) { display:none; }
.pix { font-family:var(--pix); }
.stApp p, .stApp li { color:var(--navy); }

/* top bar: Streamlit's header restyled as the v6 nav */
header[data-testid="stHeader"] { background:var(--nav); border-bottom:4px solid var(--nav-edge); color:#fff; }
[data-testid="stDecoration"], [data-testid="stMainMenu"], [data-testid="stAppDeployButton"],
[data-testid="stToolbarActions"], [data-testid="stStatusWidget"] { display:none !important; }
[data-testid="stHeaderLogo"] { image-rendering:pixelated; height:22px; }
:has(> [data-testid="stHeaderLogo"]) { display:flex; align-items:center; overflow:visible; width:auto; max-width:none; background:none; border:0; }
:has(> [data-testid="stHeaderLogo"])::after { content:"CANARY"; font-family:var(--pix); font-size:13px; color:#fff; margin-left:10px; }
[data-testid="stTopNav"] { justify-content:flex-end; padding-right:88px; gap:4px; }
[data-testid="stTopNavLink"] { border:2px solid #fff; border-radius:0; padding:9px 9px; background:transparent; color:#fff; }
[data-testid="stTopNavLink"] span, [data-testid="stTopNavLink"] p { font-family:var(--pix) !important; font-size:9px !important; color:inherit !important; }
[data-testid="stTopNavLink"]:hover { background:rgba(255,255,255,.15); }
[data-testid="stTopNavLink"][aria-current="page"] { background:var(--yellow); border-color:var(--yellow); color:var(--navy); }
/* phones: Streamlit folds the top nav into a sidebar opened from the header */
:has(> [data-testid="stHeaderLogo"])::after { order:1; }
[data-testid="stExpandSidebarButton"] { order:2; margin-left:12px; border:2px solid #fff; border-radius:0; }
[data-testid="stExpandSidebarButton"], [data-testid="stExpandSidebarButton"] * { color:#fff !important; }
[data-testid="stSidebar"] { background:var(--nav); border-right:4px solid var(--nav-edge); }
[data-testid="stSidebar"] * { color:#fff; }
[data-testid="stSidebarNavLink"] { border:2px solid #fff; border-radius:0; margin:4px 0; }
[data-testid="stSidebar"] button[data-testid^="stBaseButton"], header button[data-testid^="stBaseButton"] { background:transparent !important; border:0; box-shadow:none; padding:4px; }
[data-testid="stSidebarNavLink"] span, [data-testid="stSidebarNavLink"] p { font-family:var(--pix) !important; font-size:10px !important; color:#fff !important; }
[data-testid="stSidebarNavLink"][aria-current="page"] { background:var(--yellow); border-color:var(--yellow); }
[data-testid="stSidebarNavLink"][aria-current="page"] span, [data-testid="stSidebarNavLink"][aria-current="page"] p { color:var(--navy) !important; }

/* the 🎨 theme picker sits at the right of the top bar */
.st-key-theme-picker { position:fixed; top:12px; right:16px; z-index:999991; width:auto !important; }
.st-key-theme-picker [data-testid="stPopoverButton"] { background:transparent; color:#fff; border:2px solid #fff;
  border-radius:0; box-shadow:none; font-family:var(--pix); font-size:9px; padding:6px 9px; min-height:0; }
.st-key-theme-picker [data-testid="stPopoverButton"]:hover { background:rgba(255,255,255,.15); color:#fff; }
[data-testid="stPopoverBody"] { background:var(--nav); border:3px solid #000; border-radius:0; }
[data-testid="stPopoverBody"] button { width:100%; justify-content:flex-start; font-family:var(--pix); border:2px solid #fff;
  border-radius:0; background:transparent; color:#fff; box-shadow:none; padding:9px 10px; min-height:0; }
[data-testid="stPopoverBody"] button p { font-family:var(--pix); font-size:9px; color:inherit; }
[data-testid="stPopoverBody"] button:hover { background:rgba(255,255,255,.15); color:#fff; border-color:#fff; }
[data-testid="stPopoverBody"] button[data-testid="stBaseButton-primary"] { background:var(--yellow); color:var(--navy); border-color:var(--yellow); }

/* buttons, links and inputs in the v6 style */
.stApp button[data-testid^="stBaseButton"], [data-testid="stPageLink"] a {
  font-family:var(--pix); font-size:11px; line-height:1.4; padding:12px 14px; min-height:0; border:3px solid var(--navy);
  border-radius:0; background:#fff; color:var(--navy); box-shadow:3px 3px 0 var(--navy); text-decoration:none; }
.stApp button[data-testid^="stBaseButton"] p, [data-testid="stPageLink"] a p, [data-testid="stPageLink"] a span {
  font-family:var(--pix); font-size:11px; color:inherit; }
.stApp button[data-testid^="stBaseButton"]:hover, [data-testid="stPageLink"] a:hover { background:var(--yellow); color:var(--navy); border-color:var(--navy); }
.stApp button[data-testid^="stBaseButton-primary"], [data-testid="stPageLink"] a.go { background:var(--navy); color:#fff; }
.stApp button[data-testid^="stBaseButton-primary"]:hover { background:#2d3363; color:#fff; }
.stApp button[data-testid^="stBaseButton"]:active { transform:translate(2px,2px); box-shadow:1px 1px 0 var(--navy); }
.stApp button[data-testid^="stBaseButton"]:focus:not(:active) { border-color:var(--navy); color:inherit; }
/* search suggestions: body font, left-aligned, name bold with state and status smaller below */
[class*="st-key-pick-"] button { width:100%; justify-content:flex-start !important; text-align:left; padding:10px 14px; }
[class*="st-key-pick-"] button > div, [class*="st-key-pick-"] button > div > span,
[class*="st-key-pick-"] button [data-testid="stMarkdownContainer"] { justify-content:flex-start !important; text-align:left !important; width:100%; }
[class*="st-key-pick-"] button p { font-family:inherit !important; font-size:16px !important; line-height:1.35; text-align:left !important; margin:0; }
[class*="st-key-pick-"] button p:last-child { font-size:13px !important; color:var(--muted); }
[class*="st-key-pick-"] button::before, .bank-icon { content:""; flex:0 0 auto; display:inline-block; width:32px; height:32px;
  margin-right:14px; border:2px solid var(--navy); background:#fff center/18px no-repeat; image-rendering:pixelated;
  background-image:url("{PLACEHOLDER}"); }
.bank-icon { vertical-align:middle; margin-bottom:4px; }
h3.start-title { font-size:11px !important; margin:0 0 10px; line-height:1.6; }
[class*="st-key-box-start-"] [class*="st-key-pick-"] button { box-shadow:none; }
[data-testid="stTextInputRootElement"] { border:3px solid var(--navy) !important; border-radius:0; box-shadow:3px 3px 0 var(--navy); background:#fff; }
[data-testid="stTextInputRootElement"] input { font-size:17px; color:var(--navy); background:#fff; }
[data-testid="stForm"] { border:0; padding:0; }

/* v6 cards: white, navy border, hard offset shadow */
.box, [class*="st-key-box-"] { background:var(--paper); border:3px solid var(--navy); box-shadow:5px 5px 0 var(--navy); color:var(--navy); }
[class*="st-key-box-"] { padding:18px; }
h1.pix, h2.pix { color:var(--navy); }
h1.pix { font-size:20px; line-height:1.5; margin:0 0 10px; padding:0; }
h2.pix { font-size:13px; line-height:1.6; margin:0 0 10px; padding:0; }
.lede { font-size:17px; max-width:760px; margin:0 0 20px; }
.note { font-size:14px; color:var(--muted); }
.foot { text-align:center; margin-top:30px; font-size:13px; color:var(--muted); }
.on-bg { margin:4px 0 12px; } .on-bg.strong { font-weight:700; }

/* home */
.hero { text-align:center; padding:24px 0 18px; }
.hero svg.pixel { display:block; margin:0 auto 18px; }
.hero .title { font-family:var(--pix); font-size:clamp(36px, 10vw, 88px); line-height:1.1; margin:0; padding:0;
  color:var(--navy); text-shadow:6px 6px 0 var(--yellow); letter-spacing:4px; }
.hero .tag { font-family:var(--pix); font-size:clamp(10px, 2vw, 14px); margin:22px 0 8px; line-height:1.8; color:var(--navy); }
.st-key-home-search { max-width:680px; margin:0 auto; }
/* the two bank search boxes (Home, Find): taller, larger text */
.st-key-home-q [data-testid="stTextInputRootElement"], .st-key-find-search [data-testid="stTextInputRootElement"] { height:58px; }
.st-key-home-q input, .st-key-find-search input { font-size:20px !important; padding:0 18px !important; height:100%; }
.st-key-home-search [data-testid="stFormSubmitButton"] button { height:58px; padding:0 26px; }
.hero { padding-top:clamp(24px, 9vh, 96px); }
.what.home-below { margin-top:clamp(56px, 22vh, 220px); }
.what { padding:22px; margin:6px 0 22px; font-size:18px; }
.stats { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:16px; margin-bottom:8px; }
@media (max-width:860px){ .stats { grid-template-columns:repeat(2,minmax(0,1fr)); } }
@media (max-width:420px){ .stats { grid-template-columns:1fr; } }
.stat { padding:16px; }
.stat .big { font-family:var(--pix); font-size:24px; margin:10px 0 8px; line-height:1.2; }
.stat .big small { font-size:11px; }
.stat .lab { font-family:var(--pix); font-size:9px; line-height:1.6; }
.st-key-box-miss { background:var(--cream); }
.miss { display:grid; grid-template-columns:auto 1fr; gap:20px; align-items:center; }
.miss p { margin:0; }
.st-key-box-miss [data-testid="stPageLink"] { margin-left:98px; }
@media (max-width:700px){ .st-key-box-miss [data-testid="stPageLink"] { margin-left:0; } }
.st-key-box-miss [data-testid="stPageLink"] a, .st-key-box-why-answer [data-testid="stPageLink"] a { background:var(--navy); color:#fff; }
.st-key-box-miss [data-testid="stPageLink"] a:hover, .st-key-box-why-answer [data-testid="stPageLink"] a:hover { background:#2d3363; color:#fff; }
@media (max-width:700px){ .miss { grid-template-columns:1fr; } }
[class*="st-key-box-card-"] { position:relative; height:100%; }
[class*="st-key-box-card-"]:hover { background:var(--yellow); }
[class*="st-key-box-card-"] p { font-size:15px; }
[class*="st-key-box-card-"] [data-testid="stElementContainer"] { position:static; }
[class*="st-key-box-card-"] [data-testid="stPageLink"] a::after { content:""; position:absolute; inset:0; z-index:1; }

/* why */
.why-hero { text-align:center; padding:4px 0 10px; }
.why-hero svg.pixel { display:block; margin:0 auto 14px; }
.why-hero h1.pix { font-size:24px; }
.st-key-box-why-answer { background:var(--cream); }

/* chips, sliders and the 2023 / watchlist pages */
/* Streamlit 1.67 draws segmented-control chips as button[data-variant="segmented_control"]; the chosen one
   carries [data-selected] (no per-button test id). Its own style is a pale tint of the primary colour. */
[data-testid="stButtonGroup"] button[data-variant="segmented_control"] { min-height:0; }
[data-testid="stButtonGroup"] button[data-variant="segmented_control"][data-selected]:not([data-disabled]) {
  background:var(--navy); border-color:var(--navy); color:#fff; }
[data-testid="stButtonGroup"] button[data-variant="segmented_control"][data-selected]:not([data-disabled]) p { color:#fff; }
[data-testid="stButtonGroup"] { flex-wrap:wrap; gap:8px; }
.cs-head { display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; align-items:flex-start; margin:14px 0; }
.cs-head h2.pix { font-size:18px; text-shadow:3px 3px 0 var(--yellow); }
.status { font-family:var(--pix); font-size:9px; padding:7px 9px; border:2px solid var(--navy); display:inline-block; background:#fff; color:var(--navy); }
.status.failed { background:#ffc9c9; } .status.near { background:var(--yellow); }
.ct { font-weight:800; font-size:15px; margin-top:6px; } .cst { font-size:13px; color:var(--muted); }
.side-q { font-family:var(--pix); font-size:9px; }
.side-rank { font-family:var(--pix); font-size:22px; margin:8px 0 4px; }
.side-row { display:flex; justify-content:space-between; gap:10px; padding:8px 0; border-bottom:2px dotted #ced4da; font-size:15px; }
.side-bars { font-family:var(--pix); font-size:8px; margin-top:16px; line-height:1.6; }
.bar { font-size:14px; margin-top:8px; }
.bar .track { height:10px; background:var(--soft); border:2px solid var(--navy); margin-top:4px; }
.bar .fill { height:100%; background:#e8590c; }
.say { margin-top:14px; padding:12px; background:var(--cream); border:3px solid var(--navy); font-size:15px; color:var(--navy); }
.three { display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:16px; margin:14px 0 18px; }
@media (max-width:760px){ .three { grid-template-columns:1fr; } }
.three .stat .big { font-size:22px; }

/* how it works: the replay's bank picker and the four-step strip (arrows between steps; stacked on phones) */
.st-key-how-picker { max-width:560px; }
.st-key-how-picker label p { font-weight:700; color:var(--navy); }
.st-key-how-picker [role="group"]:has(> input) { border:3px solid var(--navy); border-radius:0; box-shadow:3px 3px 0 var(--navy); background:#fff; }
.st-key-how-picker input { font-size:16px; color:var(--navy); background:#fff; }
h2.how-strip-title { margin-top:26px; }
.steps { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:26px; margin:6px 0 10px; }
.step { position:relative; padding:16px; }
.step p { font-size:15px; margin:6px 0; }
.step:not(:last-child)::after { content:"▶"; position:absolute; right:-22px; top:50%; margin-top:-10px; font-size:16px; color:var(--navy); }
.mark { display:inline-block; font-family:var(--pix); font-size:9px; padding:4px 6px; border:2px solid var(--navy); margin-bottom:8px; }
.mark.ai { background:#d0ebff; } .mark.code { background:#e9ecef; }
@media (max-width:860px){ .steps { grid-template-columns:repeat(2,minmax(0,1fr)); } .step:nth-child(2)::after { content:none; } }
@media (max-width:520px){ .steps { grid-template-columns:1fr; gap:22px; } .step:not(:last-child)::after { content:"▼"; right:auto; left:50%; top:auto; bottom:-21px; margin:0 0 0 -8px; } }
"""

BASE_CSS = BASE_CSS.replace("{PLACEHOLDER}", icons.PLACEHOLDER)  # the pixel bank for banks without a website

STANDARD_CSS = ""

DETECTIVE_CSS = """
[data-testid="stAppViewContainer"] { background-color:#b4875a;
  background-image:radial-gradient(#9a6d43 1.4px, transparent 1.8px), radial-gradient(#c99b6c 1.1px, transparent 1.6px), radial-gradient(#8f6440 1px, transparent 1.4px);
  background-size:13px 13px, 21px 21px, 34px 34px; background-position:0 0, 6px 9px, 15px 3px; }
:root { --nav:#1a1a1a; }
.box, [class*="st-key-box-"] { position:relative; overflow:visible; }
.box::before, [class*="st-key-box-"]::before { content:""; position:absolute; top:-10px; left:50%; margin-left:-7px;
  width:14px; height:14px; background:#e03131; border:3px solid var(--navy); box-shadow:2px 2px 0 rgba(0,0,0,.35); z-index:2; }
.stats .box::before { top:-10px; }
"""

BASKETBALL_CSS = """
[data-testid="stAppViewContainer"] { background-color:#b97a45;
  background-image:
    radial-gradient(circle at 50% 300px, transparent 168px, rgba(255,255,255,.9) 168px 174px, transparent 174px),
    linear-gradient(to bottom, transparent 297px, rgba(255,255,255,.9) 297px 303px, transparent 303px),
    repeating-linear-gradient(90deg, rgba(70,35,8,.16) 0 3px, transparent 3px 58px),
    repeating-linear-gradient(90deg, transparent 0 29px, rgba(255,225,180,.14) 29px 31px, transparent 31px 58px);
  background-repeat:no-repeat, no-repeat, repeat, repeat; }
:root { --nav:#1c4e80; --nav-edge:#74c0fc; }
h1.page-title, h2.page-title, .st-key-how-picker label p { color:#fff; text-shadow:2px 2px 0 var(--navy); }
"""

# Text that sits straight on the cork board or the court (not in a card) goes on a small paper tag, so it is
# readable whatever is behind it. (White text with a navy shadow lost to Streamlit's own text colour.)
PAPER_TAG_CSS = """
.lede, .foot, .on-bg, .hero .tag, .cs-head .note, .bank-head .note {
  display:inline-block; background:var(--paper); color:var(--navy) !important; text-shadow:none !important;
  font-weight:600; padding:4px 10px; border:2px solid var(--navy); box-shadow:3px 3px 0 var(--navy); }
.foot { display:table; margin:30px auto 0; }
.cs-head .note, .bank-head .note { margin-top:6px; }
"""
DETECTIVE_CSS += PAPER_TAG_CSS
BASKETBALL_CSS += PAPER_TAG_CSS

THEME_CSS = {"standard": STANDARD_CSS, "detective": DETECTIVE_CSS, "basketball": BASKETBALL_CSS}


# --------------------------------------------------------------------------------------------- helpers
def current_theme() -> str:
    theme = st.session_state.get("theme", "standard")
    return theme if theme in THEMES else "standard"


def _set_theme(theme: str) -> None:
    st.session_state["theme"] = theme


def apply_theme() -> None:
    """Inject the base v6 CSS plus the current theme's background and top-bar colours."""
    st.session_state["theme"] = current_theme()
    html_block(f"<style>{BASE_CSS}{THEME_CSS[current_theme()]}</style>")


def theme_buttons(prefix: str) -> None:
    """One button per theme; the current one is highlighted. Keys are f"{prefix}-{theme}"."""
    for theme in THEMES:
        st.button(THEME_LABELS[theme], key=f"{prefix}-{theme}", on_click=_set_theme, args=(theme,),
                  type="primary" if theme == current_theme() else "secondary")


def theme_picker() -> None:
    """The 🎨 popover at the right of the top bar."""
    with st.container(key="theme-picker"), st.popover("🎨 ▾", help="Change theme"):
        theme_buttons("theme-pick")


def page_title(title: str, lede: str | None = None) -> None:
    """A page heading in the pixel font (white on the court in the basketball theme)."""
    lede_html = f'<p class="lede">{html.escape(lede)}</p>' if lede else ""
    html_block(f'<h1 class="pix page-title">{html.escape(title)}</h1>{lede_html}')


def footer() -> None:
    html_block(f'<p class="foot">{FOOTER}</p>')
