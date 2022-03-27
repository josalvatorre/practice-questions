from typing import List


def generate_parenthesis(n: int) -> List[str]:
    if n <= 0:
        return []

    # length of a combination should be n*2.
    comb_len = n << 1

    combs: List[str] = []

    def backtrace(stack_size: int, parens: List[str]) -> None:
        # Base case.
        if len(parens) == comb_len:
            combs.append("".join(parens))
            return

        # How many parentheses remain?
        remaining = comb_len - len(parens)

        # Base case.
        if stack_size == remaining:
            parens.extend((")" for _ in range(0, remaining)))
            combs.append("".join(parens))
            return

        if stack_size == 0:
            # We cannot close, only open.
            parens.append("(")
            backtrace(stack_size + 1, parens)
        else:
            # We can open or close.
            parens_copy = parens.copy()

            parens.append("(")
            backtrace(stack_size + 1, parens)

            parens_copy.append(")")
            backtrace(stack_size - 1, parens_copy)
        pass

    backtrace(0, [])
    return combs
