#!usr/bin/python3.6

import random

# Setting the 4 directions that the snake can move in
up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

# Class that creates the playable snake
class Player:

	# Parametrised constructor that initializes the snake
	def __init__(self,color,x,y,size):
		self.length = 1
		self.color = color
		self.parts = [(x,y)]
		self.size = size
		self.direction = random.choice([up,down,left,right])
		self.score = 0

	# Function that returns the position of the snake's head
	def get_snake_head(self):
		return self.parts[0]

	# Function that allows the snake to turn in a particular direction
	def turn(self,direction):
		if self.length > 1 and (direction[0] * (-1),direction[1] * (-1)) == self.direction:
			# The snake cannot turn in the opposite direction
			return
		else:
			self.direction = direction

	# Function that moves the snake in a particular direction
	def move(self):
		current_pos = self.get_snake_head()
		x,y = self.direction

		# Calculate the new position of the snake
		new_pos_x = current_pos[0] + (x * (self.size) / 4)
		new_pos_y = current_pos[1] + (y * (self.size) / 4)
		new_pos = (new_pos_x,new_pos_y)

		if len(self.parts) > 2 and new_pos in self.parts[2:]:
			# If the snake's head collides with a portion of its body, game over
			return False
		else:
			self.parts.insert(0,new_pos)
			if len(self.parts) > self.length:
				self.parts.pop()
			return True