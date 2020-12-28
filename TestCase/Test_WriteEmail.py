from PageObject.WriteEmailPage import WriteEmail
from Public.SetUp_TearDown import su_td
from PageObject.LoginPage import Login
from time import *
import allure


class Test_WriteEmail_class(su_td, WriteEmail, Login):
    username = 'yuxiao8520'  # 声明用户名
    password = '5esHc2Tp5nMULGa'  # 声明密码

    def test_user_login(self):  # 登录成功测试模块

        self.type_iframe()
        self.type_username(self.username)  # 调用用户名方法
        self.type_password(self.password)  # 调用密码方法

        self.submit()  # 调用登录按钮方法
        self.parentframe()  # 跳出登录框
        sleep(5)
        success = self.type_success()  # 获取登录信息
        if success == 'yuxiao8520@126.com':
            filename = '登录成功' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
            dir = su_td().insert_img(self.driver, filename)  # 截图
            with allure.step('用户名：Long 密码：123456'):
                file = open(dir, mode='rb').read()
                allure.attach(file, '添加图片', allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
        else:
            t = '登录失败' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
            su_td().insert_img(self.driver, t)  # 截图
            self.assertEqual(success, 'yuxiao8520@126.com', msg='登录失败')  # 判断是否登录成功

    def test_email(self):
        mailaddres='164357259@qq.com'
        mailtitle='测试1'
        mailtext='正文1'
        self.writeEmail_button_click()
        self.email_address(mailaddres)
        self.email_title(mailtitle)
        self.body_iframe()
        self.email_text(mailtext)
        self.default_content()
        self.send()
