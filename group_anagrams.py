from collections import defaultdict
from typing import DefaultDict, List


def group_anagrams(words: List[str]) -> List[List[int]]:
    if len(words) == 0:
        return []

    groups_by_sorted_words: DefaultDict[str, List[str]] = defaultdict(
        lambda: []
    )

    for word in words:
        sorted_word = "".join(sorted(word))
        groups_by_sorted_words[sorted_word].append(word)

    return list(groups_by_sorted_words.values())
