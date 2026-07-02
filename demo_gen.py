#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""

def frange(start, stop, step=0.25):
    """ """
    current = float(start)
    while current < stop:
        yield current
        current += step

print(list(frange(1, 3, 1)))

for z in frange(1, 10, 0.25):
    print(z)