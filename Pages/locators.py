from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_VIEW = (By.ID, "login_form")
    REGISTRATION_VIEW = (By.ID, "register_form")
