import pygame
from pygame.locals import *
pygame.init()

from pellets import *
from character import * 
from pacman import *
from ghosts import *
from walls import * 

Surface = pygame.display.set_mode((588, 650), 0, 32)
pygame.display.set_caption("Pacman")

import random, copy

background = pygame.image.load("src/img/pacman.png").convert()
pacman = Pacman()
ghosts = [Ghost()]
walls = Walls.createList(Walls())
pellets_normal = Pellets.createListNormal (Pellets())
pellets_special = Pellets.createListSpecial (Pellets())
clock = pygame.time.Clock()

pygame.font.init()
myFont = pygame.font.SysFont('Arial', 30)

Surface.fill((0, 0, 0))
text = myFont.render('Welcome to Pacman! Click anywhere to play', False, (255, 255, 255))
screen.blit(text, (40, 40))
pygame.display.update()

keepGoing_game = True

while keepGoing_game:
    # Round loop
    keepGoing_round = True
    while keepGoing_round:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            # Quitting
            if event.type == QUIT:
                keepGoing_game = keepGoing_round = False
            # Arrow key down
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pacman.moveUp = True
                    pacman.moveLeft = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 0
                elif event.key == K_LEFT:
                    pacman.moveLeft = True
                    pacman.moveUp = pacman.moveDown = pacman.moveRight = False
                    pacman.direction = 1
                elif event.key == K_DOWN:
                    pacman.moveDown = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveRight = False
                    pacman.direction = 2
                elif event.key == K_RIGHT:
                    pacman.moveRight = True
                    pacman.moveUp = pacman.moveLeft = pacman.moveDown = False
                    pacman.direction = 3

            # Arrow key up
            elif event.type == KEYUP:
                pacman.moveUp = pacman.moveLeft = pacman.moveDown = pacman.moveRight = False

        # Move pacman rectangle
        pacman.move(walls)

        # Check if pacman must teleport to the other side
        pacman.teleport()

        # Animate and rotate pacman sprite
        pacman.getSurface()

        # Check if pacman has eaten any pellets and delete them
        Pellets.check (Pellets (), pellets_normal, pellets_special, pacman, ghosts)

        # Add a new ghost if necessary
        Ghost.add (Ghost (), ghosts)

        # Move ghosts
        for g in ghosts:
            g.move (walls, pacman)

        # If the mouse button gets pressed, the game screen appears
        if pygame.mouse.get_pressed == True:
            Surface.fill((0, 0, 0))
            Surface.blit(background, (0, 0))
            Surface.blit(pacman.getScoreSurface(), (10, 10))
            Surface.blit(pacman.getLivesSurface(), (WINDOWSIZE[0] - 200, 10))
        for p in pellets_small:
            Surface.blit(p_rect, (p[0], p[1]))
        for p in pellets_large: 
            Surface.blit(p_rect, (p[0], p[1]))
        for g in ghosts:
            Surface.blit(g.surface, g.rect)
            Surface.blit(pacman.surface, pacman.rect)
            pygame.display.update()

                # Check if pacman collided with a ghost
        for g in ghosts [:]:
            if pacman.rect.colliderect (g.rect): 
                keepGoing_round = False
                pacman.lives -= 1

                if len(pellets_normal) == 0 and len(pellets_special) == 0:
                    keepGoing_game = keepGoing_round = False

        for g in ghosts:
            g.reset()

        # End of game screen
        Surface.fill((0, 0, 0))
        surface_temp = None

    if pacman.lives == 0:       # Player loses
        surface_temp = pacman.getLosingSurface()

    elif len (pellets_normal) == 0 and len (pellets_special) == 0:     # Player wins
        surface_temp = pacman.getWinningSurface()

    if surface_temp != None:        # Player loses or wins (does not quit)
        rect_temp = surface_temp.get_rect()
        rect_temp.center = Surface.get_rect().center
        Surface.blit(surface_temp, rect_temp)
        pygame.display.update()