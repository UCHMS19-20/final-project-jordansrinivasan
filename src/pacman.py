import pygame, sys
from pygame.locals import *
import copy

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)
pygame.display.flip()

x_speed = 0
y_speed = 0



ghost_1_x = 33
ghost_1_y = 33
ghost_2_x = 555
ghost_2_y = 33
ghost_3_x = 33
ghost_3_y = 617
ghost_4_x = 555
ghost_4_y = 617

size = 20

class Coordinates:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

pac = Coordinates(screen.get_width()//2, screen.get_height()//2)
pressed_up = False
pressed_down = False
pressed_left = False
pressed_right = False

while True:
    ghost_1 = pygame.image.load("img/ghost1.png")
    ghost_2 = pygame.image.load("img/ghost2.png")
    ghost_3 = pygame.image.load("img/ghost3.jpg")
    ghost_4 = pygame.image.load("img/ghost4.png")

    ghost_1 = pygame.transform.scale(ghost_1, (size, size))
    ghost_2 = pygame.transform.scale(ghost_2, (size, size))
    ghost_3 = pygame.transform.scale(ghost_3, (size, size))
    ghost_4 = pygame.transform.scale(ghost_4, (size, size))

    bg = pygame.image.load("img/background.png")
    screen.blit(bg, (0,0))  

    screen.blit(ghost_1, (ghost_1_x, ghost_1_y))
    screen.blit(ghost_2, (ghost_2_x, ghost_2_y))
    screen.blit(ghost_3, (ghost_3_x, ghost_3_y))
    screen.blit(ghost_4, (ghost_4_x, ghost_4_y))

    pacman = pygame.draw.circle(screen, (255, 255, 0), (pac.x, pac.y), 6)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressed_up = True           
            elif event.key == pygame.K_DOWN:
                pressed_down = True
            elif event.key == pygame.K_LEFT:
                pressed_left = True
            elif event.key == pygame.K_RIGHT:
               pressed_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pressed_up = False
            elif event.key == pygame.K_DOWN:
                pressed_down = False
            elif event.key == pygame.K_LEFT:
                pressed_left = False
            elif event.key == pygame.K_RIGHT:
                pressed_right = False

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

    pac.x += x_speed
    pac.y += y_speed

    if pac.x > 650:
        pac.x = 0
        pac.y = pac.y
    elif pac.x < 0:
        pac.x = 650
        pac.y = pac.y

    walls = [
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
    for rect in walls:
        pygame.draw.rect(screen, (0, 255, 50), rect, -1)
        if pacman.colliderect(rect):
            if x_speed != 0:
                x_speed = -x_speed
            if y_speed != 0:
                y_speed = -y_speed
    pygame.display.flip()

    if ghost_1_x <= pac.x:
        ghost_1_x += 1
    if ghost_1_x >= pac.x:
        ghost_1_x -= 1
    if ghost_1_y <= pac.y:
        ghost_1_y += 1
    if ghost_1_y >= pac.y:
        ghost_1_y -= 1

    if ghost_2_x <= pac.x:
        ghost_2_x += 1
    if ghost_2_x >= pac.x:
        ghost_2_x -= 1
    if ghost_2_y <= pac.y:
        ghost_2_y += 1
    if ghost_2_y >= pac.y:
        ghost_2_y -= 1

    if ghost_3_x <= pac.x:
        ghost_3_x += 1
    if ghost_3_x >= pac.x:
        ghost_3_x -= 1
    if ghost_3_y <= pac.y:
        ghost_3_y += 1
    if ghost_3_y >= pac.y:
        ghost_3_y -= 1

    if ghost_4_x <= pac.x:
        ghost_4_x += 1
    if ghost_4_x >= pac.x:
        ghost_4_x -= 1
    if ghost_4_y <= pac.y:
        ghost_4_y += 1
    if ghost_4_y >= pac.y:
        ghost_4_y -= 1

    if pac.x <= ghost_1_x and pac.x >= ghost_1_x and pac.y <= ghost_1_y and pac.y >= ghost_1_y:
        sys.exit()
    if pac.x <= ghost_2_x and pac.x >= ghost_2_x and pac.y <= ghost_2_y and pac.y >= ghost_2_y:
        sys.exit()
    if pac.x <= ghost_3_x and pac.x >= ghost_3_x and pac.y <= ghost_3_y and pac.y >= ghost_3_y:
        sys.exit()  
    if pac.x <= ghost_4_x and pac.x >= ghost_4_x and pac.y <= ghost_4_y and pac.y >= ghost_4_y:
        sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
