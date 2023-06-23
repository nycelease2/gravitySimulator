#!/bin/python3
import pygame

#variables
screen_WIDTH = 500
screen_HEIGHT = 600

class drawOnScreen:
    def __init__(self, screen):
        self.screen = screen

    def circle(self, x, y, color, radius):
        pygame.draw.circle(self.screen, color, (x,y), radius)

def pygameInit():#used to initialize pygame library
    pygame.init()
    screen = pygame.display.set_mode((screen_WIDTH, screen_HEIGHT))
    pygame.display.set_caption("Gravity Simulator")
    return screen

def gameloop(running):

    screen = pygameInit()
    screenUpdater = drawOnScreen(screen)

    while running == True:
        screenUpdater.circle(50, 60, (255,255,0), 50)#x, y, color and radius

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
if __name__ == "__main__":
    running = True
    gameloop(running)
