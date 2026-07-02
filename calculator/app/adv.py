#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines several Advanced calculator
# functions
""" 
    Advanced Calculator functions including power, modulus and
    square root functions
"""
import sys
def mod(x, z):
    """ Return REMAINDER after integer div of x/z """
    return float(x%z)

def power(x, z):
    """ Return POWER of x to z as a float """
    return float(x**z)

def sqrt(x):
    """ Return Square root of x as a float """
    return float(x**0.5)

def main():
    print("----------- ADV Calc -----------")
    print(f"90 % 8 = {mod(90, 8)}")
    print(f"90 ** 2 = {power(90, 2)}")
    print(f"\N{square root}90 = {sqrt(90)}")
    print("---------------------------------")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute if ran directly as a program.
    # Ignore if imported as a module
    main()
    sys.exit(0)