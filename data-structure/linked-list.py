"""
Linked lists are a fundamental data structure in computer science, consisting of a sequence of nodes, 
where each node contains data and a reference (or link) to the next node in the sequence. 
Linked lists can be of various types such as singly linked lists, doubly linked lists, 
and circular linked lists. Here, we'll focus on implementing a basic singly linked list and a doubly linked list in Python.

1. Singly Linked List
In a singly linked list, each node points to the next node in the sequence, and the last node points to None.

2. Doubly Linked List
In a doubly linked list, each node contains a reference to both the next node and the previous node.

"""


class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.previous = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        node = Node(value=val)
        if not self.head:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node

    def prepend(self, val):
        node = Node(value=val)
        node.next = self.head
        self.head = node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_value(self, val):
        pointer = self.head
        if pointer.value == val:
            self.head = pointer.next
            return
        while pointer.next and pointer.next.value != val:
            pointer = pointer.next
        if pointer.next:
            pointer.next = pointer.next.next


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, val):
        node = Node(value=val)
        if not self.head:
            self.head = node
        else:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = node
            node.previous = pointer

    def prepend(self, val):
        node = Node(value=val)
        if self.head:
            self.head.previous = node
        node.next = self.head
        self.head = node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end=" <-> ")
            current_node = current_node.next
        print("None")

    def delete_value(self, val):
        pointer = self.head
        if pointer and pointer.value == val:
            self.head = pointer.next
            self.head.previous = None
            return
        while pointer.next and pointer.next.value != val:
            pointer = pointer.next
        if pointer.next:
            pointer.next = pointer.next.next
            pointer.next.previous = pointer


if __name__ == "__main__":

    ll = SingleLinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None
    ll.delete_value(2)
    ll.display()  # Output: 0 -> 1 -> 3 -> None

    dll = DoubleLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    dll.display()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
    dll.delete_value(2)
    dll.display()  # Output: 0 <-> 1 <-> 3 <-> None
