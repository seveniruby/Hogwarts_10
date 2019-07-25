from unittest.mock import MagicMock

import requests
import pytest

@pytest.fixture(autouse=True)
def mock_requests(monkeypatch):
    """Remove requests.sessions.Session.request for all tests."""
    #monkeypatch.delattr("requests.sessions.Session.request")
    def mock(*args, **kwargs):
        print("mock")
        print(args)
        print(kwargs)
        return "mock"

    #monkeypatch.setattr(requests.sessions.Session, "request", mock)
    monkeypatch.setattr(requests.sessions.Session, "send", mock)
    #monkeypatch.setattr("requests.sessions.Session.request", mock)


def test_post(mock_requests):
    print(requests.request("get", "http://www.baidu.com"))
    print(requests.post("http://www.baidu.com"))

def test_mock():
    requests.request=MagicMock(return_value="mock")
    print(requests.request("get", "http://www.baidu.com"))