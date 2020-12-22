from PageObject.LoginPage import Login
from Public.Base import BasePage
from selenium import webdriver
import allure

class su_td(Login):

    driver=webdriver.Firefox()
    driver.maximize_window()
    log=''

    # @allure.step('打开网址')
    def setup_class(self):
        self.log = Login()  # 声明Login类对象，因Login类继承于OpenPage类且OpenPage类有默认参数，
                                          # 所以在声明对象时需传入参数
        self.log.goto_url(selenium_driver=self.driver)
        # self.log.open()  # 调用打开网页方法open
        self.log.type_iframe()  # 调用iframe切换方法，进入登录框中

    @allure.title('关闭网址')
    def teardown_class(self):
        self.driver.quit()   # 结束浏览器调用