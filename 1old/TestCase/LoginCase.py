import sys
import os
path='E:\GitTest\126mail(Pytest)'  #获取相对路径并将路径中'/'转换为'\\'
sys.path.append(path+'\\Models') #因Jenkins构建时无法找到自添加文件，所以需要将自添加文件夹写入环境变量中
sys.path.append(path+'\\Public')
sys.path.append(path+'\\TestCase')
sys.path.append(path+'\\Report')
from MyUnittest import Mytest
from Screenshot import insert_img
from time import *
import pytest
class LoginTest(Mytest):

    username = 'yuxiao8520'  # 声明用户名
    password = '5esHc2Tp5nMUL'  # 声明密码

    def test_user_login(self):  # 登录成功测试模块

       self.log.type_username(self.username)  # 调用用户名方法
       self.log.type_password(self.password)  # 调用密码方法
       self.log.submit()  # 调用登录按钮方法
       sleep(10)
       success=self.log.type_success() #获取登录信息

       self.assertEqual(success,'yuxiao8520@126.com',msg='登录成功')  #判断是否登录成功
       t = '登录成功'+strftime("%Y-%m-%d %H_%M_%S")  #获取当前时间
       insert_img(self.driver,t)  #截图

    def test_user_error(self):  # 账号为空测试模块

        self.log.type_password(self.password)  # 调用密码方法
        self.log.submit()  # 调用登录按钮方法
        sleep(2)
        success = self.log.type_error() #获取错误提示信息
        self.log.type_clear()  #清除输入的信息

        if success != '请输入帐号':  #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
            insert_img(self.driver, '账号不能为空')  #截图
            self.assertEqual(success, '请输入帐号', msg='账号不能为空')  #返回错误提示

    def test_password_error(self): # 密码为空测试模块

        self.log.type_username(self.username)  # 调用用户名方法
        self.log.submit()  # 调用登录按钮方法
        sleep(2)
        success = self.log.type_error() #获取错误提示信息
        self.log.type_clear()  #清除输入的信息

        if success != '请输入密码':  #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
            insert_img(self.driver, '密码不能为空') #截图
            self.assertEqual(success, '请输入密码', msg='密码不能为空') #返回错误提示

    def test_up_error(self):  # 帐号或密码错误测试模块

        self.log.type_username(self.username)  # 调用用户名方法
        self.log.type_password('1')  # 调用密码方法
        self.log.submit()  # 调用登录按钮方法
        sleep(2)
        success = self.log.type_error() #获取错误提示信息
        self.log.type_clear()  #清除输入的信息

        if success != '帐号或密码错误': #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
            insert_img(self.driver, '帐号或密码错误') #截图
            self.assertEqual(success, '帐号或密码错误',msg='帐号或密码错误') #返回错误提示

if __name__=='__main__':
    # main()
    pytest.main(['LoginCase.p::LoginTest::test_user_login'])