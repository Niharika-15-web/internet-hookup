from playwright.sync_api import Page,expect
def test_context_menu(page:Page):
    page.goto("https://the-internet.herokuapp.com/context_menu")
    page.locator("#hot-spot").click(button = "right")