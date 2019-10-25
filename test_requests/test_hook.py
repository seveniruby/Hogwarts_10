import requests
from requests import Request, Session, Response


class TestHook:
    def test_hook_request(self):

        s = Session()
        req = s.get("http://www.baidu.com/")

        req=Request("GET", "http://www.baidu.com/")
        data=req.prepare()
        print(data)
        print("2")
        resp = s.send(data)

        print(resp.status_code)

    def test_hook_request2(self):
        s = Session()
        req = Request('GET', "http://www.baidu.com")

        prepped = s.prepare_request(req)

        # do something with prepped.body
        prepped.body = 'Seriously, send exactly these bytes.'

        # do something with prepped.headers
        prepped.headers['Keep-Dead'] = 'parrot'

        resp = s.send(prepped
                      )

        print(resp.status_code)

    def print_url(self, r: Response, *args, **kwargs):
        print(r.url)
        r.json()



    def test_hook_response(self):
        r=requests.get('https://httpbin.org/', hooks={'response': self.print_url, "request": self.print_url})
        print(r.text)