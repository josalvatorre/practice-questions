from typing import List


def run_length_encoding(string: str) -> str:
    max_chunk_len = 9
    run_len_encoding_chunks: List[str] = []

    def add_chunk(chunks: List[str], chunk_length: int, char: str) -> None:
        chunks.append(f"{chunk_length}{char}")
        pass

    chunk_start = 0
    # We use a 2-element sliding window, so process all but the last char.
    for i in range(len(string) - 1):
        # cut new chunk if the next char is different than this char
        # or if we've exceeded the maximum chunk length.
        chunk_len = i + 1 - chunk_start
        if string[i] != string[i + 1] or chunk_len >= max_chunk_len:
            # record this chunk
            add_chunk(run_len_encoding_chunks, chunk_len, string[i])
            # cut new chunk
            chunk_start = i + 1
            pass
        pass
    # There will be one more chunk.
    chunk_len = len(string) - chunk_start
    if chunk_len > 0:
        add_chunk(run_len_encoding_chunks, chunk_len, string[-1])

    return "".join(run_len_encoding_chunks)
