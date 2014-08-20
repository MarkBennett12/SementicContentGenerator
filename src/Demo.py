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
    entitylist = []
    
    # Set up the scope for the exec function
    environment = {}
    environment['pygame'] = globals()['pygame']
    environment["entityList"] = entitylist

    # Setup pygame
    pygame.init()
    size = width, height = 320, 240
    screen = pygame.display.set_mode(size)
    background = 0, 0, 0
    
    # Setup semantic generator
    network = NetworkDefinition.GetNetwork()
    #print str(network)
    print "instanciating world"
    print str(globals())
        
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        network.StartInstanciation(entitylist, environment)
        screen.fill(background)
        for entity in entitylist:
            print "entity in game loop = " + str(entity)
            print "entity.attributes in game loop = " + str(entity.attributes)
            for attribute in entity.attributes:
                print "attribute in game loop = " + str(attribute)
                #print str(environment['pos'])
                #print str(environment)
                exec(attribute.script, globals(), environment)
        pygame.display.update()

