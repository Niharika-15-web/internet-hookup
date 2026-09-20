from playwright.sync_api import Page,expect
def test_drop_drown(page:Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option('1')
    page.locator("#dropdown").select_option("2")