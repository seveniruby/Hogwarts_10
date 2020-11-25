import json

import requests
import pytest
from requests import Response
from jsonpath import jsonpath
from jsonschema import validate


class TestHTTP:
    def setup(self):
        # self.proxies = {'http': 'http://127.0.0.1:7778/'}
        self.proxies = None

    def test_get(self):
        r = requests.get('https://testerhome.com/hogwarts')
        print(r)

    def test_get_query(self):
        url = "http://47.95.238.18:8090/#/HTTP_Methods/get_get"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        r = requests.get(url, params=payload)
        self.inspect_response(r)

    def test_get_query_header(self):
        url = "http://47.95.238.18:8090/get"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a': "2", "bcd": "header demo", "accept": "application/json"}
        r = requests.get(url, params=payload, headers=headers)
        self.inspect_response(r)

    def test_post(self):
        url = "http://47.95.238.18:8090/post"
        payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        headers = {'a': "2", "bcd": "header demo", "accept": "application/json"}

        r = requests.post(url, data=payload, headers=headers, proxies=self.proxies)
        self.inspect_response(r)

    def test_testerhome(self):
        url = "https://testerhome.com/api/v3/topics.json"
        r = requests.get(url, params={'limit': '2'})
        assert r.json()['topics'][0]['id'] == 22952

    def test_hogwarts(self):
        url = "https://home.testing-studio.com/categories.json"
        r = requests.get(url)
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'

    def test_hogwarts_jsonpath(self):
        url = "https://home.testing-studio.com/categories.json"
        r = requests.get(url)
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'


    def test_get_login(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        assert data['topics'][-1]['user']['login'] == 'liangqiangWang'

    def test_get_login_jsonpath(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        assert jsonpath(data, "$.topics[?(@.user.login == '944527839')].user.id")[0] == 21277

    def test_get_login_jsonschema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_xueqiu_search(self):
        url = "https://xueqiu.com/stock/search.json"
        params = {"code": "sogo", "size": "3", "page": "1"}
        header = {"Accept": "application/json",
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
                  # "Cookie": "aliyungf_tc=AQAAABP9S18PYAUAFgm3c1TLP+uXTo/T; acw_tc=2760822715709547793664705e33a2d518643654d94fbaecb98934f091dc2e; xq_a_token=d831cd39b53563679545656fba1f4efd8e48faa0; xq_a_token.sig=kxPAlGGsJ6qG9gNgnf4tIE0i41U; xq_r_token=fd2f0f487c8298cad8e7519f1560abb7a18c589d; xq_r_token.sig=U3HiCW_eRXnt70cdEuK9nDbDmjM; u=541570954781608; Hm_lvt_1db88642e346389874251b5a1eded6e3=1570954783; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1570954783; device_id=573ca601344af6a914f4ab83171b34cf"
                  }
        cookies = {
            "xq_a_token": "d831cd39b53563679545656fba1f4efd8e48faa0",
            #      "xq_r_token": "fd2f0f487c8298cad8e7519f1560abb7a18c589d",
            # "u": "541570954781608",
            # "device_id": "573ca601344af6a914f4ab83171b34cf",
            # "xq_a_token.sig": "kxPAlGGsJ6qG9gNgnf4tIE0i41U",
            # "xq_r_token.sig": "U3HiCW_eRXnt70cdEuK9nDbDmjM"
        }
        r = requests.get(url, params=params, headers=header, cookies=cookies)
        print(r.text)
        assert r.json()['stocks'][0]['name'] == '搜狗'

    def inspect_response(self, r: Response):
        print(r.headers)
        print(r.cookies)
        print(r.status_code)
        print(r.encoding)
        print(r.url)
        print(r.content)
        print(r.text)
        print(r.raw)
        print(r.json())
