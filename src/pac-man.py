import pygame, sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)
pygame.display.flip()

x_speed = 0
y_speed = 0

class Coordinates:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

free_to_move_left = False
free_to_move_right = False
free_to_move_up = False
free_to_move_down = False

pac = Coordinates(screen.get_width()//2, screen.get_height()//2)
pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False
while True:
    bg = pygame.image.load("src/img/pacman.png")
    screen.blit(bg, (0,0))
    pacman = pygame.draw.circle(screen, (255, 255, 0), (pac.x, pac.y), 6, 0)    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressed_up = True
                free_to_move_up = True            
            elif event.key == pygame.K_DOWN:
                pressed_down = True
                free_to_move_down = True
            elif event.key == pygame.K_LEFT:
                pressed_left = True
                free_to_move_left = True
            elif event.key == pygame.K_RIGHT:
               pressed_right = True
               free_to_move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False
                free_to_move_up = True
            elif event.key == pygame.K_DOWN:
                pressed_down = False
                free_to_move_down = True
            elif event.key == pygame.K_LEFT:
                pressed_left = False
                free_to_move_left = True
            elif event.key == pygame.K_RIGHT:
                pressed_right = False
                free_to_move_right = True
    if pressed_left:
        x_speed = -2
        y_speed = 0
    if pressed_right:
        x_speed = 2
        y_speed = 0
   
    if pressed_up:
        y_speed = -2
        x_speed = 0
    if pressed_down: 
        y_speed = 2
        x_speed = 0


    if pac.x > 650:
        pac.x = 0
        pac.y = pac.y
    elif pac.x < 0:
        pac.x = 650
        pac.y = pac.y

    rectangles_list = [
        pygame.Rect(54, 54, 63, 44),
        pygame.Rect(159, 54, 83, 44),
        pygame.Rect(285, 0, 20, 98),
        pygame.Rect(347, 54, 83, 44),
        pygame.Rect(472, 54, 63, 44),
        pygame.Rect(54, 139, 63, 20),
        pygame.Rect(222, 139, 146, 20),
        pygame.Rect(472, 139, 63, 20),
        pygame.Rect(159, 139, 20, 146),
        pygame.Rect(411, 139, 20, 146),
        pygame.Rect(159, 202, 83, 20),
        pygame.Rect(285, 139, 20, 83),
        pygame.Rect(347, 202, 83, 20),
        pygame.Rect(159, 326, 20, 83),
        pygame.Rect(222, 390, 146, 20),
        pygame.Rect(411, 326, 20, 83),
        pygame.Rect(54, 452, 63, 20),
        pygame.Rect(159, 452, 83, 20),
        pygame.Rect(285, 390, 20, 83),
        pygame.Rect(347, 452, 83, 20),
        pygame.Rect(472, 452, 63, 20),
        pygame.Rect(0, 515, 54, 20),
        pygame.Rect(97, 452, 20, 84),
        pygame.Rect(472, 452, 20, 84),
        pygame.Rect(534, 515, 54, 20),
        pygame.Rect(159, 515, 20, 83),
        pygame.Rect(222, 515, 146, 20),
        pygame.Rect(411, 515, 20, 83),
        pygame.Rect(54, 578, 189, 20),
        pygame.Rect(285, 515, 20, 83),
        pygame.Rect(347, 578, 189, 20),
        pygame.Rect(0, 0, 588, 12),
        pygame.Rect(0, 0, 12, 212),
        pygame.Rect(576, 0, 12, 212),
        pygame.Rect(0, 202, 117, 83),
        pygame.Rect(471, 202, 117, 83),
        pygame.Rect(0, 326, 117, 83),
        pygame.Rect(471, 326, 117, 83),
        pygame.Rect(0, 409, 12, 241),
        pygame.Rect(0, 638, 588, 12),
        pygame.Rect(576, 409, 12, 241),
        pygame.Rect(221, 264, 52, 11),
        pygame.Rect(316, 264, 52, 11),
        pygame.Rect(221, 264, 11, 83),
        pygame.Rect(357, 264, 11, 83),
        pygame.Rect(221, 336, 147, 11)
    ]
    
    for rect in rectangles_list:
        pygame.draw.rect(screen, (0, 255, 50), rect, -1)
        if pacman.colliderect(rect):
            if y_speed <= 0:
                free_to_move_up = False
            elif y_speed >= 0:
                free_to_move_down = False
            elif x_speed <= 0:
                free_to_move_left = False
            elif x_speed >= 0:
                free_to_move_right = False
    if free_to_move_left:
        pac.x += x_speed 
    elif free_to_move_right:
        pac.x -= x_speed
    elif free_to_move_up:
        pac.y -= y_speed
    elif free_to_move_down:
        pac.y += y_speed

    
    pygame.display.flip()

    food = [
        pygame.Rect(30, 30, 6, 6),
        pygame.Rect(51, 30, 6, 6),
        pygame.Rect(72, 30, 6, 6),
        pygame.Rect(93, 30, 6, 6),
        pygame.Rect(114, 30, 6, 6),
        pygame.Rect(135, 30, 6, 6), 
        pygame.Rect(156, 30, 6, 6),
        pygame.Rect(177, 30, 6, 6),
        pygame.Rect(198, 30, 6, 6),
        pygame.Rect(219, 30, 6, 6),
        pygame.Rect(240, 30, 6, 6),
        pygame.Rect(261, 30, 6, 6),
        pygame.Rect(323, 30, 6, 6),
        pygame.Rect(344, 30, 6, 6),
        pygame.Rect(365, 30, 6, 6),
        pygame.Rect(386, 30, 6, 6),
        pygame.Rect(407, 30, 6, 6),
        pygame.Rect(428, 30, 6, 6),
        pygame.Rect(449, 30, 6, 6),
        pygame.Rect(470, 30, 6, 6),
        pygame.Rect(491, 30, 6, 6),
        pygame.Rect(512, 30, 6, 6),
        pygame.Rect(533, 30, 6, 6),
        pygame.Rect(554, 30, 6, 6),
        pygame.Rect(30, 52, 6, 6),
        pygame.Rect(30, 73, 6, 6),
        pygame.Rect(30, 95, 6, 6),
        pygame.Rect(30, 116, 6, 6),
        pygame.Rect(30, 138, 6, 6),
        pygame.Rect(30, 159, 6, 6),
        pygame.Rect(30, 180, 6, 6),
        pygame.Rect(135, 52, 6, 6),
        pygame.Rect(135, 73, 6, 6),
        pygame.Rect(135, 95, 6, 6),
        pygame.Rect(135, 116, 6, 6),
        pygame.Rect(135, 138, 6, 6),
        pygame.Rect(135, 159, 6, 6),
        pygame.Rect(135, 180, 6, 6),
        pygame.Rect(135, 201, 6, 6),
        pygame.Rect(135, 221, 6, 6),
        pygame.Rect(135, 241, 6, 6),
        pygame.Rect(135, 262, 6, 6),
        pygame.Rect(135, 282, 6, 6),
        pygame.Rect(135, 302, 6, 6),
        pygame.Rect(135, 323, 6, 6),
        pygame.Rect(135, 344, 6, 6),
        pygame.Rect(135, 365, 6, 6),
        pygame.Rect(135, 386, 6, 6),
        pygame.Rect(135, 407, 6, 6),
        pygame.Rect(135, 428, 6, 6),
        pygame.Rect(135, 449, 6, 6),
        pygame.Rect(135, 470, 6, 6),
        pygame.Rect(135, 490, 6, 6),
        pygame.Rect(135, 511, 6, 6),
        pygame.Rect(135, 532, 6, 6),
        pygame.Rect(135, 553, 6, 6),
        pygame.Rect(261, 52, 6, 6),
        pygame.Rect(261, 73, 6, 6),
        pygame.Rect(261, 95, 6, 6),
        pygame.Rect(261, 116, 6, 6),
        pygame.Rect(323, 52, 6, 6),
        pygame.Rect(323, 73, 6, 6),
        pygame.Rect(323, 95, 6, 6),
        pygame.Rect(323, 116, 6, 6),
        pygame.Rect(449, 52, 6, 6),
        pygame.Rect(449, 73, 6, 6),
        pygame.Rect(449, 95, 6, 6),
        pygame.Rect(449, 116, 6, 6),
        pygame.Rect(449, 138, 6, 6),
        pygame.Rect(449, 159, 6, 6),
        pygame.Rect(449, 180, 6, 6),
        pygame.Rect(449, 201, 6, 6),
        pygame.Rect(449, 221, 6, 6),
        pygame.Rect(449, 241, 6, 6),
        pygame.Rect(449, 262, 6, 6),
        pygame.Rect(449, 282, 6, 6),
        pygame.Rect(449, 302, 6, 6),
        pygame.Rect(449, 323, 6, 6),
        pygame.Rect(449, 344, 6, 6),
        pygame.Rect(449, 365, 6, 6),
        pygame.Rect(449, 386, 6, 6),
        pygame.Rect(449, 407, 6, 6),
        pygame.Rect(449, 428, 6, 6),
        pygame.Rect(449, 449, 6, 6),
        pygame.Rect(449, 470, 6, 6),
        pygame.Rect(449, 490, 6, 6),
        pygame.Rect(449, 511, 6, 6),
        pygame.Rect(449, 532, 6, 6),
        pygame.Rect(449, 553, 6, 6),
        pygame.Rect(554, 52, 6, 6),
        pygame.Rect(554, 73, 6, 6),
        pygame.Rect(554, 95, 6, 6),
        pygame.Rect(554, 116, 6, 6),
        pygame.Rect(554, 138, 6, 6),
        pygame.Rect(554, 159, 6, 6),
        pygame.Rect(554, 180, 6, 6),
        pygame.Rect(51, 116, 6, 6),
        pygame.Rect(72, 116, 6, 6),
        pygame.Rect(93, 116, 6, 6),
        pygame.Rect(114, 116, 6, 6), 
        pygame.Rect(156, 116, 6, 6),
        pygame.Rect(177, 116, 6, 6),
        pygame.Rect(198, 116, 6, 6),
        pygame.Rect(219, 116, 6, 6),
        pygame.Rect(240, 116, 6, 6),
        pygame.Rect(261, 116, 6, 6),
        pygame.Rect(281, 116, 6, 6),
        pygame.Rect(303, 116, 6, 6),
        pygame.Rect(344, 116, 6, 6),
        pygame.Rect(365, 116, 6, 6),
        pygame.Rect(386, 116, 6, 6),
        pygame.Rect(407, 116, 6, 6),
        pygame.Rect(428, 116, 6, 6),
        pygame.Rect(470, 116, 6, 6),
        pygame.Rect(491, 116, 6, 6),
        pygame.Rect(512, 116, 6, 6),
        pygame.Rect(533, 116, 6, 6),
        pygame.Rect(198, 138, 6, 6),
        pygame.Rect(198, 159, 6, 6),
        pygame.Rect(198, 180, 6, 6),
        pygame.Rect(386, 138, 6, 6),
        pygame.Rect(386, 159, 6, 6),
        pygame.Rect(386, 180, 6, 6),
        pygame.Rect(51, 180, 6, 6),
        pygame.Rect(72, 180, 6, 6),
        pygame.Rect(93, 180, 6, 6),
        pygame.Rect(114, 180, 6, 6),
        pygame.Rect(219, 180, 6, 6),
        pygame.Rect(240, 180, 6, 6),
        pygame.Rect(261, 180, 6, 6),
        pygame.Rect(323, 180, 6, 6),
        pygame.Rect(344, 180, 6, 6),
        pygame.Rect(365, 180, 6, 6),
        pygame.Rect(470, 180, 6, 6),
        pygame.Rect(491, 180, 6, 6),
        pygame.Rect(512, 180, 6, 6),
        pygame.Rect(533, 180, 6, 6),
        pygame.Rect(261, 201, 6, 6),
        pygame.Rect(261, 221, 6, 6),
        pygame.Rect(261, 241, 6, 6),
        pygame.Rect(323, 201, 6, 6),
        pygame.Rect(323, 221, 6, 6),
        pygame.Rect(323, 241, 6, 6),
        pygame.Rect(198, 241, 6, 6),
        pygame.Rect(219, 241, 6, 6),
        pygame.Rect(240, 241, 6, 6),
        pygame.Rect(281, 241, 6, 6),
        pygame.Rect(303, 241, 6, 6),
        pygame.Rect(344, 241, 6, 6),
        pygame.Rect(365, 241, 6, 6),
        pygame.Rect(386, 241, 6, 6),
        pygame.Rect(198, 262, 6, 6),
        pygame.Rect(198, 282, 6, 6),
        pygame.Rect(198, 302, 6, 6),
        pygame.Rect(198, 323, 6, 6),
        pygame.Rect(198, 344, 6, 6),
        pygame.Rect(198, 365, 6, 6),
        pygame.Rect(198, 386, 6, 6),
        pygame.Rect(198, 407, 6, 6),
        pygame.Rect(198, 428, 6, 6),
        pygame.Rect(386, 262, 6, 6),
        pygame.Rect(386, 282, 6, 6),
        pygame.Rect(386, 302, 6, 6),
        pygame.Rect(386, 323, 6, 6),
        pygame.Rect(386, 344, 6, 6),
        pygame.Rect(386, 365, 6, 6),
        pygame.Rect(386, 386, 6, 6),
        pygame.Rect(386, 407, 6, 6),
        pygame.Rect(386, 428, 6, 6),
        pygame.Rect(9, 302, 6, 6),
        pygame.Rect(30, 302, 6, 6), 
        pygame.Rect(51, 302, 6, 6), 
        pygame.Rect(72, 302, 6, 6),  
        pygame.Rect(93, 302, 6, 6),  
        pygame.Rect(114, 302, 6, 6),
        pygame.Rect(156, 302, 6, 6),
        pygame.Rect(177, 302, 6, 6),
        pygame.Rect(407, 302, 6, 6),
        pygame.Rect(428, 302, 6, 6),
        pygame.Rect(470, 302, 6, 6),
        pygame.Rect(491, 302, 6, 6),
        pygame.Rect(512, 302, 6, 6),
        pygame.Rect(533, 302, 6, 6),
        pygame.Rect(554, 302, 6, 6),
        pygame.Rect(575, 302, 6, 6),
        pygame.Rect(219, 365, 6, 6),
        pygame.Rect(240, 365, 6, 6),
        pygame.Rect(261, 365, 6, 6),
        pygame.Rect(281, 365, 6, 6),
        pygame.Rect(303, 365, 6, 6),
        pygame.Rect(323, 365, 6, 6),
        pygame.Rect(344, 365, 6, 6),
        pygame.Rect(365, 365, 6, 6),
        pygame.Rect(30, 428, 6, 6),
        pygame.Rect(51, 428, 6, 6),
        pygame.Rect(72, 428, 6, 6),
        pygame.Rect(93, 428, 6, 6),
        pygame.Rect(114, 428, 6, 6),
        pygame.Rect(156, 428, 6, 6),
        pygame.Rect(177, 428, 6, 6),
        pygame.Rect(219, 428, 6, 6),
        pygame.Rect(240, 428, 6, 6),
        pygame.Rect(261, 428, 6, 6),
        pygame.Rect(323, 428, 6, 6),
        pygame.Rect(344, 428, 6, 6),
        pygame.Rect(365, 428, 6, 6),
        pygame.Rect(407, 428, 6, 6),
        pygame.Rect(428, 428, 6, 6),
        pygame.Rect(470, 428, 6, 6),
        pygame.Rect(491, 428, 6, 6),
        pygame.Rect(512, 428, 6, 6),
        pygame.Rect(533, 428, 6, 6),
        pygame.Rect(554, 428, 6, 6),
        pygame.Rect(30, 449, 6, 6),
        pygame.Rect(30, 470, 6, 6),
        pygame.Rect(30, 490, 6, 6),
        pygame.Rect(261, 449, 6, 6),
        pygame.Rect(261, 470, 6, 6),
        pygame.Rect(261, 490, 6, 6),
        pygame.Rect(323, 449, 6, 6),
        pygame.Rect(323, 470, 6, 6),
        pygame.Rect(323, 490, 6, 6),
        pygame.Rect(554, 449, 6, 6),
        pygame.Rect(554, 470, 6, 6),
        pygame.Rect(554, 490, 6, 6),
        pygame.Rect(51, 490, 6, 6),
        pygame.Rect(72, 490, 6, 6),
        pygame.Rect(156, 490, 6, 6),
        pygame.Rect(177, 490, 6, 6),
        pygame.Rect(198, 490, 6, 6),
        pygame.Rect(219, 490, 6, 6),
        pygame.Rect(240, 490, 6, 6),
        pygame.Rect(281, 490, 6, 6),
        pygame.Rect(303, 490, 6, 6),
        pygame.Rect(344, 490, 6, 6),
        pygame.Rect(365, 490, 6, 6),
        pygame.Rect(386, 490, 6, 6),
        pygame.Rect(407, 490, 6, 6),
        pygame.Rect(428, 490, 6, 6),
        pygame.Rect(512, 490, 6, 6),
        pygame.Rect(533, 490, 6, 6),
        pygame.Rect(72, 511, 6, 6),
        pygame.Rect(72, 532, 6, 6),
        pygame.Rect(72, 553, 6, 6),
        pygame.Rect(198, 511, 6, 6),
        pygame.Rect(198, 532, 6, 6),
        pygame.Rect(198, 553, 6, 6),
        pygame.Rect(386, 511, 6, 6),
        pygame.Rect(386, 532, 6, 6),
        pygame.Rect(386, 553, 6, 6),
        pygame.Rect(512, 511, 6, 6),
        pygame.Rect(512, 532, 6, 6),
        pygame.Rect(512, 553, 6, 6),
        pygame.Rect(30, 553, 6, 6),
        pygame.Rect(51, 553, 6, 6),
        pygame.Rect(93, 553, 6, 6),
        pygame.Rect(114, 553, 6, 6),
        pygame.Rect(219, 553, 6, 6),
        pygame.Rect(240, 553, 6, 6),
        pygame.Rect(261, 553, 6, 6),
        pygame.Rect(323, 553, 6, 6),
        pygame.Rect(344, 553, 6, 6),
        pygame.Rect(365, 553, 6, 6),
        pygame.Rect(470, 553, 6, 6),
        pygame.Rect(491, 553, 6, 6),
        pygame.Rect(533, 553, 6, 6),
        pygame.Rect(554, 553, 6, 6),
        pygame.Rect(30, 574, 6, 6),
        pygame.Rect(30, 595, 6, 6),
        pygame.Rect(30, 616, 6, 6),
        pygame.Rect(261, 574, 6, 6),
        pygame.Rect(261, 595, 6, 6),
        pygame.Rect(261, 616, 6, 6),
        pygame.Rect(323, 574, 6, 6),
        pygame.Rect(323, 595, 6, 6),
        pygame.Rect(323, 616, 6, 6),
        pygame.Rect(554, 574, 6, 6),
        pygame.Rect(554, 595, 6, 6),
        pygame.Rect(554, 616, 6, 6),
        pygame.Rect(51, 616, 6, 6),
        pygame.Rect(72, 616, 6, 6),
        pygame.Rect(93, 616, 6, 6),
        pygame.Rect(114, 616, 6, 6),
        pygame.Rect(135, 616, 6, 6),
        pygame.Rect(156, 616, 6, 6),
        pygame.Rect(177, 616, 6, 6),
        pygame.Rect(198, 616, 6, 6),
        pygame.Rect(219, 616, 6, 6),
        pygame.Rect(240, 616, 6, 6),
        pygame.Rect(281, 616, 6, 6),
        pygame.Rect(303, 616, 6, 6),
        pygame.Rect(344, 616, 6, 6),
        pygame.Rect(365, 616, 6, 6),
        pygame.Rect(386, 616, 6, 6),
        pygame.Rect(407, 616, 6, 6),
        pygame.Rect(428, 616, 6, 6),
        pygame.Rect(449, 616, 6, 6),
        pygame.Rect(470, 616, 6, 6),
        pygame.Rect(491, 616, 6, 6),
        pygame.Rect(512, 616, 6, 6),
        pygame.Rect(533, 616, 6, 6)
    ]
    for rect in food:
        pygame.draw.rect(screen, (255, 255, 255), rect)  
        pygame.display.flip()
    if pacman.colliderect(rect):
        food.remove(rect)
        screen.blit (screen, (rect.x, rect.y))   
    
        

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
            