import copy
from typing import List


def merge_sort(array: List[int]) -> List[int]:

    def merge(
        range_a: range, range_b: range,
        array_in: List[int], array_out: List[int],
    ) -> None:
        # indices tracking
        # range_a, range_b, array_out, and remaining_range
        a = range_a.start
        b = range_b.start
        # range of
        # Note: we're assuming that range_a and range_b
        # are back-to-back
        o = range_a.start
        #
        remaining_range = None
        while True:
            if range_b.stop <= b:
                remaining_range = range(a, range_a.stop)
                break
            elif range_a.stop <= a:
                remaining_range = range(b, range_b.stop)
                break

            if array_in[a] <= array_in[b]:
                array_out[o] = array_in[a]
                a += 1
            else:
                array_out[o] = array_in[b]
                b += 1
            o += 1

        if remaining_range is not None:
            for r in remaining_range:
                array_out[o] = array_in[r]
                o += 1
        pass

    array_prime = copy.deepcopy(array)

    def sort(range_: range, out_to_prime: bool) -> None:
        if len(range_) <= 1:
            return

        middle = (range_.start + range_.stop) // 2
        left = range(range_.start, middle)
        right = range(middle, range_.stop)

        # To conserve memory, we'll alternate
        # between input and output arrays
        if out_to_prime:
            array_in = array
            array_out = array_prime
        else:
            array_in = array_prime
            array_out = array

        for side in (left, right):
            sort(side, not out_to_prime)

        merge(left, right, array_in, array_out)
        pass

    sort(range(len(array)), out_to_prime=False)
    return array
