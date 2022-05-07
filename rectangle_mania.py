from typing import Dict, List, Set


def rectangle_mania(coords: List[List[int]]) -> int:
    def point_exists(x: int, y: int) -> bool:
        ys = xy_tree.get(x)
        if ys is None:
            return False
        return y in ys

    xy_tree: Dict[int, Set[int]] = {}

    for x, y in coords:
        ys = xy_tree.get(x)
        if ys is None:
            ys = set()
            xy_tree[x] = ys
        ys.add(y)
        pass

    rect_count = 0

    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            # Ensure that coords[i] has smaller x than coords[j].
            a, b = (i, j) if coords[i][0] <= coords[j][0] else (j, i)

            x_1, y_1 = coords[a]
            x_2, y_2 = coords[b]

            # We need bottom-left and top-right coordinates.
            if x_2 <= x_1 or y_2 <= y_1:
                continue

            if point_exists(x_1, y_2) and point_exists(x_2, y_1):
                rect_count += 1
        pass

    return rect_count
