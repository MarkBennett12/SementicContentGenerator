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
    windowSize = width, height = 320, 240
    screen = pygame.display.set_mode(windowSize)
    background = 0, 0, 0
    
    # Set up the scope for the exec function
    globalEnvironment = {}
    globalEnvironment['pygame'] = globals()['pygame']
    globalEnvironment['sys'] = globals()['sys']
    globalEnvironment["entityList"] = entitylist
    globalEnvironment['screen'] = screen
    globalEnvironment['windowSize'] = windowSize

    # Setup semantic generator
    network = NetworkDefinition.GetNetwork(globalEnvironment)
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        network.StartInstanciation(entitylist)
        #screen.fill(background)
        print "RUNNING ============================================================================"
        
        for entity in entitylist:
            print "running " + entity.name
            for attribute in entity.attributes:
                #print "In demo.py, entity: " + entity.name + ", environment: " + str(entity.environment)
                #print "executing \n'" + attribute.script + "'\n"
                exec(attribute.script, globalEnvironment, entity.environment)
                
        #raw_input("press key")
        
        pygame.display.flip()

