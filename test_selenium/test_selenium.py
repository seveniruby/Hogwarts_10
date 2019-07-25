from time import sleep

from selenium import webdriver

def test_browser():
    browser = webdriver.Chrome()
    browser.get('https://testerhome.com')


def test_firefox():
    webdriver.Firefox().get("https://testerhome.com")

def test_search():
    browser=webdriver.Chrome()
    browser.get("https://testerhome.com")
    search=browser.find_element_by_name("q")
    search.send_keys("selenium")
    sleep(20)




