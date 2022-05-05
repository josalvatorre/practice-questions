from typing import Generator, List


def powerset(array: List[int]) -> List[List[int]]:
    def apply_mask(mask: List[bool]) -> List[int]:
        return [array[i] for i in range(len(array)) if mask[i]]

    def possible_masks(
        mask: List[bool], start: int
    ) -> Generator[List[bool], None, None]:
        if len(mask) <= start:
            yield mask
            return

        for val in (True, False):
            mask[start] = val
            yield from possible_masks(mask, start + 1)
        pass

    return list(
        map(
            apply_mask,
            possible_masks(
                [False] * len(array),
                0,
            ),
        )
    )
