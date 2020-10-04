import pygame
import os
import time
import numpy as np 	
import random


# COLORES
SNAKE_COLOR = (5, 250, 10) 
BACKGROUND_COLOR = (0, 0, 0) 
FOOD_COLOR = (250, 10, 10) 


class Food():
	def __init__(self, coor, color = FOOD_COLOR, size = 10):
		self.food_x = coor[0]
		self.food_y = coor[1]
		self.color = color
		self.size = size

	def __repr__(self):
		return "Food: \n"+\
				f"\tfood_x: {self.food_x}\n" + \
				f"\tfood_y: {self.food_y}\n"



class Snake():
	def __init__(self, color = SNAKE_COLOR, speed = 10,  size = 10, **kwargs):
		self.color = color
		self.length = 1
		self.body = []
		self.x_position = kwargs.get('initial_x')
		self.y_position = kwargs.get('initial_y')
		self.x_distance = 0
		self.y_distance = 0
		self.speed = speed
		self.size = size

	def __repr__(self):
		return "Snake: \n"+\
				f"\tlength: {self.length}, type: {type(self.length)}\n" + \
				f"\tx_position: {self.x_position}, type: {type(self.x_position)}\n" + \
				f"\ty_position: {self.y_position}, type: {type(self.y_position)}\n" + \
				f"\tsize: {self.size}, type: {type(self.size)}\n"


	def feed(self):
		self.length += 1

	def has_collide(self, x_boundary, y_boundary):

		collide_itself = False
		for i in self.body[:-1]:
			if i ==  (self.x_position, self.y_position):
				collide_itself = True
				break

		return self.x_position <= 0 or self.x_position >= x_boundary or \
				self.y_position <= 0 or self.y_position >= y_boundary or \
				collide_itself

	def change_position(self):
		self.x_position = self.x_position + self.x_distance
		self.y_position = self.y_position + self.y_distance


class SnakeGame():
	def __init__(self):
		self.game = pygame.init()
		self.font_style = pygame.font.SysFont(None, 30)
		self.display = pygame.display.set_mode((500, 500))
		self.name = pygame.display.set_caption("Basa's Snake")
		self.clock = pygame.time.Clock()
		self.playing = True
		self.game_over = False
		self.possible_x_values = np.arange(0, self.display.get_width(), 10).tolist()
		self.possible_y_values = np.arange(0, self.display.get_height(), 10).tolist()
		self.color = BACKGROUND_COLOR
		self.food = Food(coor = self.set_random_coords())
		self.snake = Snake(initial_x = int(self.display.get_width()/2),\
							initial_y = int(self.display.get_height()/2))

		self.jugar()


	def lost_message(self):
		message = pygame.font.SysFont(None, 30).render('Has perdido. Pulsa ESPACIO para continuar.',\
														True, (250, 10, 10))
		self.display.blit(message, [int(self.display.get_width()/10), int(self.display.get_height()/3)])
		pygame.display.update()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						SnakeGame()
				if event.type == pygame.QUIT:
					quit()		

	def snake_desc(self):
		print(self.snake)

	def food_desc(self):
		print(self.food)

	def create_snake(self):
		for x in self.snake.body:
			pygame.draw.rect(self.display, self.snake.color, [x[0], x[1], self.snake.size, self.snake.size])



	def jugar(self):

		while(self.playing):

			if self.game_over == True:
				self.lost_message()

			self.display.fill(self.color)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT and self.snake.x_distance != - self.snake.speed:
						self.snake.x_distance = self.snake.speed
						self.snake.y_distance = 0
					elif event.key == pygame.K_LEFT and self.snake.x_distance != self.snake.speed:
						self.snake.x_distance = - self.snake.speed
						self.snake.y_distance = 0
					elif event.key == pygame.K_DOWN and self.snake.y_distance != - self.snake.speed:
						self.snake.x_distance = 0
						self.snake.y_distance = self.snake.speed
					elif event.key == pygame.K_UP and self.snake.y_distance != self.snake.speed:
						self.snake.x_distance = 0
						self.snake.y_distance = - self.snake.speed	

			# Dibujo comida
			pygame.draw.rect(self.display, self.food.color, [self.food.food_x, self.food.food_y,\
															 self.food.size, self.food.size])	

			self.snake.change_position()

			# Compruebo si la serpiente pasa por encima de la comida
			if self.snake.x_position == self.food.food_x and \
				self.snake.y_position == self.food.food_y:
					print('te has alimentado')
					self.snake.feed()
					self.food = Food(self.set_random_coords())
									
									
			snake_Head = (self.snake.x_position, self.snake.y_position)

			self.snake.body.append(snake_Head)

			if len(self.snake.body) > self.snake.length:
				del self.snake.body[0]

			# Dibujo snake
			self.create_snake()

			if self.snake.has_collide(self.display.get_width(), self.display.get_height()):
				self.game_over = True

			pygame.display.update()
			self.clock.tick(30)


	def set_random_coords(self):
		return (np.random.choice(self.possible_x_values), np.random.choice(self.possible_y_values))





if __name__ == '__main__':
	snake_game = SnakeGame()