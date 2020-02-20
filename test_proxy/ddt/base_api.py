import requests


class BaseApi:
    @classmethod
    def request(cls, steps):
        # 最好使用yaml与class的转换，而不是dict词典

        for step in steps:
            r = requests.request(method=step["method"], url=step["url"])
            print(r.status_code)
