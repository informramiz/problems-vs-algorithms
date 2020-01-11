"""
Author: Ramiz Raja
Created on: 12/01/2020
Problem: Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers.
The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    n = len(ints)
    if n == 0:
        # empty array
        return (None, None)

    min_value = ints[0]
    max_value = ints[0]
    for number in ints:
        if number > max_value:
            max_value = number
        elif number < min_value:
            min_value = number

    return min_value, max_value


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def test_function(array):
    min_max = get_min_max(array)
    expected = (min(array), max(array))
    assert_(expected=expected, actual=min_max)


def tests():
    array = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(array)
    test_function(array)

    array = [2, 1, 0, 4, 8]
    test_function(array)

    # edge cases
    test_function([1, 1])
    test_function([-1, -8])
    test_function([0])


tests()