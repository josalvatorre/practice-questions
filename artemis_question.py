from collections import defaultdict
from typing import DefaultDict, List, Set, Tuple


def connect_neighbors(neighbors_list: List[Tuple[int]]) -> List[int]:
    if len(neighbors_list) == 0:
        return []

    neighbors_dict: DefaultDict[int, Set[int]] = defaultdict(lambda: set())
    for x, y in neighbors_list:
        neighbors_dict[x].add(y)
        neighbors_dict[y].add(x)

    first = next(
        element
        for element, neighbors in neighbors_dict.items()
        if len(neighbors) == 1
    )
    connected = [first]

    while True:
        current = connected[-1]
        neighbors = neighbors_dict[current]

        # discard already-seen left neighbor
        if len(connected) >= 2:
            neighbors.discard(connected[-2])

        if len(neighbors) == 0:
            break
        else:
            connected.append(neighbors.pop())
        pass

    return connected


if __name__ == '__main__':
    for input_ in (
        [(1, 2), (2, 3), (3, 4)],
        [(4, 1), (3, 1), (2, 4)],
        [(5, 2), (4, 1), (1, 2)],
    ):
        print(connect_neighbors(input_))
        pass
