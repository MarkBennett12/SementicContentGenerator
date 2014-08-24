'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork
import GameObject

def GetNetwork(globalEnvironment):
    network = SemanticNetwork.Network(globalEnvironment)
    
    solidObjCollisionDef = """
def collide(pos, withobj):
    if pos[0] >= withobj[0] or pos[0] < 0 or pos[1] >= withobj[1] or pos[1] < 0:
        return True
    else:
        return False
"""
    solidObj = SemanticNetwork.Node("solidObj", [GameObject.Attribute("pos", True, GameObject.AttributeType.Init , '[0, 0]'), GameObject.Attribute("collide",  False, GameObject.AttributeType.Init, solidObjCollisionDef)])
    solidObj.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
    network.AddNode(solidObj)
    
    ballMoveDef = """
if collide(pos, parent_size):
    speed[0] *= -1
    speed[1] *= -1

pos[0] += speed[0]
pos[1] += speed[1]
"""
    ball = SemanticNetwork.Node("ball", [GameObject.Attribute("image", False, GameObject.AttributeType.Init, 'image = pygame.image.load("ball.gif")'), GameObject.Attribute("pos",  True, GameObject.AttributeType.Init, '[20, 20]'), GameObject.Attribute("speed",  True, GameObject.AttributeType.Init, '[1, 1]'), GameObject.Attribute("move", False, GameObject.AttributeType.Runtime, ballMoveDef), GameObject.Attribute("show", False, GameObject.AttributeType.Runtime, 'screen.blit(image, pos)')])
    ball.AddRelation("isa", solidObj, SemanticNetwork.ControlRelationActions.Inherit, {})
    network.AddNode(ball)
    
    level = SemanticNetwork.Node("level", [GameObject.Attribute("colour",  True, GameObject.AttributeType.Init, '[0, 0, 0]'), GameObject.Attribute("size",  True, GameObject.AttributeType.Init, 'windowSize'), GameObject.Attribute("show", False, GameObject.AttributeType.Runtime, 'screen.fill(colour)')])
    level.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
    level.AddRelation("hasa", ball, SemanticNetwork.ControlRelationActions.Instanciate, {})
    network.AddNode(level)
    network.GetWorld().AddRelation("hasa", level, SemanticNetwork.ControlRelationActions.Instanciate, {})

    return network
