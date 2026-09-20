from playwright.sync_api import Page,Expect
def test_multiple_windows(page:Page):
    page.goto("https://the-internet.herokuapp.com/windows")
    page.get_by_role("link", name = "Click Here").click()