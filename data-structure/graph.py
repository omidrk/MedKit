"""
Graphs are data structures that consist of a set of nodes (vertices) and a set of edges connecting these nodes. 
In Python, graphs can be implemented using various methods, including adjacency lists, adjacency matrices, 
and with the help of libraries like networkx. Below are different ways to implement graphs in Python:

1. Adjacency List
An adjacency list representation of a graph is efficient in terms of space and is straightforward to implement.

2. Adjacency Matrix
An adjacency matrix is a 2D array where the cell at row i and column j indicates the presence (and sometimes the weight) of an edge between vertex i and vertex j.

3. Using networkx Library
networkx is a comprehensive library for the creation, manipulation, and study of complex networks of nodes and edges.

Choosing an Implementation
- Adjacency List: Efficient for space, easy to iterate over neighbors. Good for sparse graphs.
- Adjacency Matrix: Simpler to implement for dense graphs but less space-efficient for sparse graphs.
- networkx Library: Powerful and flexible, ideal for more complex graph operations and analysis.
For most practical purposes, especially if you're dealing with complex graph algorithms or need to visualize the graph, 
networkx is a robust choice. For simpler applications, an adjacency list or matrix might be more appropriate.

"""


## Adjacency List implemetation
class adj_list_graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
        else:
            print("already existed")

    def add_edge(self, v1, v2, directed=False):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1) if not directed else None  # if undirected

    def display(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])


## 2. Adjacency Matrix implementation


class adj_matrix_graph:
    def __init__(self, size) -> None:
        self.graph = [[0] * size] * size

    def add_edge(self, v1, v2, directed=True):
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1 if not directed else 0

    def display(self):
        for row in self.graph:
            print(row)


if __name__ == "__main__":
    # Example Usage:
    g = adj_list_graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_edge("A", "B")
    g.add_edge("A", "C", directed=True)
    g.add_edge("B", "C")
    g.display()

    g = adj_matrix_graph(3)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.display()
