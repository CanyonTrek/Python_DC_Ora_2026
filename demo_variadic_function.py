#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match strings/data using
# str testing and pattern matching using the RE module
"""
    Collection of tools to search for Regex Patterns in files
"""
import re

# Example of a Variadic function that allows
# variable number of parameters (TUPLE)
def search_pattern(pattern=r"^.{19}$", *files):
    """ Search for Regex patterns in multiple files and
        return number of lines matched
    """
    lines = 0
    reobj = re.compile(pattern)  # Compile PATTERN only ONCE
    for file in files:
        fh_in = open(file, mode="rt")

        for line in fh_in:
            # m = re.search(pattern, line)  # Match multiple patterns
            m = reobj.search(line)  # Match Compiled pattern against line
            if m:
                lines =+ 1
                print(f"Matched {m.group()}")
    return lines

search_pattern(r"^([A-Z]).*\1$", r"f:\labs\words", r"f:\labs\words2", r"f:\labs\words3")
