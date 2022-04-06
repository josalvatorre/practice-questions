from itertools import islice, zip_longest
from typing import List, NamedTuple, Tuple


def group_anagrams(words: List[str]) -> List[List[int]]:
    if len(words) == 0:
        return []

    class SortedWordInfo(NamedTuple):
        sorted_word: str
        index: int

    sorted_words: List[Tuple[str, int]] = sorted(
        SortedWordInfo(
            sorted_word="".join(sorted(word)),
            index=i,
        )
        for i, word in enumerate(words)
    )

    groups: List[List[str]] = [[]]

    for sw_info_1, sw_info_2 in zip_longest(
        islice(sorted_words, 0, len(sorted_words)),
        islice(sorted_words, 1, len(sorted_words)),
    ):
        group_1 = groups[-1]

        if (
            sw_info_2 is not None
            and sw_info_1.sorted_word != sw_info_2.sorted_word
        ):
            groups.append([])

        group_1.append(words[sw_info_1.index])
        pass

    return groups
