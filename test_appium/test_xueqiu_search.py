# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import yaml
from appium import webdriver
import pytest
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class TestXueqiu:
    data=yaml.safe_load(open("search.yaml", 'r'))
    print(data)

    tc = yaml.safe_load(open("testcase.yaml", 'r'))
    print(tc)
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        # caps['unicodeKeyboard']= True
        # caps['resetKeyboard']= True
        caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        # 等待元素出现
        # print(self.driver.find_element(By.ID, "image_cancel").location)
        # self.driver.find_element(By.ID, "image_cancel").click()
        # self.driver.find_element_by_id("user_profile_icon")

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element_by_id("action_close").click()

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    def test_demo(self):
        x=[
            ('alibaba', 'BABA', 170),
            ('xiaomi', '01810', 8.5)
        ]

        print(yaml.safe_dump(x))

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [
        ('alibaba', 'BABA', 170),
        ('xiaomi', '01810', 8.5)
    ])
    def test_search(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='%s']/../../..//*[contains(@resource-id, 'current_price')]"
            % stock_type
        ).text)
        assert_that(price, close_to(expect_price, expect_price * 0.1))


    @pytest.mark.parametrize("keyword, stock_type, expect_price", data)
    def test_search_from_yaml(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id, 'stockCode') and @text='%s']/../../..//*[contains(@resource-id, 'current_price')]"
            % stock_type
        ).text)
        assert_that(price, close_to(expect_price, expect_price * 0.1))

    @pytest.mark.parametrize("data", tc)
    def test_search_from_model(self, data):
        TestCase(data).run(self.driver)

class TestCase:
    def __init__(self, steps):
        self.steps =steps

    def run(self, driver: WebDriver):
        for step in self.steps:
            if isinstance(step, dict):
                element=None
                if "id" in step.keys():
                    element=driver.find_element(*(By.ID, step['id']))
                elif "xpath" in step.keys():
                    element=driver.find_element(*(By.XPATH, step['xpath']))
                else:
                    print(step.keys())

                if 'input' in step.keys():
                    element.send_keys(step['input'])
                elif 'get' in step.keys():
                    element.get_attribute(step['get'])
                else:
                    element.click()



