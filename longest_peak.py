from typing import List, Tuple


def longest_peak(array: List[int]) -> int:
    def peak_len(a: Tuple[int, int, int]) -> int:
        return a[2] - a[0] + 1

    def longer_peak(
        a: Tuple[int, int, int],
        b: Tuple[int, int, int],
    ) -> Tuple[int, int, int]:
        return max((a, b), key=peak_len)

    # init to peak_len == -1
    longest_peak_null = (-1, None, -2)
    longest_peak = longest_peak_null

    left_i = 0
    tip_i = None

    for i in range(1, len(array)):
        # uphill or flat
        if array[i - 1] <= array[i]:
            # There is a right if
            # we already recorded a tip and it wasn't the previous element.
            right_exists = tip_i is not None and tip_i < i - 1

            # If right_exists, then we just broke from downhill, so record this peak
            if right_exists:
                longest_peak = longer_peak(
                    longest_peak,
                    (left_i, tip_i, i - 1),
                )

            # if flat, start a new peak
            if array[i - 1] == array[i]:
                left_i = i  # this is the min
                tip_i = None
            elif right_exists:
                left_i = i - 1  # min was previous element
                tip_i = None
        # downhill
        else:
            if tip_i is None:
                # if we just started the peak, let's just restart the peak
                if left_i == i - 1:
                    left_i = i
                # set the tip to the previous element
                else:
                    tip_i = i - 1
        # else, keep going downhill
    # collect last peak
    if tip_i is not None and tip_i < (last_i := len(array) - 1):
        longest_peak = longer_peak(
            longest_peak,
            (left_i, tip_i, last_i),
        )

    return 0 if longest_peak == longest_peak_null else peak_len(longest_peak)
