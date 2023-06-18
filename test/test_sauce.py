from pages.home_page import HomePage

def test_login(driver):
    home_page = HomePage(driver)
    home_page.go_to()
    home_page.login("standard_user", "secret_sauce")
    home_page.is_login_invisible
    assert home_page.check_products_page() == "Products"
    home_page.add_to_cart_backpack
    home_page.is_backpack_added
    home_page.add_to_cart_jacket
    home_page.is_jacket_added
    home_page.your_cart
    assert home_page.selected_backpack() == "Sauce Labs Backpack"
    assert home_page.selected_jacket() == "Sauce Labs Fleece Jacket"
    home_page.checkout_button
    home_page.checkout_page
    home_page.first_name("lejla")
    #home_page.last_name("romano")
    #home_page.checkout_info("lejla", "romano", "72000")
    #home_page.overview_page
    #assert home_page.overview_backpack() == "Sauce Labs Backpack"
    #assert home_page.overview_jacket() == "Sauce Labs Fleece Jacket"
    #home_page.finish_button
    #home_page.checkout_completed
    #home_page.logout_button
    #assert home_page.are_you_back_to_login_page == True

    



