from functools import reduce
from typing import List


def tandem_bicycle(
    red_speeds: List[int],
    blue_speeds: List[int],
    fastest: bool,
) -> int:

    red_speeds.sort()
    blue_speeds.sort()

    if fastest:
        speeds = zip(red_speeds, reversed(blue_speeds))
    else:
        speeds = zip(red_speeds, blue_speeds)
        pass

    return reduce(
        lambda acc, pair: acc + max(pair),
        speeds,
        0,
    )
