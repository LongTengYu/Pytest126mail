from LoginPage import Login
from Public import Base
from selenium import webdriver

class Mytest(Base):
    driver=webdriver.Firefox()
    driver.maximize_window()
    log=''

    def setup_class(self):
        self.log = Login(self.driver)  # 声明Login类对象，因Login类继承于OpenPage类且OpenPage类有默认参数，
                                       # 所以在声明对象时需传入参数
        self.log.open()  # 调用打开网页方法open
        self.log.type_iframe()  # 调用iframe切换方法


    def teardown_class(self):
        self.driver.quit()   # 结束浏览器调用