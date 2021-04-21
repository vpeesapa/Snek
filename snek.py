#!usr/bin/python3.6

import pygame
from colors import Colors
from player import Player
from food import Food

# Intialising the game engine
pygame.init()

# Open a new window
window_width = 800
window_height = 600
window_size = (window_width,window_height)
window = pygame.display.set_mode(window_size,0,32)
pygame.display.set_caption("Snek")

grid_size = 20
grid_width = window_width / grid_size
grid_height = window_height / grid_size

def drawGrid(surface):
	for y in range(0,int(grid_height)):
		for x in range(0,int(grid_width)):
			r = pygame.Rect((x * grid_size,y * grid_size),(grid_size,grid_size))
			if (x + y) % 2 == 0:
				pygame.draw.rect(surface,(93,216,228),r)
			else:
				pygame.draw.rect(surface,(84,194,205),r)

surface = pygame.Surface(window.get_size())
surface = surface.convert()

# Declaring a variable that proceeds with the game if there is no particular outcome
continueGame = True

# Global variables
font_size = 16
font = pygame.font.SysFont("monospace",font_size)

# Dimensions of one section of the snake's body
snake_size = 20

# Dimensions of the food that the snake can consume
food_size = 20

# Creating the snake
snake = Player(Colors["black"],window_width / 2,window_height / 2,snake_size)

# Initialising the food
food = Food(food_size)

# Creating a clock that controls the rate at which the window updates
clock = pygame.time.Clock()

def eatsFood():
	return snake.get_snake_head() == food.position

# Main gameplay loop that is only broken if the snake dies
while continueGame:

	drawGrid(surface)

	# Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			# If the user voluntarily closes the window
			continueGame = False

	keys = pygame.key.get_pressed()
	if keys[pygame.K_x]:
		# If x is pressed, the game closes
		continueGame = False
	if keys[pygame.K_UP]:
		# If the up arrow key is pressed, the snake should move upwards
		snake.turn((0,-1))
	if keys[pygame.K_DOWN]:
		# If the down arrow key is pressed, the snake should move downwards
		snake.turn((0,1))
	if keys[pygame.K_LEFT]:
		# If the left arrow key is pressed, the snake should move towards the left
		snake.turn((-1,0))
	if keys[pygame.K_RIGHT]:
		# If the right arrow key is pressed, the snake should move towards the right
		snake.turn((1,0))
	
	# --Game Logic--
	# Check if the snake eats the food
	if eatsFood():
		snake.length += 1
		snake.score += 1
		food.randomize_position()

	# Check if the snake is not going out of bounds
	snake_head = snake.get_snake_head()
	if snake_head[0] <= 0 or snake_head[0] + snake_size >= window_width:
		continueGame = False
	if snake_head[1] <= font_size or snake_head[1] + snake_size >= window_height:
		continueGame = False

	# --Draw all the components onto the screen--
	window.fill(Colors["white"])

	# Draw the snake
	for part in snake.parts:
		pygame.draw.rect(surface,snake.color,(part[0],part[1],grid_size,grid_size))
		pygame.draw.rect(surface,(93,216,228),(part[0],part[1],grid_size,grid_size),1)

	# Drawing the food
	pygame.draw.rect(surface,food.color,(food.position[0],food.position[1],grid_size,grid_size))
	pygame.draw.rect(surface,(93,216,228),(food.position[0],food.position[1],grid_size,grid_size),1)

	window.blit(surface,(0,0))

	# Displaying the score in the top-left corner of the window
	text = font.render("Score: " + str(snake.score),1,Colors["black"])
	window.blit(text,(5,10))

	# Updates the screen with whatever's drawn so far
	pygame.display.update()

	if continueGame:
		# The snake should continously move in a single direction
		continueGame = snake.move()

	# Limit the clock to 10 frames per second
	clock.tick(10)

# Stops the game engine after the user has exited the main gameplay loop
pygame.quit()