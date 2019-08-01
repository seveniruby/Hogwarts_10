import logging
from time import sleep, time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
class TestSelenium:
    def setup(self):
        chrome_options=webdriver.ChromeOptions()
        chrome_options.debugger_address="127.0.0.1:9999"

        self.driver=webdriver.Chrome(options= chrome_options)
        self.driver.implicitly_wait(20)
        # self.driver.get('https://testerhome.com')

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("https://www.baidu.com")

    def test_firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com")

    def test_search(self):
        search=self.driver.find_element_by_name("q")
        search.send_keys("selenium")

    def test_0725(self):
        self.driver.find_element(By.CSS_SELECTOR, '.title [title*="先到先得"]').click()
        self.driver.find_element(By.XPATH, '//p[contains(text(), "问卷")]/a').click()
        for w in self.driver.window_handles:
            logging.info(w)
            self.driver.switch_to.window(w)
            logging.info(self.driver.title)


        sleep(5)
        for w in self.driver.window_handles:
            logging.info(w)
            self.driver.switch_to.window(w)
            logging.info(self.driver.title)

        self.driver.execute_script("window.scrollTo(0, 500)")

        self.driver.switch_to.frame(0)
        #self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, "iframe"))

        logging.info(self.driver.current_url)
        logging.info(self.driver.current_window_handle)
        logging.info(self.driver.title)

        # ActionChains(self.driver) \
        #     .click_and_hold(self.driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-input")) \
        #     .move_to_element(self.driver.find_element(By.CSS_SELECTOR, ".form-header__title"))\
        #     .release() \
        #     .perform()



        #self.driver.find_element(By.XPATH, "(//input[@class='ant-checkbox-input'])[1]").click()
        #self.driver.find_element(By.CSS_SELECTOR, ".form-header__title").click()

        #logging.info(self.driver.page_source)
        #logging.info(len(self.driver.find_elements_by_xpath("//*[@class='ant-checkbox-input']")))
        self.driver.find_element(By.CSS_SELECTOR, ".ant-checkbox-input").click()


    def test_explicit_wait(self):
        self.driver.find_element_by_partial_link_text("社区").click()
        self.driver.find_element_by_partial_link_text("最新发布").click()
        logging.info(time())
        WebDriverWait(self.driver, 15).until(
            expected_conditions.invisibility_of_element_located((By.CSS_SELECTOR, ".topic .title a")))

        logging.info(time())


    def test_form_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("seveniruby@testerhome.com")


        self.driver.find_element(By.CSS_SELECTOR, "#user_password").send_keys("123456")
        self.driver.find_element(By.CSS_SELECTOR, "#user_remember_me").click()

        element=self.driver.find_element(By.CSS_SELECTOR, "#new_user > div.from-group.checkbox > label")
        logging.info(element.is_displayed())
        logging.info(element.id)
        logging.info(element.tag_name)
        logging.info(element.text)
        logging.info(element.location)
        logging.info(element.size)
        logging.info(element.rect)
        logging.info(element.get_attribute("for"))


        self.driver.find_element(By.NAME, "commit").click()
        # sleep(30)

    def test_upload_file(self):
        self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_upload_label").click()










