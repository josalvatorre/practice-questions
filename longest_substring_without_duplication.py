from typing import Dict, Optional, Tuple


def longest_substring_without_duplication(string: str) -> str:
    def bigger_interval(
        current: Optional[Tuple[int, int]],
        new: Tuple[int, int],
    ) -> Tuple[int, int]:
        if current is None:
            return new
        else:
            return max(
                current,
                new,
                key=lambda interval: interval[1] - interval[0],
            )

    last_seen: Dict[str, int] = {}

    start_index = 0
    max_interval: Optional[Tuple[int, int]] = None

    for i, char in enumerate(string):
        last_index = last_seen.get(char)
        if last_index is not None and start_index <= last_index:
            max_interval = bigger_interval(
                max_interval,
                (start_index, i),
            )
            # start after the repeating character so that
            # we only have one instance of char in our string
            start_index = last_index + 1
        last_seen[char] = i

    max_interval = bigger_interval(
        max_interval,
        (start_index, len(string)),
    )
    return string[max_interval[0] : max_interval[1]]
