'''

图结构

vertices

adj_list



Graph (保存顶点的主列表) 和 Vertex (将表示图中的每个顶点)
'''

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = []

    def addNeighbour(self,nbr):

        self.connectedTo.append(nbr)

    def getConnections(self):

        return  self.connectedTo

    def search(self,temp_key):
        if temp_key in self.connectedTo:
            return True

        else:
            return False
'''

{key:Vertex}
a[key] = value
'''
class Graph:
    def __init__(self):
        self.vertexes = {}

        self.numvertexes = 0

    def addVertex(self,key):
        self.numvertexes += 1

        newVertex = Vertex(key)

        self.vertexes[key] = newVertex

    def getVex(self):

        return self.vertexes.keys()

if __name__ == '__main__':

    G_a = Graph()
    for i in range(4):
        G_a.addVertex(i)

    G_a.vertexes[0].addNeighbour(1)
    G_a.vertexes[0].addNeighbour(2)

    G_a.vertexes[1].addNeighbour(0)
    G_a.vertexes[1].addNeighbour(2)

    G_a.vertexes[2].addNeighbour(0)
    G_a.vertexes[2].addNeighbour(1)
    G_a.vertexes[2].addNeighbour(2)

    G_a.vertexes[3].addNeighbour(2)



