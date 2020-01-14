# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 13:03
# @Author  : zhaihuide@jiandan100.cn
# @Site    : 
# @File    : demo.py
# @Software: PyCharm


# demo = '2020年01月02日'
# # print(len(demo))
# res = demo[0:5]
# for i in demo[5:]:
#     if i != '0':
#         res += i
# print(res)
# import datetime
#
# now = datetime.datetime.now()
# print(now.strftime('%Y-%m-%d'))
# year = str(int(now.strftime('%Y')))
# month = str(int(now.strftime('%m')))
# day = str(int(now.strftime('%d')))
# a = year + '年' + month + '月' + day + '日'
# print(a)

demo = {
    '1001': '关屏幕',
    '1002': '开屏幕',
    '1003': '重启手机',
    '1004': '关机',
    '1005': 'home键',
    '1006': '后退键',
    '1007': '上划',
    '1008': '下划',
    '1009': '左划',
    '1010': '右划',
    '1011': '虚拟定位',
    '1012': '自定义指令',
    '2001': '重启软件',
    '2002': '打开软件首页',
    '2003': '更新软件',
    '2004': '上报手机设备信息'
}
import random

print(random.choice(list(demo)))