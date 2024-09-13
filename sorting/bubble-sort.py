"""
Bubble Sort is a simple sorting algorithm that works by repeatedly stepping through the list to be sorted, 
comparing each pair of adjacent items, and swapping them if they are in the wrong order. 
Total no. of passes: n-1
Total no. of comparisons: n*(n-1)/2

input = [-1,8,3,62,0,4]

"""

from typing import List


def bubble_sort(arr: List):
    size = len(arr)
    for i in range(size):
        for j in range(size - i):
            # visualize the evolution
            print(arr)
            if j + 1 < size - i and arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


if __name__ == "__main__":
    input = [-1, 8, 3, 62, 0, 4, -6]
    bubble_sort(input)
