#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close, and
# randomly read, write to a TEXT/Binary file.
""" 
    DocString
"""
SOF = 0 # Start of file
CUR = 1 # Current file position
EOF = 2 # End of file

# Open filehandle for READING in TEXT mode
with open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="rt") as fh_in:
    fh_in.seek(90, SOF) # Seek forwards 90 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

    fh_in.seek(135, SOF) # Seek forwards 135 chars from SOF
    text = fh_in.read(30)
    print(f"Text at {fh_in.tell() - len(text)} = {text}")

print("-" * 50)

# Open filehandle for READING in BINARY/BYTES mode
with open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="rb") as fh_data:
    fh_data.seek(-90, EOF) # Seek back 90 bytes from EOF
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")

    fh_data.seek(-65, CUR) # Seek back 65 bytes from current position
    text = fh_data.read(30)
    print(f"Text at {fh_data.tell() - len(text)} = {text}")
