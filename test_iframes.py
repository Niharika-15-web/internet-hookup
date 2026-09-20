from playwright.sync_api import Page,expect
def test_iframes(page:Page):
    page.goto("https://the-internet.herokuapp.com/nested_frames")
    top_frame = page.frame(name = 'frame-top')
    left_frame = top_frame.child_frames[0]
    expect(left_frame.locator("body")).to_contain_text("LEFT")

    middle_frame = top_frame.child_frames[1]
    expect(middle_frame.locator("body")).to_contain_text("MIDDLE")

    right_frame = top_frame.child_frames[2]
    expect(right_frame.locator("body")).to_have_text("RIGHT")


