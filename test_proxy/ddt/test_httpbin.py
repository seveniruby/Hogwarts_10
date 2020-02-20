import os
import re

import pytest
import requests
import yaml

from test_proxy.ddt.httpbin import Httpbin


def get_testcases():
    testcases = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".data.yaml"):
                testcases.append(os.path.join(root, file))

    return testcases


class TestHttpbin:

    def setup(self):
        self.httpbin = Httpbin()

    @pytest.mark.parametrize("file", get_testcases())
    def test_request(self, file):
        # 读取测试数据
        testcase_data = None
        with open(file) as f:
            testcase_data = yaml.safe_load(f)
        print(yaml.dump(testcase_data))
        # 读取测试步骤
        testcase_steps = None
        testcase_step_file = '.'.join(file.split('.')[0:-3]) + ".step.yaml"
        with open(testcase_step_file) as f:
            testcase_steps = yaml.safe_load(f)
        print(testcase_steps)
        self.httpbin.get(testcase_steps)


    def test_post(self, data):
        pass
