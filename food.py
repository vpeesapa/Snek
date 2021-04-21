#!usr/bin/python3.6

import random
from colors import Colors

# Class that creates the food that will be consumed by the snake
class Food:

	# Parametrised constructor that initializes the food
	def __init__(self,size):
		self.position = (0,0)
		self.color = Colors["yellow"]
		self.size = size
		self.randomize_position()

	# Function that randomizes the position of the food
	def randomize_position(self):
		self.position = (random.randint(0,38) * self.size,random.randint(0,28) * self.size)