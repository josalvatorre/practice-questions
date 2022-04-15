from typing import List


def sort_stack(stack: List[int]) -> List[int]:
    def insert(stack: List[int], element: int) -> None:
        if len(stack) == 0 or stack[-1] <= element:
            stack.append(element)
            return

        top = stack.pop()
        insert(stack, element)
        stack.append(top)
        pass

    if len(stack) == 0:
        return stack

    top = stack.pop()
    sort_stack(stack)
    insert(stack, top)
    return stack
