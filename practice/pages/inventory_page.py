
class InventoryPage:
    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self, product_name):
        self.page.locator(f".inventory_item:has-text('{product_name}')").get_by_role("button", name= "Add to cart").click()

    def open_cart(self):
        self.page.locator('[data-test="shopping-cart-link"]').click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge")