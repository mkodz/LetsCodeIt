from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.Login("test@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "title is correct")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.finalMark("test_validLogin", result2, "login is successful")

    @pytest.mark.run(order=1)
    def test_InValidLogin(self):
        self.lp.Login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True
