from selenium.webdriver.common.by import By
import time
from conftest import driver
from locators.login_page_locators import LoginPageLocators
from pages.create_account_page import CreateAccountPage
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://164.92.218.36:8080/login?back=my-account"
        
    def load(self):
        self.driver.get(self.url)

    @property
    def email_field(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL_FIELD)
    
    @property
    def password_field(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
    
    @property
    def submit_btn(self):
        return self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON)
    
    @property
    def error_message(self):
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE)
    
    @property
    def get_error_message(self):
        time.sleep(4)
        return self.error_message.text

    def login(self, username, password):
        time.sleep(2)
        self.email_field.send_keys(username)
        time.sleep(2)
        self.password_field.send_keys(password)
        time.sleep(2)
        self.submit_btn.click()
        time.sleep(2)
    
    def go_to_create_account_page(self):
        def create_account():
            self.driver.find_element(By.LINK_TEXT, "Немає профілю? Створіть зараз").click()
            time.sleep(7)
            return CreateAccountPage(self.driver)
        return create_account
