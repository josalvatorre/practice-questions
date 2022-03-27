from typing import Generator, List, NamedTuple


def smallest_difference(array_1: List[int], array_2: List[int]) -> List[int]:
    """
    Return the pair of ints with the smallest absolute difference
    """

    def abs_diff(a: int, b: int) -> int:
        return abs(a - b)

    class DiffNumNum(NamedTuple):
        a: int
        b: int

        def diff(self) -> int:
            return abs_diff(self.a, self.b)

    array_1.sort()
    array_2.sort()

    def diffs() -> Generator[DiffNumNum, None, None]:
        """
        generator will give diffs of neighboring values.
        """
        i = j = 0
        last_i = len(array_1) - 1
        last_j = len(array_2) - 1

        while True:
            yield DiffNumNum(a=array_1[i], b=array_2[j])

            if i == last_i and j == last_j:
                return
            elif i == last_i:
                j += 1
            elif j == last_j:
                i += 1
            else:
                next_j_diff = abs_diff(array_1[i], array_2[j + 1])
                next_i_diff = abs_diff(array_1[i + 1], array_2[j])

                if next_j_diff <= next_i_diff:
                    j += 1
                else:
                    i += 1

    min_diff = min(diffs(), key=lambda d: d.diff())
    return [min_diff.a, min_diff.b]
