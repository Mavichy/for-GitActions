from unittest import TestCase
from main import calculator

class Test(TestCase):
    def test_calculator(self):
        a = calculator(1, 3, "+")
        self.assertEqual(a, 4)

    def test_calculator_sum(self):
        a = calculator(10, 15, "+")
        self.assertEqual(a, 25)

    def test_calculator_mult(self):
        a = calculator(7, 8, "*")
        self.assertEqual(a, 56)

    def test_calculator_div(self):
        a = calculator(15, 3, "/")
        self.assertEqual(a, 5.0)

    def test_calculator_intdiv(self):
        a = calculator(32, 15, "//")
        self.assertEqual(a, 2)

    def test_calculator_mod(self):
        a = calculator(33, 15, "%")
        self.assertEqual(a, 3)

    def test_calculator_rand(self):
        for i in range(1000):
            a = calculator(15, 33, "%")
            self.assertTrue(a in range(15,34))