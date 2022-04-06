def longest_palindromic_substring(string: str) -> str:

    longest = None

    for i in range(0, len(string)):
        for sep in range(0, 2):

            start = i
            end = i + sep

            while (
                0 <= start
                and end < len(string)
                and string[start] == string[end]
            ):
                start -= 1
                end += 1

            start += 1
            end -= 1

            pal = string[start : end + 1]

            longest = (
                pal
                if longest is None
                else max(
                    longest,
                    pal,
                    key=len,
                )
            )

    return longest
