def binary_search(array, target):
    def floored_mean(a: int, b: int) -> int:
        return (a + b) // 2

    start = 0
    end = len(array) - 1

    while start <= end:
        med = floored_mean(start, end)
        if target < array[med]:
            end = med - 1
            continue
        elif array[med] < target:
            start = med + 1
            continue
        return med
    return -1
