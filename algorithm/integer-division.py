#!/usr/bin/env python3

def divide(numerator: int, denominator: int) -> int:
    # The answer will be negative if the numerator xor denominator is negative.
    negative = (numerator < 0) ^ (denominator < 0)

    numerator = abs(numerator)
    denominator = abs(denominator)

    quotient = 0
    while numerator >= denominator:
        numerator -= denominator
        quotient += 1

    if negative:
        quotient *= -1

    return quotient

if __name__ == "__main__":
    print("Running assertions...")
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2
    assert divide(2, 4) == 0
    assert divide(-4, 2) == -2
    assert divide(-4, -2) == 2
    assert divide(-5, 2) == -2
    print("All good!")
