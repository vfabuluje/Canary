"""Bank website icons, loaded by the visitor's browser from DuckDuckGo's icon service.

DuckDuckGo doesn't track who asks. Only a plain domain from the export (checked again here) reaches the
markup; a bank without one (most closed banks) shows a small pixel bank instead.
"""

from urllib.parse import quote

from canary.ingest_websites import clean_domain

ICON_URL = "https://icons.duckduckgo.com/ip3/{domain}.ico"
_PIXEL_BANK = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 9 8' shape-rendering='crispEdges'>"
               "<path fill='#1e2240' d='M3 0h3v1H3zM1 1h7v1H1zM0 2h9v1H0zM1 3h1v3H1zM4 3h1v3H4zM7 3h1v3H7zM0 6h9v2H0z'/>"
               "</svg>")
PLACEHOLDER = "data:image/svg+xml," + quote(_PIXEL_BANK)


def icon_url(website) -> str | None:
    """The icon address for a bank's domain, or None when there is no usable domain."""
    domain = clean_domain(website) if isinstance(website, str) else None
    return ICON_URL.format(domain=domain) if domain else None


def _image(website) -> str:
    url = icon_url(website)
    return f'background-image:url("{url}"); background-size:24px 24px;' if url else ""


def results_css(suggestions: list[dict]) -> str:
    """One rule per search result whose bank has a website; the rest keep the pixel bank."""
    rules = [f'.st-key-pick-{int(s["cert"])} button::before {{ {_image(s.get("website"))} }}'
             for s in suggestions if icon_url(s.get("website"))]
    return "<style>" + "\n".join(rules) + "</style>" if rules else ""


def badge(website) -> str:
    """The icon tile for a bank page header."""
    return f'<span class="bank-icon" style=\'{_image(website)}\'></span>'
