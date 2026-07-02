#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO COPY and optionall
# FILTER collections (str/tuple/list/dict/set) to a destination
# collection using several techniques..
""" 
    DocString
"""
# Source collection
students = ['luiza', 'bob', 'victor', 'bob', 'oscar', 'isla', 'grace']

# Iterate through the source collection and optionally filer
# 1.Using Iterator loop + source, optional if (filtering), an expression
wee_names = []
for name in students: # 1.Iterator loop plus source
    if len(name) <= 5: # 2.Optional if (filtering)
        wee_names.append(name.upper()) # 3.Expressions
print(f"1.Short names = {wee_names}")

# 2.Using Iterator loop + source, user function (filtering), an expression
def filter_names(name):
    """ Return True if business logic is True """
    if len(name) <= 5:
        return True
    else:
        return False

wee_names = []
for name in students: # 1.Iterator loop plus source
    if filter_names(name): # 2.Optional if (filtering)
        wee_names.append(name.upper()) # 3.Expressions
print(f"2.Short names = {wee_names}")

# 3.Using built-in filter() (Iterating), user function (filtering)
wee_names = list(filter(filter_names, students))
print(f"3.Short names = {wee_names}")

# 4.Using built-in filter() (Iterating), lambda function (filtering)
wee_names = list(filter(lambda name: len(name) <= 5, students))
print(f"4.Short names = {wee_names}")

# 5.Using LIST Comprehension (expr + optional condition + iterator loop)
wee_names = [ name.upper() for name in students if len(name) <= 5 ]
print(f"5.Short names = {wee_names}")

# 5.1.Using LIST Comprehension (expr + optional condition + iterator loop)
wee_names = [ (name.upper(), len(name)) for name in students if len(name) <= 5 ]
print(f"5.1.Short names = {wee_names}")

# 5.2.Using DICT Comprehension (expr + optional condition + iterator loop)
# Free EXTRA filtering - all duplicate keys removed! :-)
wee_names = { name.upper(): len(name) for name in students if len(name) <= 5 }
print(f"5.2.Short names = {wee_names}")

# 5.3.Using SET Comprehension (expr + optional condition + iterator loop)
# Free EXTRA filtering - all duplicate values removed! :-)
wee_names = { name.upper() for name in students if len(name) <= 5 }
print(f"5.3.Short names = {wee_names}")