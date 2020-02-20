import os

import pystache


class Template:
    @classmethod
    def render(cls, path, dict):
        render = pystache.Renderer(escape=lambda u: u)
        print(os.path.abspath(os.getcwd()))
        with open(path) as f:
            content = f.read()
            parsed = pystache.parse(content)
            result = render.render(parsed, dict)
            return result