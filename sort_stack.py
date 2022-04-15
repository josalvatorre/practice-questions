from typing import List, Optional


def sort_stack(stack: List[int]) -> List[int]:
    def push_if_not_min(x: int):
        nonlocal minimum, stack

        if x == minimum:
            minimum = None
        else:
            stack.append(x)
        pass

    def stack_insert(target_depth: int, actual_depth: int, current: int):
        nonlocal minimum

        if actual_depth == target_depth:
            stack.append(minimum)
            push_if_not_min(current)
            return

        top = stack.pop()
        minimum = min(minimum, top)
        stack_insert(target_depth, actual_depth + 1, top)

        push_if_not_min(current)
        pass

    for target_depth in reversed(range(1, len(stack))):
        top = stack.pop()
        minimum: Optional[int] = top
        stack_insert(target_depth, 0, top)
    return stack
