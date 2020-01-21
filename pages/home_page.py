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
    # 因selenium定位操作list中的元素有偶现的bug，故使用js
    click_action_num_css_js = "document.querySelector(\"button[data-id='{}']\").click()"
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
        if not isinstance(IMEI, list):
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
            # '1001': '关屏幕',
            # '1002': '开屏幕',
            # '1003': '重启手机',
            # '1004': '关机',
            # '1005': 'home键',
            # '1006': '后退键',
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

        for i in range(count):
            random_key = random.choice(list(action_list))
            print(action_list[random_key])
            if i != 0:
                self.click_batch_operation_btn()
            time.sleep(1)
            self.driver.execute_script(self.click_action_num_css_js.format(random_key))
            time.sleep(1)
            self.click(self.action_result_ok_btn)
            time.sleep(1)
