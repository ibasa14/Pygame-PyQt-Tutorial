import pygame
import os
import math
import numpy as np

PANEL_SPEED = 2
BALL_SPEED = 2
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
        self.x_position = self.x_position + round(math.cos(math.radians(angle)) * self.speed)
        self.y_position = self.y_position + round(math.sin(math.radians(angle)) * -(self.speed))


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
    def __init__(self, width = 50, height = 5, color = PANEL_COLOR,speed = PANEL_SPEED, **kwargs):
        self.x_position = kwargs.get('initial_x')
        self.y_position = kwargs.get('initial_y')
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

    def move(self, direction, display_width, wall_width):
        if direction == 'right':
            if display_width -  (self.x_position + self.width) >= self.speed:
                self.x_position += self.speed
            else:
                pass
        else:
            if self.x_position - self.speed >= 0:
                self.x_position -= self.speed
            else:
                pass            
    

class SelfPongGame():
    def __init__(self):
        self.game = pygame.init()
        self.display = pygame.display.set_mode((300, 300))
        self.name = pygame.display.set_caption("Basa's Self Pong")
        self.panel = Panel(initial_x = int(self.display.get_width()/2), initial_y = self.display.get_height())
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
        self.collide_counter = 0
        self.angle = None
        self.play()

    def start_message(self):
        
        message = pygame.font.SysFont(None, 25).render('Pulsa ESPACIO para empezar.',\
														True, (250, 10, 10))
        self.display.blit(message, [int(self.display.get_width()/8), int(self.display.get_height()/3)])
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #os.environ['PONG_ON'] = 'False'
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.ball.static = False
                        self.angle =  np.random.randint(35, 145)
                        self.started = True
                        return

    def game_over_message(self):
        
        message = pygame.font.SysFont(None, 25).render('¡Has perdido! Pulsa ESPACIO.',\
														True, (250, 10, 10))
        self.display.blit(message, [int(self.display.get_width()/8), int(self.display.get_height()/3)])
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #os.environ['PONG_ON'] = 'False'
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        SelfPongGame()



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
                                                            
    def draw_panel(self):
        pygame.draw.rect(self.display, self.panel.color, [self.panel.x_position, self.panel.y_position - self.panel.height,\
                                                          self.panel.width, self.panel.height])
    
    def draw_ball(self):
        pygame.draw.circle(self.display, self.ball.color, (int(self.ball.x_position), int(self.ball.y_position)), self.ball.radius)

    def normalize_angle(self):
        # primero normalizamos : 0 < angle < 360
        angle_normalized =  self.angle % 360

        # pasamos a positivo en caso de que sea necesario
        if angle_normalized < 0:
            angle_normalized += 360
        
        self.angle = angle_normalized



    def check_collide(self):
        if self.collide_counter > 0:
            self.collide_counter -= 1
        else:
            # pared izquierda
            if self.ball.x_position <= 0 and self.ball.y_position != 0:
                if self.angle >= 180:
                    self.angle = self.angle - 270
                else:
                    self.angle =  180 - self.angle
                self.collide_counter = 15
                self.normalize_angle()
                #print(f"El angulo nuevo es angle: {self.angle}")
                return

            #pared de arriba
            if self.ball.y_position <= 0:
                if self.angle >= 90:
                    self.angle = 360 - self.angle
                else:
                    self.angle = self.angle + 270
                self.collide_counter = 15
                self.normalize_angle()
                #print(f"El angulo nuevo es angle: {self.angle}")
                return

            #pared izquierda
            if self.ball.x_position >= self.display.get_width():
                if self.angle >= 0:
                    self.angle = 180 - self.angle
                else:
                    self.angle = 360 - self.angle + 180
                self.collide_counter = 15
                self.normalize_angle()
                #print(f"El angulo nuevo es angle: {self.angle}")
                return

            if self.ball.y_position >= self.display.get_height() - self.panel.height and \
                self.ball.x_position >= self.panel.x_position and \
                self.ball.x_position <= self.panel.x_position + self.panel.width:
                # si toca el panel le damos un valor aleatorio pero en funcion de donde sea el contacto
                # parte izquierda
                if self.ball.x_position <= self.panel.x_position + int(self.panel.width / 4):
                    self.angle = np.random.randint(150, 165)
                # parte central izquierda    
                elif self.ball.x_position <= self.panel.x_position +  int(self.panel.width / 2):
                    self.angle = np.random.randint(110, 150)

                # parte central derecha
                elif self.ball.x_position <= self.panel.x_position +  int(self.panel.width * 0.75):
                    self.angle = np.random.randint(30, 70)

                # parte derecha
                else:
                    self.angle = np.random.randint(30, 50)   
                                                             
                self.collide_counter = 3
                #print(f"El angulo nuevo es angle: {self.angle}")
                return

            if self.ball.y_position >= self.display.get_height():
                """if self.angle >= 270:
                    self.angle = 360 - self.angle
                else:
                    self.angle = 360 + self.angle
                self.collide_counter = 3
                self.normalize_angle()"""
                self.game_over = True
                print(f"Has perdido")
                return




    def play(self):
        while self.playing:
            self.display.fill(self.background)
            self.draw_walls()     
            if not self.started:
                self.start_message()
            if self.game_over:
                self.game_over_message()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #os.environ['PONG_ON'] = 'False'
                    quit()
                    
            keys=pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                pass

            else:

                if keys[pygame.K_RIGHT]:
                    self.panel.move('right', self.display.get_width(), self.right_wall.width)
                if keys[pygame.K_LEFT]:
                    self.panel.move('left', self.display.get_width(), self.right_wall.width)                  

                if self.ball.static == False:
                    self.ball.move(self.angle)

            self.draw_panel()
            self.check_collide()
            self.draw_ball()
            pygame.display.update()
            self.clock.tick(120)


if __name__ == '__main__':
    #os.environ['PONG_ON'] = 'True'
    snake_game = SelfPongGame()