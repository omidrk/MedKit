"""
In Python, a stack can be implemented using various data structures such as lists, collections.deque, 
or custom classes. A stack is a LIFO (Last In, First Out) data structure, where the last element added 
is the first one to be removed. 
Here is how you can implement a stack in Python using these different approaches:
"""

## array approach


class stack:
    def __init__(self) -> None:
        self.data = []
        self.size = 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop() if not self.is_empty() else None

    def peek(self):
        return self.data[-1] if not self.is_empty() else None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return True if len(self.data) == 0 else False


## class approach


class node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class class_stack:
    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def push(self, item):
        new_node = node(item)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            head = self.head
            self.head = self.head.next
            self._size -= 1
            return head.value
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.head.value
        else:
            return None

    def size(self):
        return self._size

    def is_empty(self):
        return True if self._size == 0 else False


## collection dequeue
from collections import deque


class c_stack:
    def __init__(self):
        self.stack = deque()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
