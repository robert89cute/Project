import pygame
import os
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_w = 700 
screen_h = 600

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Flappy Spaceship')

#define font
font = pygame.font.SysFont('Showcard Gothic Regular', 60)
#define color
white = (255,255,255)
#define var
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_g = 180
pipe_f = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_f
score = 0
pass_pipe = False

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
         
high_score = 0
#load images
bg = pygame.image.load(os.path.join('Spaceflappy', 'back_image.png'))
ground = pygame.image.load(os.path.join('Spaceflappy/ground.png'))
button = pygame.image.load('Spaceflappy/restartbutton.png')
bg_sound = pygame.mixer.Sound('Spaceflappy/spaceinvaders.wav')
bg_sound.play(-1)
spaceship_sound = pygame.mixer.Sound('Spaceflappy/spaceship_sound.wav')
spaceship_sound.set_volume(0.1)

def display_high_score(screen, high_score):
    font = pygame.font.Font(None, 40)
    text = font.render("High Score: " + str(high_score), True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)


def draw_text(text, font, text_col, x, y):
     img = font.render(text, True, text_col)
     screen.blit(img, (x, y))

def reset_game():
     pipe_group.empty()
     flappy.rect.x = 100
     flappy.rect.y = int(screen_h/2)
     space_group.empty()
     space_group.add(flappy)
     score = 0
     return score

class Space(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(os.path.join('Spaceflappy', (f'players{num}.png')))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.vel = 0
        

    
    def update(self):
          
        if flying == True:
               #gravity
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 600:
                self.rect.y += int(self.vel)
        
        if game_over == False:
             
           #jump
           if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
               self.clicked = True
               self.vel = -10
               spaceship_sound.play()

           if pygame.mouse.get_pressed()[0] == 0:
               self.clicked = False


            

        #handle the animation

           self.counter += 1
           truster_cooldown = 5
   
           if self.counter > truster_cooldown:
               self.counter = 0
               self.index += 1
               if self.index >= len(self.images):
                   self.index = 0
           self.image = self.images[self.index]
        
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
            explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
            explosion_group.add(explosion)
            self.kill()

class Pipe(pygame.sprite.Sprite):
	def __init__(self, x, y, position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('Spaceflappy/pipe.png')
		self.rect = self.image.get_rect()
		#position 1 is from the top, -1 is from the bottom
		if position == 1:
			self.image = pygame.transform.flip(self.image, False, True)
			self.rect.bottomleft = [x, y - int(pipe_g / 2)]
		if position == -1:
			self.rect.topleft = [x, y + int(pipe_g / 2)]

	def update(self):
		self.rect.x -= scroll_speed
		if self.rect.right < 0:
			self.kill()
            


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(os.path.join('Spaceflappy', (f'exploxion{num}.png')))
            if size == 3:
                img = pygame.transform.scale(img,(160,160))
            #add the image to the list
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

        self.explosion_sound = pygame.mixer.Sound('Spaceflappy/Explosion.wav')
        self.explosion_sound.set_volume(1.5)
                
    def update(self):
        explosion_speed = 1
        #update explosion animation
        self.counter += 1

        if self.counter >- explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
                    
        #if the animation is complete,delet explosion
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()

            self.explosion_sound.play()

class Button():
     def __init__(self, x, y, image):
          self.image = image
          self.rect = self.image.get_rect()
          self.rect.topleft = (x,y)

     def draw(self):
          
          action = False
          #get mouse position
          position = pygame.mouse.get_pos()

          #check of mouse is over the button
          if self.rect.collidepoint(position):
               if pygame.mouse.get_pressed()[0] == 1:
                    action = True
                    
          #draw button
          screen.blit(self.image, (self.rect.x, self.rect.y))

          return action
    
pipe_group = pygame.sprite.Group()
space_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

flappy = Space(100, int(screen_h / 2))
space_group.add(flappy)

#create restart button instance
button = Button(screen_w // 2 -  50, screen_h // 2 - 100, button)

run = True 
while run:

    clock.tick(fps)
    #bg
    screen.blit(bg, (0,0))
    
    #spaceship
    
    pipe_group.draw(screen)

    #the ground
    screen.blit(ground, (ground_scroll, 250))
    space_group.draw(screen)
    space_group.update()
    explosion_group.draw(screen)
    explosion_group.update()

    #check the score
    if len(pipe_group) > 0 and len(space_group) > 0 :
         if space_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left\
         and space_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right\
         and pass_pipe == False:
            pass_pipe = True

         if pass_pipe == True:
            if space_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False

    draw_text(str(score), font, white, int(screen_w / 2), 40)

    
    #look for collision
    if pygame.sprite.groupcollide(space_group, pipe_group, False, False) or flappy.rect.top < 0:
         game_over = True
          
    #check if the spaceship hit the ground
    if flappy.rect.bottom >= 550:
        game_over = True
        flying = False

    if game_over == False and flying == True:
     #generate new pipes
     time_now = pygame.time.get_ticks()
     if time_now - last_pipe > pipe_f:
         pipe_h = random.randint(-100, 100) 
         btm_pipe = Pipe(screen_w, int(screen_h / 2) + pipe_h, -1)
         top_pipe = Pipe(screen_w, int(screen_h / 2) + pipe_h, 1)
         pipe_group.add(btm_pipe)
         pipe_group.add(top_pipe)
         last_pipe = time_now

     #bg and scroll
     ground_scroll -= scroll_speed
     if abs(ground_scroll) > 100:
        ground_scroll = 0
     pipe_group.update()
    
    #check for gameover and reset
    if game_over == True:
        if button.draw() == True:
            game_over = False
            score = reset_game()
        
        #update high score
        if score > high_score:
             high_score = score
             with open('score.txt', 'w') as file:
                  file.write(str(high_score))
    
    display_high_score(screen, high_score)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()