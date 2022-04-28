from typing import List

INF = float("inf")
NEG_INF = float("-inf")


def in_order(array: List[int], index: int) -> bool:
    x = NEG_INF if index == 0 else array[index - 1]
    y = array[index]
    z = INF if index == len(array) - 1 else array[index + 1]
    return x <= y <= z


def subarray_sort(array: List[int]) -> List[int]:
    min_ooo = INF
    max_ooo = NEG_INF

    for i, x in enumerate(array):
        if not in_order(array, i):
            min_ooo = min(min_ooo, x)
            max_ooo = max(max_ooo, x)
            pass

    if min_ooo == INF:
        return [-1, -1]

    unsorted_start = 0
    while array[unsorted_start] <= min_ooo:
        unsorted_start += 1

    unsorted_last = len(array) - 1
    while max_ooo <= array[unsorted_last]:
        unsorted_last -= 1

    return [unsorted_start, unsorted_last]
