#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and
# shrink and combine SETS. Sets are Unordered collections of
# unique values.
""" 
    DocString
"""
marvel_fans = {'donald', 'martha', 'oscar', 'charles', 'bob', 'isla'}
dc_fans = set() # Create an empty SET!

# Grow a set
dc_fans.add('donald')
dc_fans.add('robert')
dc_fans.add('luiza')

# Shrink a set removing one value at a time
# marvel_fans.pop() # Randomly removes a object
# comic_fans = marvel_fans.copy() # Copy a set

print(f"Fans of Marvel = {marvel_fans}")
print(f"Fans of DC = {dc_fans}")

print("-" * 50)
# Combine the SETS using SET operators (Remember VENN diagrams)
print(f"Fans of Marvel or DC = {marvel_fans.union(dc_fans)}")
print(f"Fans of Only Marvel AND DC = {marvel_fans.intersection(dc_fans)}")
print(f"Fans of Only Marvel = {marvel_fans.difference(dc_fans)}")
print(f"Fans of Only Marvel OR DC = {marvel_fans.symmetric_difference(dc_fans)}")
print("-" * 50)
print(f"Fans of Marvel or DC = {marvel_fans | dc_fans}")
print(f"Fans of Only Marvel AND DC = {marvel_fans & dc_fans}")
print(f"Fans of Only Marvel = {marvel_fans - dc_fans}")
print(f"Fans of Only Marvel OR DC = {marvel_fans ^ dc_fans}")