import pytest
import paying_debt_1
import paying_debt_2


class TestPayingDebt_1(object):
    def test_case_1(self):
        balance = paying_debt_1.paying_debt(42, 0.2, 0.04)
        assert balance == 31.38

    def test_case_2(self):
        balance = paying_debt_1.paying_debt(484, 0.2, 0.04)
        assert balance == 361.61


class TestPayingDebt_2(object):
    def test_case_1(self):
        payment = paying_debt_2.paying_debt_iter(3329, 0.2)
        assert payment == 310

    def test_case_2(self):
        payment = paying_debt_2.paying_debt_iter(4773, 0.2)
        assert payment == 440

    def test_case_3(self):
        payment = paying_debt_2.paying_debt_iter(3926, 0.2)
        assert payment == 360

    def test_case_4(self):
        payment = paying_debt_2.paying_debt_recur(3329, 0.2)
        assert payment == 310

    def test_case_5(self):
        payment = paying_debt_2.paying_debt_recur(4773, 0.2)
        assert payment == 440

    def test_case_6(self):
        payment = paying_debt_2.paying_debt_recur(3926, 0.2)
        assert payment == 360

    def test_case_7(self):
        payment = paying_debt_2.paying_debt_bisection(320000, 0.2)
        assert payment == 29157.09

    def test_case_8(self):
        payment = paying_debt_2.paying_debt_bisection(999999, 0.18)
        assert (payment - 90325.03) <= 0.1


if __name__ == '__main__':
    pytest.main()
