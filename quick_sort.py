import random
from typing import List


def quick_sort(array: List[int]) -> List[int]:
    def partition(start: int, end: int) -> int:
        """
        Divides array into two sublist where
        left_sublist... < pivot < right_sublist...
        Returns the pivot index.
        """
        pivot_value = array[random.randint(start, end)]
        i = start
        j = end
        while True:
            # try to find an (i, j) pair such that
            # array[i] > pivot_value > array[j]
            # ie they should swap places
            while array[i] < pivot_value:
                i += 1
            while pivot_value < array[j]:
                j -= 1
            # If we could not find an (i, j) pair,
            # then the array is partitioned.
            if j <= i:
                return j
            # swap the two values
            array[i], array[j] = array[j], array[i]
            # make sure that we don't compare the same values again
            i += 1
            j -= 1
        pass

    def sort(start: int, end: int) -> None:
        if end <= start:
            return
        pivot_index = partition(start, end)

        # sort both halves, including the pivot

        def sort_left():
            sort(start, pivot_index)

        def sort_right():
            sort(pivot_index + 1, end)

        # sort the shorter side first
        if (pivot_index - start) < (end - (pivot_index + 1)):
            sort_left()
            sort_right()
        else:
            sort_right()
            sort_left()
        pass

    sort(0, len(array) - 1)
    return array
