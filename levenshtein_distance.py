import functools
from typing import Optional


def levenshtein_distance(str1: str, str2: str) -> int:
    @functools.lru_cache(maxsize=None)
    def search(start_1: int, start_2: int) -> Optional[int]:

        if len(str1) < start_1 or len(str2) < start_2:
            return None
        if len(str1) == start_1 and len(str2) == start_2:
            return 0
        elif (
            start_1 < len(str1)
            and start_2 < len(str2)
            and str1[start_1] == str2[start_2]
        ):
            return search(start_1 + 1, start_2 + 1)
        else:
            return min(
                (
                    search_result + 1
                    for s_1, s_2 in (
                        # substitute: we take the str2 character and move on
                        (start_1 + 1, start_2 + 1),
                        # delete: we skip the str1 character
                        (start_1 + 1, start_2),
                        # insert: we take the str2 character
                        (start_1, start_2 + 1),
                    )
                    if (search_result := search(s_1, s_2)) is not None
                )
            )

    return search(0, 0)
