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
with open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="wt") as fh_out:
    for name in movies:
        print(f"{name} {movies[name]}", end="\n", file=sys.stdout)
        print(f"{name} {movies[name]}", end="\n", file=fh_out)
    # End of block, filehandle auto closed

print("-" * 50)

# Open file handle for READING in TEXT mode
with open(r"f:\labs\projects\Python_DC_Jun2026\movies.txt", mode="rt") as fh_in:
    for line in fh_in:
        print(line, end="")
