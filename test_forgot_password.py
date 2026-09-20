from playwright.sync_api import Page,expect
def test_forgot_password(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page.get_by_role("link", name = "Forgot Password")).to_be_visible()
    page.get_by_role("link", name = "Forgot Password").click()
    page.get_by_role("button",name = "Retrieve password").click()
    expect(page.get_by_role("heading",name = "Internal Server Error")).to_be_visible()
    page.screenshot(path =  "forgot password.png")
