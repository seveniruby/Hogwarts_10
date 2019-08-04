from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage
from test_po.wework_page import Wework


class ContactPage(BasePage):
    _username=(By.NAME, "username")
    _alias=(By.NAME, "english_name")
    _id=(By.NAME, "acctid")
    _mobile=(By.NAME, "mobile")
    _cancel=(By.CSS_SELECTOR, ".js_btn_cancel")
    _leave=(By.XPATH, "//*[text()='离开此页']")
    _search=(By.ID, "memberSearchInput")
    _add =(By.CSS_SELECTOR, ".js_has_member .ww_operationBar .js_add_member")
    def __init__(self, wework: Wework):
        self._driver=wework.driver
    def add_member(self, name, alias, id, mobile, **kwargs):
        #locator = ".js_has_member a.qui_btn.ww_btn.js_add_member"

        # for i in range(10):
        #     try:
        #         element=self.find(self._add)
        #         print(i)
        #         print(element.tag_name)
        #         print(element.text)
        #         print(element.rect)
        #         print(element.is_displayed())
        #         print(element.is_enabled())
        #         print(self._driver.execute_script(
        #             'return document.querySelector(".js_has_member .ww_operationBar .js_add_member").getBoundingClientRect();'))
        #
        #         self.click_by_js(*self._add)
        #         if len(self._driver.find_elements(By.XPATH, '//*[text()="取消"]'))>=1:
        #             print("OK")
        #             return
        #
        #     except Exception as e:
        #         print("except")
        #         print(e)


        def click_and_find(x):
            self.click_by_js(*self._add)
            return len(x.find_elements(By.XPATH, '//*[text()="取消"]'))>=1
        WebDriverWait(self._driver, 5).until(click_and_find)

        # WebDriverWait(self._driver, timeout=5, poll_frequency=1, ignored_exceptions=(TimeoutException)).until(
        #     expected_conditions.element_to_be_clickable(self._add))


        # for index in range(10):
        #     element=self.driver.find_element_by_css_selector(locator)
        #     print(element.rect)
        #     print(element.text)
        #     print(element.tag_name)
        #     sleep(0.5)
        #
        # print(self.driver.page_source)
        # #todo: 找到等待的状态
        # sleep(1)
        # print("3s")
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(locator).location)
        #     sleep(0.5)

        # self.click_by_js(*self._add)
        self.find(self._username).send_keys(name)
        self.find(self._alias).send_keys(alias)
        self.find(*self._id).send_keys(id)
        self.find(self._mobile).send_keys(mobile)
        self.click_by_js(*self._cancel)
        self.click_by_js(*self._leave)
        return self

    def delete_member(self):
        pass

    def get_tips(self):
        return "OK"

    def search(self, key):
        self._driver.find_element(*self._search).send_keys(key)
        return ProfilePage(self._driver)
