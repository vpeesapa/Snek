#!usr/bin/python3.6

import pygame
from colors import Colors
from player import Player

# Intialising the game engine
pygame.init()

# Open a new window
window_width = 800
window_height = 600
window_size = (window_width,window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Snek")

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

# Creating a clock that controls the rate at which the window updates
clock = pygame.time.Clock()

# Main gameplay loop that is only broken if the snake dies
while continueGame:

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
	# Check if the snake is not going out of bounds
	snake_head = snake.get_snake_head()
	if snake_head[0] <= 0 or snake_head[0] + snake_size >= window_width:
		continueGame = False
	if snake_head[1] <= font_size or snake_head[1] + snake_size >= window_height:
		continueGame = False

	# --Draw all the components onto the screen--
	window.fill(Colors["white"])

	# Displaying the score in the top-left corner of the window
	text = font.render("Score: " + str(snake.score),1,Colors["black"])
	window.blit(text,(0,0))

	# Drawing a line to make the game and the score display distinct
	pygame.draw.line(window,Colors["black"],(0,font_size),(window_width,font_size),4)

	# Draw the snake
	for part in snake.parts:
		pygame.draw.rect(window,snake.color,(part[0],part[1],snake.size,snake.size))

	# Updates the screen with whatever's drawn so far
	pygame.display.update()

	if continueGame:
		# The snake should continously move in a single direction
		continueGame = snake.move()

	# Limit the clock to 30 frames per second
	clock.tick(30)

# Stops the game engine after the user has exited the main gameplay loop
pygame.quit()