import pygame, sys
from Character import Character
from Constants import *

class Pacman (Character):
    def __init__(self):
        self.radius = 6
        self.color = YELLOW
        self.surface = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)
        self.speed = 2
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
        self.score = 0
        self.lives = 3
        self.rect = pygame.Surface.get_rect()
        self.rect.left = pygame.screen.get_width()/2
        self.rect.top = pygame.screen.get_height()/2
        self.direction = 0

    def reset (self):
        self.radius = 6
        self.color = YELLOW 
        self.surface = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)
        self.rect = pygame.Surface.get_rect()
        self.rect.left = pygame.screen.get_width()/2
        self.rect.top = pygame.screen.get_width()/2
        self.moveUp = self.moveDown = self.moveLeft = self.moveRight = False
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
        if self.rect.colliderect(pygame)

    def getScoreSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 48). render ("Score: " + str (self.score), True, YELLOW)

    def getLivesSurface (self):
        global YELLOW
        surface = pygame.font.SysFont (None, 48). render ("Lives: ", True, YELLOW)
        x = 110
        for i in range (self.lives):
            pygame.draw.circle(Pacman.surface, Pacman.color, ())
            x += 25
        return surface

    def getWinningSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 72). render ("You Win!", True, YELLOW)

    def getLosingSurface (self):
        global YELLOW
        return pygame.font.SysFont (None, 72). render ("You Lose...", True, YELLOW)
    
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
    for r in food:
        pellet = pygame.draw.rect(screen, (255, 255, 255), r)  
        if pacman.colliderect(r):
            food.remove(r)
        pygame.display.flip()

         
    
        

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            sys.exit()
            