#!/usr/bin/env python3

from inp    import *
from random import randint

sides = int_input("How many sides should the die have? ")
if sides < 2:
	while sides < 2:
		print("Give me a valid number of sides, please.")
		sides = int_input("How many sides should the die have? ")

print(randint(1, sides))
