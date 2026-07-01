#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO ITERATE through
# separate but INDEX RELATED sequences using the built-in
# zip() function
""" 
    DocString
"""
import sys
# Separate LISTS but index-related
students = ['victor', 'bob', 'robert']
fav_heroes = ['ramon arroyo', 'george carlin', 'george washington']
fav_bands = ['coldplay', 'pearl jam', 'grateful dead']
fav_locs = ['los 4 pulques', 'minnesota', 'last chance, idaho']

# ITERATE through all separate but index-related lists
# using an ITERATOR for loop plus built-in zip() function
for (s, fh, fb, fl) in zip(students, fav_heroes, fav_bands, fav_locs):
    print(s + " likes to listen to " + fb + " in " + fl + " with " + fh)

try:
    sys.exit(0) # Explicit exit with return code (0=success, 1-255=error)
    # sys.exit("goodbye") # Return "goodbye" to STDERR (red) with error code = 1
except SystemExit:
    print("Quitting..")
    sys.exit(66)