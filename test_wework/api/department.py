import json

import requests

from test_wework.api.BaseApi import BaseApi
from test_wework.api.wework import WeWork
from test_wework.utils.Utils import Utils


class Department(BaseApi):
    list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
    create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"

    def list(self, id):
        self.json_data = requests.get(self.list_url, params={"access_token": WeWork.get_token(), "id": id}).json()
        self.verbose(self.json_data)
        return self.json_data

    def create(self, name: str, parentid, order):
        # proxies = {
        #     'http': 'http://127.0.0.1:8888',
        #     'https': 'http://127.0.0.1:8888',
        # }

        self.json_data = requests.post(
            self.create_url,
            params={"access_token": WeWork.get_token()},
            # 需要设置UTF8编码
            headers={'content-type': 'application/json; charset=utf-8'},
            json={
                "name": name, "parentid": parentid, "order": order, "id": None
            },
            # proxies=proxies,
            verify=False
        ).json()

        self.verbose(self.json_data)
        return self.json_data

    def delete(self):
        pass

    def update(self):
        pass
