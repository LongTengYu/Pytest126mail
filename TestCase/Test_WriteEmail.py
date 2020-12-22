from PageObject.WriteEmailPage import WriteEmail
from Public.SetUp_TearDown import su_td
from time import *
import allure

class Test_WriteEmail_class(WriteEmail,su_td):

    def test_email(self):
        self.log.type_username(self.username)  # 调用用户名方法
        self.log.type_password(self.password)  # 调用密码方法
        self.log.submit()  # 调用登录按钮方法
        self.log.parentframe()  # 跳出登录框
        sleep(5)
        WriteEmail().writeEmail_button_click()
        WriteEmail().writeEmail_button_click()
        WriteEmail().writeEmail_button_click()
        WriteEmail().writeEmail_button_click()
        WriteEmail().writeEmail_button_click()
        WriteEmail().writeEmail_button_click()
