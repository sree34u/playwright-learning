from playwright.sync_api import expect

class ExamplePage:
    def __init__(self,page):
        self.page = page

    def open(self):
        self.page.goto("https://example.com")

    def assert_title(self):
        expect(self.page).to_have_title("Example Domain")

    def assert_heading(self):
        expect(self.page.get_by_role("heading")).to_have_text("Example Domain")