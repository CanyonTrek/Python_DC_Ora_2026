#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO PRESERVE ONE
# Python Object to a file using the pickle module
"""
    DocString
"""
import shelve
movies = { 'bob': ['deadpool', 'ready player one', 'oppenheimer'],
           'martha': ['legends of the fall', 'avengers', 'return of the jedi'],
           'luiza': ['der himmel uber berlin', 'fanny och alexander', 'the english patient']
}

tv_series = {'bob': ['cheers', 'the big bang theory'],
             'martha': ['x files', 'friends'],
             'luiza': ['crown', 'little britain']
}

books = {'bob': 'IT',
         'martha': 'the house of the spirits',
         'luiza': 'CEO Diary'
}

with shelve.open(r"f:\labs\projects\Python_DC_Jun2026\media") as db:
    db['movies'] = movies
    db['tv_series'] = tv_series
    db['books'] = books

with shelve.open(r"f:\labs\projects\Python_DC_Jun2026\media") as db:
    print(f"Bob's favourite film is {db['movies']['bob'][0]}")
    print(f"Martha's favourite tv_series is {db['tv_series']['martha'][0]}")
    print(f"Luiza's favourite book is {db['books']['luiza']}")







