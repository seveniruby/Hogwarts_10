import logging

def test_1(topics):
    logging.info("start")
    assert len(topics["topics"]) == 2
    logging.info("end")

def test_2(topics):
    assert topics["topics"][0]["deleted"] == False