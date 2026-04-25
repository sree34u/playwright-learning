from playwright.sync_api import sync_playwright, expect
from utils.login_helper import login

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    login(page)

    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-bike-light\"]").click()

    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Backpack") #use exact match + count
    # expect(page.locator("[data-test=\"inventory-item-price\"]")).to_contain_text("$29.99") price check is fragile currency values change.
    expect(page.locator("[data-test=\"shopping-cart-link\"]")).to_contain_text("1")


    browser.close()