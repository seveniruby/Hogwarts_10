from unittest import TestCase

import requests

from test_wework.utils.Utils import Utils
from jsonpath import jsonpath

class TestUtils(TestCase):
    def test_format(self):
        json={"a": 1, "b": {"c": "xxx"}}
        print(Utils.format(json))
        print(jsonpath(json, '$.a', result_type="VALUE"))
        print(jsonpath(json, '$.a', result_type="IPATH"))
        print(jsonpath(json, '$.a', result_type="PATH"))
        assert Utils.jsonpath(json, '$.a') == 1

    def test_format_json(self):
        r=requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        print(Utils.format(r))

    def test_jsonpath(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        assert Utils.jsonpath(r, "$..topics[?(@.excellent == 0)]")[0]["id"] > 20000

