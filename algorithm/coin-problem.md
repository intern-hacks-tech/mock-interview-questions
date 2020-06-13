### Coin Problem
​
Imagine you have a collection of coins which are all identical except for one
counterfit coin which is slightly lighter than the rest.  You have access to a balance 
scale which can be used to weigh the coins, but nothing else.
​
Write a function that takes a non-empty list of coins and a scale as arguments, and returns
the fake coin.  The scale has a `weigh` method that takes two lists of coins (elements of `coins`)
and returns one of three strings:
​
- `"left"` if the left side is heavier
- `"right"` if the right side is heavier
- `"equal"` if both sides are of equivalent weight
​
​
A naive solution might look like this:

```python
def findFakeCoin(coins, scale):
  for coin in coins[1:]:
    weighResult = scale.weigh([coins[0]], [coin])
    if weighResult == "left":
      return coin
​
    elif weighResult == "right":
      return coins[0]
​
  # in this case, we ~should~ only have one coin
  return coins[0]
```
​
Pretend `scale.weigh()` is expensive to compute (maybe it operates an actual robot to do the weighing.)
How can we minimize the number of times `scale.weigh()` is called?
