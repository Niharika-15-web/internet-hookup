from playwright.sync_api import Page,expect
def test_JqueryUI(page:Page):
    page.goto("https://the-internet.herokuapp.com/jqueryui/menu#")
    page.get_by_role("link",name ="Enabled").hover()
    page.get_by_role("link",name = "Downloads").hover()
    page.get_by_role("link", name = "PDF").click()

    page.goto("https://the-internet.herokuapp.com/jqueryui/menu#")
    page.get_by_role("link", name="Enabled").hover()
    page.get_by_role("link", name="Downloads").hover()
    page.get_by_role("link", name = "CSV").click()

    page.goto("https://the-internet.herokuapp.com/jqueryui/menu#")
    page.get_by_role("link", name="Enabled").hover()
    page.get_by_role("link", name="Downloads").hover()
    page.get_by_role("link", name = "Excel").click()