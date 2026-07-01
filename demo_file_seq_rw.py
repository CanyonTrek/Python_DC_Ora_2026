#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO open, and close,
# for reading, writing and appending in TEXT mode
""" 
    DocString
"""
import sys
movies = { 'bob': ['deadpool', 'ready player one', 'oppenheimer'],
           'oscar': ['titanic', 'godfather', 'shawshank redemption'],
           'luiza': ['der himmel uber berlin', 'fanny och alexander', 'the english patient'],
           'robert': ['river runs through it', 'butch cassidy', 'great escape'],
           'martha': ['legends of the fall', 'avengers', 'return of the jedi']
}

# Open filehandle for WRITING in TEXT mode
fh_out = open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="wt")

# ITERATE through the dict keys and WRITE keys+values to filehandle
for name in movies:
    print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
    print(f"{name} {movies[name]}", end="\n", file=fh_out)
    # fh_out.write(f"{name} {movies[name]}\n")

# fh_out.flush() # Flush buffers
fh_out.close() # Flush buffers and close file handle

print("-" * 50)

# Open file handle for READING in TEXT mode
fh_in = open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="rt")

# text = fh_in.read() # Read ENTIRE file into str. BE CAREFUL of huge files
# text = fh_in.read(30) # Read NEXT 30 chars into str.
# text = fh_in.readline() # Read NEXT LINE into str.
# lines = fh_in.readlines() # Read ENTIRE file into LIST. Be Careful of huge files
# print(f"1st line = {lines[0]}")
# print(f"Last line = {lines[-1]}")

# ITERATE through file one line at a time (memory efficient)
# using an ITERATOR for loop PLUS filehandle (iterator object = next/iter)
for line in fh_in:
    print(line, end="")

fh_in.close()
