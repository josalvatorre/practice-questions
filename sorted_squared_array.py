from typing import List


def square(x: int) -> int:
    return x**2


def sorted_squared_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []

    squared_sorted = [None] * len(array)
    indices = iter(range(len(array)))
    indices_reversed = reversed(range(len(array)))

    left_i = next(indices)
    right_i = next(indices_reversed)

    for i in reversed(range(len(squared_sorted))):
        if right_i < left_i:
            break

        left = square(array[left_i])
        right = square(array[right_i])

        if right <= left:
            squared_sorted[i] = left
            left_i = next(indices, None)
        else:
            squared_sorted[i] = right
            right_i = next(indices_reversed, None)
        pass

    return squared_sorted
