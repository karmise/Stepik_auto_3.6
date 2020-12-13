import time


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    butt = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket').text
    assert len(butt) != 0
