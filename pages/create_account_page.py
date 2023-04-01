from selenium.webdriver.common.by import By
from locators.create_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


class CreateAccountPage(BasePage):


    def __init__(self, driver):
        super().__init__(driver)
        self.url = "http://164.92.218.36:8080/login?create_account=1"
        

    def load(self):
        self.driver.get(self.url)

    
    def form_sir_or_madam(self, form="sir"):
        if form == 'sir':
            return self.driver.find_element(*CreateAccountPageLocators.SIR)
        else:
            return self.driver.find_element(*CreateAccountPageLocators.MADAM)

    @property
    def first_name(self):
        return self.driver.find_element(*CreateAccountPageLocators.FIRST_NAME)
    
    @property
    def last_name(self):
        return self.driver.find_element(*CreateAccountPageLocators.LAST_NAME)
    
    @property
    def email(self):
        return self.driver.find_element(*CreateAccountPageLocators.EMAIL)
    
    @property
    def password(self):
        return self.driver.find_element(*CreateAccountPageLocators.PASSWORD)
    
    @property
    def birthday(self):
        return self.driver.find_element(*CreateAccountPageLocators.BIRTHDAY)
    
    @property
    def submit_button(self):
        return self.driver.find_element(*CreateAccountPageLocators.SUBMIT_BUTTON)
    
    @property
    def advertising_chbx(self):
        return self.driver.find_element(*CreateAccountPageLocators.ADVERTISING)
    
    @property
    def customer_privacy_chbx(self):
        return self.driver.find_element(*CreateAccountPageLocators.CUSTOMER_PRIVACY)
    
    @property
    def newsletter_chbx(self):
        return self.driver.find_element(*CreateAccountPageLocators.NEWSLETTER)
    
    @property
    def policy_chbx(self):
        return self.driver.find_element(*CreateAccountPageLocators.POLICY)

    def create_account(self, first_name, last_name, email, password, birthday, form, checkboxes='no'):
        self.form_sir_or_madam(form).click()
        self.first_name.send_keys(first_name)
        self.last_name.send_keys(last_name)
        self.email.send_keys(email)
        self.password.send_keys(password)
        self.birthday.send_keys(birthday)
        if checkboxes == 'yes':
            self.advertising_chbx.click()
            self.customer_privacy_chbx.click()
            self.newsletter_chbx.click()
            self.policy_chbx.click()

        self.submit_button.click()

    @property
    def success_message(self):
        return self.driver.find_element(*CreateAccountPageLocators.SUCCESS_MSG)
    
    @property
    def get_success_message(self):
        return self.success_message.text

    @property
    def error_message(self):
        return self.driver.find_element(*CreateAccountPageLocators.ERROR_MSG)
    
    @property
    def get_error_message(self):
        return self.error_message.text
    
    @property
    def title(self):
        return self.driver.find_element(*CreateAccountPageLocators.PAGE_TITLE)

    @property
    def get_page_title(self):
        return self.title.text
