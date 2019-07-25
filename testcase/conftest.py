import requests
import pytest
import logging


logging.basicConfig(level=logging.DEBUG)
@pytest.fixture()
def topics():
    url="http://0.0.0.0:8000/topics.json"
    logging.info(url)
    #url="https://testerhome.com/api/v3/topics.json?limit=2"
    yield requests.get(url).json()
    logging.info("after yield")



@pytest.fixture(params=["https://testerhome.com/api/v3/topics.json?limit=2", "http://0.0.0.0:8000/topics.json"])
def topics2(request):
    url=request.param
    logging.info(url)
    #url="https://testerhome.com/api/v3/topics.json?limit=2"

    def fin():
        logging.info("after yeild teardown")

    request.addfinalizer(fin)
    return requests.get(url).json()


@pytest.fixture(params=[
    "https://testerhome.com/api/v3/topics.json?limit=2",
    "http://0.0.0.0:8000/topics.json",
    "http://127.0.0.1:8000/topics.json"
])
def topics3(request):
    url=request.param
    logging.info(url)
    #url="https://testerhome.com/api/v3/topics.json?limit=2"

    def fin():
        logging.info("after yeild teardown")

    request.addfinalizer(fin)
    return requests.get(url).json()




