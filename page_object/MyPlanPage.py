import time

from page_object.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyPlanPage(BasePage):
    """By Locators"""
    close_pop_up = (By.CLASS_NAME, 'modal_closeWrapper__BBoXJ')
    see_more_stats = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[2]/div/div/div/div[2]/a/button')
    display_verification = (By.CLASS_NAME, 'title_title__N2u-v')
    month_button = (By.XPATH,
                    '//*[@id="root"]/div/section/section/section/section[2]/section/section/div/div[1]/div/div[2]/div/a[2]')
    year_button = (By.XPATH,
                   '//*[@id="root"]/div/section/section/section/section[2]/section/section/div/div[1]/div/div[2]/div/a[3]')
    account_button = (By.XPATH, '//*[@id="root"]/div/header/div/section/nav[1]/ul/div/div/div/div/div[1]')
    your_account = (By.LINK_TEXT, 'Your Account')
    account_name = (By.CLASS_NAME, 'account-overview_usernameWrapper__Tyo1z')
    edit_profile = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/a/button')
    first_name = (By.ID, 'firstName')
    save_button = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/form/div[6]/div[2]/div/div/button')
    my_plan_button = (By.XPATH, '//*[@id="root"]/div/header/div/section/nav[1]/ul/div/div/a[1]')
    display_profile_name = (By.XPATH, '//*[@id="root"]/div/header/div/section/nav[1]/ul/div/div/div/div/div[1]/span')

    """constructor of the class"""

    def __init__(self, driver):
        super().__init__(driver)

    """Page actions for My PLan"""

    def navigate_to_stats_week(self):
        self.do_click(self.close_pop_up)
        self.do_click(self.see_more_stats)
        week = self.get_element_text(self.display_verification)
        return week

    def navigate_to_stats_month(self):
        self.do_click(self.close_pop_up)
        self.do_click(self.see_more_stats)
        self.do_click(self.month_button)
        month = self.get_element_text(self.display_verification)
        return month

    def navigate_to_stats_year(self):
        self.do_click(self.close_pop_up)
        self.do_click(self.see_more_stats)
        self.do_click(self.year_button)
        year = self.get_element_text(self.display_verification)
        return year

    def navigate_to_account(self):
        self.do_click(self.close_pop_up)
        self.do_click(self.account_button)
        self.do_click(self.your_account)
        username = self.get_element_text(self.account_name)
        return username

    def navigate_to_profile(self):
        time.sleep(2)
        self.do_click(self.close_pop_up)
        self.do_click(self.account_button)
        self.do_click(self.your_account)
        self.do_click(self.edit_profile)
        self.do_send_keys(self.first_name, Keys.CONTROL + "a")
        self.do_send_keys(self.first_name, Keys.DELETE)
        self.do_send_keys(self.first_name, "Rahul The QA")
        self.do_click(self.save_button)
        self.do_click(self.my_plan_button)
        profile_name = self.get_element_text(self.display_profile_name)
        return profile_name
