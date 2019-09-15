import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_button_exist(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket"),\
        "There is no 'Add to Cart' button on the page"
