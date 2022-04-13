from typing import Iterable, List, Sequence, Tuple, TypeVar

T = TypeVar("T")


def reversed_enumerate(array: Sequence[T]) -> Iterable[Tuple[int, T]]:
    for i in reversed(range(0, len(array))):
        n = array[i]
        yield i, n
    pass


def next_greater_element(array: List[int]) -> List[int]:
    """
    0 [5, 0]       5
    4 [5, 4]       5
    1 [5, 4, 1]    4
    2 [5, 4, 2]    4
    0 [5, 4, 2, 0] 2
    3 [5, 4, 3]    4
    6 [6]          _
    --wrap--
    5 [6, 5]       6

    5 [5]          _
    0 [5, 0]       5
    4 [5, 4]       5
    1 [5, 4, 1]    4
    6 [6]          _
    2 [6]          6
    0 [6]          6
    3 [6]          6
    6 [6]          _
    --wrap--
    5 [6, 5]       6
    """

    greaters = [None] * len(array)
    greater_stack = []

    def record_greater(index: int, number: int):
        while 0 < len(greater_stack) and greater_stack[-1] <= number:
            greater_stack.pop()

        if len(greater_stack) > 0:
            greaters[index] = greater_stack[-1]

        greater_stack.append(number)
        pass

    for i, n in reversed_enumerate(array):
        record_greater(i, n)

    for i, n in reversed_enumerate(array):
        if greaters[i] is not None:
            continue
        record_greater(i, n)
        if greaters[i] is None:
            greaters[i] = -1

    return greaters
