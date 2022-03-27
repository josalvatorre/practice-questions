from typing import List


def array_of_products(array: List[int]) -> List[int]:
    factors_left = [1] * len(array)
    factors_right = [1] * len(array)

    for i in range(1, len(array)):
        factors_left[i] = factors_left[i - 1] * array[i - 1]

    for i in range(len(array) - 2, -1, -1):
        factors_right[i] = factors_right[i + 1] * array[i + 1]

    return list(factors_left[i] * factors_right[i] for i in range(len(array)))
