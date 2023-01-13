#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self):
      
        self.adjacency_list ={}
    
    def addVertices(self, vertex):
        if vertex not in self.adjacency_list.keys():
              self.adjacency_list[vertex]=[]
              return True
        return False

    def addEdege(self, vertex1,vertices2):
        if vertex1 in self.adjacency_list.keys() and vertices2 in self.adjacency_list.keys():
              self.adjacency_list[vertex1].append(vertices2)
              self.adjacency_list[vertices2].append(vertex1)
              print("successfully connectin build between vertices")
              return True
        return f"sorry no vertices are available"
    def print_graph(self):
        for vertices in self.adjacency_list:
            print(f"{vertices} : {self.adjacency_list[vertices]}")
    
    
    
    def remove_edge(self,vertex1,vertices2):
        if vertex1 in self.adjacency_list.keys() and vertices2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertices2)
                self.adjacency_list[vertices2].remove(vertex1)
                print("successfully connectin remove between vertices")
                return True

            except ValueError:
                pass

        return False

      
    def remove_vertx(self,vertex1):
        if vertex1 in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex1]:
                self.adjacency_list[other_vertex].remove(vertex1)
                
                
            
            del self.adjacency_list[vertex1]
            print("successfully veretex are deleted")
            return True
       

        return False


g = Graph()
g.addVertices("A")
g.addVertices("B")
g.addVertices("C")
g.addVertices("D")
g.addEdege("A","B")
g.addEdege("A","C")
g.addEdege("A","D")
g.addEdege("B","C")
g.addEdege("C","D")
print(g.adjacency_list)
g.print_graph()
g.remove_edge("A","B")
print("after remove edge")
g.print_graph()
g.remove_vertx("D")
print("REmoval Vertices from Graph")
g.print_graph()

# otpot like

# successfully connectin build between vertices
# successfully connectin build between vertices
# successfully connectin build between vertices
# successfully connectin build between vertices
# successfully connectin build between vertices
# {'A': ['B', 'C', 'D'], 'B': ['A', 'C'], 'C': ['A', 'B', 'D'], 'D': ['A', 'C']}
# A : ['B', 'C', 'D']
# B : ['A', 'C']
# C : ['A', 'B', 'D']
# D : ['A', 'C']
# successfully connectin remove between vertices A-B
# after remove edge
# A : ['C', 'D']
# B : ['C']
# C : ['A', 'B', 'D']
# D : ['A', 'C']
# successfully veretex are deleted
# REmoval Vertices D from Graph
# A : ['C']
# B : ['C']
# C : ['A', 'B']



