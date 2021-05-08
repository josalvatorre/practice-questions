import itertools
from typing import List


def number_of_ways_to_make_change(target: int, denoms: List[int]) -> int:
    # sort descending
    denoms.sort(reverse=True)

    def combos(target_: int, d: int) -> int:
        if target_ == 0:
            return 1
        elif len(denoms) <= d:
            return 0

        den = denoms[d]
        return sum(
            combos(target_ - diff, d + 1)
            for diff in itertools.takewhile(
                lambda total: total <= target_,
                (den * t for t in itertools.count(start=0, step=1)),
            )
        )

    return combos(target, 0)
