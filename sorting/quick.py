"""
    Implementation of QuickSort

    1) Base case is a list of length 1 or less. (they're already sorted!)
    2) Select a Pivot (we'll select the right-most for simplicity)
    3) Place all values greater than the pivot to the right.
    4) Repeat for left and right sublists (the pivot is in the right place)

"""


def quicksort(L):
    if len(L) <= 1:
        return L

    pivot_i = len(L) - 1
    i = 0
    while i < pivot_i:
        if L[i] >= L[pivot_i]:
            tmp = L[pivot_i]
            L[pivot_i] = L[pivot_i-1]
            L[pivot_i-1] = tmp

            # swap if we haven't yet
            if pivot_i - 1 != i:
                tmp = L[i]
                L[i] = L[pivot_i]
                L[pivot_i] = tmp

            pivot_i -= 1
        else:
            i += 1

    return quicksort(L[:pivot_i]) + [L[pivot_i]] + quicksort(L[pivot_i+1:])

if __name__ == '__main__':
    L = [8,2,0,22,6]
    print(quicksort(L))