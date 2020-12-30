from Public.Base import BasePage
from selenium import webdriver


class su_td(BasePage):
    '''
    特别说明：
    当pytest调用类级别的setup_class和teardown_class方法时，其方法后边self参数会自动传入类本身，而不是类的对象。
    所以在setup_class方法中以self调用其他方法时，视为类直接调用方法，其调用格式为class.function(parameter)。
    若被调用的函数有self参数时，则作为普通型参，必须为其传参数。
    '''

    def setup_class(self):  # 类级别的setup方法，只在类开始时执行一次
        driver = webdriver.Firefox()  # 打开Firefox浏览器
        driver.maximize_window()  # 将浏览器最大化
        self.goto_url(self, driver)  # 传入实例对象的self和浏览器驱动driver

    def teardown_class(self):  # 类级别的teardown方法，只在类结束时执行一次
        self.driver.quit()  # 结束浏览器调用
