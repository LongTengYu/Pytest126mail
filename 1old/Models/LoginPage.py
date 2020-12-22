from selenium.webdriver.common.by import *
from OpenURL import OpenPage
from time import *

class Login(OpenPage):  # LoginPage类中主要对登陆页面上的元素进行封装，使其成为更具体的操作方法。
                             # 例如，用户名，密码和登陆按钮都被封装成了方法。
    url = '/'
    username_loc = (By.XPATH, "//input[@name='email']")  # 定义用户名的元素获取方式和元素锚点
    password_loc = (By.XPATH, "//input[@name='password']")  # 定义密码的元素获取方式和元素锚点
    submit_loc = (By.LINK_TEXT, '登  录')  # 定义登录按钮的元素获取方式和元素锚点
    iframe_loc = (By.XPATH, '//iframe[contains(@id,"x-URS-iframe")]')  # 定义登录框的元素获取方式和元素锚点
    error_loc  = (By.XPATH,"//div[@class='ferrorhead']")  # 定义错误提示语获取方法和元素锚点
    success_loc = (By.XPATH,"//span[@id = 'spnUid']")  # 定义登录后获取用户名的获取方法和元素锚点


    def type_iframe(self):  # 登录框方法
        iframe = self.find_element_method(*self.iframe_loc)  # 因继承了Page类，所有可以调用Page类中的find_element_method方法来
        self.driver.switch_to.frame(iframe)  # 获取页面元素


    def type_username(self, username):  # 用户名方法
        self.find_element_method(*self.username_loc).send_keys(username)


    def type_password(self, password):  # 用户密码方法
        self.find_element_method(*self.password_loc).send_keys(password)

    def type_error(self):  #错误提示语获取方法
        sleep(2)
        return self.find_element_method(*self.error_loc).text

    def type_success(self):  # 获取登录后的用户名用于判断是否登录成功
        return self.find_element_method(*self.success_loc).text


    def submit(self):  # 登录按钮方法
        self.find_element_method(*self.submit_loc).click()

    def type_clear(self):  # 清除用户名和密码
        self.find_element_method(*self.username_loc).clear()
        self.find_element_method(*self.password_loc).clear()
