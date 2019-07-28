from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        self.driver = webdriver.Chrome()

        self.driver.get('https://testerhome.com')
        self.driver.implicitly_wait(5)

    def teardown(self):
        #self.driver.quit()
        pass

    def test_0728(self):
        self.driver.find_element(By.CSS_SELECTOR, '.title [title*="SoloPi："]').click()
        time.sleep(2)

        time.sleep(3)

        #元素定位没有报错，但是就是点不中
        for i in range(5):
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, '.fa.fa-list').click()
            toc=self.driver.find_element(By.XPATH, '(//ul/li[contains(@class,"toc-level-2")])[2]')
            print(toc.location)
            print(toc.size)
            #li控件的中心点坐标碰巧不响应点击
            a = self.driver.find_element(By.XPATH, '(//ul/li[contains(@class,"toc-level-2")]/a)[2]')
            print(a.location)
            print(a.size)
            a.click()

