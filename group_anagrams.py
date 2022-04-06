from typing import Dict, List


def group_anagrams(words: List[str]) -> List[List[int]]:
    if len(words) == 0:
        return []

    groups_by_sorted_words: Dict[str, List[str]] = {}

    for word in words:
        sorted_word = "".join(sorted(word))

        group = groups_by_sorted_words.get(sorted_word)
        if group is None:
            groups_by_sorted_words[sorted_word] = [word]
        else:
            group.append(word)

    return list(groups_by_sorted_words.values())
