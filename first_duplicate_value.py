from typing import List


def first_duplicate_value(array: List[int]) -> int:

    for x in map(abs, array):
        # The index of the possibly negated value.
        x_seen_index = x - 1
        # If negated, then we already saw this value
        # on some other iteration.
        if array[x_seen_index] < 0:
            return x
        # Flag as seen by negating it.
        array[x_seen_index] = -array[x_seen_index]

    return -1
