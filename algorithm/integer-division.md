## Integer Division

This is a great question to challenge a construct that many people have taken for granted: division. It will force the candidate to take a step back and break down what it actually means to divide a number by another. I will usually recommend resisting the temptation bitwise operations -- that approach tends to be complex and difficult to debug.

### Prompt

Write a function that does integer division without using the language's division operator (usually `/`).

Clarification: Integer division, also referred to as floor division, is division in which the remainder is discarded.

### Test cases

After the candidate is happy with their solution, have them try some of these inputs and compare the output. Often they will realize that they didn't account for negative numbers. That's great! Now you get to work with them through handling negatives.

| Input | Output |
|:-----:|:------:|
| `4`, `2` | `2` |
| `5`, `2` | `2` |
| `2`, `4` | `0` |
| `-4`, `2` | `-2` |
| `-4`, `-2` | `2` |
| `-5`, `2` | `-2`* |

*This answer isn't necessarily correct. Depending on the language, integer division may be implemented where the answer is rounded toward negative infinity (or floored) or rounded toward zero. In Python and Ruby, the answer is `-3`. In C, the answer is `-2`. We're accepting `-2` here because the point of this exercise is not to be tricky but to solve a problem together.

### Sample solution

```python
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
```

For a working version, see [integer-division.py](integer-division.py).
