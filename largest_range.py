from dataclasses import dataclass
from typing import List, Optional, Set


@dataclass
class Interval:
    first: int
    last: int

    def length(self: "Interval") -> int:
        return self.last - self.first + 1

    def to_list(self: "Interval") -> List[int]:
        return [self.first, self.last]

    pass


def largest_range(array: List[int]) -> Optional[List[int]]:
    if len(array) == 0:
        return None

    numbers: Set[int] = set(array)
    not_seen: Set[int] = set(array)

    max_interval = Interval(array[0], array[0])

    while len(not_seen) > 0:
        b = not_seen.pop()
        count = 1

        a = b - 1
        while a in numbers:
            count += 1
            a -= 1
            pass

        c = b + 1
        while c in numbers:
            count += 1
            c += 1
            pass

        max_interval = max(
            max_interval,
            Interval(a + 1, c - 1),
            key=lambda inter: inter.length(),
        )
        pass

    return max_interval.to_list()
