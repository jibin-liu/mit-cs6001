"""
Use bisection search to calculate power root of a given number x.
If x is positive, only positive power root will be output.

About bisection search: it will work for any sequence with "ordering"
properties. That means fun(x) varies monotonically with x.
"""


def calculate_power_root(x, power=2):
    if x == 0:
        raise ValueError('input is invalid')

    else:
        low = 0
        new_x = abs(x)
        high = new_x if new_x > 1 else 1
        guess = (high + low) / 2
        limit = 0.00001
        guess_number = 0

        while abs(guess ** power - new_x) >= limit:
            if guess ** power > new_x:
                high = guess
            else:
                low = guess

            guess = (high + low) / 2
            guess_number += 1

        print('Number of guess is %d' % guess_number)

    if x > 0:
        return guess
    else:
        return -guess

