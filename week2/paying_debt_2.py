"""
write a program that calculates the minimum fixed monthly payment needed
in order pay off a credit card balance within 12 months. By a fixed monthly
payment, we mean a single number which does not change each month, but
instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
* balance - the outstanding balance on the credit card
* annualInterestRate - annual interest rate as a decimal

Assume that the interest is compounded monthly according to the balance at
the end of the month (after the payment for that month is made). The monthly
payment must be a multiple of $10 and is the same for all months. Notice that
it is possible for the balance to become negative using this payment scheme,
which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) +
                             (Monthly interest rate x Monthly unpaid balance)

"""


def paying_debt_iter(balance, annualInterestRate):
    """ calculate monthly fixed payment using iteration """
    fixed_payment = 10
    remaining_balance = balance
    monthly_rate = annualInterestRate / 12.0

    while remaining_balance > 0:
        for i in range(12):
            remaining_balance = (remaining_balance - fixed_payment) *\
                                (1 + monthly_rate)

        if remaining_balance > 0:
            remaining_balance = balance
            fixed_payment += 10

    print('Lowest Payment: %d' % fixed_payment)
    return fixed_payment


def paying_debt_recur(balance, annualInterestRate, min_fix_pay=10):
    """ calculate monthly fixed payment using recursion """
    remaining_balance = balance
    monthly_rate = annualInterestRate / 12.0
    for i in range(12):
        remaining_balance = (remaining_balance - min_fix_pay) *\
                            (1 + monthly_rate)

    if remaining_balance <= 0:
        print('Lowest Payment: %d' % min_fix_pay)
        return min_fix_pay
    else:
        min_fix_pay += 10
        return paying_debt_recur(balance, annualInterestRate, min_fix_pay)


def paying_debt_bisection(balance, annualInterestRate):
    """
    calculate monthly fixed payment using recursion and bisection search.
    """
    monthly_rate = annualInterestRate / 12.0
    min_monthly_pay = balance / 12.0
    max_monthly_pay = (balance * (1 + monthly_rate) ** 12) / 12.0

    def find_min_monthly_pay(min_monthly_pay, max_monthly_pay, balance):
        remaining_balance = balance
        guess = (min_monthly_pay + max_monthly_pay) / 2.0

        for i in range(12):
            remaining_balance = (remaining_balance - guess) *\
                                (1 + monthly_rate)

        if abs(remaining_balance) < 0.1:
            return round(guess, 2)
        else:
            if remaining_balance > 0:
                return find_min_monthly_pay(guess, max_monthly_pay, balance)
            elif remaining_balance < 0:
                return find_min_monthly_pay(min_monthly_pay, guess, balance)

    return find_min_monthly_pay(min_monthly_pay, max_monthly_pay, balance)
