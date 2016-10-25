"""
Use bisection search to calculate square root of a given number x
"""


def calculate_square_root(x, power=2):
    low = 0
    high = x
    guess = (high + low) / 2
    limit = 0.001
    guess_number = 0

    while abs(guess ** power - x) >= limit:
        if guess ** power > x:
            high = guess
        else:
            low = guess

        guess = (high + low) / 2
        guess_number += 1

    print('Guess Number is %d' % guess_number)

    return guess

