from playwright.sync_api import sync_playwright, expect
from utils.login_helper import login

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    login(page)

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".inventory_item").first).to_have_count(6)

    browser.close()
