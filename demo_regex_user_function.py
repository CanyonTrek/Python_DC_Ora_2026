#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match strings/data using
# str testing and pattern matching using the RE module
"""
    DocString
"""
import re

def search_pattern(pattern=r"^.{19}$", file=r"f:\labs\words"):
    fh_in = open(file, mode="rt")
    lines = 0
    reobj = re.compile(pattern) # Compile PATTERN only ONCE

    for line in fh_in:
        # m = re.search(pattern, line)  # Match multiple patterns
        m = reobj.search(line)  # Match Compiled pattern against line
        if m:
            lines =+ 1
            print(f"Matched {m.group()}")
    return lines

print(f"Lines returned = {search_pattern()}")
num_lines = search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words")
print(f"Matched {num_lines}")