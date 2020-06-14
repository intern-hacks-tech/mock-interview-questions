## Adaptive Allowlist

### Prompt
Suppose you run a service that tracks fraudulent activity from IP addresses. The service needs to increment a counter for every known-good request and reset the counter to zero when a fraudulent request is received. This data will be used to inform controls such as skipping additional authentication challenges for more reputable addresses.

The data is derived from access logs and submitted to your service as a list of tuples representing request dispositions:

```python
[
    # (timestamp, ip_address, disposition)
    (1592096350, "1.2.3.4", "GENUINE"),
    (1592096351, "2.3.4.5", "GENUINE"),
    (1592096352, "1.2.3.4", "GENUINE"),
    (1592096353, "1.2.3.4", "FRAUD"),
    (1592096354, "1.2.3.4", "GENUINE"),
    (1592096355, "1.2.3.4", "GENUINE"),
    (1592096356, "2.3.4.5", "FRAUD"),
]
```

The results would look something like this:

```python
{
    "1.2.3.4": 2,
    "2.3.4.5": 0
}
```

Write a function that accepts a list of tuples (or something similar in your language) and creates a similar map of the data.

### For the interviewer

- Don't mention the timestamps -- see if the candidate asks if they can assume the data is in the correct order, or if they decide to sort the data anyway.
- Look for familiarity with language features, especially if the candidate has indicated that they have a high proficiency with the chosen language. For example, `defaultdict` in Python is super handy for this exercise.

### Sample solution

```python
allowlist = defaultdict(int)

def update_allowlist(entries: Tuple[int, str, str]):
    sorted_entries = sorted(entries)
    for entry in sorted_entries:
        _, ip_addr, disposition = entry
        if disposition == "GENUINE":
            allowlist[ip_addr] += 1
        elif disposition == "FRAUD":
            allowlist[ip_addr] = 0
```

For a working version, see [adaptive-allowlist.py](adaptive-allowlist.py).

### Follow-up

If you have extra time, see how the candidate would handle some extra functionality. Some options:

- How would you change your answer to handle multiple submissions of data?
  - This would require storing the last-seen timestamp for each IP, or even the last fraudulent timestamp and last genuine. If the newer data has a timestamp prior to the stored timestamp, what would they do with the data?
- How would you approach persisting the results?
- What about persisting the results for reading/writing by multiple instances of your application?
  - Depending on the experience level of the candidate, you may not want to expect a very accurate answer. The question can still give good insight into critical thinking skills, especially if they don't have prior experience with something like this.
