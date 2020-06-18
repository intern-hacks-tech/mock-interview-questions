#!/usr/bin/env python3

from collections import defaultdict
import re
import requests

pattern = re.compile(r"[\W_]+", re.UNICODE)

# A defaultdict is nice here so we don't have to handle missing keys.
frequencies = defaultdict(int)
resp = requests.get("https://www.gutenberg.org/files/11/11-0.txt")
# Set the encoding on the response
resp.encoding = "utf-8"

# The response is a big ol' string, so we need to split it.
for word in resp.text.split():
    # Remove all non-word characters from the word.
    word = pattern.sub("", word)
    frequencies[word.lower()] += 1

frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
for x in range(10):
    print(frequencies[x][0], frequencies[x][1])
