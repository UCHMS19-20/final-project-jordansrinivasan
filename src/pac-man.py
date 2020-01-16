import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)
pygame.display.flip()

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
    bg = pygame.image.load("src/img/pacman.png")
    screen.blit(bg, (0,0))
    pygame.draw.circle(screen, (255, 255, 0), (pac.x, pac.y), 10, 0)    
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
        pac.x -= 5
    if pressed_right:
        pac.x += 5
    if pressed_up:
        pac.y -= 5
    if pressed_down:
        pac.y += 5

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
        pygame.Rect(410.5, 139, 20, 146),
        pygame.Rect(198, 250.5, 107, 27),
        pygame.Rect(355, 173, 27, 104.5),
        pygame.Rect(433, 250.5, 107, 27),

    ]
    for rect in rectangles_list:
        pygame.draw.rect(screen, (0, 255, 50), rect)
    
    pygame.display.flip()
    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
    