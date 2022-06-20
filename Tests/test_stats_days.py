from datetime import date
from Config.config import Testdata
from Tests.test_base import BaseTest
from page_object.LoginPage import LoginPage


class Test_Status_of_Stats(BaseTest):

    def test_myplan_to_stats_week(self):
        self.loginPage = LoginPage(self.driver)
        myplanpage = self.loginPage.do_login(Testdata.Username, Testdata.Password)
        week_test = myplanpage.navigate_to_stats_week()
        assert week_test == Testdata.Display_Days

    def test_myplan_to_stats_month(self):
        self.loginPage = LoginPage(self.driver)
        myplanpage = self.loginPage.do_login(Testdata.Username, Testdata.Password)
        month_test = myplanpage.navigate_to_stats_month()
        assert month_test == Testdata.Display_month

    def test_myplan_to_stats_year(self):
        self.loginPage = LoginPage(self.driver)
        myplanpage = self.loginPage.do_login(Testdata.Username, Testdata.Password)
        year_test = myplanpage.navigate_to_stats_year()
        current_year = date.today().year
        assert str(current_year) in year_test

