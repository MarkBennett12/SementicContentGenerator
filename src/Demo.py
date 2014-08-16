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
    network.StartInstanciation(entitylist)
    print str(entitylist)
    
    for entity in entitylist:
        print entity
        for attribute in entitylist[entity]:
            print attribute
            exec(entitylist[entity][attribute])

        
