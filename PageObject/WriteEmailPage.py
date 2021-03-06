from time import *
from selenium.webdriver.common.by import By
from Public.Base import BasePage


# 写邮件
class WriteEmail(BasePage):
    writeEmail_button_loc = (By.XPATH, '//span[(text()="写 信")]')
    email_address_loc = (By.XPATH, '//input[contains(@class,"nui-editableAddr-ipt")]')
    email_title_loc = (By.XPATH, '//input[contains(@id,"subjectInput")]')
    body_iframe_loc = (By.XPATH, '//iframe[@class="APP-editor-iframe"]')
    email_text_loc = (By.XPATH, '//body[contains(@class,"nui-scroll")]')
    send_loc = (By.XPATH, '//span[text()="发送"]')

    # 点击写信按钮，进入写信页面
    def writeEmail_button_click(self):
        self.find_element_method(*self.writeEmail_button_loc).click()
        sleep(2)

    # 输入收件人地址
    def email_address(self, mailaddres):
        self.find_element_method(*self.email_address_loc).send_keys(mailaddres)
        sleep(1)

    # 输入邮件标题
    def email_title(self, mailtitle):
        self.find_element_method(*self.email_title_loc).send_keys(mailtitle)
        sleep(1)

    # 定位iframe   通过xpath路径获取iframe控件
    def body_iframe(self):
        iframe = self.find_element_method(*self.body_iframe_loc)  # 因继承了Page类，所有可以调用Page类中的find_element_method方法来
        self.driver.switch_to.frame(iframe)  # 获取页面元素
        sleep(1)

    # 输入邮件正文，并返回到父iframe中
    def email_text(self, mailtext):
        self.find_element_method(*self.email_text_loc).send_keys(mailtext)

    # 点击发送按钮
    def send(self):
        self.find_element_method(*self.send_loc).click()
        sleep(5)

    # 返回到主目录下
    def default_content(self):
        self.driver.switch_to.default_content()
