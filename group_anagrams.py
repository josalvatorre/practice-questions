from itertools import islice, zip_longest
from typing import List, Tuple


def group_anagrams(words: List[str]) -> List[List[int]]:
    if len(words) == 0:
        return []

    sorted_words: List[Tuple[str, int]] = sorted(
        ("".join(sorted(word)), i) for i, word in enumerate(words)
    )

    groups: List[List[str]] = [[]]

    for sw_info_1, sw_info_2 in zip_longest(
        islice(sorted_words, 0, len(sorted_words)),
        islice(sorted_words, 1, len(sorted_words)),
    ):
        group_1 = groups[-1]

        if sw_info_2 is not None and sw_info_1[0] != sw_info_2[0]:
            groups.append([])

        group_1.append(words[sw_info_1[1]])
        pass

    return groups
