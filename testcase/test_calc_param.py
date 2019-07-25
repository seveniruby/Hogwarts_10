import json
from unittest import TestCase
from ddt import ddt, data, file_data, unpack
import yaml
from src.calc import Calc
import pytest

class TestCalc:

    def setup(self) -> None:
        self.calc=Calc()

    @pytest.mark.parametrize("a, b, c", [
        (1, 1, 2),
        (1, 0, 1),
        (1, -1, 0),
        (1, 1000000, 1000001)
    ])
    def test_add(self, a, b , c):
        print(a,b,c)
        assert self.calc.add(a, b)==c

    # @file_data("calc.yaml")
    @pytest.mark.parametrize("a,b,c", yaml.load(open("calc2.yaml")))
    def test_div(self, a, b , c):
        print(a,b,c)
        assert self.calc.div(a, b) == c
