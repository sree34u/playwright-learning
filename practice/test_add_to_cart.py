from playwright.sync_api import sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.get_cart_count()).to_have_text("1")

    browser.close()