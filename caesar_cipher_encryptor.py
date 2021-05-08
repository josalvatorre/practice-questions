def caesar_cipher_encryptor(lowercase: str, key: int) -> str:
    alphabet_length = len('abcdefghijklmnopqrstuvwxyz')
    # 'a' marks the beginning of the alphabet.
    a_int: int = ord('a')

    # join the ints converted back into characters (using chr)
    return ''.join(map(chr, map(
        # shift and wrap
        lambda letter_int: (letter_int + key - a_int) % alphabet_length + a_int,
        # convert into sequence of ints (character values)
        map(ord, lowercase)
    )))
