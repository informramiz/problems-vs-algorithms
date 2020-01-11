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
    # square root of 0 is 0 and 1 is 1 so return the same
    if n == 0 or n == 1:
        return n

    # square root of a number is: a value that can be multiplied by itself to give the given number
    # As sqrt(n) will be between [2, n/2] so do a simple binary search to find the solution
    start = 1
    end = n/2
    ans = 2
    while start <= end:
        m = (start + end) // 2
        if m * m == n:
            return m
        elif m * m < n:
            # save last m for which (m*m) < n because in cases like 27 which are not perfect squares we need
            # the lower bound which for 27 will be 5
            ans = m
            # sqrt(n) is probably greater than m so move to the right side
            start = m + 1
        else:  # m * m > n
            # sqrt(n) is probably is smaller so move to the left side
            end = m - 1

    return ans


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




