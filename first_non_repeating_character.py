from collections import defaultdict
from typing import DefaultDict, Dict


def first_non_repeating_character(string: str) -> int:

    occurances: DefaultDict[str, int] = defaultdict(lambda: 0)
    first_indices: Dict[str, int] = {}

    for i, c in enumerate(string):
        occurances[c] += 1
        if c not in first_indices:
            first_indices[c] = i

    return min(
        (first_indices[c] for c, count in occurances.items() if count == 1),
        default=-1,
    )
