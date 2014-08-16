'''
Created on 11 Aug 2014

@author: mark
'''

# This is where the actual semantic network gets created and attributes assigned to nodes and relations.

import SemanticNetwork

network = SemanticNetwork.Network()

# Test code to demonstrate the __str__ functionality, nonsense attributes
nodeD = SemanticNetwork.Node("NodeC", {'molly': 'print "This is attibute molly"', 'danny': 'print "This is attibute danny"'})
nodeD.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {'john': 'print "This is attibute john"', 'slim': 'print "This is attibute slim"'})
network.AddNode(nodeD)

nodeC = SemanticNetwork.Node("NodeC", {'nobby': 'print "This is attibute nobby, from NodeC"', 'nitwit': 'print "This is attibute nitwit from NodeC"'})
nodeC.AddRelation("isa", network.GetBase(), SemanticNetwork.ControlRelationActions.Inherit, {'wibble': 'print "This is attibute wibble"', 'wobble': 'print "This is attibute wobble"'})
network.AddNode(nodeC)

nodeA = SemanticNetwork.Node("NodeA", {'sally': 'print "This is attibute sally"', 'debs': 'print "This is attibute debs"'})
nodeA.AddRelation("isa", nodeC, SemanticNetwork.ControlRelationActions.Inherit, {'jack': 'print "This is attibute jack"', 'sape': 'print "This is attibute snape"'})
nodeA.AddRelation("isa", nodeD, SemanticNetwork.ControlRelationActions.Inherit, {'probability': 'probability = 0.5'})
network.AddNode(nodeA)
network.GetWorld().AddRelation("hasa", nodeA, SemanticNetwork.ControlRelationActions.Instanciate, {'bill': 'print "This is attibute bill"', 'mary': 'print "This is attibute mary"'})

nodeB = SemanticNetwork.Node("NodeB", {'bob': 'print "This is attibute bob"', 'dolly': 'print "This is attibute dolly"'})
nodeB.AddRelation("isa", nodeC, SemanticNetwork.ControlRelationActions.Inherit, {'jill': 'print "This is attibute jill"', 'sarah': 'print "This is attibute sarah"'})
network.AddNode(nodeB)
network.GetWorld().AddRelation("hasa", nodeB, SemanticNetwork.ControlRelationActions.Instanciate, {'samuel': 'print "This is attibute samuel"', 'maddie': 'print "This is attibute maddie"'})

nodeA.AddRelation("likes", nodeB, SemanticNetwork.ControlRelationActions.Associate, {'probability': 'probability = 0.8', 'snot': 'print "This is attibute snot and snot likes " + target'})

nodeE = SemanticNetwork.Node("NodeB", {'nob': 'print "This is attibute nob"', 'smelly': 'print "This is attibute smelly"'})
nodeE.AddRelation("isa", nodeC, SemanticNetwork.ControlRelationActions.Inherit, {'fill': 'print "This is attibute fill"', 'empty': 'print "This is attibute empty"'})
network.AddNode(nodeE)
network.GetWorld().AddRelation("hasa", nodeE, SemanticNetwork.ControlRelationActions.Instanciate, {'probability': 'probability = 0.9', 'count': 'count = 6 / 2'})

def GetNetwork():
    return network
