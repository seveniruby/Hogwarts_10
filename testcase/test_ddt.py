from unittest import TestCase

from ddt import ddt, data


@ddt
class TestDDT(TestCase):
    @data(True, False, True)
    def test_a(self, value):
        self.assertTrue(value)

