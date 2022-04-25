from collections import defaultdict
from typing import DefaultDict


def character_frequencies(chars: str) -> DefaultDict[str, int]:
    freqs = defaultdict(lambda: 0)
    for c in chars:
        freqs[c] += 1
    return freqs


def generate_document(characters: str, document: str) -> bool:
    char_freqs = character_frequencies(characters)
    for doc_char, doc_freq in character_frequencies(document).items():
        if char_freqs[doc_char] < doc_freq:
            return False
    return True
