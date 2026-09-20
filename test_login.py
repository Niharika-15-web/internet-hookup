from playwright.sync_api import Page,expect
def test_login_page(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page.get_by_role("link",name = "Form Authentication")).to_be_visible()
    page.get_by_role("link",name = "Form Authentication").click()
    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name = "Login").click()

    expect(page).to_have_url("https://the-internet.herokuapp.com/secure")
    page.get_by_role("heading",name =  "Secure Area")
    expect(page.get_by_text("You logged into a secure area!")).to_be_visible()
    page.screenshot(path = "Login Authentication.png")
