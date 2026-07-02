#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This module defines a class of Tank
""" 
    Tank class
"""
from app import vehicle

class Tank(vehicle.Vehicle):
    # 2 Components: Attributes/Data + Behaviour/Methods
    def __init__(self, country, model):
        vehicle.Vehicle.__init__(self, country, model)
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._health = 100
        self._shells = 20
        # No explicit return, as called implicitly/automatically


    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None

    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None

    def shoot(self):
        self._shells -= 1
        return None

    def take_damage(self, damage):
        self._health -= damage
        return None

    # And now for some SPECIAL methods
    # Example of OPERATOR overloading
    def __add__(self, other):
        return self._health + other._health

    # Example of Duck Typing - our Tank can now QUACK like a duck!
    def __str__(self):
        return f"Model={self.model}, health={self._health}, speed={self._speed}"

    # Examples of a GETTER and a SETTER
    def get_health(self):
        return self._health

    def set_health(self, new_health):
        self._health = new_health
        return None

    # Wrapping getter+setter with a ONE variable name interface
    tank_health = property(get_health, set_health)