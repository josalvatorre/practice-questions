from functools import lru_cache
from typing import List, Optional


def min_number_of_coins_for_change(amount: int, denoms: List[int]) -> int:

    denoms.sort(reverse=True)

    def min_coins(remaining: int, start: int) -> Optional[int]:

        if remaining < 0:
            return None
        if remaining == 0:
            return 0

        min_coin_count = None
        for d in range(start, len(denoms)):
            denomination = denoms[d]

            for coin_count in reversed(
                range(
                    1,
                    (remaining // denomination) + 1,
                )
            ):
                result = min_coins(
                    remaining - (denomination * coin_count),
                    d + 1,
                )
                if result is not None:
                    result += coin_count
                    if min_coin_count is None:
                        min_coin_count = result
                    else:
                        min_coin_count = min(
                            result,
                            min_coin_count,
                        )
        return min_coin_count

    coins = lru_cache(maxsize=None)(min_coins)(amount, 0)
    if coins is None:
        return -1
    return coins
