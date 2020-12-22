import sys
import os
path=os.path.dirname(__file__).replace('/','\\')  #获取相对路径并将路径中'/'转换为'\\'
print(path)
sys.path.append(path+'\\Models') #因Jenkins构建时无法找到自添加文件，所以需要将自添加文件夹写入环境变量中
sys.path.append(path+'\\Public')
sys.path.append(path+'\\TestCase')
sys.path.append(path+'\\Report')
# from LoginCase import *
# from time import *
# from HTMLTestRunnerCN import *
# from Email import EmailEnclosure
# import unittest
import pytest




def main():
    a=1
    # suit = unittest.TestSuite() #声明测试集合
    # suit.addTest(LoginTest('test_up_error')) #加载测试方法
    # suit.addTest(LoginTest('test_user_error'))
    # suit.addTest(LoginTest('test_password_error'))
    # suit.addTest(LoginTest('test_user_login'))

    # t = strftime("%Y-%m-%d %H_%M_%S")  # 获取时间，并将时间格式化为字符串
    # fp = open(path+'\\Report\\result' + t + '.html', 'wb')  # 打开文件，并写入。若没有该文件则自动创建文件
    #
    # runner = HTMLTestReportCN()    #声明一个HEMLTestRunner对象runner
    # runner.stream=fp               #stream指定测试报告文件
    # runner.title='126邮箱测试报告'  #title定义报告标题
    # runner.description='测试环境：Windows 10   浏览器：Chrome' #description定义报告副标题
    # runner.tester='LTY'  #tester定义测试人员名称
    # runner.run(suit)  # 运行测试用例集，并将测试结果写入到测试报告中
    # fp.close()  # 关闭报告文件

    # subject = 'Python SMTP 邮件测试'  # 邮件标题
    # file_name='126邮箱测试报告'+t+'.html'  #邮件附件名称
    # Emailtext='126邮箱测试报告'  #邮件正文
    # #EmailEnclosure(subject,file_name,Emailtext)  # 调用Email发送方法'''

# if __name__=='__main__':
#     # main()
#     pytest.main(['./TestCase/LoginCase.py::LoginTest::test_user_login'])