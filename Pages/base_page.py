
class BasePage():
    from selenium.common.exceptions import NoSuchElementException

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (self.NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)
