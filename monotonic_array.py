from typing import List, Optional, Callable
import itertools
import operator


def is_monotonic(array: List[int]) -> bool:
    if len(array) <= 1:
        return True

    # 2-element sliding window of previous and current values
    prevs_currs = zip(
        itertools.islice(array, len(array)-1),
        itertools.islice(array, 1, len(array)),
    )

    # will either be < or >
    still_mono: Optional[Callable[[int, int], bool]] = None

    # find out whether to use < or >
    for prev, curr in prevs_currs:
        if prev == curr:
            continue

        still_mono = operator.le if prev < curr else operator.ge
        if not still_mono(prev, curr):
            return False
        break

    return all(still_mono(*pc) for pc in prevs_currs)
