from typing import List


def powerset(array: List[int]) -> List[List[int]]:

    def apply_mask(mask: List[bool]):
        return [
            array[i] for i in range(len(array)) if mask[i]
        ]

    def possible_masks(mask: List[bool], start: int):
        if len(mask) <= start:
            yield mask
        else:
            for val in (True, False):
                mask[start] = val
                for m in possible_masks(mask, start + 1):
                    yield m
        pass

    return [
        apply_mask(mask) for mask in possible_masks(
            [False for _ in range(len(array))],
            0
        )
    ]
