"""
    Implementation details on Merge Sort:

        1. Break up your lists into two halves (Left and Right)
            a. Continue until your lists are size one or less (Recursively)
        2. Merge your two halves (which in the call stack's view, you're starting from small sublists)

    Runtime Complexity:
    O(nlogn)


    Space Complexity:
    O(n)

    We take up a call stack frame for each element of the list in the split phase.
"""

def merge_two_sorted_lists(L, R):
    resultant = list()
    while len(L) > 0 or len(R) > 0:
        if len(L) > 0 and len(R) == 0:
            resultant.append(L.pop(0))
        elif len(L) == 0 and len(R) > 0:
            resultant.append(R.pop(0))
        elif L[0] < R[0]:
            resultant.append(L.pop(0))
        else:
            resultant.append(R.pop(0))

    return resultant


def merge_sort(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2
    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    return merge_two_sorted_lists(left, right)


if __name__ == '__main__':
    L = [1,8,2,19,4]
    print(merge_sort(L))

    L = []
    print(merge_sort(L))
