"""
Author: Ramiz Raja
Created on: 11/01/2020
Problem 3: Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers.
You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot
differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time
complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when
there are more than one possible answers, return any one.
"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    n = len(input_list)
    heap_sort(input_list)

    decimal_value = 1
    n1 = 0
    for i in range(0, n, 2):
        n1 += input_list[i] * decimal_value
        decimal_value *= 10

    decimal_value = 1
    n2 = 0
    for i in range(1, n, 2):
        n2 += input_list[i] * decimal_value
        decimal_value *= 10

    return n1, n2


def heap_sort(array):
    # convert array into max-heap
    n = len(array)
    for i in range(n-1, -1, -1):
        heapify_down(array, i, n)

    # swap max element at the end and call heapify again repeatedly
    for i in range(n-1, -1, -1):
        # Remove max element from heap: involves following 2 steps
        # 1. swap max element (array[0]) with element at last
        array[0], array[i] = array[i], array[0]
        # 2. heapify the root element (array[0] is always the root in a heap) till the i-1 index or n = i size
        heapify_down(array, 0, i)


def heapify_down(array, parent, n):
    while parent < n:
        left = 2 * parent + 1
        right = 2 * parent + 2
        max_index = parent

        if left < n and array[left] > array[parent]:
            max_index = left

        if right < n and array[right] > array[max_index]:
            max_index = right

        if max_index != parent:
            # swap parent with child that has maximum value (max_index child)
            array[parent], array[max_index] = array[max_index], array[parent]
            # now check on the child
            parent = max_index
        else:
            # parent is fine so no need to check down
            break


def assert_(expected, actual):
    assert expected == actual, f"expected={expected}, actual={actual}"
    print("Pass")


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    assert_(expected=sum(solution), actual=sum(output))


def tests():
    test_case = ([1, 2, 3, 4, 5], [542, 31])
    test_function(test_case)

    test_case = ([4, 6, 2, 5, 9, 8], [964, 852])
    test_function(test_case)

    # edge cases
    test_case = ([1, 0, 0, 0, 1], [100, 10])
    test_function(test_case)

    test_case = ([0, 0], [0, 0])
    test_function(test_case)

    test_case = ([], [0, 0])
    test_function(test_case)


tests()
