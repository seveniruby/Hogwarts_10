from unittest import TestCase
from ddt import ddt, data, file_data, unpack
import yaml
from src.calc import Calc


@ddt
class TestCalc(TestCase):

    def setUp(self) -> None:
        self.calc=Calc()

    @data((1,1,2),
          (1,0, 1),
          (1, -1, 0),
          (1, 1000000, 1000001)
          )
    @unpack
    def test_add(self, a, b , c):
        print(a,b,c)
        self.assertEqual(self.calc.add(a, b), c)

    @file_data("calc.yaml")
    def test_div(self, a, b , c):
        print(a,b,c)
        self.assertEqual(self.calc.div(a, b), c)
