from playwright.sync_api import Page,expect
def test_JS_Alerts(page:Page):
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name = "Click for JS Alert").click()
    expect(page.locator("#result")).to_have_text("You successfully clicked an alert")

    page.once("dialog",lambda dialog: dialog.accept())
    page.get_by_role("button", name = "Click for JS Confirm").click()
    expect(page.locator("#result")).to_contain_text("You clicked: Ok")

    page.once("dialog", lambda dialog: dialog.accept("Hello"))
    page.get_by_role("button" , name = "Click for JS Prompt").click()
    expect(page.locator("#result")).to_have_text("You entered: Hello")