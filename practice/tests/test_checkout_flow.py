from playwright.sync_api import sync_playwright, expect
import re
from utils.login_helper import login

with sync_playwright() as p:
    browser = p.chromium.launch(headless= False)
    page = browser.new_page()

    login(page)

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()
    page.locator('[data-test="shopping-cart-link"]').click()
    
    page.locator('[data-test="checkout"]').click()
    page.fill('[data-test="firstName"]', "Sree")
    page.fill('[data-test="lastName"]', "Nath")
    page.fill('[data-test="postalCode"]', "547890")
    page.get_by_role('button', name= "Continue").click()

    expect(page.locator("[data-test='title']")).to_contain_text(re.compile(r"Checkout:\s*Overview"))
    expect(page.locator("[data-test='total-label']")).to_have_text(re.compile(r"^Total:\s*\$\d+(\.\d{1,2})?$"))
    page.locator("[data-test='finish']").click()
    expect(page.locator('[data-test="complete-header"]')).to_be_visible()
    expect(page.locator('[data-test="complete-header"]')).to_have_text(re.compile(r"Thank you for your order!"))
