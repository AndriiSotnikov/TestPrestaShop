
from pages.login_page import LoginPage
from pages.create_account_page import CreateAccountPage
from pages.main_page import MainPage
import time
import pytest
from test_data.test_data import WholeStoreData


class TestPrestaShop:


    @pytest.fixture(scope='function', autouse=True)
    def logout_if_authorized(request, driver):
        yield
        main_page = MainPage(driver)
        if 'Вийти' in main_page.get_user_information:
            time.sleep(1)
            main_page.logout.click()
            time.sleep(3)


    def test_successful_login_v2(self, driver, login_data, name="John", last_name="Doe"):
        email, password = login_data
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        login_page.load()
    
        login_page.login(email, password)
        assert main_page.get_user_information == f'\ue7ff Вийти {name} {last_name}'


   
    def test_unsuccessful_login(self, driver, email="incorrect_username@gmail.com", password="incorrect_password"):
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login(email, password)
        assert login_page.get_error_message == WholeStoreData.login_alert

   
    def test_navigation_to_create_account(self, driver):
        login_page = LoginPage(driver)
        login_page.load()
        create_account = login_page.go_to_create_account_page()
        create_account_page = create_account()
        assert create_account_page.get_page_title == WholeStoreData.reg_page_title

    
    def test_successful_account_creation(self, driver, name="John", last_name="Doe", email="johndoe1001@example.com", password="password", birth="1995-04-07", form="sir", checkboxes="yes"):
        create_account_page = CreateAccountPage(driver)
        create_account_page.load()
        create_account_page.create_account(name, last_name, email, password, birth, form, checkboxes)
        time.sleep(5)
        main_page = MainPage(driver)
        assert main_page.get_user_information == f'\ue7ff Вийти {name} {last_name}'

    
    def test_unsuccessful_account_creation(self, driver, name="John", last_name="Doe", email="johndoe7@example.com", password="password", birth="1995-04-07", form="sir", checkboxes="yes"):
        create_account_page = CreateAccountPage(driver)
        create_account_page.load()
        create_account_page.create_account(name, last_name, email, password, birth, form, checkboxes)
        time.sleep(2)
        assert create_account_page.get_error_message == WholeStoreData.email_in_use_alert