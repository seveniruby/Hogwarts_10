from test_proxy.ddt.base_api import BaseApi


class Httpbin(BaseApi):
    def get(self, data):
        self.request(data)

    def post(self, data):
        self.request(data)
