"""
tests for calculate_power_root function
"""

from calculate_power_root import calculate_power_root
import pytest
import random
import math


class TestSquareRootCalculator(object):
    def test_zero(self):
        with pytest.raises(ValueError):
            calculate_power_root(0)

    def test_constant_integer(self):
        assert calculate_power_root(4, 2) == 2

    def test_integer_greater_than_one(self):
        x = random.randint(1, 1000000)
        p = random.randint(1, 100)
        assert abs(calculate_power_root(x, p) - x ** (1 / p)) <= 0.00001

    def test_contant_positive_decimal(self):
        assert calculate_power_root(0.25, 2) == 0.5

    def test_between_zero_and_one(self):
        x = random.random()
        p = random.randint(1, 100)
        assert abs(calculate_power_root(x, p) - x ** (1 / p)) <= 0.0001


if __name__ == '__main__':
    pytest.main()
