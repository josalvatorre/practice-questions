def is_palindrome(string: str) -> bool:
    end = len(string) - 1
    # We don't need to check the middle element
    # if length is odd.
    for start in range(len(string) // 2):
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True
