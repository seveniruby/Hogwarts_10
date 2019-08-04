from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:
    def setup(self):
        # chrome_options=webdriver.ChromeOptions()
        # chrome_options.debugger_address="127.0.0.1:9222"
        #
        # self.driver=webdriver.Chrome(options= chrome_options)


        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # self.driver.get('https://testerhome.com')

        url='https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get(url)
        cookies={
            "wwrtx.vst": "bwwJzXzX7P30bdCMNff5DBmaUIkdDUQZYG-ynNp8Oi1d87eZZpJv8t-obxiDtpDRbKkRYnjHAbrvkZEeAlRqqcgXmuT1u24LsC7F1HkwrYmlU-zyg1d4vgzEM2jCVmUFD02KuvHf60UpRWs3WGzQ4pS-pc32aM0w7BTNKVE9srAU8jMWxrjgllRJlItc_ap3nKajZLdOVbrEUHw2kRiUn18BMwWNSo1-h2E4dkh5CmZ52AdZjhb_qOXYjQZjeVoC5yajQL041wAFbgkoRvGk5Q",
            "wwrtx.d2st": "a1678792",
            "wwrtx.sid": "PvmFAAW3_ZQOnOfp5SzMi8wH6yHkmO-qU5JS55P3PM0Q8lrAI_GgrlcwvKitXKHf",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970325013047104",
            "wxpay.vid": "1688853941438590",
        }
        for k,v in cookies.items():
            self.driver.add_cookie({ "name": k, "value": v})
        self.driver.get(url)

    def teardown(self):
        sleep(3)
        #self.driver.quit()

    def test_upload_file(self):
        element_add=self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")
        element_add.click()
        print(self.driver.execute_script("console.log('hello from selenium')"))
        print(self.driver.execute_script("return document.title;"))
        self.driver.execute_script("arguments[0].click();", element_add)
        #
        # self.driver.execute_script("arguments[0].click();",
        #                            self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input"))
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input")\
            .send_keys("/Users/seveniruby/PycharmProjects/Hogwarts10/images/霍格沃兹测试学院1024.png")

        print(self.driver.page_source)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel"))
        )
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element_by_css_selector(".js_next"))

    def click_by_js(self, by, locator):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, locator)
                                   )


    def test_upload_file(self):
        self.click_by_js((By.CSS_SELECTOR, ".js_upload_file_selector"))
        self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input")\
            .send_keys("/Users/seveniruby/PycharmProjects/Hogwarts10/images/霍格沃兹测试学院1024.png")

        print(self.driver.page_source)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel"))
        )
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element_by_css_selector(".js_next"))
        self.click_by_js((By.CSS_SELECTOR, ".js_next"))

    def test_cookie(self):
        pass
        # url='https://work.weixin.qq.com/wework_admin/frame#contacts'
        # self.driver.get(url)
        # cookies={
        #     "wwrtx.vst": "bwwJzXzX7P30bdCMNff5DBmaUIkdDUQZYG-ynNp8Oi1d87eZZpJv8t-obxiDtpDRbKkRYnjHAbrvkZEeAlRqqcgXmuT1u24LsC7F1HkwrYmlU-zyg1d4vgzEM2jCVmUFD02KuvHf60UpRWs3WGzQ4pS-pc32aM0w7BTNKVE9srAU8jMWxrjgllRJlItc_ap3nKajZLdOVbrEUHw2kRiUn18BMwWNSo1-h2E4dkh5CmZ52AdZjhb_qOXYjQZjeVoC5yajQL041wAFbgkoRvGk5Q",
        #     "wwrtx.d2st": "a1678792",
        #     "wwrtx.sid": "PvmFAAW3_ZQOnOfp5SzMi8wH6yHkmO-qU5JS55P3PM0Q8lrAI_GgrlcwvKitXKHf",
        #     "wwrtx.ltype": "1",
        #     "wxpay.corpid": "1970325013047104",
        #     "wxpay.vid": "1688853941438590",
        # }
        # for k,v in cookies.items():
        #     self.driver.add_cookie({ "name": k, "value": v})
        # self.driver.get(url)

    def test_add_member(self):

        #locator = ".js_has_member a.qui_btn.ww_btn.js_add_member"
        locator = ".js_has_member .ww_operationBar .js_add_member"
        WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))


        for index in range(10):
            element=self.driver.find_element_by_css_selector(locator)
            print(element.rect)
            print(element.text)
            print(element.tag_name)
            sleep(0.5)
        #
        # print(self.driver.page_source)
        # #todo: 找到等待的状态
        # sleep(3)
        # print("3s")
        # for index in range(10):
        #     print(self.driver.find_element_by_css_selector(locator).location)
        #     sleep(0.5)

        self.click_by_js(By.CSS_SELECTOR, locator)
        self.driver.find_element(By.NAME, "username").send_keys("name")
        self.driver.find_element(By.NAME, "english_name").send_keys("english_name")
        self.driver.find_element_by_name("acctid").send_keys("acctid")
        self.driver.find_element_by_name("mobile").send_keys("15600530000")











