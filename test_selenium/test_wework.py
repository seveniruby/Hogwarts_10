from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:
    def setup(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.debugger_address="127.0.0.1:9999"

        self.driver=webdriver.Chrome(options= chrome_options)
        self.driver.implicitly_wait(5)
        # self.driver.get('https://testerhome.com')

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

    def click_by_js(self, locator):
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(locator)
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




