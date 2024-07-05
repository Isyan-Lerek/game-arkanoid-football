from random import randint
from time import time as timer 
from pygame import *
import pygame

font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 36)


clock = pygame.time.Clock()

# backgournd music
mixer.init()
mixer.music.load('game_sound.ogg')
mixer.music.play()
mixer.music.set_volume(0.5)


ting_sound = mixer.Sound('ting.ogg')
ketukan_sound = mixer.Sound('ketukan.ogg')
ledakan_sound = mixer.Sound('ledakan.ogg')

img_bg = "lapangan.png"  
img_ball = "ball_1.png"  
img_hero = "messi.png"  
img_enemy = "cr7.png"  
img_peti = "peti.png"
img_bom = "bom.png"

score_p1 = 0 
score_p2 = 0 # ships destroyed
goal = 1  # how many ships need to be shot down to win
lost = 0  # ships missed
max_lost = 1 

game_over = False

 
class GameSprite(sprite.Sprite):
    # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)

        # every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        

        # every sprite must have the rect property – the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.new_y = 0

    # method drawing the character on the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# main player class
class Player_1(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_q] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_a] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
class Player_2(GameSprite):
    # method to control the sprite with arrow keys
    def update(self):
        keys = key.get_pressed()
        if keys[K_p] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_l] and self.rect.y < win_height - 80:
            self.rect.y += self.speed



win_width = 700
win_height = 500
display.set_caption("SHHHHHHHHhhh")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_bg), (win_width, win_height))

p_1_w = 50
p_1_h = 50
p_1_s = 3
p_1 = Player_1(img_hero, 25, 230, p_1_w, p_1_h, p_1_s)

p_2_w = 50
P_2_h = 50
p_2_s = 3
p_2 = Player_2(img_enemy, 620, 230, p_2_w, P_2_h, p_2_s)

b_w = 25
b_h = 25
b_s = 3
ball = GameSprite(img_ball, 60, 60, b_w, b_h, b_s)
dx = 3
dy = 3



while not game_over:
    window.blit(background, (0,0))
    
    ball.reset()
    p_1.reset()
    p_2.reset()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    ball.rect.x += dx
    ball.rect.y += dy
    
    if ball.rect.y > 500 or ball.rect.y < 0:
        dy *= -1
    

    if ball.rect.colliderect(p_1.rect) or ball.rect.colliderect(p_2.rect) :
        ting_sound.play()
    
    
    
    
    if ball.rect.colliderect(p_1.rect) or ball.rect.colliderect(p_2.rect) :
        dx *= -1
    if ball.rect.x <25 and (ball.rect.y >180 and ball.rect.y <280):
        score_p2 = score_p2 + 1
        ball.rect.x, ball.rect.y = 330,250
    text_p2 = font2.render("Score_player2: " + str(score_p2), 1, (255, 255, 255))
    window.blit(text_p2, (475, 35))

    if ball.rect.x >620 and (ball.rect.y >180 and ball.rect.y <280):
        score_p1 = score_p1 + 1
        ball.rect.x, ball.rect.y = 330,250
    text_p1 = font2.render("Score_player1: " + str(score_p1), 1, (255, 255, 255))
    window.blit(text_p1, (25, 35))
    
    
    ball.update()
    p_1.update()
    p_2.update()
    
    pygame.display.update()
    clock.tick(40)







































































