from playwright.sync_api import Page,expect
def test_file_download(page:Page):
    page.goto("https://the-internet.herokuapp.com/download")

    with page.expect_download() as download_info:
     page.get_by_role("link", name = "somefile.txt", exact = True).click()
     download = download_info.value
     download.save_as("somefile.txt")
