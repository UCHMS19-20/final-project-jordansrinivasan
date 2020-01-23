import pygame, sys
from character import *

class Pacman (Character):
    def __init__(self):
        self.radius = 6
        self.color = (255, 255, 0)
        self.speed = 2
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.score = 0
        self.lives = 3
        self.rect = pygame.Surface.get_rect()
        self.rect.left = 303
        self.rect.top = 616
        self.surface = pygame.draw.circle(Surface, self.color, (self.rect.left, self.rect.top), self.radius)
        self.direction = 0

    def reset (self):
        self.radius = 6
        self.color = YELLOW 
        self.rect = pygame.Surface.get_rect()
        self.rect.left = 303
        self.rect.top = 616
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.surface = pygame.draw.circle(Surface, self.color, (self.rect.left, self.rect.top), self.radius)
        self.direction = 0

    def move (self, walls):
        if self.moveUp and self.canMove (0, walls):
            Character.move(self, 0)
        elif self.moveLeft and self.canMove (1, walls):
            Character.move (self, 1)
        elif self.moveDown and self.canMove (2, walls):
            Character.move (self, 2)
        elif self.moveDown and self.canMove (3, walls):
            Character.move (self, 3)

    def teleport (self):
        if self.rect.left <= 0:
            self.rect.left = 588
        elif self.rect.left >= 588:
            self.rect.left = 0

    def getScoreSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 48). render ("Score: " + str (self.score), True, YELLOW)

    def getLivesSurface (self):
        global YELLOW
        surface = pygame.font.SysFont (None, 48). render ("Lives: ", True, YELLOW)
        x = 110
        for i in range (self.lives):
            pygame.draw.circle(Pacman.surface, Pacman.color, (x, 10))
            x += 25
        return surface

    def getWinningSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 72). render ("You Win!", True, YELLOW)

    def getLosingSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 72). render ("You Lose...", True, YELLOW)