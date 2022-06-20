from Config.config import Testdata
from Tests.test_base import BaseTest
from page_object.LoginPage import LoginPage


class Test_account_details(BaseTest):

    def test_account_id(self):
        self.loginPage = LoginPage(self.driver)
        myplanpage = self.loginPage.do_login(Testdata.Username, Testdata.Password)
        account_user_id = myplanpage.navigate_to_account()
        assert account_user_id == Testdata.Username

    def test_account_edit_property(self):
        self.loginPage = LoginPage(self.driver)
        myplanpage = self.loginPage.do_login(Testdata.Username, Testdata.Password)
        account_profile_name= myplanpage.navigate_to_profile()
        assert account_profile_name == Testdata.Display_Profile_name