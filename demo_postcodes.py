#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will clean the data in a postcodes
# file and validate as a proper UK postcode.
""" 
    DocString
"""
import re
fh_in = open(r"f:\labs\postcodes.txt", mode="rt")

valid = 0
invalid = 0

for postcode in fh_in:
    if postcode.isspace(): continue
    postcode = re.sub(r"\s+", r"", postcode)
    postcode = postcode.upper()
    postcode = re.sub(r"(\d[A-Z][A-Z])$", r" \1", postcode)

    m = re.search(r"^[A-Z]{1,2}\d{1,2}[A-Z]?\s\d[A-Z][A-Z]$", postcode)
    if m:
        print(postcode)
        valid += 1
    else:
        invalid += 1

print(f"Valid postcodes = {valid}")
print(f"Invalid postcodes = {invalid}")