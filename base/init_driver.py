# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 16:45
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : init_driver.py
# @Software: PyCharm
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class InitDriver(object):

    driver = None

    @classmethod
    def init_driver(cls):
        if not cls.driver:
            # chrome_options = Options()
            # chrome_options.add_argument('--disable-infobars')
            # # # chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            # # # chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
            # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            # # # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # # # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            # # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            # # # chrome_options.add_argument("user-agent='iphone'")  # 伪装user-agent 成iPhone
            # cls.driver = webdriver.Chrome(chrome_options=chrome_options)
            cls.driver = webdriver.Chrome()
            # cls.driver = webdriver.Firefox()
            cls.driver.maximize_window()
            cls.driver.get("https://webadmin.jd100.com/")
            cls.driver.implicitly_wait(10)
        return cls.driver


if __name__ == '__main__':
    driver = InitDriver.init_driver()
    time.sleep(3)
    # driver.get_screenshot_as_file("./demo.png")
    driver.quit()
