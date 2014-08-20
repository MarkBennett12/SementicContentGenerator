'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork
import GameObject

network = SemanticNetwork.Network()

ball = SemanticNetwork.Node("ball", [GameObject.Attribute("image", GameObject.AttributeType.Init, 'print "initialising ball"\nimage = pygame.image.load("ball.gif")'), GameObject.Attribute("pos", GameObject.AttributeType.Init, 'print "initialising pos"\npos = [2, 2]\nprint str(pos)'), GameObject.Attribute("move", GameObject.AttributeType.Behaviour, 'print "moving ball"\npos[0] += 2\npos[1] += 2\nprint str(pos)'), GameObject.Attribute("show", GameObject.AttributeType.Behaviour, 'screen.blit(image, pos)')])
ball.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
network.AddNode(ball)
network.GetWorld().AddRelation("hasa", ball, SemanticNetwork.ControlRelationActions.Instanciate, {})

def GetNetwork():
    return network
