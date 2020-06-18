#!/usr/bin/env python3

from collections import defaultdict
import pprint
from typing import Tuple

allowlist = defaultdict(int)


def update_allowlist(entries: Tuple[int, str, str]):
    sorted_entries = sorted(entries)
    for entry in sorted_entries:
        _, ip_addr, disposition = entry
        if disposition == "GENUINE":
            allowlist[ip_addr] += 1
        elif disposition == "FRAUD":
            allowlist[ip_addr] = 0


if __name__ == "__main__":
    example_entries = [
        # (timestamp, ip_address, disposition)
        (1592096350, "1.2.3.4", "GENUINE"),
        (1592096351, "2.3.4.5", "GENUINE"),
        (1592096352, "1.2.3.4", "GENUINE"),
        (1592096353, "1.2.3.4", "FRAUD"),
        (1592096354, "1.2.3.4", "GENUINE"),
        (1592096355, "1.2.3.4", "GENUINE"),
        (1592096356, "2.3.4.5", "FRAUD"),
    ]

    update_allowlist(example_entries)
    print(dict(allowlist))
