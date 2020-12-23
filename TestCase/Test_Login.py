from Public.SetUp_TearDown import su_td
from PageObject.LoginPage import Login
from time import *
import allure

@allure.feature('登录模块')  #声明模块名称
@allure.description('用例描述')  #声明描述
@allure.suite('登录套件')
class Test_Login1(su_td,Login):

    username = 'yuxiao8520'  # 声明用户名
    password = '5esHc2Tp5nMULGa'  # 声明密码
    def test_user_login(self):  # 登录成功测试模块
       self.type_iframe()
       self.type_username(self.username)  # 调用用户名方法
       self.type_password(self.password)  # 调用密码方法
       self.submit()  # 调用登录按钮方法
       self.parentframe() #跳出登录框
       sleep(5)
       success=self.type_success() #获取登录信息
       if success=='yuxiao8520@126.com':
           filename = '登录成功' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
           dir = su_td().insert_img(self.driver, filename)  # 截图
           with allure.step('用户名：Long 密码：123456'):
               file = open(dir, mode='rb').read()
               allure.attach(file, '添加图片', allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
       else:
           t = '登录失败' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
           su_td().insert_img(self.driver, t)  # 截图
           self.assertEqual(success, 'yuxiao8520@126.com', msg='登录失败')  # 判断是否登录成功

    # @allure.link('https://mail.126.com/')
    # @allure.title('登录成功测试')
    # def test_user_login(self):  # 登录成功测试模块
    #
    #    self.log.type_username(self.username)  # 调用用户名方法
    #    self.log.type_password(self.password)  # 调用密码方法
    #    self.log.submit()  # 调用登录按钮方法
    #    self.log.parentframe() #跳出登录框
    #    sleep(5)
    #    success=self.log.type_success() #获取登录信息
    #    if success=='yuxiao8520@126.com':
    #        filename = '登录成功' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
    #        dir = su_td().insert_img(self.driver, filename)  # 截图
    #        with allure.step('用户名：Long 密码：123456'):
    #            file = open(dir, mode='rb').read()
    #            allure.attach(file, '添加图片', allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
    #    else:
    #        t = '登录失败' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
    #        su_td().insert_img(self.driver, t)  # 截图
    #        self.assertEqual(success, 'yuxiao8520@126.com', msg='登录失败')  # 判断是否登录成功


    # @allure.title('账号为空测试')
    # def test_user_error(self):  # 账号为空测试模块
    #
    #     self.log.type_password(self.password)  # 调用密码方法
    #     self.log.submit()  # 调用登录按钮方法
    #     sleep(2)
    #     success = self.log.type_error() #获取错误提示信息
    #     self.log.type_clear()  #清除输入的信息
    #
    #     if success != '请输入帐号':  #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
    #         su_td().insert_img(self.driver, '账号不能为空')  #截图
    #         self.assertEqual(success, '请输入帐号', msg='账号不能为空')  #返回错误提示
    #
    # @allure.title('密码为空测试')
    # def test_password_error(self): # 密码为空测试模块
    #
    #     self.log.type_username(self.username)  # 调用用户名方法
    #     self.log.submit()  # 调用登录按钮方法
    #     sleep(2)
    #     success = self.log.type_error() #获取错误提示信息
    #     self.log.type_clear()  #清除输入的信息
    #
    #     if success != '请输入密码':  #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
    #         su_td().insert_img(self.driver, '密码不能为空') #截图
    #         self.assertEqual(success, '请输入密码', msg='密码不能为空') #返回错误提示
    #
    # @allure.title('帐号或密码错误测试')
    # def test_up_error(self):  # 帐号或密码错误测试模块
    #
    #     self.log.type_username(self.username)  # 调用用户名方法
    #     self.log.type_password('1')  # 调用密码方法
    #     self.log.submit()  # 调用登录按钮方法
    #     sleep(2)
    #     success = self.log.type_error() #获取错误提示信息
    #     self.log.type_clear()  #清除输入的信息
    #
    #     if success != '帐号或密码错误': #根据错误信息判断测试结果是否成功，若不成功则截图保存并返回错误提示
    #         su_td().insert_img(self.driver, '帐号或密码错误') #截图
    #         self.assertEqual(success, '帐号或密码错误',msg='帐号或密码错误') #返回错误提示



