import pygame
from pygame.locals import *
import sys
import os




def main():
    pygame.init()
    screen = pygame.display.set_mode((300,200))
    
    os.environ["SDL_VIDEODRIVER"] = "dummy"

    pygame.display.set_caption("GAME")
     

    while (1):
        screen.file((0,0,0))
        pygame.draw.ellipse(screen,(0.100,0),(50,50,200,100),5)
        pygame.display.upate()


        for evet in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

