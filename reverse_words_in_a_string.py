def reverse_words(s: str) -> str:
    # split by whitespace.
    lst = s.split(' ')
    return ' '.join((x for x in reversed(lst) if x != ''))
