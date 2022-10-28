import pygame

pygame.init()

def draw_text(screen, txt, x, y, police, color):
    txt_font = pygame.font.Font("Blippo Bold.ttf", police)
    txt = txt_font.render(txt, True, color)
    txt_rect = txt.get_rect()
    txt_rect.center =  (x, y)
    screen.blit(txt,txt_rect)
    
class BasicTimer:
    def __init__(self, time_to_wait = 2):
        self.time_to_wait = time_to_wait
        self.current_time = 0
        self.start_time = pygame.time.get_ticks()
    
    def do_Function(self, func1, func2):
        self.current_time = pygame.time.get_ticks()
        
        if self.current_time - self.start_time < self.time_to_wait:
            try:
                func1[0](func2[1])  
            except:
                print("jesus there ain't no paramaters here")        
        else:
            try:
                func2[0](func1[1])
            except:
                print('hallelujah')