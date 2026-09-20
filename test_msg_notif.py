from playwright.sync_api import Page,expect
def test_msg_notif(page:Page):
    page.goto("https://the-internet.herokuapp.com/notification_message_rendered")
    page.get_by_role("link", name = "Click here").click()
    expect(page.get_by_role("heading", name = "Notification Message")).to_be_visible()

    notification = page.locator("#flash")

    text = notification.inner_text()
    assert "Action unsuccesful, please try again" in text  or "Action successful" in text