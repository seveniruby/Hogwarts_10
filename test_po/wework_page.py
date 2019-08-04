from selenium import webdriver


class Wework:

    def __init__(self):
        # chrome_options=webdriver.ChromeOptions()
        # chrome_options.debugger_address="127.0.0.1:9222"
        #
        # self.driver=webdriver.Chrome(options= chrome_options)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # self.driver.get('https://testerhome.com')

        url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
        self.driver.get(url)
        cookies = {
            "wwrtx.vst": "XXXXXXX",
            "wwrtx.d2st": "XXXXXXX",
            "wwrtx.sid": "XXXXXXX",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "XXXXXXX",
            "wxpay.vid": "XXXXXXX",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
