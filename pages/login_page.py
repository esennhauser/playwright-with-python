from pages.base_page import BasePage
from playwright.sync_api import expect


class LoginPage(BasePage):

    USERNAME_INPUT = '[data-test="username"]'
    PASSWORD_INPUT = '[data-test="password"]'
    LOGIN_BUTTON = '[data-test="login-button"]'
    ERROR_MESSAGE = ".error-message-container"

    def fill_credentials(self, username, password):
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_login(self):
        self.page.locator(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.fill_credentials(username, password)
        self.click_login()

    def verify_dashboard(self):
        products_title = self.page.locator('[data-test="title"]')
        expect(products_title).to_be_visible()

    def verify_login_error(self, message):
        expect(self.page.locator(self.ERROR_MESSAGE)).to_contain_text(message)
