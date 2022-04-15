def balanced_brackets(string: str) -> bool:
    open_to_close = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    close_to_open = {close: open_ for open_, close in open_to_close.items()}

    brackets_stack = []

    for c in string:
        close = open_to_close.get(c)
        if close is not None:
            # then c is open
            brackets_stack.append(c)
            continue

        open_ = close_to_open.get(c)
        if open_ is None:
            # then c is a garbage character
            continue
        # else c is a close character

        if len(brackets_stack) == 0 or brackets_stack[-1] != open_:
            return False
        brackets_stack.pop()

    return len(brackets_stack) == 0
