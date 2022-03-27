from typing import List, Set


def cycle_in_graph(edges: List[List[int]]) -> bool:
    """
    ith element (a list) in @edges represents outbound edges for vertex i.

    Each list has indices of destination vertices for edges starting
    from vertex i.
    """

    def in_a_cycle(v_start: int, dests: Set[int]) -> bool:
        """
        init dests to empty set on the first call
        """
        if v_start in dests:
            return True
        else:
            return any(
                in_a_cycle(v_end, dests | {v_start})
                for v_end in edges[v_start]
            )

    return any(in_a_cycle(v_start, set()) for v_start in range(len(edges)))
