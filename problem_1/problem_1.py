"""
Author: Ramiz Raja
Created on: 11/01/2020
Problem:
"""


def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    # square root of a number is: a value that can be multiplied by itself to give the given number
    square_root = 0
    while (square_root * square_root) < n:
        square_root += 1

    if (square_root * square_root) == n:
        return square_root
    else:
        return square_root - 1


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def tests():
    number = 9
    assert_(expected=3, actual=sqrt(number))

    number = 16
    assert_(expected=4, actual=sqrt(number))

    number = 27
    assert_(expected=5, actual=sqrt(number))

    # edge cases
    number = 0
    assert_(expected=0, actual=sqrt(number))

    number = 1
    assert_(expected=1, actual=sqrt(number))

    number = 2
    assert_(expected=1, actual=sqrt(number))


tests()




