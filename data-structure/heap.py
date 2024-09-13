"""
A heap is a specialized binary tree-based data structure that satisfies the heap property. 
Heaps are commonly used to implement priority queues and for heap sort.

There are two types of heaps:

- Max-Heap: The value of each node is greater than or equal to the values of its children. 
            The maximum value is always at the root.
- Min-Heap: The value of each node is less than or equal to the values of its children. 
            The minimum value is always at the root.

Suppose we are given an array, arr[] representing the complete binary tree. The left and 
the right child of ith node are in indices 2*i+1 and 2*i+2.

Operations:
- Insertion:
    - If we insert a new element into the heap since we are adding a new element into the heap so 
      it will distort the properties of the heap so we need to perform the heapify operation so 
      that it maintains the property of the heap.
    - This operation also takes O(logN) time.

- Deletion:
    - If we delete the element from the heap it always deletes the root element of the tree and replaces 
      it with the last element of the tree.
    - Since we delete the root element from the heap it will distort the properties of the heap so we need 
      to perform heapify operations so that it maintains the property of the heap. 
    - It takes O(logN) time.
"""


class MaxHeap:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.heap = []

    def _left_child(self, idx: int) -> int:
        return 2 * idx + 1

    def _right_child(self, idx: int) -> int:
        return 2 * idx + 2

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _heapify_up(self, idx: int) -> None:
        parent_index = self._parent(idx)
        if self.heap[idx] > self.heap[parent_index] and idx > 0:
            self._swap(idx, parent_index)
            self._heapify_up(parent_index)
        else:
            return

    def _heapify_down(self, idx: int) -> None:

        left_child_idx = self._left_child(idx)
        right_child_idx = self._right_child(idx)
        biggest_index = idx

        if (
            self._valid_index(left_child_idx)
            and self.heap[left_child_idx] > self.heap[biggest_index]
        ):
            biggest_index = left_child_idx
        if (
            self._valid_index(right_child_idx)
            and self.heap[right_child_idx] > self.heap[biggest_index]
        ):
            biggest_index = right_child_idx

        if biggest_index != idx:
            self._swap(idx, biggest_index)
            self._heapify_down(biggest_index)

    def _swap(self, index_a, index_b):
        self.heap[index_a], self.heap[index_b] = self.heap[index_b], self.heap[index_a]

    def _valid_index(self, idx) -> bool:
        return True if idx > 0 and idx < len(self.heap) else False

    def insert(self, item: int) -> None:
        if len(self.heap) > self.max_size:
            print("Heap is at full size.")
            return

        self.heap.append(item)
        if len(self.heap) > 1:
            self._heapify_up(len(self.heap) - 1)

    def pop_max(self) -> int:
        if len(self.heap) == 1:
            return self.heap.pop()

        if len(self.heap) == 0:
            print("MaxHeap is empty.")
            return None

        item_index = 0
        poped_item = self.heap[item_index]
        last_element = self.heap.pop()
        self.heap[item_index] = last_element
        self._heapify_down(item_index)
        return poped_item


if __name__ == "__main__":
    max_heap = MaxHeap(10)
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(6)
    max_heap.insert(5)
    max_heap.insert(2)
    max_heap.insert(4)
    max_heap.insert(9)
    max_heap.insert(7)
    max_heap.insert(8)

    print(max_heap.heap)
    print(max_heap.pop_max())
    print(max_heap.heap)
