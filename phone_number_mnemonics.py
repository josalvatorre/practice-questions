from typing import Generator, List, Optional


def phone_number_mnemonics(phone_number: str) -> List[str]:

    number_choices = [
        "0",
        "1",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz",
    ]

    selections: List[Optional[str]] = [None] * len(phone_number)

    def mnemonics(start: int) -> Generator[str, None, None]:
        if start == len(phone_number):
            yield "".join(selections)
            return

        number = int(phone_number[start])

        for choice in number_choices[number]:
            selections[start] = choice
            yield from mnemonics(start + 1)
        return

    return list(mnemonics(0))
