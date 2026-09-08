from pages.base_page import BasePage
from playwright.sync_api import expect


class ProductPage(BasePage):

    PRODUCTS_TITLE = '[data-test="title"]'
    SHOPPING_CART = '[data-test="shopping-cart-link"]'
    PRODUCT = '[data-test="inventory-item"]'
    PRODUCT_NAME = '[data-test="inventory-item-name"]'

    def verify_products_page(self):
        expect(
            self.page.locator(self.PRODUCTS_TITLE)
        ).to_have_text("Products")

    def add_product_to_cart(self, product_name):
        product = self.page.locator(self.PRODUCT).filter(
            has=self.page.locator(self.PRODUCT_NAME).get_by_text(
                product_name,
                exact=True
            )
        )

        expect(product).to_be_visible()

        product.get_by_role(
            "button",
            name="Add to cart"
        ).click()

    def click_cart(self):
        self.page.locator(self.SHOPPING_CART).click()

    def verify_product_in_cart(self, product_name):
        expect(
            self.page.get_by_text(product_name, exact=True)
        ).to_be_visible()
        