# Node of the adjacency list
class TemporalEdge:
    def __init__(self, source, destination, time):
        self.source = source
        self.destination = destination
        self.time = time
        self.next = None
        self.is_traversed = False

    def __str__(self):
        return "[ " + self.source + ", " + self.destination + ", " + str(self.time) + ", " + str(
            self.is_traversed) + "]"


class TemporalGraph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, src, dest, time):
        # Edges initialization
        if self.graph.get(src) is None:
            self.graph[src] = None
        if self.graph.get(dest) is None:
            self.graph[dest] = None

        # Node added to the adjacency list
        edge = TemporalEdge(src, dest, time)
        edge.next = self.graph[src]
        self.graph.update({src: edge})

    def print_graph(self):
        for i in self.graph.keys():
            print("Adjacency list of vertex {}:\n[".format(i), end="")
            temp = self.graph.get(i)
            while temp:
                print(" -> (" + temp.destination + ", " + temp.time + ") ", end="")
                temp = temp.next
            print("] \n")

    # Get the list of all the nodes
    def get_nodes(self):
        return list(self.graph.keys())

    # Get the list of all the edges
    def get_edges(self):
        edges = []
        for i in self.graph.keys():
            temp = self.graph.get(i)
            while temp:
                edges.append(temp)
                temp = temp.next
        return edges

    # Get node neighbors, given a node
    def get_neighbors(self, node):
        neighbors = []
        temp = self.graph.get(node)
        while temp:
            neighbors.append(temp.destination)
            temp = temp.next
        # Remove duplications
        neighbors = list(dict.fromkeys(neighbors))
        neighbors.sort()
        return neighbors

    # Get node neighbors, given u and v (v optional)
    def get_edge_neighbor(self, u, v=None):
        edge_neighbor = []
        temp = self.graph.get(u)
        while temp:
            if (v is None) or (v is not None and temp.destination == v):
                edge_neighbor.append(temp)
            temp = temp.next
        return edge_neighbor
