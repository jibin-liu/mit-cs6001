"""
implementation of different search and sorting techniques
1. linear search: O(n)
2. bisection search: O(logn). list has to be sorted first.
3. random sorting
4. bubble sorting: O(n^2)
5. search sorting: O(n^2)
6. merge sorting: O(nlogn)

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
            return bisection_search(L[mid+1:], e)


def random_sort(L):
    """
    if L is not sorted, shuffle it randomly.
    """
    is_sorted = False

    while not is_sorted:
        random.shuffle(L)
        is_sorted = True

        for i in range(1, len(L)):
            if L[i] < L[i-1]:
                is_sorted = False
                break

    return L


def bubble_sort(L):
    """
    if one element is greater than it's next element, switch their values.
    """
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(L) - 1):
            if L[i] > L[i+1]:
                is_sorted = False
                L[i], L[i+1] = L[i+1], L[i]

    return L


def selection_sort(L):
    """
    Find the smallest element and put it on index 0; then find the second
    smallest element and put it on index 1; etc...
    """
    for i in range(len(L) - 1):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]

    return L


def merge_sort(L):
    """
    split L into half to sort, and then merge the results
    """
    def merge(a, b):
        """
        merging process, a and b will be already sorted.
        """
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        if i < len(a):
            result.extend(a[i:])

        if j < len(b):
            result.extend(b[j:])

        return result

    if len(L) < 2:
        return L
    else:
        mid = len(L) // 2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        return merge(left, right)
