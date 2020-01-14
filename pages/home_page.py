# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 16:58
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : home_page.py
# @Software: PyCharm
import random
import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class HomePage(BaseAction):
    group_control_manage = By.XPATH, '//*[@lay-tips="群控管理"]'
    device_manage = By.XPATH, '//*[@lay-href="groupcontrol/phone/list"]'
    all_choice_btn = By.XPATH, "//*[@class='layui-icon layui-icon-ok']"
    batch_operation_btn = By.XPATH, '//*[@data-type="batchedit"]'
    action_num_xpath = By.XPATH, '//*[@data-id="{}"]'
    action_result_ok_btn = By.XPATH, "//*[@class='layui-layer-btn0']"
    choice_btn = By.XPATH, "//*[@class='layui-icon layui-icon-ok']"
    IMEI = By.XPATH, '//*[@data-field="imei"]'

    def click_group_control_manage(self):
        self.click(self.group_control_manage)

    def click_device_manage(self):
        self.click(self.device_manage)

    def click_all_choice_btn(self):
        self.click(self.all_choice_btn, index=0)

    def click_batch_operation_btn(self):
        self.click(self.batch_operation_btn)

    def click_choice_btn(self, IMEI):
        """
        单选
        :param IMEI: type must be list
        :return: None
        """
        if not isinstance(type(IMEI), list):
            raise TypeError('IMEI must be list')
        choice_btn_list = self.find_elements(self.choice_btn)
        IMEI_list = self.find_elements(self.IMEI)
        del choice_btn_list[0]
        del IMEI_list[0]
        res_dict = {}
        for choice_btn, IMEI_text in zip(choice_btn_list, IMEI_list):
            res_dict[IMEI_text.text] = choice_btn
        for i in IMEI:
            res_dict[str(i)].click()

    def random_click_action_list(self, count):
        action_list = {
            '1001': '关屏幕',
            '1002': '开屏幕',
            # '1003': '重启手机',
            # '1004': '关机',
            '1005': 'home键',
            '1006': '后退键',
            '1007': '上划',
            '1008': '下划',
            '1009': '左划',
            '1010': '右划',
            # '1011': '虚拟定位',
            # '1012': '自定义指令',
            # '2001': '重启软件',
            # '2002': '打开软件首页',
            # '2003': '更新软件',
            # '2004': '上报手机设备信息'
        }

        # action_num_list = [i for i in range(1001, 1013)] + [j for j in range(2001, 2005)]
        # action_ele_list = [(self.action_num_xpath[0], self.action_num_xpath[1].format(i)) for i in action_num_list]
        for i in range(count):
            random_key = random.choice(list(action_list))
            print(action_list[random_key])
            action_ele = self.action_num_xpath[0], self.action_num_xpath[1].format(random_key)
            if i != 0:
                self.click_batch_operation_btn()
            time.sleep(1)
            self.click(action_ele)
            time.sleep(1)
            try:
                self.click(self.action_result_ok_btn)
            except Exception:
                while True:
                    try:
                        self.find_element(self.action_result_ok_btn)
                        self.click(self.action_result_ok_btn)
                        print('第二次点击{}按键'.format(action_list[random_key]))
                        break
                    except Exception:
                        self.click(action_ele)
                        print('重新点击{}按键'.format(action_list[random_key]))
