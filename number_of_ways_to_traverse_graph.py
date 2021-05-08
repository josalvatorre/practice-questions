def number_of_ways_to_traverse_graph(width: int, height: int) -> int:

    def ways(w: int, h: int) -> int:
        if w == h == 0:
            # count this as one valid path
            return 1
        elif w < 0 or h < 0:
            # do not count this invalid path
            return 0
        # we're not done
        return sum(ways(*pos) for pos in ((w - 1, h), (w, h - 1)))

    return ways(width - 1, height - 1)
