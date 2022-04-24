from typing import List


def minimum_waiting_time(queries: List[int]) -> int:
    queries.sort()
    total = 0

    for i, time in enumerate(queries):
        total += ((len(queries) - 1) - i) * time
        pass

    return total
