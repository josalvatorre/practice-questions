from typing import List


def cycle_in_graph(edges: List[List[int]]) -> bool:
    v_count = len(edges)

    ever_visited = [False] * v_count
    in_search_path = [False] * v_count

    def in_cycle(v_start: int) -> bool:
        ever_visited[v_start] = in_search_path[v_start] = True

        for v_dest in edges[v_start]:
            # we haven't visited v_dest
            if not ever_visited[v_dest]:
                if in_cycle(v_dest):
                    return True
            # there's a path from v_dest to v_dest
            elif in_search_path[v_dest]:
                return True
            # else we already visited v_dest and found no cycle

        in_search_path[v_start] = False
        return False

    return any(
        in_cycle(v) for v in range(len(edges))
        if not ever_visited[v]
    )
