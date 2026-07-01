#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO create, and grow, and shrink,
# and access a dict - UNORDERED collection with unique keys.
# From Python 3.6 onwards - dict are INSERTION ORDER
""" 
    DocString
"""
import pprint
# Example of a multi-dimensional dict of lists
movies = { 'bob': ['deadpool', 'ready player one', 'oppenheimer'],
           'oscar': ['titanic', 'godfather', 'shawshank redemption'],
           'luiza': ['der himmel uber berlin', 'fanny och alexander', 'the english patient']
}

# Grow a dict
movies['robert'] = ['river runs through it', 'butch cassidy', 'great escape']
movies['martha'] = ['legends of the fall', 'avengers', 'return of the jedi']

movies.pop('oscar') # Remove key+value pair
movies.popitem() # Removes LAST INSERTED key+value

# films = movies.copy() # Copy dict
# films.clear() # Empty the dir

pprint.pprint(movies)
print("-" * 60)

# Access keys+values in dict..
print(f"Bob's favourite movies are {movies['bob']}")
print(f"Bob's favourite movies are {movies.get('bob')}")
print(f"Luiza's ultimate movies is {movies['luiza'][0]}")
print("-" * 60)

# OR we could ITERATE through the keys/values or both in a dict
# USing an ITERATOR for loop and the keys
for name in movies.keys():
    print(f"{name} likes {movies[name]}")

# USing an ITERATOR for loop and the values
for films in movies.values():
    print(f"Recommended films = {films}")

# USing an ITERATOR for loop and the key_value pairs
for (name, films) in movies.items():
    print(f"{name} loves {films}")
