from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    def __init__(self, wework):
        self.driver=wework.driver
    def add_member(self, name, alias, id, mobile, **kwargs):
        #locator = ".js_has_member a.qui_btn.ww_btn.js_add_member"
        locator = ".js_has_member .ww_operationBar .js_add_member"
        WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))


        # for index in range(10):
        #     element=self.driver.find_element_by_css_selector(locator)
        #     print(element.rect)
        #     print(element.text)
        #     print(element.tag_name)
        #     sleep(0.5)
        #
        # print(self.driver.page_source)
        # #todo: 找到等待的状态
        sleep(1)
        # print("3s")
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(locator).location)
        #     sleep(0.5)

        self.click_by_js(By.CSS_SELECTOR, locator)
        self.driver.find_element(By.NAME, "username").send_keys(name)
        self.driver.find_element(By.NAME, "english_name").send_keys(alias)
        self.driver.find_element_by_name("acctid").send_keys(id)
        self.driver.find_element_by_name("mobile").send_keys(mobile)
        self.click_by_js(By.CSS_SELECTOR, ".js_btn_cancel")
        self.click_by_js(By.XPATH, "//*[text()='离开此页']")
        return self

    def delete_member(self):
        pass

    def get_tips(self):
        return "OK"

    def search(self, key):
        self.driver.find_element_by_id("memberSearchInput").send_keys(key)
        return ProfilePage(self.driver)
