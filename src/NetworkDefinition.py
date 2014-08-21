'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork
import GameObject

network = SemanticNetwork.Network()

solidObj = SemanticNetwork.Node("solidObj", [GameObject.Attribute("pos", GameObject.AttributeType.Init, 'pos = [0, 0]'), GameObject.Attribute("collide(with)", GameObject.AttributeType.Init, 'def collide(withobj):\n\tif pos[0] >= withobj[0] or pos[1] >= withobj[1]:\n\t\treturn True\n\telse:\n\t\treturn False')])
solidObj.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
network.AddNode(solidObj)

ball = SemanticNetwork.Node("ball", [GameObject.Attribute("image", GameObject.AttributeType.Init, 'image = pygame.image.load("ball.gif")'), GameObject.Attribute("pos", GameObject.AttributeType.Init, 'pos = [2, 2]'), GameObject.Attribute("move", GameObject.AttributeType.Runtime, 'if collide(size):\n\tpos[0] -= 1\n\tpos[1] -= 1\nelse:\n\tpos[0] += 1\n\tpos[1] += 1'), GameObject.Attribute("show", GameObject.AttributeType.Runtime, 'screen.blit(image, pos)')])
ball.AddRelation("isa", solidObj, SemanticNetwork.ControlRelationActions.Inherit, {})
network.AddNode(ball)

level = SemanticNetwork.Node("level", [GameObject.Attribute("colour", GameObject.AttributeType.Init, 'colour = 0, 0, 0'), GameObject.Attribute("show", GameObject.AttributeType.Runtime, 'screen.fill(colour)')])
level.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {})
level.AddRelation("hasa", ball, SemanticNetwork.ControlRelationActions.Instanciate, {})
network.AddNode(level)
network.GetWorld().AddRelation("hasa", level, SemanticNetwork.ControlRelationActions.Instanciate, {})

def GetNetwork():
    return network
