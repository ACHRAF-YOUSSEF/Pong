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
x_coord = 50
y_coord = 50
x_vel = 8
y_vel = 8
color = RED


# clock
clock = pygame.time.Clock()

# main loop
run = True
while run:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if x_coord >= WIDTH or x_coord <= 0:
        x_vel *= -1
        
    if y_coord >= HEIGHT or y_coord <= 0:
        y_vel *= -1
            
    pygame.draw.circle(screen, color, (x_coord, y_coord), 15)
    
    x_coord += x_vel
    y_coord += y_vel
    
    pygame.display.update()
    clock.tick(FPS)

# quit the game
pygame.quit()
quit()