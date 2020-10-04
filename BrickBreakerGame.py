import pygame
import os
import math
import numpy as np

PANEL_SPEED = 20
BALL_SPEED = 1
PANEL_COLOR = (230, 15, 20)
BALL_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0,0,0)
WALL_COLOR = (240, 90, 30)


class Ball():
    def __init__(self, color = BALL_COLOR, radius = 3, speed = BALL_SPEED, **kwargs):
        self.color = color
        self.radius = radius
        self.x_position = kwargs.get('initial_x')
        self.y_position = kwargs.get('initial_y')
        self.speed = speed
        self.static = True

    def move(self, angle):
        self.x_position = self.x_position + round(math.cos(math.radians(angle) * self.speed))
        self.y_position = self.y_position + round(math.sin(math.radians(angle) * -(self.speed)))


class Wall():
    def __init__(self, x_position, y_position, width, height, angle, color = WALL_COLOR):
        self.x_position = x_position
        self.y_position = y_position
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color

    def __repr__(self):
        return "Wall\n" + \
                f"\tx_position: {self.x_position}\n" + \
                f"\ty_position: {self.y_position}\n" + \
                f"\theight: {self.height}\n" + \
                f"\twidth: {self.width}\n" + \
                f"\tangle: {self.angle}\n" + \
                f"\tcolor: {self.color}\n"


    

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
    

class BrickBreakerGame():
    def __init__(self):
        self.game = pygame.init()
        self.display = pygame.display.set_mode((500, 500))
        #self.panel = Panel(initial_x = int(self.display.get_width()/2), initial_y = self.display.get_height())
        self.playing = True
        self.game_over = False
        self.background = BACKGROUND_COLOR
        self.move_ticker = 0
        self.right_wall = Wall(self.display.get_width(), 0, 4, self.display.get_height(), 270)
        self.left_wall = Wall(0, 0, 4, self.display.get_height(), 90)
        self.top_wall = Wall(0, 0, self.display.get_width(), 4, 180)
        self.bottom_wall = Wall(0, self.display.get_height(), self.display.get_width(),  4, 0)
        self.ball = Ball(initial_x = int(self.display.get_width()/2), initial_y = self.display.get_height() - 3 - self.bottom_wall.height)
        self.objects_dict = {
                            'right_wall': self.right_wall,
                            'left_wall': self.left_wall,
                            'top_wall': self.top_wall,
                            'bottom_wall': self.bottom_wall
                             }       
        self.show_walls_info()
        self.clock = pygame.time.Clock()
        self.started = False
        self.angle = None
        self.play()

    def start_message(self):
        
        message = pygame.font.SysFont(None, 30).render('Pulsa ESPACIO para empezar.',\
														True, (250, 10, 10))
        self.display.blit(message, [int(self.display.get_width()/5), int(self.display.get_height()/3)])
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.static = False
                        self.angle = 60 #np.random.randint(35, 145)
                        print(f"este es el valor de angle: {self.angle}")
                        self.started = True
                        return


    def show_walls_info(self):
        print(self.right_wall)
        print(self.left_wall)
        print(self.top_wall)

    def draw_walls(self):
        pygame.draw.rect(self.display, self.right_wall.color, [self.right_wall.x_position - self.right_wall.width, self.right_wall.y_position,\
                                                                self.right_wall.width, self.right_wall.height])
        pygame.draw.rect(self.display, self.left_wall.color, [self.left_wall.x_position, self.left_wall.y_position,\
                                                                self.left_wall.width, self.left_wall.height])
        pygame.draw.rect(self.display, self.top_wall.color, [self.top_wall.x_position, self.top_wall.y_position ,\
                                                                self.top_wall.width, self.top_wall.height])
        pygame.draw.rect(self.display, self.bottom_wall.color, [self.bottom_wall.x_position, self.bottom_wall.y_position - self.bottom_wall.height ,\
                                                                self.bottom_wall.width, self.bottom_wall.height])                                                                  
    def draw_panel(self):
        pygame.draw.rect(self.display, self.panel.color, [self.panel.x_position, self.panel.y_position - self.panel.height,\
                                                          self.panel.width, self.panel.height])
    
    def draw_ball(self):
        pygame.draw.circle(self.display, self.ball.color, (int(self.ball.x_position), int(self.ball.y_position)), self.ball.radius)

    def check_collide(self):
        for key in self.objects_dict.keys():
            if self.ball.x_position == self.objects_dict[key].x_position and \
                self.ball.x_position == self.objects_dict[key].x_position:
                print(f'hubo una colision en {key}')

    def play(self):
        while self.playing:
            self.display.fill(self.background)
            self.draw_walls()     
            if not self.started:
                self.start_message()
            if self.game_over:
                pass
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                    
            if self.ball.static == False:
                self.ball.move(self.angle)


            """if event.key == pygame.K_RIGHT:
                        self.panel.move('right')
                        pygame.key.set_repeat(1, 10)
                    if event.key == pygame.K_LEFT:
                        self.panel.move('left')
                        pygame.key.set_repeat(1, 10)
                """
            """keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                if self.move_ticker == 0:
                    self.move_ticker = 10
                    self.panel.move('left')

            if keys[pygame.K_RIGHT]:
                if self.move_ticker == 0: 
                    self.move_ticker = 10  
                    self.panel.move('right')"""

            """if self.move_ticker > 0:
                self.move_ticker -= 1"""
            """if not self.ball.static:
                self.ball.move(self.angle)"""
            self.check_collide()
            self.draw_ball()
            #self.draw_panel()
            pygame.display.update()
            self.clock.tick(30)

if __name__ == '__main__':
    brick_breaker_game = BrickBreakerGame()
