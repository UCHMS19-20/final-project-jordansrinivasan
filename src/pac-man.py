import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((736, 736))
bg = pygame.image.load("src/img/pacman.png")
screen.blit(bg, (0,0))
pygame.display.flip()

class Coordinates:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

pac = Coordinates(screen.get_width()//2, screen.get_height()//2)

while True:
    pygame.draw.circle(screen, (255, 255, 0), (pac.x, pac.y), 20, 0)    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pac.y = pac.y + 10
            elif event.key == pygame.K_DOWN:
                pac.y = pac.y - 10
            elif event.key == pygame.K_LEFT:
                pac.x = pac.x - 10
            elif event.key == pygame.K_RIGHT:
                pac.x = pac.x + 10
        if event.type == pygame.QUIT:
            pygame.quit()
   