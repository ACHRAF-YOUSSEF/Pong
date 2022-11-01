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

player1wins = 0
player2wins = 0

incremented = False

winner = ""

# functions
def game_reset() -> None:
    global score1 , score2, winner, incremented
    if win():
        draw_text(screen, winner, WIDTH//2, HEIGHT//2 - 50, 50, WHITE)
        draw_text(screen, "Press space to restart!", WIDTH//2, HEIGHT//2, 50, WHITE)     
        
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            ball.y_vel = ball.x_vel = 10
            ball.resetVel()
            player1.resetVel()
            player2.resetVel()
            player1.resetPos(40, HEIGHT//2 - 60)
            player2.resetPos(WIDTH - 65, HEIGHT//2 - 60)
            score1 = score2 = 0
            incremented = False
            winner = ""

def win() -> bool:
    global winner, player1wins, player2wins, incremented
    
    if score1 >= 11 and score1 - score2 >= 2:
        winner = 'player1 wins'
        ball.x_coord = WIDTH // 2
        ball.y_coord = HEIGHT // 2
        ball.x_vel = ball.y_vel = 0
        
        if not incremented:
            player1wins += 1
            incremented = True
            
        return True
        
    elif score2 >= 11 and score2 - score1 >= 2:
        winner = 'player2 wins'
        ball.x_coord = WIDTH // 2
        ball.y_coord = HEIGHT // 2
        ball.x_vel = ball.y_vel = 0
    
        if not incremented:
            player2wins += 1
            incremented = True
        
        return True   
        
    return False

def scoring() -> None:
    global score1, score2, score
    
    if ball.x_coord <= 0:
        ball.x_coord = WIDTH // 2
        ball.y_coord = HEIGHT // 2
        ball.x_vel = ball.default_vel
        ball.y_vel = ball.default_vel
        score2 += 1
        
    elif ball.x_coord >= WIDTH:
        ball.x_coord = WIDTH // 2
        ball.y_coord = HEIGHT // 2
        ball.x_vel = ball.default_vel
        ball.y_vel = ball.default_vel
        score1 += 1
        
    score = f"{score1}           {score2}"
    
def draw_text(screen: pygame.Surface, txt: str, x: int, y: int, police: int, color: tuple) -> None:
    txt_font = pygame.font.Font(None, police)
    txt = txt_font.render(txt, True, color)
    txt_rect = txt.get_rect()
    txt_rect.center =  (x, y)
    screen.blit(txt, txt_rect)
    
def drawNet() -> None:
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
        
        self.default_vel = 10
        self.l = [10, -10]
        
        self.x_vel = self.l[randint(0, 1)]
        self.y_vel = self.l[randint(0, 1)]      
        
    def ifCollision(self) -> None:
        if ball_rect.colliderect(player1_rect) or ball_rect.colliderect(player2_rect):
            if self.x_coord <= player1_rect.x + player1.width + 1:
                self.x_coord = player1_rect.right + 1
                self.x_vel *= -1
                self.x_vel += 0.5
                self.y_vel -= 0.5
            
            if self.x_coord >= player2_rect.x:
                self.x_coord = player2_rect.x - 1
                self.x_vel *= -1
                self.x_vel -= 0.5
                self.y_vel += 0.5
                
    def resetVel(self) -> None:
        self.x_vel = self.default_vel
        self.y_vel = self.default_vel
    
    def move(self) -> None:
        self.x_coord += self.x_vel
        self.y_coord += self.y_vel
        
        if self.y_coord >= HEIGHT or self.y_coord <= 0:
            self.y_vel *= -1

class Player:
    def __init__(self, x_coord: int, y_coord: int, color: tuple, width: int, height: int) -> None:
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color
        self.width = width
        self.height = height
        
        self.default_vel = 10
        self.y_vel = self.default_vel
        
    def resetVel(self) -> None:
        self.y_vel = self.default_vel
    
    def resetPos(self, x, y) -> None:
        self.x_coord = x
        self.y_coord = y
        
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
    
    # rects
    ball_rect = pygame.draw.circle(screen, ball.color, (ball.x_coord, ball.y_coord), ball.radius)
    player1_rect = pygame.draw.rect(screen, player1.color, (player1.x_coord, player1.y_coord, player1.width, player1.height))
    player2_rect = pygame.draw.rect(screen, player2.color, (player2.x_coord, player2.y_coord, player2.width, player2.height))
    
    ball.ifCollision()
    
    # update movements
    ball.move()
    player1.move((pygame.K_s, pygame.K_z, pygame.K_LSHIFT))
    player2.move((pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP))
    
    scoring()
    draw_text(screen, score, WIDTH//2, 30, 50, WHITE)
    draw_text(screen, f"wins : {player1wins}", 60, 30, 30, WHITE)
    draw_text(screen, f"wins : {player2wins}", WIDTH - 60 - player2.width, 30, 30, WHITE)
    
    game_reset()
    
    pygame.display.update()
    clock.tick(FPS)

# quit the game
pygame.quit()
quit()
