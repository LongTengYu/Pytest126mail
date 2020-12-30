import pytest
from PageObject.WriteEmailPage import WriteEmail
from Public.SetUp_TearDown import su_td
from PageObject.LoginPage import Login
from time import *
import allure


@allure.feature('发送邮件模块')  # 声明模块名称
@allure.description('发送邮件用例描述')  # 声明描述
@allure.suite('发送邮件套件')
@allure.link('https://mail.126.com/', '126邮箱地址')
class Test_WriteEmail_class(su_td, WriteEmail, Login):

    # --------------------------------------------
    username = '126邮箱账号'  # 126邮箱账号
    password = '126邮箱密码'  # 126邮箱密码
    # --------------------------------------------

    @allure.title('登录')
    @allure.severity('blocker')
    @pytest.mark.run(order=5)  # 根据pytest运行机制，当多个测试文件一起执行时，其不同文件中的用例的order编号要顺序编排。
    def test_user_login(self):  # 登录成功测试模块

        self.type_iframe()
        self.type_username(self.username)  # 调用用户名方法
        self.type_password(self.password)  # 调用密码方法
        self.submit()  # 调用登录按钮方法
        self.parentframe()  # 跳出登录框
        sleep(20)
        success = self.type_success()  # 获取登录信息

        # -----------------------------------------------------------------------------
        if success == '用户名':
            # -----------------------------------------------------------------------------

            filename = '登录成功' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
            dir = su_td().insert_img(self.driver, filename)  # 截图
            with allure.step('用户名：Long 密码：123456'):
                file = open(dir, mode='rb').read()
                allure.attach(file, '添加图片', allure.attachment_type.JPG)  # 用于向测试报告中输入一些附加的信息，通常是一些测试数据，截图等
        else:
            t = '登录失败' + strftime("%Y-%m-%d %H_%M_%S")  # 获取当前时间
            su_td().insert_img(self.driver, t)  # 截图
            self.assertEqual(success, 'yuxiao8520@126.com', msg='登录失败')  # 判断是否登录成功

    @allure.title('发邮件')
    @allure.severity('blocker')
    @pytest.mark.run(order=6)
    def test_email(self):

        # --------------------------------------------
        mailaddres = '收件邮箱地址'  # 收件地址
        # --------------------------------------------

        mailtitle = '测试1'
        mailtext = '正文1'
        self.writeEmail_button_click()  # 点击【写信】按钮
        self.email_address(mailaddres)  # 输入收件地址
        self.email_title(mailtitle)  # 输入邮件标题
        self.body_iframe()  # 获取邮件框的iframe
        self.email_text(mailtext)  # 写入邮件正文
        self.default_content()  # 返回页面主目录，用于跳出邮件框的iframe
        self.send()  # 点击【发送】按钮
