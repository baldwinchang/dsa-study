"""
    Stack Implementation using a Linked List

    Since we only care about the most recent value inserted into
    a stack (LIFO), a linked list with no extra tracking variables. (only the head!)

    There are no traversals happening in any of the operations:

    Insert: O(1)
    Pop/Removal: O(1)

    Really good! Space is minimal at O(n), as you need to store a node for every value.
"""

from dsa.lists import LL

class Stack:

    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, value):
        new_node = LL(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        if self.length > 0:
            popped_element = self.head
            self.head = self.head.next
            self.length -= 1
            return popped_element.value

    def peek(self):
        if self.length > 0:
            return self.head.value

    def empty(self):
        return self.length == 0


if __name__ == '__main__':
    s = Stack()
    for i in range(15):
        s.insert(i)
        print("Length: {}, Peek: {}".format(s.length, s.peek()))

    while not s.empty():
        print("Popped value: {}".format(s.pop()))

