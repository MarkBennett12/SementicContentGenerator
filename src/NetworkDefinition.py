'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork
import GameObject

network = SemanticNetwork.Network()

collisionDef = """
def collide(withobj):
    if pos[0] >= withobj[0] or pos[0] < 0 or pos[1] >= withobj[1] or pos[1] < 0:
        return True
    else:
        return False
"""

moveDef = """
if collide(size):
    speed[0] *= -1
    speed[1] *= -1

pos[0] += speed[0]
pos[1] += speed[1]
"""
#
# GameObject.Attribute("pos", GameObject.AttributeType.Init, 'pos = [10, 10]'), 
solidObj = SemanticNetwork.Node("solidObj", [GameObject.Attribute("pos", GameObject.AttributeType.Init , 'pos = [0, 0]'), GameObject.Attribute("collide(with)", GameObject.AttributeType.Init, collisionDef)])
solidObj.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
network.AddNode(solidObj)

ball = SemanticNetwork.Node("ball", [GameObject.Attribute("image", GameObject.AttributeType.Init, 'image = pygame.image.load("ball.gif")'), GameObject.Attribute("pos", GameObject.AttributeType.Init, 'pos = [20, 20]'), GameObject.Attribute("speed", GameObject.AttributeType.Init, 'speed = [1, 1]'), GameObject.Attribute("move", GameObject.AttributeType.Runtime, moveDef), GameObject.Attribute("show", GameObject.AttributeType.Runtime, 'screen.blit(image, pos)')])
ball.AddRelation("isa", solidObj, SemanticNetwork.ControlRelationActions.Inherit, {})
network.AddNode(ball)

level = SemanticNetwork.Node("level", [GameObject.Attribute("colour", GameObject.AttributeType.Init, 'colour = 0, 0, 0'), GameObject.Attribute("show", GameObject.AttributeType.Runtime, 'screen.fill(colour)')])
level.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
level.AddRelation("hasa", ball, SemanticNetwork.ControlRelationActions.Instanciate, {})
network.AddNode(level)
network.GetWorld().AddRelation("hasa", level, SemanticNetwork.ControlRelationActions.Instanciate, {})

def GetNetwork():
    return network
