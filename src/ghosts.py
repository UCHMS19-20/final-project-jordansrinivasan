import pygame
import copy
from character import *

Surface = pygame.display.set_mode((588, 650), pygame.FULLSCREEN)

class Ghost(Character):

    TIME = 1800
    time = TIME

    def __init__ (self):
        self.color = (255, 255, 0)
        self.rect = self.surface.get_rect()
        self.rect_left = 241
        self.rect_top = 221
        self.surface = pygame.draw.circle (Surface, self.color, (self.rect_left, self.rect_top))
        self.speed = 2
        self.course = [0] * (50 / self.speed)

    # resets ghost's position
    def reset(self):
        self.rect_left = 315
        self.rect_top = 275
        self.course = [0] * (50 / self.speed)

    def add(self, ghosts):
        Ghost.time -= 1
        if len(ghosts) == 0:
            if Ghost.time > (Ghost.TIME / 10.0):
                Ghost.time = (Ghost.TIME / 10.0)
            if Ghost.time <= 0:
                ghosts.append(Ghost())
                Ghost.time = Ghost.TIME


    # determines how far ghost can move before colliding with wall
    def canMove_distance (self, direction, walls):
        test = copy.deepcopy (self)
        counter = 0
        while True:
            if not Character.canMove (test, direction, walls):
                break
            Character.move (test, direction)
            counter += 1
        return counter

    # Uses AI to move ghost closer to Pacman
    def move (self, walls, pacman):
        if len (self.course) > 0:
            if self.canMove (self.course [0], walls) or self.rect.colliderect (pygame.Rect((268, 248), (112, 64))):
                Character.move (self, self.course [0])
                del self.course [0]
            else:
                self.course = []
        else:
            xDistance = pacman.rect.left - self.rect_left
            yDistance = pacman.rect.top - self.rect_top
            choices = [-1, -1, -1, -1]

            # Checks to see which directions to move in order to be closer to Pacman, as well as the order of these directions.
            if abs (xDistance) > abs (yDistance):     
                if xDistance > 0:       
                    choices [0] = 3
                    choices [3] = 1
                elif xDistance < 0:     
                    choices [0] = 1
                    choices [3] = 3
                if yDistance > 0:        
                    choices [1] = 2
                    choices [2] = 0
                elif yDistance < 0:     
                    choices [1] = 0
                    choices [2] = 2
                else:

                    if self.canMove_distance (2, walls) < self.canMove_distance (0, walls):     
                        choices [1] = 2
                        choices [2] = 0
                    elif self.canMove_distance (0, walls) < self.canMove_distance (2, walls):       
                        choices [1] = 0
                        choices [2] = 2      
            elif abs (yDistance) >= abs (xDistance):        
                if yDistance > 0:       
                    choices [0] = 2
                    choices [3] = 0
                elif yDistance < 0:     
                    choices [0] = 0
                    choices [3] = 2   
                if xDistance > 0:       
                    choices [1] = 3
                    choices [2] = 1
                elif xDistance < 0:     
                    choices [1] = 1
                    choices [2] = 3
                else:       # xDistance == 0
                    if self.canMove_distance (3, walls) < self.canMove_distance (1, walls):    
                        choices [1] = 3
                        choices [2] = 1
                    elif self.canMove_distance (1, walls) < self.canMove_distance (3, walls):       
                        choices [1] = 1
                        choices [2] = 3

            choices_original = choices [:]
            for i, x in enumerate (choices [:]):
                if x == -1 or (not Character.canMove (self, x, walls)):
                    del choices [choices.index (x)]

            if len (choices) > 0:
                Character.move (self, choices [0])
                if choices_original.index (choices [0]) >= 2:       # if move is 3rd or 4th choice
                    for i in range (int (90)):
                        self.course.append (choices [0])