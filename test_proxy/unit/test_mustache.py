import os

import pystache


class TestMustache:
    def test_render(self):
        render = pystache.Renderer(escape=lambda u: u)
        print(os.path.abspath(os.getcwd()))
        with open("../test_http.mustache") as f:
            content = f.read()
            parsed = pystache.parse(content)
            method = "post"
            dict = {
                "method": method.__repr__(),
                "url": "http://47.95.238.18:8090/post".__repr__(),
                "params": [
                    {"key1": "value1"},
                    {"key2": "value2"},
                ]
            }
            result = render.render(parsed, dict)

            print(result)
