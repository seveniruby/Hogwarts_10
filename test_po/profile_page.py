from time import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_po.base_page import BasePage


class ProfilePage(BasePage):
    def update(self, **kwargs):
        self.click_by_js(By.CSS_SELECTOR, ".ww_operationBar .js_edit")
        element=self._driver.find_element(By.NAME, "username")
        element.clear()
        element.send_keys(kwargs["name"])
        self.click_by_js(By.CSS_SELECTOR, ".js_save")

    def disable(self):
        pass

    def enable(self):
        pass

    def delete(self):
        pass
    def invite(self):
        pass


