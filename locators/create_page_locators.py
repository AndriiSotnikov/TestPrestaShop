from selenium.webdriver.common.by import By

class CreateAccountPageLocators:
    SIR = (By.ID, "field-id_gender-1")
    MADAM = (By.ID, "field-id_gender-2")
    FIRST_NAME = (By.ID, "field-firstname")
    LAST_NAME = (By.ID, "field-lastname")
    EMAIL = (By.ID, "field-email")
    PASSWORD = (By.ID, "field-password")
    BIRTHDAY = (By.ID, "field-birthday")
    SUBMIT_BUTTON = (By.XPATH, "//*[@data-link-action='save-customer']")
    SUCCESS_MSG = (By.XPATH, "//div[@class='alert alert-success']")
    ERROR_MSG = (By.XPATH, "//*[@class='alert alert-danger']")

    ADVERTISING = (By.XPATH, "//input[@name='optin']")
    CUSTOMER_PRIVACY = (By.XPATH, "//input[@name='customer_privacy']")
    NEWSLETTER = (By.XPATH, "//input[@name='newsletter']")
    POLICY = (By.XPATH, "//input[@name='psgdpr']")
    PAGE_TITLE = (By.CSS_SELECTOR, ".page-header")