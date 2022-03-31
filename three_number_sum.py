from typing import List, Tuple


def three_number_sum(
    array: List[int],
    target_sum: int,
) -> List[Tuple[int, int, int]]:

    array.sort()
    triplets = []

    for a_index in range(0, len(array) - 2):
        a = array[a_index]

        if 1 <= a_index and a == array[a_index - 1]:
            # we already saw this value
            continue

        def next_unique_b_index(current_b_index: int, current_c_index: int):
            current_b_index += 1
            while True:
                if current_c_index <= current_b_index:
                    return None
                if array[current_b_index] != array[current_b_index - 1]:
                    return current_b_index
                current_b_index += 1

        def next_unique_c_index(current_b_index: int, current_c_index: int):
            current_c_index -= 1
            while True:
                if current_c_index <= current_b_index:
                    return None
                if array[current_c_index] != array[current_c_index + 1]:
                    return current_c_index
                current_c_index -= 1

        b_index = a_index + 1
        c_index = len(array) - 1
        while (
            b_index is not None and c_index is not None and b_index < c_index
        ):
            b = array[b_index]
            c = array[c_index]

            current_sum = a + b + c

            if current_sum < target_sum:
                # too small, go bigger
                b_index = next_unique_b_index(b_index, c_index)
            elif target_sum < current_sum:
                # too big, go smaller
                c_index = next_unique_c_index(b_index, c_index)
            else:
                triplets.append([a, b, c])
                b_index = next_unique_b_index(b_index, c_index)
                if b_index is None:
                    break
                c_index = next_unique_c_index(b_index, c_index)

    return triplets
