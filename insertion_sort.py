from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    while True:
        swapped = False
        # i, j will be all neighboring indices.
        for i in range(len(array) - 1):
            j = i + 1

            if array[i] > array[j]:
                swapped = True
                array[i], array[j] = array[j], array[i]
        # we finished when there were no swaps.
        if not swapped:
            return array
