from typing import List


def merge_sort(array: List[int]) -> List[int]:
    def merge(sorted_1, sorted_2) -> List[int]:
        # merged should have enough room for both lists
        merged = [None] * (len(sorted_1) + len(sorted_2))
        # indices
        i = 0  # sorted_1
        j = 0  # sorted_2
        m = 0  # merged
        r = 0  # remaining_list
        remaining_list = None

        while True:
            if len(sorted_1) <= i:
                remaining_list = sorted_2
                r = j
                break
            elif len(sorted_2) <= j:
                remaining_list = sorted_1
                r = i
                break

            if sorted_2[j] <= sorted_1[i]:
                merged[m] = sorted_2[j]
                j += 1
            else:
                merged[m] = sorted_1[i]
                i += 1
            m += 1
            pass

        if remaining_list is not None:
            while m < len(merged):
                merged[m] = remaining_list[r]
                m += 1
                r += 1

        return merged

    def sort(lst: List[int]) -> List[int]:
        if len(lst) <= 1:
            return lst

        middle = len(lst) // 2

        return merge(
            sort(lst[:middle]),
            sort(lst[middle:]),
        )

    return sort(array)
