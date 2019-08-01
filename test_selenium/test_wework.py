from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium:
    def setup(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.debugger_address="127.0.0.1:9999"

        self.driver=webdriver.Chrome(options= chrome_options)
        self.driver.implicitly_wait(5)
        # self.driver.get('https://testerhome.com')

    def test_upload_file(self):
        element_add=self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")
        print(element_add.text)
        print(element_add.rect)
        element_add.click()
        print(self.driver.execute_script("console.log('hello from selenium')"))
        print(self.driver.execute_script("return document.title;"))

        # self.driver.find_element(By.CSS_SELECTOR, ".js_upload_label").click()
