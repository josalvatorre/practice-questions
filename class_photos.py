from typing import List


def class_photos(
    red_heights: List[int],
    blue_heights: List[int],
) -> bool:

    red_heights.sort()
    blue_heights.sort()

    shorter_heights, taller_heights = (
        (red_heights, blue_heights)
        if red_heights[0] < blue_heights[0]
        else (blue_heights, red_heights)
    )

    return all(
        shorter < taller
        for shorter, taller in zip(shorter_heights, taller_heights)
    )
