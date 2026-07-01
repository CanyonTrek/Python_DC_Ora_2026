#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This script will demo HOWTO define, and call
# user functions with optional parameters and optional default
# values
""" 
    DocString
"""
# Example of a user function with
# optional parameter passing with default values.
# Annotations = preferred data for passing in (not enforced)
# Enforce named following parameters *,
def say_hello(greeting:str="ciao", recipient:str="amici")->None:
    message = f"{greeting} {recipient}"
    print(message)
    return None


say_hello("hello", "my friends") # Positional parameter passing
say_hello(greeting="halo", recipient="mo charidean") # Named parameter passing
say_hello( recipient="mes amis", greeting="bonjour") # Named parameters in different order
say_hello("hola", recipient="amigos") # Mixed parameters (positional->named)
say_hello("ciao", 3.14)
say_hello()

# Fact Finding - display annotations for a user function
print(f"Annotations for say_hello = {say_hello.__annotations__}")


