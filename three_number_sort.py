from typing import List


def three_number_sort(array: List[int], order: List[int]) -> List[int]:
    def swap(i: int, j: int) -> None:
        array[i], array[j] = array[j], array[i]
        pass

    non_match_index = 0

    for o in order:
        while True:
            while non_match_index < len(array) and array[non_match_index] == o:
                non_match_index += 1

            if len(array) <= non_match_index:
                break

            swapped = False
            for i in range(non_match_index + 1, len(array)):
                x = array[i]
                if x == o:
                    swap(i, non_match_index)
                    non_match_index += 1
                    swapped = True
                    break

            if not swapped:
                break
            pass
        pass
    return array
