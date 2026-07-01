#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO split and rejoin strings
# using the str.split() and str.join() methods
""" 
    DocString
"""
# Sample line from /etc/passwd on Linux for the root user account.
line = "root:x:0:0:The Super User:/root:/bin/ksh"

# And I want to modify the string! BUT str are IMMUTABLE!
fields = line.split(":") # Returns a LIST - which is MUTABLE!
fields[4] = "The Administrator"
fields[6] = "/bin/bash"
print(fields)
line = ":".join(fields) # Returns a new str
print("Modified line =", line)
