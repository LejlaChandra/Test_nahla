from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    def __init__(self, driver):
        self.selenium_driver = driver
        self.wait = WebDriverWait(driver, timeout=70)
    
    def go_to(self):
        self.selenium_driver.get("https://www.saucedemo.com/")
        self.selenium_driver.maximize_window()
    
    def login(self, username, password):
        login_link_locator = (By.ID, "login_button_container")
        wait_login_link = self.wait.until(EC.element_to_be_clickable(login_link_locator))
        wait_login_link.click()

        username_field_locator = (By.ID, "user-name")
        wait_username_field = self.wait.until(EC.element_to_be_clickable(username_field_locator))
        wait_username_field.click()
        wait_username_field.clear()
        wait_username_field.send_keys(username)

        password_field = self.selenium_driver.find_element(By.ID, "password")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.selenium_driver.find_element(By.ID, "login-button")
        login_button.click()

    def is_login_invisible(self):
        login_link_locator = (By.ID, "login_button_container")
        self.wait.until(EC.invisibility_of_element_located(login_link_locator))      
    
     
    def check_products_page(self):
        products_page_tuple = (By.XPATH, "//span[text() = 'Products']")
        wait_products_page = self.wait.until(EC.element_to_be_clickable(products_page_tuple))

        products_page_text = wait_products_page.text
        return products_page_text
    
    def add_to_cart_backpack(self):
        add_to_cart_backpack_button_locator = (By.ID, "add-to-cart-sauce-labs-backpack")
        wait_add_to_cart_backpack_button = self.wait.until(EC.element_to_be_clickable(add_to_cart_backpack_button_locator))
        wait_add_to_cart_backpack_button.click()

    def is_backpack_added(self):
        add_backpack_locator = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.wait.until(EC.invisibility_of_element_located(add_backpack_locator))
        
    def add_to_cart_jacket(self):
        add_to_cart_jacket_button_locator = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        wait_add_to_cart_jacket_button = self.wait.until(EC.element_to_be_clickable(add_to_cart_jacket_button_locator))
        wait_add_to_cart_jacket_button.click()

    def is_jacket_added(self):
        add_jacket_locator = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.wait.until(EC.invisibility_of_element_located(add_jacket_locator ))

        cart_button = self.selenium_driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a/span")   
        cart_button.click()

    def your_cart(self):
        your_cart_locator = (By.CSS_SELECTOR, "span.title")
        self.wait.until (EC.text_to_be_present_in_element(your_cart_locator, "Your Cart"))
        
    
    def selected_backpack (self):
        selected_backpack_locator = (By.CSS_SELECTOR, "#item_4_title_link > div.inventory_item_name")
        wait_selected_backpack = self.wait.until(EC.element_to_be_clickable(selected_backpack_locator))
        selected_backpack_text = wait_selected_backpack.text
        return selected_backpack_text
    
    def selected_jacket (self):
        selected_jacket_locator = (By.CSS_SELECTOR, "#item_5_title_link > div.inventory_item_name")
        wait_selected_jacket = self.wait.until(EC.element_to_be_clickable(selected_jacket_locator))
        selected_jacket_text = wait_selected_jacket.text
        return selected_jacket_text
    
    def checkout_button(self):
        checkout_button_locator = (By.ID, "checkout")
        wait_checkout_button = self.wait.until(EC.element_to_be_clickable(checkout_button_locator))
        wait_checkout_button.click()

    def checkout_page (self):
        checkout_page_locator = (By. CSS_SELECTOR, "span.title")
        self.wait.until (EC.text_to_be_present_in_element(checkout_page_locator, "Checkout: Your Information"))
    
    def first_name(self, firstName):
        first_name_locator = (By.ID, "first-name")
        wait_first_name_field = self.wait.until(EC.element_to_be_clickable(first_name_locator))
        wait_first_name_field.click()
        wait_first_name_field.clear()
        wait_first_name_field.send_keys(firstName)
    
    def last_name(self, lastName):
        last_name_locator = (By.ID, "last-name")
        wait_last_name = self.wait.until(EC.element_to_be_clickable(last_name_locator))
        wait_last_name.click()
        wait_last_name.clear()
        wait_last_name.send_keys(lastName)

    def zipcode(self, zipCode):
        zipcode_locator = (By.ID, "postal-code")
        wait_zipcode = self.wait.until(EC.element_to_be_clickable(zipcode_locator))
        wait_zipcode.click()
        wait_zipcode.clear()
        wait_zipcode.send_keys(zipCode)

        continue_button = self.selenium_driver.find_element(By.ID, "continue")
        continue_button.click()

    def overview_page(self):
        overview_page_locator = (By.CSS_SELECTOR, "span.title")
        self.wait.until(EC.text_to_be_present_in_element(overview_page_locator, "Checkout: Overview"))
        
    def overview_backpack (self):
        overview_backpack_locator = (By.XPATH, "//*[@id='item_4_title_link']/div")
        wait_overview_backpack = self.wait.until(EC.element_to_be_clickable(overview_backpack_locator))
        overview_backpack_text = wait_overview_backpack.text
        return overview_backpack_text
    
    def overview_jacket (self):
        overview_jacket_locator = (By.XPATH, "//*[@id='item_5_title_link']/div")
        wait_overview_jacket = self.wait.until(EC.element_to_be_clickable(overview_jacket_locator))
        overview_jacket_text = wait_overview_jacket.text
        return overview_jacket_text
  
    def finish_button(self):
        finish_button_locator = (By.ID, "finish")
        wait_finish_button = self.wait.until(EC.element_to_be_clickable(finish_button_locator))
        wait_finish_button.click()
     
    def checkout_completed (self):
        checkout_completed_locator = (By.XPATH, "//*[@id='header_container']/div[2]/span")
        self.wait.until (EC.text_to_be_present_in_element(checkout_completed_locator, "Checkout: Complete!"))
    
        menu_button = self.selenium_driver.find_element (By.ID, "react-burger-menu-btn")
        menu_button.click()
    
    def logout_button(self):
        logout_button_locator = (By.ID, "logout_sidebar_link")
        wait_logout_button = self.wait.until(EC.element_to_be_clickable(logout_button_locator))
        wait_logout_button.click()
 
    def are_you_back_to_login_page (self):
        login_container = self.selenium_driver.find_element(By.ID, "login_button_container")
        login_container.click()
        
        