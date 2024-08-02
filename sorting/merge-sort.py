"""
Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input array 
into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array.

In simple terms, we can say that the process of merge sort is to divide the array into two halves, 
sort each half, and then merge the sorted halves back together. This process is repeated until the entire array is sorted.
Here’s a step-by-step explanation of how merge sort works:

    1-Divide: Divide the list or array recursively into two halves until it can no more be divided.
    2-Conquer: Each subarray is sorted individually using the merge sort algorithm.
    3-Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.
input = [-1, 8, 3, 62, 0, 4, -6]
"""

from typing import List, Tuple


def devide(arr: List):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return left, right
    else:
        raise


def merge_sort(arr: List) -> List:
    size = len(arr)

    if size > 1:
        # Devide
        left, right = devide(arr)
        l_left = len(left)
        l_right = len(right)
        # Sort
        if l_left > 1:
            left = merge_sort(left)
        if l_right > 1:
            right = merge_sort(right)
        # conquere
        i, j = 0, 0
        temp_merge = []
        while i < l_left and j < l_right:
            if left[i] < right[j]:
                temp_merge.append(left[i])
                i += 1
            elif left[i] > right[j]:
                temp_merge.append(right[j])
                j += 1
            elif left[i] == right[j]:
                temp_merge.append(left[i])
                temp_merge.append(right[j])
                i += 1
                j += 1
        if i < l_left:
            temp_merge = temp_merge + left[i:]
        if j < l_right:
            temp_merge = temp_merge + right[j:]
        return temp_merge
    else:
        return arr


if __name__ == "__main__":
    input = [-1, 8, 3, 62, 0, 4, -6]
    res = merge_sort(input)
    print(res)
