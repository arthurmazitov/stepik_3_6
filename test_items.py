link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_submit(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button.text == "Añadir al carrito"
