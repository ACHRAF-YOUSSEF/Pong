#imPorts
import pygame
import random as rng
import time
import car_engine as ce


#initialise Pygame
pygame.init()

#constants
    #screen settings
DE_WIDTH = 1920
DE_HEIGHT = 1080
WIDTH = 1024
HEIGHT = 720
SCALE = (1920/WIDTH) / (1080/HEIGHT)

    #colors
black = (0,0,0)
white = (255, 255, 255)
red = (255,0,0)
green = (0, 255, 0)
blue = (0,0, 255)

    #Fps
fps = 60


#screen + window name
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("PING")

#fonctions

def draw_net():
    offset = 10
    for i in range(11):
        pygame.draw.rect(screen, white, ((WIDTH//2 - 2.5 ), i*(HEIGHT//16)+offset, 5, (HEIGHT//16)))
        offset += 20

def win(score1, score2):
    if score1 == 11 and score1 - score2 > 1:
        ce.draw_text(screen, "P1 wins", WIDTH//2 - 100, HEIGHT//2, 50, white)
        ball.y_vel = ball.x_vel = 0
        return True
    elif score2 == 11 and score2 - score1 > 1:
        ce.draw_text(screen, "P2 wins", WIDTH//2 +100, HEIGHT//2, 50, white)
        ball.y_vel = ball.x_vel = 0
        return True
    

def game_reset():
    global score_p1, score_p2
    if win(score_p1, score_p2) == True:
        ce.draw_text(screen, "Press space to restart", WIDTH//2, (HEIGHT//2) +70, 50, white)     
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            ball.y_vel = ball.x_vel = ball.start_vel
            score_p1 = score_p2 = 0
    
def scoring():
    global score_p2, score_p1, score_disp 
    
    if ball.x_coord <= 0:
        score_p2 +=1 
        ball.x_coord = (WIDTH//2)
        ball.y_coord = (HEIGHT//2)
        ball.x_vel *= -1
        
    if ball.x_coord >= WIDTH:
        score_p1 +=1
        ball.x_coord = (WIDTH//2)
        ball.y_coord = (HEIGHT//2)
        ball.x_vel *= -1
            
    score_disp = f"{score_p1}           {score_p2}"
        
#classes

class Ball:
    def __init__(self, x_coord: int, y_coord: int, color: tuple, radius: int) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color
        self.radius = radius
        
        self.start_vel = 10
        self.x_vel = 10
        self.y_vel = 10

    def move(self):
        self.x_coord += self.x_vel
        self.y_coord += self.y_vel
            
        if self.y_coord>= HEIGHT or self.y_coord <= 0:
            self.y_vel *= -1

    def collision(self) -> None:
        if ball_rect.colliderect(p1_rect) or ball_rect.colliderect(p2_rect):
            if self.x_coord <= p1_rect.x + p1.width + 1:
                self.x_coord = p1_rect.right +1
                self.x_vel *= -1
            if self.x_coord >= p2_rect.x:
                self.x_coord = p2_rect.x -1
                self.x_vel *= -1
    
class Player:
    def __init__(self, color: tuple, x_coord: int, y_coord:int, width: int, height:int) -> None:
        self.color = color
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.width = width
        self.height = height
        self.vel = 10
        
        self.current_Time = 0
        self.starter_time = pygame.time.get_ticks()
        
    def move(self, controls: tuple):
        keys = pygame.key.get_pressed()
        
        if keys[controls[0]] and self.y_coord < HEIGHT - self.height:
            self.y_coord += self.vel
        
        if keys[controls[1]] and self.y_coord > 0:
            self.y_coord -= self.vel
            
            
    
# variables
score_p1 = 0
score_p2 = 0   
score_disp = f"{score_p1}           {score_p2}"
    
#objects 

ball = Ball((WIDTH//2), (HEIGHT//2), white, 15)
p1 = Player(white, 50, (HEIGHT/2)-62, 25, 125)
p2 = Player(white, WIDTH - 75, (HEIGHT/2)-62, 25, 125)


#clock
clock = pygame.time.Clock()


#main game looP
run = True
while run:
    screen.fill(black)
    #game end
    win(score_p1, score_p2)  
    game_reset()
    draw_net()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False                         

    #rects
    ball_rect = pygame.draw.circle(screen, ball.color, (ball.x_coord, ball.y_coord), ball.radius)
    p1_rect = pygame.draw.rect(screen, p1.color, (p1.x_coord, p1.y_coord, p1.width, p1.height))
    p2_rect = pygame.draw.rect(screen, p2.color, (p2.x_coord, p2.y_coord, p2.width, p2.height))
    hitbox1 = pygame.draw.rect(screen, red, (p1.x_coord+4, p1.y_coord+6, p1.width, p1.height-12))
    hitbox2 = pygame.draw.rect(screen, red, (p2.x_coord-4, p2.y_coord+6, p2.width, p2.height-12))
    
    #movement
    ball.move()
    p1.move((pygame.K_d, pygame.K_a, pygame.K_LSHIFT))
    p2.move((pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP))
    ball.collision()
    
    #score update
    scoring()
    print()
    ce.draw_text(screen, score_disp, (WIDTH//2), 30, 50, white)   
    
    
    pygame.display.update()
    clock.tick(fps)
     
     
#self exPlanatory (quit game) 
pygame.quit()
quit()