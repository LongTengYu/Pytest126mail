import pytest
from time import *
import os
from Public.Email import EmailEnclosure
from Public.ZipPack import *


def main():
    t = strftime("%Y-%m-%d %H_%M_%S")  # 获取时间，并将时间格式化为字符串
    input_path = './Report/Html/'  # 被打包文件路径
    output_path = './Report/Zip'  # 打包完成输出路径
    output_name = 'test' + t + '.zip'  # 打包文件名称
    zip_path(input_path, output_path, output_name)  # 将Html报告进行zip打包
    subject = 'Python SMTP 邮件测试'  # 邮件标题
    file_name = '126邮箱测试报告' + t + '.zip'  # 邮件附件名称
    Emailtext = '126邮箱测试报告'  # 邮件正文
    EmailEnclosure(subject, file_name, Emailtext)  # 调用Email发送方法


if __name__ == '__main__':
    test_user_login = 'TestCase/Test_Login.py::Test_Login1::test_user_login'
    test_user_error = 'TestCase/Test_Login.py::Test_Login1::test_user_error'
    test_password_error = 'TestCase/Test_Login.py::Test_Login1::test_password_error'
    test_up_error = 'TestCase/Test_Login.py::Test_Login1::test_up_error'
    test_writemaillogin='TestCase/Test_WriteEmail.py::Test_WriteEmail_class::test_user_login'
    test_writemail='TestCase/Test_WriteEmail.py::Test_WriteEmail_class::test_email'
    # pytest.main(['--alluredir','./Report/HtmlData',test_user_error,test_password_error,test_up_error,test_user_login,'-v','-s'])
    # pytest.main(['--alluredir', './Report/HtmlData', test_user_login, '-v', '-s'])
    pytest.main(['--alluredir', './Report/HtmlData', test_user_login ,'-v', '-s'])
    pytest.main(['--alluredir', './Report/HtmlData', test_writemaillogin,test_writemail, '-v', '-s'])
    # split = 'allure '+'generate '+'./Report/HtmlData '+'-o '+'./Report/Html '+'--clean'
    # os.system(split)
    # main()
