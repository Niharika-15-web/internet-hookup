from playwright.sync_api import Page,expect
def test_checkbox(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page.get_by_role("link", name ="Checkboxes"))
    page.get_by_role("link", name = "Checkboxes").click()

    checkbox1 = page.get_by_role("checkbox").nth(0)
    checkbox2 =page.get_by_role("checkbox").nth(1)

    checkbox1.check()
    expect(checkbox1).to_be_checked()

    checkbox2.uncheck()
    expect(checkbox2).not_to_be_checked()




