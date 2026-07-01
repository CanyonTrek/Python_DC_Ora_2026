#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO match strings/data using
# str testing and pattern matching using the RE module
""" 
    DocString
"""
import re
# Open file for READING in TEXT mode
fh_in = open(r"f:\labs\words", mode="rt")

# Iterate through the file handle using an ITERATOR loop
for line in fh_in:
    # Example of str testing
    # if line.startswith("Y") and line.rstrip("\n").endswith("n")\
    #        and "town" in line:
    # m = re.search(r"town", line) # Match lines with "town"
    # m = re.search(r"^town", line)  # Match lines starting with "town"
    # m = re.search(r"town$", line)  # Match lines ending with "town"
    # m = re.search(r"^town$", line)  # Match lines with only "town"
    # m = re.search(r"^.own$", line)  # Match lines 4 chars ending "own"
    # m = re.search(r"^...................$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"^.{19}$", line)  # Match lines EXACTLY 19 chars
    # m = re.search(r"^[ads]own$", line)  # Match lines with [ads] followed by "own"
    # m = re.search(r"^[A-Z]", line)  # Match lines starting with a CAPITAL
    # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # Match lines with 3 consecutive vowels
    # m = re.search(r"[aeiou]{5,}", line)  # Match lines at least 5 consecutive vowels
    # m = re.search(r"[0-9][0-9]", line)  # Match lines with TWO DIGITS
    # m = re.search(r"\.", line)  # Match lines with a DOT
    # m = re.search(r"[.]", line)  # Match lines with a DOT
    # m = re.search(r"^[A-Z].*[A-Z]$", line)  # Match lines start/end with CAPITAL
    # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # Match lines start/end with CAPITAL
    # m = re.search(r"^(.)(.).\2\1$", line, flags=re.I)  # Match 5 char palindromes
    # m = re.search(r"^([A-Z]).*\1$", line)  # Match lines start/end with SAME CAPITAL
    # m = re.fullmatch(r"^(.)(.).\2\1\n$", line)  # Match ENTIRE line including hidden chars
    m = re.search(r"pineapple|spongebob|patrick", line)  # Match multiple patterns
    if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()}")
        # print(f"Matched {m.group()} on {line.rstrip()} at {m.start()}-{m.end()} "
        #        f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")