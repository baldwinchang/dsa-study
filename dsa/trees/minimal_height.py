"""
Question from CTCI: Trees and Graphs 4.2

Given a sorted (increasing order) array with unique integer
elements, write an algorithm to create a binary search tree
with minimal height.

---

A sorted, unique, array will have exactly half of its elements that would lie in a BST in the
first half of the array, and its other half in the second half.

By picking the middle element each pass from the full array, then its left array and right array,
we can create a balanced tree with a simple insert algorithm (finding the first spot that the element would lie).

We implement this with a stack to be a tracker for which elements left to operate on.

Analysis:

BST naive insert: O(logn) - you traverse at most the height of the tree.
You do this for each element we add to the BST. Therefore, we have a complexity of O(nlogn).

"""

from dsa.trees.binary import insert

def create_minimal_tree(arr):
    to_process = [arr]
    root = None

    while len(to_process) > 0:
        a = to_process.pop()
        mid = len(a) // 2
        root = insert(root, a[mid])


        left = a[:mid]
        right = a[mid+1:]

        if len(left) > 0:
            to_process.append(left)

        if len(right) > 0:
            to_process.append(right)

    return root


if __name__ == '__main__':
    tree = create_minimal_tree([i for i in range(7)])
    print(tree)