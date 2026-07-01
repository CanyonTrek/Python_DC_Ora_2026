#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO CHECK which platform
# your script is running on..
""" 
    DocString
"""
import sys
import os

if sys.platform == "win32":
    my_home = os.environ["HOMEPATH"]
else:
    my_home = os.environ["HOME"]

print("My home directory is:", my_home)
