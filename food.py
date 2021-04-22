#!usr/bin/python3.6

import random
import time
from colors import Colors

# Class that creates the food that will be consumed by the snake
class Food:

	# Parametrised constructor that initializes the food
	def __init__(self,size):
		self.size = size
		self.position = (random.randint(1,38) * self.size,random.randint(1,28) * self.size)
		self.color = Colors["yellow"]
		self.birth_time = time.time()
		self.time_to_live = 10

	def can_destroy(self):
		return time.time() > self.birth_time + self.time_to_live

	# Function that randomizes the position of the food
	def randomize_position(self):
		self.position = (random.randint(1,38) * self.size,random.randint(1,28) * self.size)
		self.color = random.choice([Colors["yellow"],Colors["red"]])
		self.birth_time = time.time()

		if self.color == Colors["yellow"]:
			self.time_to_live = 10
		elif self.color == Colors["red"]:
			self.time_to_live = 3