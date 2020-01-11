"""
Author: Ramiz Raja
Created on: 12/01/2020
Problem: Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
You're not allowed to use any sorting function that Python provides.

Note: O(n) does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still
be an O(n) solution but it will not count as single traversal.
"""


def sort_012(array):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       array(list): List to be sorted
    """
    next_index_0 = 0
    next_index_2 = len(array) - 1
    front_index = 0
    while front_index <= next_index_2:
        # Trick: front_index will only move if a[front_index] == 0 or a[front_index] == 1 to make sure front
        # of array is 0s followed by 1s, if a[front_index] == 2 then it will not move so that we can check
        # on next iteration that the a[front_index]'s new value is valid.

        if array[front_index] == 0:
            # move it on the left by swapping (front_index, next_index_0)
            array[front_index] = array[next_index_0]
            array[next_index_0] = 0
            front_index += 1
            next_index_0 += 1
        elif array[front_index] == 2:
            # move it to the right by swapping (front_index, next_index_2)
            array[front_index] = array[next_index_2]
            array[next_index_2] = 2
            next_index_2 -= 1
            # front_index will not move in this case because the new value of a[front_index] may be 0 or 2 and we need
            #  to check and handle it accordingly. This check will be done automatically if we don't move front_index
            # in this iteration
        else:
            # array[front_index] == 1, keep skipping ones until you encounter another 0 or 1
            # because we are only swapping 0s and 2s and it will automatically bring 1s to their right position
            front_index += 1

    return array


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def test_function(test_case):
    sorted_array = sort_012(test_case)
    assert_(expected=sorted(test_case), actual=sorted_array)


def tests():
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

    # edge cases
    test_function([0, 0, 0])
    test_function([1, 1, 1])
    test_function([1, 0])
    test_function([])
    test_function([0, 1, 2])


tests()