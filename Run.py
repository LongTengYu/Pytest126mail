import pytest
from time import *
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
    '''
    特别说明：
    pytest的运行机制是将所有被执行文件先轮巡一遍后再执行。这一点要特别注意。对用例的执行顺序是有影响的。
    '''
    test_login='TestCase/Test_Login.py'
    test_email='TestCase/Test_WriteEmail.py'
    pytest.main(['--alluredir', './Report/HtmlData', test_login,test_email, '-vs'])
    split = 'allure '+'generate '+'./Report/HtmlData '+'-o '+'./Report/Html '+'--clean'
    os.system(split)
    main()
