from typing import List


def min_number_of_jumps(array: List[int]) -> int:
    if len(array) == 1:
        return 0

    jumps = 0
    max_reach = array[0]
    steps = array[0]

    for i in range(1, len(array) - 1):
        max_reach = max(max_reach, i + array[i])
        steps -= 1
        if steps == 0:
            # We had to jump somewhere.
            jumps += 1
            steps = max_reach - i
        pass

    # +1 is the final jump to i = len(array)-1.
    return jumps + 1
