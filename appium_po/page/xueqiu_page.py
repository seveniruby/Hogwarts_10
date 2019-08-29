from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.profile_page import ProfilePage
from appium_po.page.search_page import SearchPage
from appium_po.page.trade_page import TradePage


class XueqiuPage:

    def __init__(self):

        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['autoGrantPermissions'] = True
        #caps['unicodeKeyboard']= True
        #caps['resetKeyboard']= True
        caps['automationName']='uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(12)
        #等待元素出现
        WebDriverWait(self.driver, 60).until(
            expected_conditions.visibility_of_element_located((By.ID, 'image_cancel'))
        )


        def click_cancel(x):
            if self.driver.find_element(By.ID, "image_cancel").is_displayed():
                print("displayed")
                self.driver.find_element(By.ID, "image_cancel").click()
            else:
                print("no displayed")

            return len(self.driver.find_elements(By.ID, "image_cancel")) >= 1

        WebDriverWait(self.driver, 60).until_not(click_cancel)

        self.driver.find_element_by_id("user_profile_icon")


    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        return ProfilePage()

    def get_ads(self):
        return False

    def goto_trade(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)



