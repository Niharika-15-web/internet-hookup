from playwright.sync_api import Page,expect
def test_drag_drop(page:Page):
    page.goto("https://the-internet.herokuapp.com/")
    expect(page.get_by_role("link",name ="Drag and Drop"))
    page.get_by_role("link",name ="Drag and Drop").click()
    box_a = page.locator("#column-a")
    box_b = page.locator("#column-b")
    box_a.drag_to(box_b)
    box_b.drag_to(box_a)
    page.screenshot(path = "Drag_drop screenshot.png")
