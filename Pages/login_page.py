from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert self.browser.current_url.count('/login/'), 'URL not contains /login/'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_VIEW), "Login view is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_VIEW), "Registration view is not presented"
