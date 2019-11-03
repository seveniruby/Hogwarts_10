import requests

from test_wework.api.BaseApi import BaseApi
from test_wework.api.wework import WeWork
from test_wework.utils.Utils import Utils


class Department(BaseApi):
    list_url="https://qyapi.weixin.qq.com/cgi-bin/department/list"

    def list(self, id):
        r=requests.get(self.list_url, params={ "access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(r)
        return r

    def create(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
