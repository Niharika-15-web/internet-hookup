from playwright.sync_api import Page,expect
def test_AB_testing(page:Page):
     page.goto("https://the-internet.herokuapp.com/")
     expect(page.get_by_role("link",name ="A/B Testing")).to_be_visible()
     page.get_by_role("link",name = "A/B Testing").click()
     expect(page).to_have_url("https://the-internet.herokuapp.com/abtest")
     control = page.get_by_role("heading", name = "A/B Test Control")
     variation = page.get_by_role("heading", name = "A/B Test Variation 1")
     expect(control.or_(variation)).to_be_visible()
     page.screenshot(path = "AB testing Control screenshot.png")

     page.go_back()
     expect(page).to_have_url("https://the-internet.herokuapp.com/")

     expect(page.get_by_role("link",name = "File Upload")).to_be_visible()
     page.get_by_role("link",name ="File Upload").click()
     page.locator("#file-upload").set_input_files(r"AB testing Control screenshot.png")
     page.get_by_role("button",name = "Upload").click()
