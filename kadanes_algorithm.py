from typing import List


def kadanes_algorithm(array: List[int]) -> int:
    current = greatest_sum = array[0]

    for i in range(1, len(array)):
        x = array[i]
        # reset or extend the sequence?
        current = max(x, current + x)
        # update the greatest sum
        greatest_sum = max(greatest_sum, current)

    return greatest_sum
