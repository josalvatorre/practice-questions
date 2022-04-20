from typing import List


def min_number_of_coins_for_change(total: int, denoms: List[int]) -> int:

    coin_counts = [float("inf")] * (total + 1)
    coin_counts[0] = 0

    for denomination in denoms:
        for amount in range(len(coin_counts)):
            if denomination <= amount:
                coin_counts[amount] = min(
                    coin_counts[amount],
                    1 + coin_counts[amount - denomination],
                )
        pass

    if coin_counts[-1] == float("inf"):
        return -1
    return coin_counts[-1]
