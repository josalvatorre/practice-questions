from typing import List


def valid_starting_city(
    distances: List[int], fuel: List[int], mpg: int
) -> int:
    miles_rem = 0

    start_cand = 0
    start_cand_miles_rem = 0

    for i in range(1, len(distances)):

        dist_from_prev = distances[i - 1]
        fuel_from_prev = fuel[i - 1]

        miles_rem += (fuel_from_prev * mpg) - dist_from_prev

        if miles_rem < start_cand_miles_rem:
            start_cand_miles_rem = miles_rem
            start_cand = i

    return start_cand
