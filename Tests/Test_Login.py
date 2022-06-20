from Config.config import Testdata
from Tests.test_base import BaseTest
from page_object.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_logging(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(Testdata.Username, Testdata.Password)
