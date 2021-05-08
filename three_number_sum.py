from typing import List, Tuple, TypeVar, Callable, Optional
import operator

# Element type for binary search
T = TypeVar('T')


def binary_search(
    array: List[T], target: T,
    less_than: Callable[[T, T], bool] = operator.lt,
    start: int = 0, end: Optional[int] = None
) -> Optional[int]:
    def floored_median(a: int, b: int) -> int:
        return (a + b) // 2

    end = len(array) - 1 if end is None else end

    while start <= end:
        med = floored_median(start, end)
        if less_than(target, array[med]):
            end = med - 1
            continue
        elif less_than(array[med], target):
            start = med + 1
            continue
        return med
    return None


def three_number_sum(
        array: List[int], target_sum: int,
) -> List[Tuple[int, int, int]]:
    # array is ascending
    array.sort()
    triplets = []

    # i < j < k and array[i] < array[j] < array[k]
    # i starts at smallest, keeps increasing
    for i in range(0, len(array)-2):
        # k starts at biggest, keeps decreasing
        for k in range(len(array)-1, i, -1):
            # array[j] needs to equal remainder in order to
            # fulfill the triplet.
            remainder = target_sum - (array[i] + array[k])

            j = binary_search(
                array=array, target=remainder,
                start=i+1, end=k-1,
            )
            if j is None:
                continue

            triplets.append((array[i], array[j], array[k]))

    return triplets
