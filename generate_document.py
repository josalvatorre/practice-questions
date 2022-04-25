from collections import defaultdict
from typing import DefaultDict


def character_frequencies(chars: str) -> DefaultDict[str, int]:
    freqs = defaultdict(lambda: 0)
    for c in chars:
        freqs[c] += 1
    return freqs


def generate_document(characters: str, document: str) -> bool:
    char_freqs = character_frequencies(characters)

    for doc_char in document:
        char_freq = char_freqs[doc_char]
        if char_freq == 0:
            return False
        char_freqs[doc_char] -= 1
    return True
