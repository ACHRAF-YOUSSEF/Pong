# imports
import pygame
from random import randint

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
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")

# variables
score1 = 0
score2 = 0
score = f"{score1}           {score2}"

# functions
def draw_text(screen: pygame.Surface, txt: str, x: int, y: int, police: int, color: tuple):
    txt_font = pygame.font.Font("Blippo Bold.ttf", police)
    txt = txt_font.render(txt, True, color)
    txt_rect = txt.get_rect()
    txt_rect.center =  (x, y)
    screen.blit(txt,txt_rect)
    
def drawNet():
    screen.fill(BLACK)
    offset = 10
    
    for _ in range(11):
        y = _ * (HEIGHT//16) + offset
        pygame.draw.rect(screen, WHITE, (WIDTH//2 - 2.5, y, 5, HEIGHT//16))
        offset += 20

# classes
class Ball:
    def __init__(self, x_coord: int, y_coord: int, color: tuple, radius: int) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color
        self.radius = radius
        
        self.x_vel = 10
        self.y_vel = 10
        
    def move(self) -> None:
        self.x_coord += self.x_vel
        self.y_coord += self.y_vel
        
        if self.x_coord >= WIDTH or self.x_coord <= 0:
            self.x_vel *= -1
            self.color = self.randomColor()
        
        if self.y_coord >= HEIGHT or self.y_coord <= 0:
            self.y_vel *= -1
            self.color = self.randomColor()
            
    def randomColor(self) -> tuple:
        return (randint(0, 255),randint(0, 255), randint(0, 255))

class Player:
    def __init__(self, x_coord: int, y_coord: int, color: tuple, width: int, height: int) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color
        self.width = width
        self.height = height
        
        self.default_vel = 5
        self.y_vel = self.default_vel
        # self.facingUp = True
        
        # self.timer = BasicTimer(3)
        
    def move(self, controls: tuple) -> None:
        keys = pygame.key.get_pressed()
        
        # if keys[controls[2]] and keys[controls[0]] or keys[controls[2]] and keys[controls[1]]:
        #     self.timer.do_Function()
        
        if keys[controls[0]] and self.y_coord < HEIGHT - self.height:
            self.y_coord += self.y_vel
            # self.facingUp = False
            
        if keys[controls[1]] and self.y_coord > 0:
            self.y_coord -= self.y_vel
            # self.facingUp = True
            
    # def dash(self, amount):
    #     if self.facingUp and self.y_coord > 0:
    #         self.y_coord -= self.y_vel * amount
            
    #     elif self.y_coord < HEIGHT - self.height:
    #         self.y_coord += self.y_vel * amount
        
    # def resetVel(self):
    #     self.y_vel = self.default_vel
    #     self.current_time = 0
    #     self.start_time = pygame.time.get_ticks() 

# class BasicTimer:
#     def __init__(self, time_to_wait = 2):
#         self.time_to_wait = time_to_wait
#         self.current_time = 0
#         self.start_time = pygame.time.get_ticks()
    
#     def do_Function(self):
#         self.current_time = pygame.time.get_ticks()
        
#         if self.current_time - self.start_time > self.time_to_wait * 1000:
#             player1.resetVel()
            
#         else:
#             player1.dash(1.5)

# clock
clock = pygame.time.Clock()

# objects
ball = Ball(WIDTH//2, HEIGHT//2, RED, 15)
player1 = Player(40, HEIGHT//2 - 60, WHITE, 25, 120)
player2 = Player(WIDTH - 65, HEIGHT//2 - 60, WHITE, 25, 120)

# main loop
run = True
while run:
    drawNet()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    ball_rect = pygame.draw.circle(screen, ball.color, (ball.x_coord, ball.y_coord), ball.radius)
    ball.move()
    
    player1_rect = pygame.draw.rect(screen, player1.color, (player1.x_coord, player1.y_coord, player1.width, player1.height))
    player2_rect = pygame.draw.rect(screen, player2.color, (player2.x_coord, player2.y_coord, player2.width, player2.height))
    
    # update movements
    player1.move((pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP))
    player2.move((pygame.K_s, pygame.K_z, pygame.K_LSHIFT))
    
    draw_text(screen, score, WIDTH//2, 30, 50, WHITE)
    
    pygame.display.update()
    clock.tick(FPS)

# quit the game
pygame.quit()
quit()