from typing import List


def square(x: int) -> int:
    return x**2


def sorted_squared_array(array: List[int]) -> List[int]:
    if len(array) == 0:
        return []
    if 0 <= array[0]:
        # Then there are no negative numbers.
        return list(map(square, array))
    if array[-1] <= 0:
        # Then there are no positive numbers.
        return list(map(square, reversed(array)))

    first_positive = next(i for i in range(len(array)) if array[i] > 0)

    positives = map(
        square, (array[i] for i in range(first_positive, len(array)))
    )
    non_positives = map(
        square, (array[i] for i in reversed(range(0, first_positive)))
    )

    squared_sorted = []

    pos = next(positives)
    non_pos = next(non_positives)
    while any(x is not None for x in (pos, non_pos)):
        if pos is None or (non_pos is not None and non_pos <= pos):
            squared_sorted.append(non_pos)
            non_pos = next(non_positives, None)
        else:
            squared_sorted.append(pos)
            pos = next(positives, None)
        pass

    return squared_sorted
