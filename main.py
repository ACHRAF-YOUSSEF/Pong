# imports
import pygame

# initializations
pygame.init()

# constants
DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080

WIDTH = 1024
HEIGHT = 720

SCALE = (DEFAULT_WIDTH/WIDTH) / (DEFAULT_HEIGHT/HEIGHT)

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# fps
FPS = 60

# screen + caption
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pong!")

# variables

# functions

# classes
class Ball:
    def __init__(self, x_coord: int, y_coord: int, color: tuple(), radius: int) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color
        self.radius = radius
        self.x_vel = 10
        self.y_vel = 10
        
    def move(self):
        self.x_coord += self.x_vel
        self.y_coord += self.y_vel
        
        if self.x_coord >= WIDTH or self.x_coord <= 0:
            self.x_vel *= -1
        
        if self.y_coord >= HEIGHT or self.y_coord <= 0:
            self.y_vel *= -1

# clock
clock = pygame.time.Clock()

# objects
ball = Ball(50, 50, RED, 15)

# main loop
run = True
while run:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.draw.circle(screen, ball.color, (ball.x_coord, ball.y_coord), ball.radius)
    ball.move()
    
    pygame.display.update()
    clock.tick(FPS)

# quit the game
pygame.quit()
quit()