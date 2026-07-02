#! /usr/bin/env python3
# Author: DCameron
# Version: 1.0
# Description: This is an ultra realistic online game with Tanks!
""" 
    GOT - Game of Tanks
"""
import sys
from app import tank

def main():
    # Create/Instantiate 3 new Tank objects
    bob_tank = tank.Tank("German", "Tiger")
    martha_tank = tank.Tank("American", "Sherman")
    victor_tank = tank.Tank("British", "Churchill")

    # And the game begins..
    bob_tank.accel(63)
    martha_tank.accel(29)

    victor_tank.rotate_left(289)
    victor_tank.accel(23)
    victor_tank.shoot()

    # And success..
    bob_tank.take_damage(58)
    martha_tank.take_damage(28)

    # And now for some game visuals..
    print(f"Health of Bob's tank is {bob_tank._health}") # POOR CODE

    # Example of operator overloading
    print(f"Health of Bob's and Martha's tanks are {bob_tank + martha_tank}")

    # Bob has received a health boost!
    # bob_tank._health = 100 # POOR CODE as PRIVATE variable
    # print(f"New health of Bob's Tank = {bob_tank._health}") # POOR CODE
    bob_tank.set_health(101)  # SETTER = good
    print(f"New health of Bob's Tank = {bob_tank.get_health()}") # GETTER = good
    bob_tank.tank_health = 102  # Using a property variable
    print(f"New health of Bob's Tank = {bob_tank.tank_health}") # Using property

    print(f"Status of Bob's tank: {bob_tank}")
    return None

# Namespace Trick
if __name__ == "__main__":
    # Execute ONLY if ran directly as a program
    # But IGNORE if imported as a module.
    main()
    sys.exit(0)