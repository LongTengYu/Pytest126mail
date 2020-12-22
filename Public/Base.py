import os
from selenium.webdriver.remote.webdriver import  WebDriver
class BasePage(object):

    """
    基础类，用于页面对象类的继承
    """
    login_url = 'https://mail.126.com/' #声明登录地址
    url = '/'
    def goto_url(self, selenium_driver, base_url=login_url): # 在初始化方法__init__()中定义驱动（driver），基本的URL(base_url)
        self.base_url = base_url                             # 和超时时间（timeout）
        self.driver = selenium_driver
        self.driver.get(base_url)
        self.timeout = 30

    def on_page(self): #验证网页地址是否正确并返回布尔型数值

        return self.driver.current_url == (self.base_url + self.url)  # 因LoginPage类继承了Page类，所以在声明LoginPage的实例
                                                                      # 对象后，可以在Page类中直接通过实例对象引用LoginPage中
                                                                      # 的变量。即self.url

    def _open(self, url):  # 打开网页，并验证打开的网页地址是否正确
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url  # 调用验证方法

    def open(self):                # 定义open（）方法用于打开URL网站，但是它本身并未做这件事情，而是交由
                                   # _open()方法来实现。关于Url地址的断言部分，则交由on_page()方法来实现
        self._open(self.url)

    def find_element_method(self, *loc):  # 定位元素方法,*loc为一个元组类型的参数
        return self.driver.find_element(*loc)

    def insert_img(self,driver:WebDriver, filename):  # 获取Bug截图  driver:WebDriver指定driver参数为WebDriver类型
        dir = os.path.dirname(os.path.dirname(__file__)).replace('/', '\\') + '\\BugImage\\' + filename  + '.jpg'
        driver.get_screenshot_as_file(dir)  # 跨类调用get_screenshot_as_file方法时，路径只能用绝对路径，不可以使用相对路径
        return dir
