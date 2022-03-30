def get_nth_fib(n: int):
    if n <= 0:
        # There is no 0th Fibonacci number.
        return None
    if n <= 2:
        # (0, 1) are the first Fibonacci numbers.
        return n - 1

    f = [0, 1]

    for _ in range(3, n + 1):
        # calculate the ith fibonacci number
        ith = f[0] + f[1]
        # shift the sliding window forward by 1
        f[0] = f[1]
        f[1] = ith

    return ith
