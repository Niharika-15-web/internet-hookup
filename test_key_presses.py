from playwright.sync_api import Page,expect
def test_key_presses(page:Page):
    page.goto("https://the-internet.herokuapp.com/key_presses")

    target = page.locator("#target")
    target.click()

    target.press("Tab")
    expect(page.locator("#result")).to_have_text("You entered: TAB")



