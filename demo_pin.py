#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will simulate a high street bank
# ATM PIN machine and MAX of 3 attempts
""" 
    DocString
"""

master_pin = "0123"
pin = None
attempts = 0

while pin != master_pin and attempts < 3:
    pin = input("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("Invalid PIN")
        attempts += 1
else:
    # ONLY executes ONCE when while loop becomes False
    print("Too many attempts")
    print("Your card has been retained - have a nice day!")


print("Done")