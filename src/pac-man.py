import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((736, 736))
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
        elif event.type == pygame.QUIT:
            pygame.quit()
    
    if pressed_left:
        pac.x -= 5
    if pressed_right:
        pac.x += 5
    if pressed_up:
        pac.y -= 5
    if pressed_down:
        pac.y += 5

    if pac.x > 736:
        pac.x = 0
        pac.y = pac.y
    
    rectangles_list = [
        pygame.Rect(67, 68, 80, 54),
        pygame.Rect(198, 68, 107, 54),
        pygame.Rect(355, 0, 27, 122),
        pygame.Rect(433, 68, 107, 54),
        pygame.Rect(589, 68, 81, 54),
        pygame.Rect(67, 173, 80, 27),
        pygame.Rect(278, 173, 182, 27),
        pygame.Rect(589, 173, 81, 27),
        pygame.Rect(198, 173, 27, 182),
        pygame.Rect(513, 173, 27, 182),
        pygame.Rect(198, 250.5, 107, 27),
        pygame.Rect(355, 173, 27, 104.5),
        pygame.Rect(433, 250.5, 107, 27),

    ]
    for rect in rectangles_list:
        pygame.draw.rect(screen, (0, 255, 50), rect)
    
    pygame.display.flip()
    