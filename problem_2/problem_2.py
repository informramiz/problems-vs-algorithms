"""
Author: Ramiz Raja
Created on: 11/01/2020

Problem: Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4
"""


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # As array is sorted (even if it is rotated), with a little tweak to the binary search logic we can use
    # binary search and achieve the desired solution in ln(n)
    n = len(input_list)
    start = 0
    end = n - 1
    while start <= end:
        m = (start + end) // 2
        if input_list[m] == number:
            return m
        elif input_list[start] > input_list[end]:  # check if array part [start, end] is rotated or not
            # if input_list[start] > input_list[end] then that means the array part we are checking still contains
            # rotated numbers
            if number <= input_list[end]:
                # if number <= input_list[end] then that means number is in range [m+1, end]
                start = m + 1
            else:
                # if number > input_list[end] then that means number is in range [start, m-1]
                end = m - 1
        # below are the cases executed only when current array range [start, end] is not rotated
        elif number > input_list[m]:
            # number is in range [m+1, end]
            start = m + 1
        else:
            # number < mid number so number is in range [start, m-1]
            end = m - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    assert_(expected=linear_search(input_list, number), actual=rotated_array_search(input_list, number))


def tests():
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])


tests()
