from playwright.sync_api import Page,expect
def test_Redirections(page:Page):
    page.goto("https://the-internet.herokuapp.com/redirector")
    page.get_by_role("link", name = "here").click()

    expect(page).to_have_url("https://the-internet.herokuapp.com/status_codes")

    page.get_by_role("link", name = "200").click()
    page.get_by_role("heading", name = "Status Codes")
    page.get_by_role("heading" , name = "This page returned a 200 status code.")

    page.go_back()

    page.get_by_role("link", name = "500").click()
    page.get_by_role("heading", name="Status Codes")
    page.get_by_role("heading", name="This page returned a 500 status code.")





