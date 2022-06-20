from Config.config import Testdata
from page_object.BasePage import BasePage
from selenium.webdriver.common.by import By

from page_object.MyPlanPage import MyPlanPage


class LoginPage(BasePage):
    """By Locators"""
    Cookies = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div/div/div/buttonn')
    Login = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[2]/header/div/section/nav[1]/ul/li[5]/div')
    Email = (By.ID, 'mail')
    Password = (By.ID, 'password')
    Login_button = (By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[2]/div[1]/div[2]/div/div/form/button')

    """constructor of the class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Testdata.Base_URL)
        self.driver.find_element(By.XPATH, '//*[@id="gatsby-focus-wrapper"]/div[1]/div/div/div/button').click()
        self.driver.maximize_window()

    """Page actions for Login"""

    def do_login(self, username, password):
        # self.do_click(self.Cookies)
        self.do_click(self.Login)
        self.do_send_keys(self.Email, username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Login_button)
        return MyPlanPage(self.driver)
