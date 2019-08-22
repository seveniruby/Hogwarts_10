from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.profile_page import ProfilePage
from appium_po.page.search_page import SearchPage


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
        print(self.driver.page_source)
        print(self.driver.find_element(By.ID, "image_cancel").location)
        self.driver.find_element(By.ID, "image_cancel").click()
        self.driver.find_element_by_id("user_profile_icon")


    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        return ProfilePage()

    def get_ads(self):
        return False


