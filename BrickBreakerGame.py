import pygame
import os
import math

PANEL_SPEED = 20
PANEL_COLOR = (230, 15, 20)
BALL_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0,0,0)


class Ball():
    def __init__(self, color = BALL_COLOR, radius = 3, **kwargs):
        self.color = color
        self.radius = radius
        self.x_position = kwargs.get('initial_x')
        self.y_position = kwargs.get('initial_y')


class Panel():
    def __init__(self, width = 30, height = 6, color = PANEL_COLOR,speed = PANEL_SPEED, **kwargs):
        self.x_position = kwargs.get('initial_x')
        self.y_position = kwargs.get('initial_y')
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self, direction):
        if direction == 'right':
            self.x_position += self.speed
            self.y_position = self.y_position
        else:
            self.x_position -= self.speed
            self.y_position = self.y_position            
    
    def has_collide(self):
        pass
            

class BrickBreakerGame():
    def __init__(self):
        self.game = pygame.init()
        self.display = pygame.display.set_mode((500, 500))
        self.ball = Ball(initial_x = int(self.display.get_width()/2), initial_y = self.display.get_height())
        self.panel = Panel(initial_x = int(self.display.get_width()/2), initial_y = self.display.get_height())
        self.playing = True
        self.game_over = False
        self.background = BACKGROUND_COLOR
        self.move_ticker = 0
        self.play()

    def draw_panel(self):
        pygame.draw.rect(self.display, self.panel.color, [self.panel.x_position, self.panel.y_position - self.panel.height,\
                                                          self.panel.width, self.panel.height])
    
    def draw_ball(self):
        pygame.draw.circle(self.display, self.ball.color, (int(self.ball.x_position), int(self.ball.y_position - self.ball.radius)), self.ball.radius)

    def play(self):
        while self.playing:
            self.display.fill(self.background)
            if  self.game_over:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                """    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.panel.move('right')
                        pygame.key.set_repeat(1, 10)
                    if event.key == pygame.K_LEFT:
                        self.panel.move('left')
                        pygame.key.set_repeat(1, 10)
                """
                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    if self.move_ticker == 0:
                        self.move_ticker = 10
                        self.panel.move('left')

                if keys[pygame.K_RIGHT]:
                    if self.move_ticker == 0: 
                        self.move_ticker = 10  
                        self.panel.move('right')

            if self.move_ticker > 0:
                self.move_ticker -= 1
            self.draw_ball()
            self.draw_panel()
            pygame.display.update()
if __name__ == '__main__':
    brick_breaker_game = BrickBreakerGame()
