"""
Dijkstra’s algorithm is used to find the shortest path between nodes in a graph, which may represent, for example, road networks. The algorithm works by iteratively picking the closest node and updating the shortest path to its neighbors.

Steps:

1 - Initialize:
    - Mark all nodes as unvisited.
    - Set the initial node's distance to 0 and all others to infinity (inf).
    - Keep track of the predecessor node for each node, which is the node that provides the shortest path.

2 - Visit the Node with the Smallest Tentative Distance:
    - For the current node, update the distances to its neighbors by comparing the existing distances to 
      the new calculated distances (current node's distance + edge weight to neighbor).

3 - Repeat:
    - Once a node is visited, it is marked as "visited" and will not be checked again.
    - Continue visiting nodes with the smallest tentative distance until all nodes are visited.

4 - End:
    - Once all nodes are visited, the shortest path from the source node to any other node is determined.
"""


class adj_matrix_graph:
    def __init__(self, size: int) -> None:
        self.graph = [[0] * size for _ in range(size)]
        self.size = size

    def add_edge(self, vert1: int, vert2: int, weight: int):
        self.graph[vert1][vert2] = weight
        self.graph[vert2][vert1] = weight

    def display(self):
        for row in self.graph:
            print(row)

    def dijkstra(self, start_v: int, end_v: int):
        info = dict(
            zip(range(self.size), ([float("inf"), None] for _ in range(self.size)))
        )
        visited = []
        searching_node = start_v
        # info[start_v]
        while searching_node != end_v:
            visited.append(searching_node)
            """ 
            info hold the accumulated value for node plus previous 
            node in list. EX: info[0]=[4,6].
            idx and vert are for the next node.
            current node value is info[searching_node][0]
            next node value is info[idx][0] = info[searching_node] + vert
            """
            for idx, vert in enumerate(self.graph[searching_node]):
                distance = (
                    info[searching_node][0] + vert
                    if info[searching_node][0] < float("inf")
                    else vert
                )
                if vert > 0 and idx not in visited and distance < info[idx][0]:
                    info[idx][0] = distance
                    info[idx][1] = searching_node
            ## getting the node with minimum distance as next node
            ## min_value structure is [index,value]
            min_val = [None, float("inf")]
            for k, v in info.items():
                if v[0] < min_val[1] and k not in visited:
                    min_val = [k, v[0]]
            ## changing searching_node to min node as next
            searching_node = min_val[0]

        ## printing the result like: A -3-> B -4-> C
        while info[searching_node][1] != None:
            print(f"({searching_node}) <--{info[searching_node][0]}--", end=" ")
            searching_node = info[searching_node][1]
        print(f"({start_v})")
        print(f"total distance : {info[end_v][0]}")


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
    g.dijkstra(3, 5)
