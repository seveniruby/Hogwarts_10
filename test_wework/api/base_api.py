import requests

from test_wework.utils.Utils import Utils
import pprint


class BaseApi:
    printer = pprint.PrettyPrinter(indent=2)
    json_data = None

    proxies = {
        'http': 'http://127.0.0.1:8888',
        'https': 'http://127.0.0.1:8888',
    }

    @classmethod
    def verbose(cls, json_object=json_data):
        print(Utils.format(json_object))
        # cls.printer.pprint(json_object)

    # @classmethod
    # def jsonpath(cls, expr):
    #     return Utils.jsonpath(cls.json_data, expr)

    def jsonpath(self, expr):
        return Utils.jsonpath(self.json_data, expr)

    def request(self, method, url, params: dict, json, data):
        from test_wework.api.wework import WeWork
        #todo: 封装从外部读取api、或者api默认追加的一些参数
        self.json_data = requests.request(
            method, url=url,
            params=params.update({"access_token": WeWork.get_app_token()})
        )
        self.verbose(self.json_data)
        return self.json_data
