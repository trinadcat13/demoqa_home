from pages.swag_labs import SwagLabs
def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()
    assert swag_labs_page.exist_login()
    assert swag_labs_page.exist_password()