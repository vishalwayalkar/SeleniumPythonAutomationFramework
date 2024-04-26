from test.Pages.LoginPage import LoginPage
from test.Utilities.ObjectActions import ObjectActions
from selenium.webdriver.common.by import By


class LoginKeywords:
    @staticmethod
    def login_in_with_valid_credential(driver, username, password):
        ObjectActions.set_text(driver, LoginPage.I_USERNAME, username)
        ObjectActions.set_text(driver, LoginPage.I_PASSWORD, password)
        ObjectActions.click(driver, LoginPage.B_LOGIN)
        assert ObjectActions.get_text(driver, (By.XPATH,
                                               '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6')) == "Dashboard"

    @staticmethod
    def log_out(driver):
        ObjectActions.click(driver, (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li'))
        ObjectActions.click(driver, (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'))
        assert ObjectActions.get_text(driver, (By.XPATH,
                                               '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/h5')) == "Login"

    @staticmethod
    def login_in_with_invalid_credential(driver, username, password):
        ObjectActions.set_text(driver, LoginPage.I_USERNAME, username)
        ObjectActions.set_text(driver, LoginPage.I_PASSWORD, password)
        ObjectActions.click(driver, LoginPage.B_LOGIN)
        assert ObjectActions.get_text(driver, LoginPage.P_INVALID_CREDENTIAL) == "Invalid credentials"
