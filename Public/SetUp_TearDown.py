from Public.Base import BasePage
from selenium import webdriver


class su_td(BasePage):
    driver = webdriver.Firefox()
    driver.maximize_window()

    def setup_class(self):
        self.goto_url(self, self.driver)

    def teardown_class(self):
        self.driver.quit()  # 结束浏览器调用
