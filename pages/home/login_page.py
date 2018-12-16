from selenium.webdriver.common.by import By
from base.basepage import BasePage
from utilities.custom_logger import customLogger
import logging
import pytest


class LoginPage(BasePage):

    log = customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailFIeld(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPassField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLogginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickLoginLink(self):
        #self.getLoginLink().click()
        self.elementClick("linktext", self._login_link)

    def enterEmail(self, email):
        #self.getEmailFIeld().send_keys(username)
        self.elementSendKeys(email, "id", self._email_field)

    def enterPassword(self, password):
        #self.getPassField().send_keys(password)
        self.elementSendKeys(password, "id", self._password_field)

    def clickLoginButton(self):
        #self.getLogginButton().click()
        self.elementClick("name", self._login_button)

    def Login(self, username="", password=""):
        self.clickLoginLink()
        self.enterEmail(username)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.islementPresent("xpath", "//*[@id='navbar']//span[text()='Test User']")
        return result

    def verifyLoginFailed(self):
        result = self.islementPresent("xpath", "//div[contains(text(), 'Invalid email or password')]")
        return result

    def verifyTitle(self):
        return self.verifyPageTitle("google")
