import pygame, sys
from character import *

Surface = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)

class Pacman (Character):
    def __init__(self):
        self.radius = 6
        self.color = (255, 255, 0)
        self.speed = 2
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.score = 0
        self.lives = 3
        self.x = 303
        self.y = 616
        self.surface = pygame.draw.circle(Surface, self.color, (self.x, self.y), self.radius)
        self.direction = 0

    def reset (self):
        self.radius = 6 
        self.color = (255, 255, 0) 
        self.x = 303
        self.y = 616
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.surface = pygame.draw.circle(Surface, self.color, (self.x, self.y), self.radius)
        self.rect = self.surface.get_rect()
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
        if self.x <= 0:
            self.x = 588
        elif self.x >= 588:
            self.x = 0

    def getScoreSurface (self):
        return pygame.font.SysFont (None, 48). render ("Score: " + str (self.score), True, self.color)

    def getLivesSurface (self):
        surface = pygame.font.SysFont (None, 48). render ("Lives: ", True, self.color)
        x = 110
        for i in range (self.lives):
            pygame.draw.circle(self.surface, self.color, (x, 10))
            x += 25
        return surface

    def getWinningSurface (self):
        return pygame.font.SysFont (None, 72). render ("You Win!", True, self.color)

    def getLosingSurface (self):
        return pygame.font.SysFont (None, 72). render ("You Lose...", True, self.color)