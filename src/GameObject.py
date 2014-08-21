'''
Created on 20 Aug 2014

@author: mark
'''

# imitates enum to make attribute types clear, the actions control
# what action the instanciator takes when it traverses a relation
# - Associate: keeps a reference to the target node, does not continue down that path
# - Inherit: accumulates the attributes of the target node into the instance and continues down that path.
# - Instanciate: Creates a new instance and accumulates any attributes into the created instance
class AttributeType:
    Init, Runtime, Probability, Count = range(4)
    
# Attribute class
class Attribute(object):
    def __init__(self, name, attrType, script):
        self.name = name
        self.type = attrType
        self.script = script 
        
    def __str__(self):
        outStr = self.name + ", "
        if self.type == AttributeType.Init:
            outStr += "initialise"      
        elif self.type == AttributeType.Runtime:
            outStr += "runtime"      
        elif self.type == AttributeType.Probability:
            outStr += "probability"      
        elif self.type == AttributeType.Count:
            outStr += "count"
        else:
            outStr += "no type"
        outStr += "'" + self.script + "'"
        return outStr      
        
# An entity in the game
class GameObject(object):
    def __init__(self, name):
        self.name = name
        self.attributes = []
        
    def __str__(self):
        outStr = self.name + " : "
        for attr in self.attributes:
            outStr += "attributes (" + str(attr) + ")"
        return outStr      
