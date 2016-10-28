import pytest
import paying_debt_1


class TestPayingDebt(object):
    def test_case_1(self):
        balance = paying_debt_1.paying_debt(42, 0.2, 0.04)
        assert balance == 31.38

    def test_case_2(self):
        balance = paying_debt_1.paying_debt(484, 0.2, 0.04)
        assert balance == 361.61


if __name__ == '__main__':
    pytest.main()
