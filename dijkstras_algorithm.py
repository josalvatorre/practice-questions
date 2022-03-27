from typing import List, Set


def dijkstras_algorithm(start: int, edges) -> List[int]:
    """
    len(edges) == number of vertices
    edges[i] == [outbound edges for vertex i]
    outbound edge: [destination vertex index, distance]
    distance is positive

    return list of shortest distances from start to other vertices
    """
    # distances[i] == shortest distance to vertex i from start
    distances = [float("inf") for _ in range(len(edges))]
    # distance from start->start is 0
    distances[start] = 0
    # set of explored vertices
    explored: Set[int] = set()
    # while we haven't explored all edges
    while len(explored) < len(edges):
        # the unexplored vertex with minimal distance from start
        current_min = min(
            (i for i in range(len(distances)) if i not in explored),
            key=distances.__getitem__,
        )
        explored.add(current_min)

        for edge in edges[current_min]:
            dst = edge[0]
            if dst in explored:
                continue
            distances[dst] = min(
                distances[current_min] + edge[1],
                distances[dst],
            )
    return list(map(lambda x: -1 if x == float("inf") else x, distances))
