
class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_backpack_to_cart(self):
        self.page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge")