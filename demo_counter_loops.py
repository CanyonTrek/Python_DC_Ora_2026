#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO repeat BLOCK of
# commands a specific number of times using a COUNTER loop.
""" 
    DocString
"""

count = 0 # 1.Initialise counter
while count < 10: # 2.Test counter
    print(count)
    count += 1 # 3.Increment counter

# Alternatively we could use a for loop plus
# the built-in range(start=0, stop=10, step=1) function
for num in range(0, 10, 1):
    print(num)

# the built-in range(0, 10, step=1) function
for num in range(0, 10):
    print(num)

# the built-in range(start=0, 10, step=1) function
for num in range(10):
    print(num)