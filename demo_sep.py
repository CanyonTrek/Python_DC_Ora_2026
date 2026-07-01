#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO 
""" 
    DocString
"""
#          01234567890123456789012345678901234567890
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("-" * len(Belgium))
print(Belgium.replace(",", ":"))
pop = Belgium[8:16]
city = Belgium[26:32]
print("Pop:", pop)
print("City:", city)
print("Total:", int(pop) + int(city))
print("-" * len(Belgium))