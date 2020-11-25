import json

import requests
import base64

class TestEncode:
    origin_url="http://47.95.238.18:10000/topics.txt"
    url="http://47.95.238.18:10000/topics_encode.txt"
    def test_get(self):
        r=requests.get(self.origin_url)
        print(r.json())
        assert len(r.json()["topics"]) == 2

    def test_encode(self):
        r = requests.get(self.url)
        print(r.content)
        data=self.decode(r.content)
        print(data)
        j=json.loads(data)
        print(j)

        assert len(j["topics"]) == 2
    def decode(self, raw):
        return base64.b64decode(raw)

    def test_api(self):
        req=ApiRequest()
        req_data={
            "schema": "http",
            "encoding": "base64",
            "method": "get",
            "url": "http://docker.testing-studio.com:10000/topics_encode.txt",
            "headers": None

        }
        j=req.send(req_data)
        assert len(j["topics"]) == 2

        req_data={
            "schema": "http",
            "encoding": "",
            "method": "get",
            "url": "http://docker.testing-studio.com:10000/topics.txt",
            "headers": None

        }
        j=req.send(req_data)
        assert len(j["topics"]) == 2




class ApiRequest:
    def send(self, data: dict):
        if data["schema"] ==  "http":
            #把host修改为ip，并附加host header
            env={
                "docker.testing-studio.com": {
                    "dev": "1.1.1.1",
                    "unit": "1.1.1.2"
                },
                "default": "dev"
            }
            data["url"]=str(data["url"]).replace(
                "docker.testing-studio.com",
                env["docker.testing-studio.com"][env["default"]]
            )
            data["headers"]["Host"]="docker.testing-studio.com"

            res=requests.request(
                data["method"],
                data["url"],
                headers=data["headers"]
            )
            if data["encoding"]=="base64":
                return json.loads(base64.b64decode(res.content))
            if data["encoding"]=="private":
                return json.loads(requests.post("url", data=res.content).content)
            else:
                return json.loads(res.content)


        elif "urllib" == data["schema"]:
            pass
        elif "dubbo" ==  data["schema"]:
            pass
        elif "websocket" == data["schema"]:
            pass
        else:
            pass


