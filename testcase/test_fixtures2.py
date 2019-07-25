import requests
import pytest
import logging


@pytest.mark.a
def test_1(topics2):
    logging.info("start")
    assert len(topics2["topics"]) == 2
    logging.info("end")


@pytest.mark.b
def test_2(topics3):
    assert topics3["topics"][0]["deleted"] == False

@pytest.mark.b
def test_3(topics2):
    assert topics2["topics"][0]["deleted"] == False