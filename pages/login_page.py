# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 16:48
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.init_driver import InitDriver


class LoginPage(BaseAction):

    username = By.ID, 'LAY-user-login-username'
    password = By.ID, 'LAY-user-login-password'
    login_btn = By.XPATH, '//*[@class="layui-btn layui-btn-fluid"]'

    def input_username(self, username):
        self.input_text(self.username, username)

    def input_pwd(self, password):
        self.input_text(self.password, password)

    def click_login(self):
        self.click(self.login_btn)

    def login(self):
        self.input_username('luoheng')
        self.input_pwd('123456')
        self.click_login()


if __name__ == '__main__':
    LoginPage(InitDriver().init_driver()).login()
