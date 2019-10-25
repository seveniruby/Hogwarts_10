import pytest
import requests
import yaml
from yaml import load, dump

def test_yaml():
    env = {
        "docker.testing-studio.com": {
            "dev": "1.1.1.1",
            "test": "1.1.1.2"
        },
        "default": "dev"
    }

    print(env)
    print(dump(env))

    yaml_str="""
    default: dev
    docker.testing-studio.com:
      dev: 1.1.1.100
      test: 1.1.1.200
    """

    print(load(yaml_str))

    f=open("demo.yaml", "w")
    print(dump(env, f))

def test_read_yaml_file():
    with open("demo.yaml", "r") as f2:
        print(load(f2))



#@pytest.mark.parametrize("num", load(open("demo.yaml", "r"))["array"])
def test_param_from_yaml(num):
    assert num>1



class HttpApi(yaml.YAMLObject):
    yaml_tag="!HttpApi"
    def __init__(self, method, url, query):
        self.method=method
        self.url=url
        self.query=query

    def send(self):
        return requests.request(self.method, self.url, params=self.query).json()

    def __repr__(self):
        return "%s(method=%r, url=%r, query=%r)" % \
               (self.__class__.__name__, self.method, self.url, self.query)


def test_write_httpapi():
    h=HttpApi("get", "https://testerhome.com/api/v3/topics.json", {'limit': '2'})
    print()
    print(dump(h, open("/tmp/1", "w")))

def test_read_httpapi():

   req=load(open("/tmp/1", "r"), Loader=yaml.Loader)
   print(req)

def test_get_login():

    req: HttpApi=load(open("httpapi.yaml", "r"))
    print(req)
    print(req.send())

    #
    # url = "https://testerhome.com/api/v3/topics.json"
    # data = requests.get(url, params={'limit': '2'}).json()
    #
    # url = "https://testerhome.com/api/v3/topics.json"
    # data = requests.get(url, params={'limit': '3'}).json()


    #assert  data['topics'][-1]['user']['login'] ==  'liangqiangWang'


