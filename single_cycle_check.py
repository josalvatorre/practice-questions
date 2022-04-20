from typing import List, Set


def has_single_cycle(array: List[int]) -> bool:

    visited: Set[bool] = set()
    position = 0

    while position not in visited:

        visited.add(position)

        position += array[position]

        if position < 0:
            position = abs(position) % len(array)
            position = 0 if position == 0 else len(array) - position
        elif len(array) <= position:
            position %= len(array)
        pass

    return len(visited) == len(array) and position == 0
