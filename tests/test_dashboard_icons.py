from canary.dashboard import icons


def test_icon_url_uses_duckduckgo_and_a_clean_domain():
    assert icons.icon_url("wellsfargo.com") == "https://icons.duckduckgo.com/ip3/wellsfargo.com.ico"
    assert icons.icon_url("https://www.WellsFargo.com/x") == "https://icons.duckduckgo.com/ip3/wellsfargo.com.ico"


def test_no_icon_without_a_usable_domain():
    for bad in (None, "", 'evil.com");}*{x:url(', "<script>", float("nan")):
        assert icons.icon_url(bad) is None


def test_results_css_only_for_banks_with_a_site():
    css = icons.results_css([{"cert": 3511, "website": "wellsfargo.com"}, {"cert": 24735, "website": None},
                             {"cert": 7, "website": 'x.com");}body{display:none'}])
    assert ".st-key-pick-3511 button::before" in css and "ip3/wellsfargo.com.ico" in css
    assert "24735" not in css and "display:none" not in css
    assert icons.results_css([{"cert": 1, "website": None}]) == ""


def test_badge_falls_back_to_the_pixel_bank():
    assert "ip3/auburnbank.com.ico" in icons.badge("auburnbank.com")
    assert "url(" not in icons.badge(None)
    assert icons.PLACEHOLDER.startswith("data:image/svg+xml,")
