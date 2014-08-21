'''
Created on 11 Aug 2014

@author: mark
'''
import sys
import pygame
import math
import NetworkDefinition
from collections import deque

if __name__ == '__main__':
    entitylist = deque()
    
    # Setup pygame
    pygame.init()
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    background = 0, 0, 0
    
    # Set up the scope for the exec function
    environment = {}
    environment['pygame'] = globals()['pygame']
    environment['sys'] = globals()['sys']
    environment["entityList"] = entitylist
    environment['screen'] = screen
    environment['size'] = size

    # Setup semantic generator
    network = NetworkDefinition.GetNetwork()
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        network.StartInstanciation(entitylist, environment)
        #screen.fill(background)
        
        for entity in entitylist:
            #print "running " + entity.name
            for attribute in entity.attributes:
                #print "executing \n'\n" + attribute.script + "\n'"
                exec(attribute.script, environment)
                
        #raw_input("press key")
        
        pygame.display.flip()

