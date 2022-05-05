from typing import List


def shifted_binary_search(array: List[int], target: int) -> int:
    def go_right() -> None:
        nonlocal left_i
        left_i = mid_i + 1
        pass

    def go_left() -> None:
        nonlocal right_i
        right_i = mid_i - 1
        pass

    left_i = 0
    right_i = len(array) - 1

    while left_i <= right_i:

        mid_i = (left_i + right_i) // 2

        if array[mid_i] == target:
            return mid_i
        elif array[left_i] <= target < array[mid_i]:
            go_left()
        elif array[mid_i] < target <= array[right_i]:
            go_right()
        elif array[left_i] <= array[mid_i]:
            # Left side is sorted, so we already know that target isn't there.
            go_right()
        else:
            # Right side is sorted, so we already know that target isn't there.
            go_left()
        pass

    return -1
