import os


def before(func):
    def new_now():
        print("setup")
        func()

    return new_now

@before
def now():
    print("2019")

def test_demo():
    now()
    print(os.path.realpath(__file__))
    print(os.getcwd())

import pytest

@pytest.mark.run(before='test_second')
def test_first():
    assert True

@pytest.mark.run(after='test_second')
def test_third():
    assert True

def test_second():
    assert True

