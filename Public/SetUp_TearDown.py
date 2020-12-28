from Public.Base import BasePage
from selenium import webdriver


class su_td(BasePage):
    def setup_method(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        self.goto_url(driver)

    def teardown_method(self):
        self.driver.quit()  # 结束浏览器调用
