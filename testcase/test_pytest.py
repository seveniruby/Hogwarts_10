
# content of test_sample.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5


def setup_function():
    print("setup_funciton")