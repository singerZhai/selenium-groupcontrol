# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 17:04
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : test_stable.py
# @Software: PyCharm
import unittest
from base.init_driver import InitDriver
from pages.home_page import HomePage
from pages.login_page import LoginPage


class TestStable(unittest.TestCase):

    driver = InitDriver.init_driver()
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    def tearDown(self):
        self.driver.quit()

    def test_stable(self):
        self.login_page.login()
        self.home_page.click_group_control_manage()
        self.home_page.click_device_manage()
        # self.home_page.click_all_choice_btn()
        self.home_page.click_choice_btn([99001178684004])
        self.home_page.click_batch_operation_btn()
        self.home_page.random_click_action_list(1000)


if __name__ == '__main__':
    unittest.main()
