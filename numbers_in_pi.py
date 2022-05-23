from functools import lru_cache
from typing import List


def numbers_in_pi(pi: str, numbers: List[str]) -> int:
    infinity = float("inf")
    numbers_set = set(numbers)
    min_count = infinity
    insertion_count = 0

    def search(last_insertion_index: int) -> None:
        nonlocal insertion_count, min_count

        if last_insertion_index == len(pi):
            # We don't count the last insertion.
            insertion_count -= 1
            min_count = min(min_count, insertion_count)
            return

        original_count = insertion_count

        for i in range(last_insertion_index + 1, len(pi) + 1):
            this_string = pi[last_insertion_index:i]
            if this_string in numbers_set:
                insertion_count += 1
                search(i)
                pass
            insertion_count = original_count
        pass

    lru_cache(maxsize=None)(search)(0)
    return -1 if min_count == infinity else min_count
