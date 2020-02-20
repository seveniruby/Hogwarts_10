import os
import sys
from pprint import pprint

import yaml
from deepdiff import DeepDiff
from mitmproxy import http

addon_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(addon_dir)
pre = {}


def response(flow: http.HTTPFlow):
    current = yaml.load(flow.response.content)
    key = flow.request.pretty_url.split('?')[0]
    global pre
    if pre:
        ddiff = DeepDiff(pre[key], current, ignore_order=True).to_dict()
        pprint(ddiff)
    pre[key] = current
