from time import *
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from Public.Base import BasePage

# 写邮件
class WriteEmail(BasePage):
    #self, driver:WebDriver, mailaddres, mailtitle, mailtext

    writeEmail_button_loc = (By.XPATH,'//span[(text()="写 信")]')
    email_address_loc = (By.XPATH,'//input[contains(@class,"nui-editableAddr-ipt")]')
    email_title_loc = (By.XPATH,'//input[contains(@id,"subjectInput")]')
    body_iframe_loc = (By.XPATH,'//iframe[@class="APP-editor-iframe"]')
    email_text_loc = (By.XPATH,'//body[contains(@class,"nui-scroll")]')
    send_loc = (By.XPATH,'//span[text()="发送"]')

    # 点击写信按钮，进入写信页面
    def writeEmail_button_click(self):
        self.find_element_method(*self.writeEmail_button_loc).click()
        sleep(2)

    # 输入收件人地址
    def email_address(self,mailaddres):
        self.find_element_method(*self.email_address_loc).send_keys(mailaddres)
        sleep(1)

    # 输入邮件标题
    def email_title(self,mailtitle):
        self.find_element_method(*self.email_title_loc).send_keys(mailtitle)
        sleep(1)

    # 定位iframe   通过xpath路径获取iframe控件
    def body_iframe(self):
        self.find_element_method(*self.body_iframe_loc)

    # 输入邮件正文，并返回到父iframe中
    def email_text(self,mailtext):
        self.find_element_method(*self.email_text_loc).send_keys(mailtext)
        self.driver.switch_to.parent_frame()

    # 点击发送按钮
    def send(self):
        self.find_element_method(*self.send_loc)
        sleep(5)