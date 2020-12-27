import os
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    """
    基础类，用于页面对象类的继承
    """
    login_url = 'https://mail.126.com/'  # 声明登录地址
    url = '/'

    def goto_url(self, selenium_driver, base_url=login_url):  # 基本的URL(base_url)
        self.base_url = base_url  # 和超时时间（timeout）
        self.driver = selenium_driver
        self.driver.get(base_url)
        self.timeout = 30

    def find_element_method(self, *loc):  # 定位元素方法,*loc为一个元组类型的参数
        return self.driver.find_element(*loc)

    def insert_img(self, driver: WebDriver, filename):  # 获取Bug截图  driver:WebDriver指定driver参数为WebDriver类型
        dir = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\BugImage\\' + filename + '.jpg'
        driver.get_screenshot_as_file(dir)  # 跨类调用get_screenshot_as_file方法时，路径只能用绝对路径，不可以使用相对路径
        return dir

