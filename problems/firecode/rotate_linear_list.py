"""
Rotate Linear Array

Analysis:
Runtime: O(n)
Each reversal works on up to the whole array

Space: O(1)
This is an in-place operation. No extra space.
"""


def rotate_left(list_numbers, k):
    swap_k = k % len(list_numbers)
    reverse_list(list_numbers, 0, len(list_numbers))

    reverse_list(list_numbers, 0, swap_k)
    reverse_list(list_numbers, swap_k, len(list_numbers))

    return list_numbers


def reverse_list(l, start, end):
    mid = (end - start) // 2
    for i in range(mid):
        tmp = l[start + i]
        l[start + i] = l[end - i - 1]
        l[end - i - 1] = tmp


print(rotate_left([1, 2, 3, 4, 5], 5))
