from typing import Generator, List


def valid_ip_addresses(
    string: str,
    start: int,
    chunks_remaining: int,
    dot_insert_indices: List[int],
) -> Generator[str, None, None]:
    if chunks_remaining <= 1:
        last_chunk = string[start:]
        last_chunk_int = int(last_chunk)
        if (
            len(last_chunk) > 3
            or 255 < last_chunk_int
            or (len(str(last_chunk_int)) != len(last_chunk))
        ):
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
        chunk = string[start:new_start]
        number = int(chunk)
        if 255 < number or (len(str(number)) != len(chunk)):
            break
        yield from valid_ip_addresses(
            string,
            new_start,
            chunks_remaining - 1,
            dot_insert_indices + [new_start],
        )
    pass


def valid_ip_addresses_list(string: str) -> List[int]:
    return list(valid_ip_addresses(string, 0, 4, []))
