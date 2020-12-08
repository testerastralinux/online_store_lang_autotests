from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_busket_button_exist(browser):
    browser.get(link)
    try:
        buttons = browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        assert False, "Add to basket button not found!"
