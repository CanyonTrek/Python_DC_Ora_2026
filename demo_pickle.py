#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE
# Python Object to a file using the pickle module
""" 
    DocString
"""
import pickle
import pprint
import gzip # Other Py Std Library modules: bz2, tarfile, shutil
movies = { 'bob': ['deadpool', 'ready player one', 'oppenheimer'],
           'oscar': ['titanic', 'godfather', 'shawshank redemption'],
           'luiza': ['der himmel uber berlin', 'fanny och alexander', 'the english patient'],
           'robert': ['river runs through it', 'butch cassidy', 'great escape'],
           'martha': ['legends of the fall', 'avengers', 'return of the jedi']
}

# Open file handle for WRITING in Binary mode
# with open(r"f:\labs\projects\Python_DC_Jun2026\movies.p", mode="wb") as fh_out:
with gzip.open(r"f:\labs\projects\Python_DC_Jun2026\movies.pgz", mode="wb") as fh_out:
    # pickle.dump(movies, fh_out, protocol=5) # Pickle protocols (0=ascii, 1-5=binary)
    pickle.dump(movies, fh_out, pickle.DEFAULT_PROTOCOL)  # Pickle = 4
    # pickle.dump(movies, fh_out, pickle.HIGHEST_PROTOCOL)  # Pickle = 5

# Open file handle for READING in Binary mode
# with open(r"f:\labs\projects\Python_DC_Jun2026\movies.p", mode="rb") as fh_in:
with gzip.open(r"f:\labs\projects\Python_DC_Jun2026\movies.pgz", mode="rb") as fh_in:
    films = pickle.load(fh_in)

pprint.pprint(movies)
print("-" * 60)
pprint.pprint(films)