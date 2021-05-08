from typing import List


def reverse_words_in_string(string: str) -> str:
    result_chunks: List[str] = []
    # index of the rightmost character in the chunk.
    # start at the rightmost element.
    chunk_right: int = len(string) - 1
    # start at the second-to-last character.
    for i in range(len(string) - 2, -1, -1):
        if string[i].isspace() != string[i + 1].isspace():
            # record this chunk
            result_chunks.append(
                string[i + 1: chunk_right + 1]
            )
            # cut a new chunk
            chunk_right = i
        pass

    if 0 <= chunk_right:
        result_chunks.append(string[:chunk_right + 1])

    return ''.join(result_chunks)
