"""
    Queue Implementation using a Linked List (w/ an extra reference to the tail)

    Similar to a Stack, we achieve constant insertion and removal by using two reference
    variables. A Queue will add values to the tail and pop values from the head.

    There are no traversals happening in any of the operations:

    Insert: O(1)
    Pop/Removal: O(1)

    Really good! Space is minimal at O(n), as you need to store a node for every value.
"""

from dsa.lists import LL

class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert(self, value):
        new_node = LL(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length != 0:
            popped_element = self.head

            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            self.length -= 1

            return popped_element.value

    def peek(self):
        if self.length > 0:
            return self.head.value

    def empty(self):
        return self.length == 0


if __name__ == '__main__':
    q = Queue()
    for i in range(15):
        q.insert(i)
        print("Length: {}, Peek: {}".format(q.length, q.peek()))

    while not q.empty():
        print("Popped value: {}".format(q.pop()))

