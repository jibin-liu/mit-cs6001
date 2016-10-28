"""
Write a program to calculate the credit card balance after one year if
a person only pays the minimum monthly payment required by the credit
card company each month.

The following variables contain values as described below:
* balance - the outstanding balance on the credit card
* annualInterestRate - annual interest rate as a decimal
* monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining
balance. At the end of 12 months, print out the remaining balance. Be sure
to print out no more than two decimal digits of accuracy.

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) +
                             (Monthly interest rate x Monthly unpaid balance)

"""


def paying_debt(balance, annualInterestRate, monthlyPaymentRate, month=12):
    monthlyInterestRate = annualInterestRate / 12.0
    for i in range(month):
        min_monthly_payment = balance * monthlyPaymentRate
        monthly_unpaid = balance - min_monthly_payment
        balance = monthly_unpaid * (1 + monthlyInterestRate)

    print('Remaining balance: %.2f' % balance)
    return float('%.2f' % balance)
