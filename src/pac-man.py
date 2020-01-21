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
        pygame.Rect(159, 54, 84, 44),
        pygame.Rect(285, 0, 20, 98),
        pygame.Rect(347, 54, 84, 44),
        pygame.Rect(472, 54, 63, 44),
        pygame.Rect(54, 139, 63, 20),
        pygame.Rect(222, 139, 146, 20),
        pygame.Rect(472, 139, 63, 20),
        pygame.Rect(159, 139, 20, 146),
        pygame.Rect(411, 139, 20, 146),
        pygame.Rect(159, 202, 84, 20),
        pygame.Rect(285, 139, 20, 83),
        pygame.Rect(347, 202, 84, 20),
        pygame.Rect(159, 326, 20, 83),
        pygame.Rect(222, 390, 146, 20),
        pygame.Rect(411, 326, 20, 83),
        pygame.Rect(54, 453, 63, 20),
        pygame.Rect(159, 453, 84, 20),
        pygame.Rect(285, 390, 20, 83),
        pygame.Rect(347, 453, 84, 20),
        pygame.Rect(472, 453, 63, 20),
        pygame.Rect(0, 515, 54, 20),
        pygame.Rect(97, 453, 20, 83),
        pygame.Rect(472, 453, 20, 83),
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

    food_pos_x = 33
    food_pos_y = 33 
    food = pygame.draw.rect(screen, (255, 255, 255), (food_pos_x, food_pos_y, 6, 6))
    for i in range (1, 20):
        new_food_pos_x = food_pos_x + (27 * i)
        new_food = pygame.draw.rect(screen, (255, 255, 255), (new_food_pos_x, food_pos_y, 6, 6))
    for i in range (1, 20):
        new_food_pos_y = food_pos_y + (31 * i)
        new_food = pygame.draw.rect(screen, (255, 255, 255), (new_food_pos_x, new_food_pos_y, 6, 6))
    
    pygame.display.flip()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
            