from typing import List


def sum_of_subarray_mins(array: List[int]) -> int:
    """
    3 1 2 5 4

    [3]
    [3 1]       [1]
    [3 1 2]     [1 2]     [2]
    [3 1 2 5]   [1 2 5]   [2 5]   [5]
    [3 1 2 5 4] [1 2 5 4] [2 5 4] [5 4] [4]

    3
    1 1
    1 1 2
    1 1 2 5
    1 1 2 4 4
    """
    sums_ending_at: List[int] = []
    prev_biggest_indices: List[int] = []

    for i, x in enumerate(array):
        while (
            0 < len(prev_biggest_indices)
            and x < array[prev_biggest_indices[-1]]
        ):
            prev_biggest_indices.pop()

        if 0 < len(prev_biggest_indices):
            last_smaller_index = prev_biggest_indices[-1]
            last_sum = sums_ending_at[last_smaller_index]
        else:
            last_smaller_index = -1
            last_sum = 0

        sums_ending_at.append(last_sum + (i - last_smaller_index) * x)
        prev_biggest_indices.append(i)
        pass

    return sum(sums_ending_at) % (10**9 + 7)
