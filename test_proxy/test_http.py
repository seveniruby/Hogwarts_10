import json
from pprint import pprint

import requests
import yaml


class TestHttp:
    def setup(self):
        pass

    def test_request(self):
        requests.request("get")

    def test_get(self):
        r = requests.get(url="", params={'key1': 'value1', 'key2': 'value2'})
        assert r.status_code == 200

    def test_post(self):
        r = requests.post('https://httpbin.org/post', data={'key': 'value'})
        pprint(yaml.dump(r))
        assert r.status_code == 200