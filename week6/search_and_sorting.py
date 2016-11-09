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


def linear_search(L, e):
    """
    go thru every element in L to find e.
    """
    for i in range(len(L)):
        if L[i] == e:
            return True

    return False
