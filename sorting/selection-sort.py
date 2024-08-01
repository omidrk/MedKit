"""
Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest)
element from the unsorted portion of the list and moving it to the sorted portion of the list. 
Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops.

input = [-1,8,3,62,0,4]
"""

from typing import List


def selection_sort(arr: List):
    size = len(arr)
    for i in range(size):
        min_index = i
        for j in range(i, size):
            if arr[j] < arr[min_index]:
                min_index = j
        # visualize the evolution
        print(arr)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == "__main__":
    input = [-1, 8, 3, 62, 0, 4, -6]
    selection_sort(input)
