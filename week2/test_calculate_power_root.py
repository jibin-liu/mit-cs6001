"""
tests for calculate_square_root function
"""

from calculate_square_root import calculate_square_root
import pytest
import random
import math


class TestSquareRootCalculator(object):
    def test_constant_integer(self):
        assert calculate_square_root(4) == 2

    def test_integer_greater_than_one(self):
        x = random.randint(1, 10000)
        assert abs(calculate_square_root(x) - math.sqrt(x)) <= 0.0001


if __name__ == '__main__':
    pytest.main()
