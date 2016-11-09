"""
implementation of different search and sorting techniques
1. linear search: O(n)
2. bisection search: O(logn). list has to be sorted first.
3. random sorting
4. bubble sorting
5. search sorting
6. merge sorting

Assume L is a list of length n, e is the element to be find
"""

import random


def linear_search(L, e):
    """
    go thru every element in L to find e.
    """
    for i in range(len(L)):
        if L[i] == e:
            return True

    return False


def bisection_search(L, e):
    """
    assume L is already sorted, and size won't change
    """
    if len(L) == 0:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        low = 0
        high = len(L)
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            return bisection_search(L[:mid], e)
        else:
            return bisection_search(L[mid + 1:], e)


def random_sort(L):
    """
    if L is not sorted, shuffle it randomly.
    """
    is_sorted = False

    while not is_sorted:
        random.shuffle(L)
        is_sorted = True

        for i in range(1, len(L)):
            if L[i] < L[i - 1]:
                is_sorted = False
                break

    return L
