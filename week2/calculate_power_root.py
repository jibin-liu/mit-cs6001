"""
Use bisection search to calculate power root of a given number x
"""


def calculate_power_root(x, power=2):
    if x == 0:
        raise ValueError('input is invalid')
    elif x > 0:
        low = 0
        high = x if x > 1 else 1
        guess = (high + low) / 2
        limit = 0.00001
        guess_number = 0

        while abs(guess ** power - x) >= limit:
            if guess ** power > x:
                high = guess
            else:
                low = guess

            guess = (high + low) / 2
            guess_number += 1

    print('Number of guess is %d' % guess_number)

    return guess

