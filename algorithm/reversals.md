## Reversals

A straightforward question that shows how comfortable someone is with string manipulation and array/list operations. Part 3 can be a fun view into critical thinking skills. This question takes a varying amount of time depending on language features and the candidate's familiarity thereof. Some more keen candidates may be able to complete it in a couple of minutes. It's less interesting that way though.


### Part 1

**Prompt**: Write a function to reverse the letters in a word. For example, the input `InternHacks` should output `skcaHnretnI`.

Things to note:
- What assumptions are made about the input?
- Do they recognize the nature of strings, i.e. that they're often an array of chars? (dependent on language)

#### Example solution

```python
def part_one(input_string: str) -> str:
    return input_string[::-1]
```


### Part 2

**Prompt**: Now add the ability to reverse the words in a sentence. For example, the input `I love InternHacks` should output `InternHacks love I`.

Things to note:
- Do they modify the existing function? Create a new function? Ask for clarification about which they should do?
- This part will vary a lot based on language. Shows how comfortable they are with language features like string tokenization.
- Once tokenized, this is the same as Part 1 -- do they recognize this?

#### Example solution

```python
def part_two(input_string: str) -> str:
    tokenized = input_string.split()
    reversed = tokenized[::-1]
    return " ".join(reversed)
```

### Part 3

**Prompt**: Finally, modify your function to reverse a sentence. For example, the input `I love InternHacks` should output `skcaHnretnI evol I`.

Things to note:
- The candidate will often start implementing this, then you can see the "Aha!" moment when they realize that it's the same as Part 1. I like this question because I find that being able to recognize repeated work with different framing is an important skill.