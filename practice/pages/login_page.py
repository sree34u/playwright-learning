
class LoginPage:
    def __init__(self, page):
        self.page = page

    def load(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.page.fill('[data-test="username"]', username)
        self.page.fill('[data-test="password"]', password)
        self.page.get_by_role("button", name="Login").click()