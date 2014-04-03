#!/usr/bin/env python3

from inp    import *
from random import randint

dice  = int_input("How many dice do ya want? ")
if dice < 1:
	while dice < 1:
		print("Give me a valid number of dice, please.")
		dice = int_input("How many dice do ya want? ")

sides = int_input("How many sides should the die have? ")
if sides < 2:
	while sides < 2:
		print("Give me a valid number of sides, please.")
		sides = int_input("How many sides should the die have? ")

for x in range(0, dice):
	print(randint(1, sides))
