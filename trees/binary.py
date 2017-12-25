"""
    Implementation of Binary Search Tree (Unbalanced)

    Search:
        1) Traverse the BST, starting at the root.
        2) If we reach None, the value does not exist (return None)
        3) At the current node
            a) if the value equals, we found it!
            b) if the value is greater than, search the left subtree.
            c) if the value is less than, search the right subtree.

        Time-complexity:
        - O(N) if we have a pathological tree (pretty much a linked list)
        - O(NLogN) if we have a balanced binary tree

    Insertion (non self balancing):
        1) Traverse the BST until we find an open space (leaf)
            a) Search until we find None!
            b) If we find the value we're trying to insert, exit! It already exists.

        * Some implementations can indeed have a count on the node

        Time-complexity: Same as search for the same reasons.

    Removal:
        1) Traverse the BST to find the value (refer to Search)
        2) Delete that node based on three distinct conditions
            1) If it has no children (it is a leaf), delete it.
            2) If it has one child, promote:
                a) Set the value of the node to its child
                b) Propagate the grandchildren to the node as children
            3) If it has 2 children:
                a) Find the smallest-largest or largest-smallest. (find the value, then delete it)
                    i) Deleting the above criteria will follow deletion conditions 2.1 and 2.2... why?
                    ii) Because the smallest-largest or largest-smallest will guaranteed have only 0 or 1 child nodess
                    iii) Otherwise, it isn't the smallest-largest or largest-smallest.
                b) Set the node's value to the smallest-largest or largest-smallest value we deleted.

"""

class TN:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return pretty_print(self)

def pretty_print(root, indent=''):
    if root is None:
        return ""

    result = ""
    result += pretty_print(root.right, indent='..' + indent)
    result += "{}{}\n".format(indent, root.value)
    result += pretty_print(root.left, indent='..' + indent)
    return result


def search(root, value):
    if root is None:
        return False

    if root.value == value:
        return True
    elif root.value > value:
        return search(root.left, value)
    else: # root.value < value
        return search(root.right, value)


def insert(root, value):
    if root is None:
        return TN(value)

    if root.value == value:
        return root
    elif root.value > value:
        root.left = insert(root.left, value)
        return root
    else: # root.value < value
        root.right = insert(root.right, value)
        return root


def smallest_largest(root):
    cursor = root
    while cursor.left is not None:
        cursor = cursor.left
    return cursor.value


def remove(root, value):
    if root is None:
        return None

    if root.value > value:
        root.left = remove(root.left, value)
        return root
    elif root.value < value:
        root.right = remove(root.right, value)
        return root

    if root.left is None and root.right is None:
        return None
    elif root.left is not None and root.right is None:
        left = root.left
        root.value = left.value
        root.left = left.left
        root.right = left.right
        return root
    elif root.left is None and root.right is not None:
        right = root.right
        root.value = right.value
        root.left = right.left
        root.right = right.right
        return root
    else:
        sl_value = smallest_largest(root.right)
        root = remove(root, sl_value)
        root.value = sl_value
        return root

if __name__ == '__main__':
    import random
    randomize = range(1,15)
    random.shuffle(randomize)

    tree = None
    for i in randomize:
        tree = insert(tree, i)
        assert search(tree, i) == True

    print(tree)

    for i in randomize:
        tree = remove(tree, i)
        assert search(tree, i) == False

    print(tree)

