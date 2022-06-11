from functools import lru_cache
from typing import List


def min_number_of_jumps(array: List[int]) -> int:
    def min_jumps(index: int) -> int:
        if index == len(array) - 1:
            return 0

        return 1 + min(
            min_jumps(new_index)
            for new_index in range(
                index + 1,
                min(index + array[index], len(array) - 1) + 1,
            )
        )

    return lru_cache(maxsize=None)(min_jumps)(0)
