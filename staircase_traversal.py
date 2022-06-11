def staircase_traversal(height: int, max_steps: int) -> int:
    current_ways = 0
    # Tracks number of ways to get to the ith step.
    # Note: there is 1 way to get to the 0th step: do nothing.
    prev_ways = [1]

    # Number of steps to get to step i = sum(prev_ways[i-max_steps, i-1])
    # To avoid repeatedly calculating that rolling window sum, we simply
    # subtract the "tail" element: the first element to leave the rolling
    # window.
    window_start_init = 1 - max_steps
    for window_start in range(window_start_init, window_start_init + height):
        tail = 0 if window_start < 1 else prev_ways[window_start - 1]
        current_ways += prev_ways[-1] - tail
        prev_ways.append(current_ways)
        pass

    return prev_ways[-1]
