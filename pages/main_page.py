from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://164.92.218.36:8080/"
         
    @property
    def user_information(self):
        return self.driver.find_element(*MainPageLocators.USER_INFO)
    
    @property
    def get_user_information(self):
        return self.user_information.text
    
    @property
    def logout(self):
        return self.driver.find_element(*MainPageLocators.LOGOUT)