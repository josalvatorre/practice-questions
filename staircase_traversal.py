def staircase_traversal(height: int, max_steps: int) -> int:
    current_ways = 0
    prev_ways = [1]

    window_start_init = 1 - max_steps
    for window_start in range(window_start_init, window_start_init + height):
        tail = 0 if window_start < 1 else prev_ways[window_start - 1]
        current_ways += prev_ways[-1] - tail
        prev_ways.append(current_ways)
        pass

    return prev_ways[-1]
