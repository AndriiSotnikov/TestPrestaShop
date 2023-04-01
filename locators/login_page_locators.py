from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_FIELD = (By.ID, "field-email")
    PASSWORD_FIELD = (By.ID, "field-password")
    SUBMIT_BUTTON = (By.ID, "submit-login")
    ERROR_MESSAGE = (By.XPATH, "//*[@class='alert alert-danger']")
    CREATE_ACC_LINK = (By.LINK_TEXT, "Немає профілю? Створіть зараз")
