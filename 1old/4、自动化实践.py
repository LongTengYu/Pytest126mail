from selenium import webdriver
from old.PublicLogin import *

import csv

# 读取CSV文件
alldata = csv.reader(open('E:\Python教学\Selenium教学\Test01\测试数据.csv'))

for data in alldata:
    username = data[0]  # 用户名
    password = data[1]  # 密码
    mailaddres = data[2]  # 收件地址
    mailtitle = data[3]  # 邮件标题
    mailtext = data[4]  # 邮件正文

    driver = webdriver.Chrome()  # 调用谷歌浏览器
    driver.maximize_window()  # 窗口最大化
    driver.get('https://mail.126.com/')  # 打开126邮箱
    sleep(2)

    # 调用登录方法，并传参
    Log().Login(driver, username, password)
    sleep(5)

    # 调用发送邮件方法
    Log().Body(driver, mailaddres, mailtitle, mailtext)

    # 调用登出方法
    Log().Logout(driver)
    sleep(5)

    driver.close()

driver.quit()
