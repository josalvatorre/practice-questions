INT32_MAX = (1 << 31) - 1
INT32_MIN = -(1 << 31)


def divide(dividend: int, divisor: int) -> int:
    # Trivial base case.
    if dividend == 0:
        return 0

    # Normalize numbers to positive. Negate quotient at the end.

    dividend_neg = dividend < 0
    divisor_neg = divisor < 0
    neg_q = dividend_neg != divisor_neg

    if dividend_neg:
        dividend = -dividend
    if divisor_neg:
        divisor = -divisor

    # Trivial base case.
    if dividend < divisor:
        return 0

    """
    The naive solution is to keep adding divisor to 0 until we get to dividend.
    That is inefficient. The dividend could be huge compared to the divisor.
    Let's use bit-shifting instead.
    """

    q = 1  # Quotient.
    qd = divisor  # qd always equals q*divisor.

    # Get as close as possible to the dividend using <<1.
    while qd << 1 <= dividend:
        # Double both.
        q <<= 1
        qd <<= 1

    # Do the same for the remainder.
    q += divide(dividend - qd, divisor)

    if neg_q:
        q = -q

    # check overflow
    if q > INT32_MAX:
        return INT32_MAX
    if q < INT32_MIN:
        return INT32_MIN

    return q
