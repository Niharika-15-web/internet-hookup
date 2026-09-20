from playwright.sync_api import Page,expect
def test_hovers(page:Page):
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.locator(".figure").nth(0).hover()
    expect(page.locator(".figcaption").nth(0)).to_contain_text("name: user1")


    page.locator(".figure").nth(1).hover()
    expect(page.locator(".figcaption").nth(1)).to_contain_text("name: user2")


    page.locator(".figure").nth(2).hover()
    expect(page.locator(".figcaption").nth(2)).to_contain_text("name: user3")