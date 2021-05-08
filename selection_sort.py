from typing import List


def selection_sort(array: List[int]) -> List[int]:

    def index_of_smallest(start_: int) -> int:
        i = start_
        for j in range(start_ + 1, len(array)):
            if array[j] < array[i]:
                i = j
        return i

    # We don't need to go all the way to the end.
    # By the time we only have one element left, the array will be sorted.
    for start in range(len(array) - 1):
        # Get the smallest element in the unsorted list.
        i_smallest = index_of_smallest(start)
        # Put it at the beginning of the unsorted list.
        # It's now part of the sorted list.
        array[start], array[i_smallest] = array[i_smallest], array[start]

    return array
