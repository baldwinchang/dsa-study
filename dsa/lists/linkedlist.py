"""
    Linked Lists are an elementary data structure where
    a node contains its value as well as a reference to the next node.


    Finding a value: O(N)
    Inserting at the head: Theta(1)
    Inserting at the tail: Theta(N)... UNLESS you have a tail reference, which would then move it to Theta(1)

"""

class LL:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return pretty_print(self)


def pretty_print(head):
    if head is None:
        return '*'

    return '{}->'.format(head.value) + pretty_print(head.next)


def create_from_list(L):
    if len(L) == 0:
        return None

    head = LL(L[0])
    cursor = head
    i = 1

    while i < len(L):
        new_node = LL(L[i])
        cursor.next = new_node
        cursor = cursor.next
        i += 1

    return head


def reverse(head):
    if head is None:
        return None

    previous = None
    cursor = head
    while cursor is not None:
        next_node = cursor.next
        cursor.next = previous
        previous = cursor
        cursor = next_node
        head = previous

    return head

if __name__ == '__main__':
    L = [6,2,1,2,8,9]
    ll = create_from_list(L)
    print(ll)

    ll_r = reverse(ll)
    print(ll_r)
