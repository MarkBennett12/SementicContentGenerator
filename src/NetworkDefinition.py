'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork

network = SemanticNetwork.Network()

# Test code to demonstrate the __str__ functionality, nonsense attributes
nodeA = SemanticNetwork.Node("NodeA", {'sally': '2345', 'debs': '5678'})
nodeA.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlAttributeActions.Inherit, {'jack': '4098', 'sape': '4139'})
network.AddNode(nodeA)
network.GetWorld().AddRelation("hasa", nodeA, SemanticNetwork.ControlAttributeActions.Instanciate, {'bill': '2012', 'mary': '6972'})

def GetNetwork():
    return network
