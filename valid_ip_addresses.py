from typing import Generator, List, Tuple


def valid_ip_addresses(
    string: str,
    start: int,
    chunks_remaining: int,
    dot_insert_indices: Tuple[int, ...],
) -> Generator[str, None, None]:
    def is_valid_chunk(start: int, end: int):
        chunk = string[start:end]
        chunk_val = int(chunk)
        return (
            len(chunk) <= 3
            and chunk_val <= 255
            and len(chunk) == len(str(chunk_val))
        )

    if chunks_remaining <= 1:
        if not is_valid_chunk(start, len(string)):
            return

        result = []
        insert_indices = iter(dot_insert_indices)
        insert_index = next(insert_indices)

        for i, c in enumerate(string):
            if i == insert_index:
                result.append(".")
                insert_index = next(insert_indices, None)
            result.append(c)
        yield "".join(result)
        return

    max_digit_count = min(3, (len(string) - 1) - start)
    for digit_count in range(1, max_digit_count + 1):
        new_start = start + digit_count

        if not is_valid_chunk(start, new_start):
            break

        yield from valid_ip_addresses(
            string,
            new_start,
            chunks_remaining - 1,
            dot_insert_indices + (new_start,),
        )
    pass


def valid_ip_addresses_list(string: str) -> List[int]:
    return list(valid_ip_addresses(string, 0, 4, ()))
