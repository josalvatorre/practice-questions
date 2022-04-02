from itertools import chain
from typing import Dict, List


def minimum_characters_for_words(words: List[str]):

    char_frequencies: Dict[str, int] = {}

    for word in words:

        word_char_frequencies: Dict[str, int] = {}

        for char in word:
            word_char_frequencies[char] = (
                word_char_frequencies.get(char, 0) + 1
            )

        for char, freq in word_char_frequencies.items():
            char_frequencies[char] = max(
                freq,
                char_frequencies.get(char, 0),
            )
        pass

    return list(
        chain.from_iterable(c * f for c, f in char_frequencies.items())
    )
