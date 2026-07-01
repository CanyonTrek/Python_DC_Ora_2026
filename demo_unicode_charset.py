#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will display the entire UNICODE charset
""" 
    DocString
"""
# Iterate through the Unicode charset from pos 0->65535
# using an ITERATOR for loop plus the built-in range() function
for pos in range(0, 65536):
    try:
        print(chr(pos), end=" ")
        # Display chars 16 per line
        if pos % 16 == 0:
            print()

    except UnicodeEncodeError:
        print(" ")
