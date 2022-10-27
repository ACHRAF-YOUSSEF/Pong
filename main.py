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
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# screen + caption
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pong!")

# variables

# main loop
run = True
while run:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()

# quit the game
pygame.quit()
quit()