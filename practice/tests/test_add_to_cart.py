from playwright.sync_api import expect
from practice.pages.login_page import LoginPage
from practice.pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_product_to_cart("Sauce Labs Backpack")

    expect(inventory_page.get_cart_count()).to_have_text("1")