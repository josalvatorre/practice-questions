from typing import List


def non_constructible_change(coins: List[int]) -> int:

    coins.sort()
    max_change = 0

    for c in coins:
        if max_change + 1 < c:
            return max_change + 1
        max_change += c

    return max_change + 1
