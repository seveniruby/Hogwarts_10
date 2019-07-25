import pytest
from requests import utils


@pytest.mark.parametrize("input, expect, encoding", [
    (" ", "%20", "UTF-8"),
    ("a=1&b=2 3", "a%3D1%26b%3D2%203", "UTF-8"),
    (" ", "%20", "GBK"),
    ("测吧", "%B2%E2%B0%C9", "GBK"),
    ("测吧", "%E6%B5%8B%E5%90%A7", "UTF-8")
])
def test_demo(input, expect, encoding):
    assert utils.quote(input, encoding=encoding) == expect
