"""
In Python, a queue can be implemented using several methods such as lists, collections.deque, or the queue module. 
A queue is a FIFO (First In, First Out) data structure, where the first element added is the first one to be removed. 
Here is how you can implement a queue in Python using these different approaches:

1. Using a List
While not the most efficient method due to the time complexity of popping from the front, you can use a list to implement a queue.

2. Using collections.deque
The deque from the collections module is optimized for fast append and pop operations from both ends, 
making it a better choice for implementing a queue.

3. Using the queue.Queue Class
The queue module provides a synchronized queue class which is useful for multi-threaded programming.

Choosing an Implementation
- List: Simple to use but not efficient for large queues due to the O(n) complexity of pop(0).
- deque: Efficient and straightforward for most queue operations; recommended for general use.
- queue.Queue: Thread-safe and suitable for multi-threaded applications, but slightly more complex to use.

For most applications, using collections.deque is recommended due to its performance benefits and ease of use.
"""


## Using List implementation
class queue:
    def __init__(self) -> None:
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0) if not self.is_empty() else None

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return True if len(self.data) == 0 else False


## using collection deque

from collections import deque


class deq_queue:
    def __init__(self) -> None:
        self.data = deque()

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.popleft() if not self.is_empty() else None

    def peek(self):
        return self.data[0] if not self.is_empty() else None

    def size(self):
        return len(self.data)

    def is_empty(self):
        return True if len(self.data) == 0 else False


## using python queue
import queue


class q_queue:
    def __init__(self) -> None:
        self.data = queue.Queue()

    def enqueue(self, item):
        self.queue.put(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.get()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            front_item = self.queue.get()
            self.queue.put(front_item)
            return front_item
        else:
            return None

    def is_empty(self):
        return self.queue.empty()

    def size(self):
        return self.queue.qsize()
