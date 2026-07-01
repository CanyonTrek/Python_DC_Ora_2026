#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO Match and substitute
# on the string using the re.sub() and re.subn() functions.
""" 
    DocString
"""
import re
# Sample line from /etc/passwd on Linux for the root user account
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to make a change!
line = re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line) # Returns a modified str
(line, num) = re.subn(r"ksh$", r"bash", line) # Returns TUPLE (str, num changes)

print(f"Modified line = {line} with {num} changes")

# RE module has a better split function
line = "root:x;0.0,The Super User:/root:/bin/ksh"
fields = re.split("[:;,.]", line) # Returns a list