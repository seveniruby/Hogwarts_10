from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver=driver


    def find(self, locator, value=None):
        if value==None:
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)
    def click_by_js(self, by, locator):
        WebDriverWait(self._driver, 5).until(expected_conditions.element_to_be_clickable((by, locator)))
        self._driver.execute_script("arguments[0].click();",
                                    self._driver.find_element(by, locator)
                                    )