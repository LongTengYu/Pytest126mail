from Public.Base  import BasePage
from Public.SetUp_TearDown import su_td
from time import *
from selenium import webdriver

class Test_AC(su_td):

    # driver=webdriver.Firefox()
    # driver.maximize_window()
    username = 'yuxiao8520'  # 声明用户名
    password = '5esHc2Tp5nMUL'  # 声明密码

    def test_ad(self):
        print('test_ad')

    def test_bd(self):
        print('test_bd')

    def test_bd2(self):
        print('test_bd2')

    def test_user_login(self):  # 登录成功测试模块

       self.log.type_username(self.username)  # 调用用户名方法
       self.log.type_password(self.password)  # 调用密码方法
       self.log.submit()  # 调用登录按钮方法
       sleep(10)
       success=self.log.type_success() #获取登录信息

       self.assertEqual(success,'yuxiao8520@126.com',msg='登录成功')  #判断是否登录成功
       t = '登录成功'+strftime("%Y-%m-%d %H_%M_%S")  #获取当前时间
       su_td().insert_img(self.driver,t)  #截图

    # def setup_class(self):
    #     print('setup')
    #     BasePage().goto_url(selenium_driver=self.driver,base_url='https://mail.126.com/')
    #
    # def teardown_class(self):
    #     print('teardown')
    #     self.driver.quit()

# class Test_BC(su_td):
#     def test_bd(self):
#         print('test_bd')
#
#     def test_bd2(self):
#         print('test_bd2')