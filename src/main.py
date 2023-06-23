#!/bin/python3
import pygame

#variables
screen_WIDTH = 500
screen_HEIGHT = 600

def drawOnScreen(screen):
    screen.fill((255,255,255))

    pygame.display.update()

def pygameInit():#used to initialize pygame library
    pygame.init()
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
    pygame.display.set_caption("Gravity Simulator")
    return screen

def gameloop(running):
    screen = pygameInit()
    while running == True:
        drawOnScreen(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    running = True
    gameloop(running)
