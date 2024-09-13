"""
Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array 
into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, 
sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
Here’s a step-by-step explanation of how merge sort works:

    1-Divide: Divide the list or array recursively into two halves until it can no more be divided.
    2-Conquer: Each subarray is sorted individually using the merge sort algorithm.
    3-Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.

# How does QuickSort Algorithm work?
There are mainly three steps in the algorithm.
    1. Choose a pivot
    2. Partition the array around pivot. After partition, it is ensured that all elements are smaller than all right and we get index of the end point of smaller elements. The left and right may not be sorted individually.
    3. Recursively call for the two partitioned left and right subarrays.
    4. We stop recursion when there is only one element is left.
input = [-1, 8, 3, 62, 0, 4, -6]
"""

from typing import List, Tuple


class quick_sort:
    def __init__(self, arr) -> None:

        self.arr = arr
        self.size = len(arr)

        left = 0
        right = len(arr) - 1
        self.sort(left, right)

    def devide(self, left: int, right: int, pivot: int) -> None:

        print(left, right, pivot)
        self.sort(left, pivot - 1) if pivot > 0 and pivot >= left else 0
        self.sort(pivot + 1, right) if pivot < self.size - 1 and pivot <= right else 0

    def sort(self, left: int, right: int) -> None:

        pivot = right
        i = left
        j = right - 1
        if right - left < 1:
            return None

        while i <= j and j >= 0 and i <= pivot:
            if self.arr[i] > self.arr[pivot]:
                if self.arr[j] < self.arr[pivot]:
                    self._swap(i, j)
                else:
                    j -= 1
            else:
                i += 1

        self._swap(i, pivot)
        pivot = i
        self.devide(left, right, pivot)

    def _swap(self, i: int, j: int) -> None:

        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]


if __name__ == "__main__":

    input = [-1, 8, 3, 62, 0, 4, -6]
    res = quick_sort(input)
    print(res.arr)
