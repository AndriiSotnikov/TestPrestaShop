from selenium.webdriver.common.by import By

class MainPageLocators:
    USER_INFO = (By.ID, "_desktop_user_info")
    LOGOUT = (By.XPATH, "//a[@class='logout hidden-sm-down']")
