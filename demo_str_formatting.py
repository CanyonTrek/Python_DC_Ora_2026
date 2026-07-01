#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO format strings using
# str concatenation, escape chars, str methods, the str.format()
# method and f-strings.
""" 
    DocString
"""
# Example dict with planetary info with the distance
# to the sun in Giga-metres
planets = {'Mercury': 57.91,
           'Venus': 108.2,
           'Earth': 149.597870,
           'Mars': 227.94
}

# Iterate through the planet keys and display planet info
# using Iterator for loop plus escape chars and str concatenation.
for planet in planets.keys():
    print("\t\t" + planet + ": " + str(planets[planet]) + " Gm")

print("-" * 50)
# using Iterator for loop plus str concatenation and str justification
# methods - OKAY
for planet in planets.keys():
    print(planet.rjust(12) + ": " + str(planets[planet]).rjust(12, '.') + " Gm")

print("-" * 50)
# using Iterator for loop plus the str.format() method - GOOD
for planet in planets.keys():
    print("{0:>12s}: {1:.>12.3f} Gm".format(planet, planets[planet]))

print("-" * 50)
# From Python 3.5 - we also have f-strings! Better!
for planet in planets.keys():
    print(f"{planet:>12s}: {planets[planet]:.>12.3f} Gm")

