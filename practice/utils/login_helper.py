def login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill('[data-test="username"]', "standard_user")
    page.fill('[data-test="password"]', "secret_sauce")
    page.get_by_role("button", name="Login").click()
    return page