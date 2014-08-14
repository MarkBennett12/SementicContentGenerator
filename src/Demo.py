'''
Created on 11 Aug 2014

@author: mark
'''
import NetworkDefinition

if __name__ == '__main__':
    entitylist = {}
    network = NetworkDefinition.GetNetwork()
    print str(network)
    print "instanciating network"
    network.Instanciate(entitylist, "world")
    print str(entitylist)
