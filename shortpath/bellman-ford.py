"""
The Bellman-Ford algorithm is used to find the shortest path from a single source node to all 
other nodes in a weighted graph. Unlike Dijkstra’s algorithm, Bellman-Ford can handle graphs 
with negative weight edges, but it is slower. It also detects if there is a negative weight 
cycle in the graph.

Steps:
1 - Initialize:
    * Set the distance of the source node to 0 and all other nodes to infinity (inf).
    * Initialize the predecessor for each node, which keeps track of the shortest path tree.

2 - Relaxation:
    * For every edge in the graph, check if the path through the edge provides a shorter 
      distance to the destination node than the current known distance. If so, update the
      distance and predecessor.

3 - Repeat:
    * Repeat the relaxation process V-1 times (where V is the number of vertices). 
      Each iteration ensures that the shortest paths for up to V-1 edges are correctly found.

4 - Negative Cycle Detection:
    * After the V-1 iterations, check all edges once more. If you can further reduce the
      distance for any node, it means that the graph contains a negative weight cycle.
"""


class adj_matrix_graph:
    def __init__(self, size: int) -> None:
        self.graph = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, vert1: int, vert2: int, weight: int) -> None:
        self.graph[vert1][vert2] = weight
        ## graph is directed by default, so no need for the following line.
        # self.graph[vert2][vert1] = weight

    def display(self) -> None:
        for row in self.graph:
            print(row)

    def bellman_ford(self, start_v: int, end_v: int) -> None:
        iter_number = self.size - 1
        distance = dict(zip(range(self.size), [float("inf") for _ in range(self.size)]))
        distance[start_v] = 0
        parent = [None] * self.size
        for it in range(iter_number):
            for v1, node in enumerate(self.graph):
                for v2, edge in enumerate(node):
                    if distance[v1] + edge < distance[v2] and edge != 0:
                        distance[v2] = distance[v1] + edge
                        parent[v2] = v1
        searching_node = end_v
        while parent[searching_node] != None:
            print(f"({searching_node}) <--{distance[searching_node]}--", end=" ")
            searching_node = parent[searching_node]
        print(f"({start_v})")
        print(f"total distance : {distance[end_v]}")


if __name__ == "__main__":
    # Example Usage:
    g = adj_matrix_graph(7)
    g.add_edge(3, 0, 4)  # D - A, weight 5
    g.add_edge(3, 4, 2)  # D - E, weight 2
    g.add_edge(0, 2, 3)  # A - C, weight 3
    g.add_edge(0, 4, 4)  # A - E, weight 4
    g.add_edge(4, 2, 4)  # E - C, weight 4
    g.add_edge(4, 6, 5)  # E - G, weight 5
    g.add_edge(2, 5, 5)  # C - F, weight 5
    g.add_edge(2, 1, 2)  # C - B, weight 2
    g.add_edge(1, 5, 2)  # B - F, weight 2
    g.add_edge(6, 5, 5)  # G - F, weight 5
    g.display()
    g.bellman_ford(3, 5)
