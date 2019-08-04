from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver=driver


    def find(self, locator, value=None):
        if value==None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)
    def click_by_js(self, by, locator):
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((by,locator)))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(by, locator)
                                   )