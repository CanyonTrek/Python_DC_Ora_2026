#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through
# a sequence (str/list/tuple/dict/sets) using an ITERATOR for
# loop
""" 
    DocString
"""
#              0               1            2           3
heroes = ['lyndsey von', 'jane goodall', 'ronaldo', 'valderrama',
          'ramon arroyo']

# Iterate through the objects in the sequence (list) using
# an ITERATOR for loop..
for name in heroes:
    print(name, end="\n")
print("Heroes =", heroes)

# Iterate through the objects in the sequence (list) AND
# MODIFY the objects using an ITERATOR for loop..
idx = 0
for name in heroes:
    print(name.upper(), end="\n")
    heroes[idx] = name.upper()
    idx += 1
print("Heroes =", heroes)

# Iterate through the objects in the sequence (list) AND
# MODIFY the objects using  ITERATOR for loop plus enumerate() function
for (idx, name) in enumerate(heroes):
    print(name.title(), end="\n")
    heroes[idx] = name.title()
print("Heroes =", heroes)