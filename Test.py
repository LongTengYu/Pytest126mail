# from time import *
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# class Log():
#     # 登录
#     def Login(self, driver, username, password):
#         # 点击登录框右上角，将登录框从扫描二维码切换至输入用户名和密码
#         # driver.find_element_by_id('lbNormal').click()
#
#         # 定位iframe   通过xpath路径获取iframe控件
#         # contains(@id,'value')方法用于标签属性值包含特定字符定位，其中@id表示需要匹配属性，value表示被包含的属性值
#         iframe = driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')
#         driver.switch_to.frame(iframe)  # 切换到iframe页签
#
#         # # 定位用户名框
#         # driver.find_element_by_xpath("//input[@name='email']").clear()  # 清空用户名框
#         # driver.find_element_by_xpath("//input[@name='email']").send_keys(username)  # 填写用户名
#
#         # 定位密码框
#         driver.find_element_by_xpath("//input[@name='password']").clear()  # 清空用户名框
#         driver.find_element_by_xpath("//input[@name='password']").send_keys(password)  # 填写用户名
#
#         # 点击登录按钮
#         driver.find_element_by_link_text('登  录').click()
#         sleep(2)
#         # wait = WebDriverWait(driver, 10)
#         # wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="ferrorhead"]')))
#         print(driver.find_element_by_xpath("//div[@class='ferrorhead']").text)
#
#         # driver.switch_to.parent_frame()
#         # sleep(2)
#         # print(driver.find_element_by_xpath("//*[@id='spnUid']"))
#         # sleep(1)
#         driver.quit()
#
#
# if __name__=='__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://mail.126.com/')
#
#     username = 'yuxiao8520'  # 声明用户名
#     password = '5esHc2Tp5nMULGa'  # 声明密码
#
#     Log().Login(driver,username,password)
#
# # import pytest
# # class Test_A():
# #     def test_a1(self):
# #         print('a1')
# #         if 1==2:
# #             print('成功')
# #         else:
# #             print('失败')
# #             self.assertEqual(1,2)
# #
# #     def test_a2(self):
# #         print('a2')
# #         assert 1==1
# #         print('a22')
# #
# #     def test_a3(self):
# #         print('a3')
# #         assert 1==1
# #         print('a33')
#
# # if __name__ == '__main__':
# #     pytest.main(['Test.py::Test_A::test_a2','Test.py::Test_A::test_a1','-v','-s'])
import zipfile
import os
# z=zipfile.ZipFile('./Report/Html/test.zip','w',zipfile.ZIP_DEFLATED)
# z.write('./Report/Html/')
# z.close()
def dfs_get_zip_file(input_path,result):

    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file,result)
        else:
            result.append(input_path+'/'+file)

def zip_path(input_path,output_path,output_name):

    f = zipfile.ZipFile(output_path+r"/"+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path+r"/"+output_name
if __name__=='__main__':
    zip_path('./Report/Html/','./Report/Zip','test.zip')