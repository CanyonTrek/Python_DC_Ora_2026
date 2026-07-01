#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script is a basic calculator app
""" 
    Calculator App with add, multiply and divide functions
"""

def add(x, z):
    """ Return Sum of X and Z as a float """
    return float(x + z)

def mul(x, z):
    """ Return Product of X and Z as a float """
    return float(x * z)

def div(x, z):
    """ Return Quotient of X divided by Z to 3 decimal places """
    return round(x/z, 3)

print(f"4 + 3 = {add(4, 3)}")
print(f"4 + 3 = {(lambda x,z: float(x+z))(4, 3)}")

print(f"4 * 3 = {mul(4, 3)}")
print(f"4 / 3 = {div(4, 3)}")