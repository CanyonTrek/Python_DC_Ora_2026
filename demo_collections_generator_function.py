#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO generate collections
# in a more memory efficient way.
""" 
    DocString
"""

def get_numbers():
    """ Return a LIST of numbers """
    numbers = []
    for x in range(0, 1000000000000):
        numbers.append(x)
    return numbers

def generate_numbers():
    """ Yield one object at a time from a collection """
    for x in range(0, 10):
        yield x

# for z in get_numbers():
for z in generate_numbers():
    print(z)


gen = generate_numbers()
while True:
    num = next(gen, -1)
    if num != -1:
        print(num)
    else:
        break

# Alternatively, we could just request a value manually..
gen = generate_numbers()
num1 = next(gen)
num2 = next(gen)
num3 = next(gen)
print(num1, num2, num3)