from playwright.sync_api import Page,expect
def test_add_remove_elements(page:Page):
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    page.get_by_role("button", name = "Add Element").click()
    page.get_by_role("button", name = "Add Element").click()
    page.get_by_role("button", name = "Add Element").click()
    expect(page.get_by_role("button", name = "delete")).to_have_count(3)

    page.get_by_role("button", name = "Delete").first.click()
    expect(page.get_by_role("button", name = "Delete")).to_have_count(2)