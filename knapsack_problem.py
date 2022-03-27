import functools
from typing import List, Union


def knapsack_problem(
    items: List[List[int]],
    capacity: int,
) -> List[Union[int, List[int]]]:
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]

    def item_value(it: List[int]) -> int:
        return it[0]

    def item_weight(it: List[int]) -> int:
        return it[1]

    @functools.lru_cache(maxsize=None)
    def optimal_subset(i: int, w: int) -> List[Union[int, List[int]]]:
        """
        we'll get the optimal subset of items[:i]
        w is the weight capacity
        """
        it = items[i]
        it_weight = item_weight(it)

        if i < 0:
            return [0, []]
        elif w < it_weight:
            # we're out of capacity, so we must skip this item
            return optimal_subset(i - 1, w)
        else:
            subresult_with_it = optimal_subset(i - 1, w - it_weight)
            subresult_without_it = optimal_subset(i - 1, w)
            return max(
                [
                    subresult_with_it[0] + item_value(it),
                    subresult_with_it[1] + [i],
                ],
                subresult_without_it,
                # maximize for the total value
                key=lambda result: result[0],
            )
        pass

    return optimal_subset(len(items) - 1, capacity)
