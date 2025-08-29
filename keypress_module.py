#################project about to create a module for keyboard key press detection#####################

import pygame

def init():
    pygame.init()
    pygame.display.set_mode((400, 400))

def getkey(KeyName):
    ans = False
    for event in pygame.event.get():
        pass
    KeyInput = pygame.key.get_pressed()
    mykey = getattr(pygame, 'K_{}'.format(KeyName.upper()))
    if KeyInput[mykey]:
        ans = True
    pygame.display.update()
    return ans

print("keypress_module.py loaded")

   