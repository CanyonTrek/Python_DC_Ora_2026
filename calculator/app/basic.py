#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines several basic calculator functions
""" 
    Basic calculator functions including add, multiply, and divide.
"""
import sys
def add(*args):
    """ Return SUM of all arguments as a float """
    sum = 0
    for num in args:
        sum += num
    return float(sum)

def mul(*args):
    """ Return PRODUCT of all arguments as a float """
    total = 1
    for num in args:
        total *= num
    return float(total)

def div(x, z):
    """ Return QUOTIENT of x divided by to 3 decimal places """
    return round(x/z, 3)

def main():
    print("----------- BASIC Calc -----------")
    print(f"4 + 3 + 2 + 1 = {add(4, 3, 2, 1)}")
    print(f"4 * 3 * 2 = {mul(4, 3, 2)}")
    print(f"4 / 3 = {div(4, 3)}")
    print("----------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute if ran directly as a program.
    # Ignore if imported as a module
    main()
    sys.exit(0)