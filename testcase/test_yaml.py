
import json

import yaml


def test_json():
    r=json.load(open("calc.json"))
    print(r)

def test_yaml():
    print(yaml.load(open("calc2.yaml")))