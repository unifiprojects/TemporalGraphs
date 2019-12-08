# Node of the adjacency list
class AdjNode:
    def __init__(self, vertex, time):
        self.vertex = vertex
        # Edge visiting time
        self.time = time
        self.next = None


class TemporalGraph:

    def __init__(self):
        self.V = []
        self.graph = {}

    def add_edge(self, src, dest, time):
        # Nodes initialization
        if self.graph.get(src) is None:
            self.graph[src] = None
        if self.graph.get(dest) is None:
            self.graph[dest] = None

        # Node added to the adjacency list
        node = AdjNode(dest, time)
        node.next = self.graph[src]
        self.graph.update({src: node})

    def print_graph(self):
        for i in self.graph.keys():
            print("Adjacency list of vertex {}:\n[".format(i), end="")
            temp = self.graph.get(i)
            while temp:
                print(" -> (" + temp.vertex + ", " + temp.time + ") ", end="")
                temp = temp.next
            print("] \n")

    # Get the list of all the nodes
    def get_nodes(self):
        return self.graph.keys()

    # Get the list of all the edges
    def get_edges(self):
        edges = []
        for i in self.graph.keys():
            temp = self.graph.get(i)
            while temp:
                edges.append([i, temp.vertex, temp.time])
                temp = temp.next
        return edges

    # Get node neighbors, given a node
    def get_neighbors(self, node):
        neighbors = []
        temp = self.graph.get(node)
        while temp:
            neighbors.append(temp.vertex)
            temp = temp.next
        # Remove duplications
        neighbors = list(dict.fromkeys(neighbors))
        return neighbors

    # Get node neighbors, given u and v (v optional)
    def get_edge_neighbor(self, u, v=None):
        edge_neighbor = []
        temp = self.graph.get(u)
        while temp:
            if (v is None) or (v is not None and temp.vertex == v):
                edge_neighbor.append([u, temp.vertex, temp.time])
            temp = temp.next
        return edge_neighbor
