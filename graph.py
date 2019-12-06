# Node of the adjacency list
class AdjNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.next = None


class Graph:

    def __init__(self):
        self.V = []
        self.graph = {}

    def add_edge(self, src, dest, weight):
        # Nodes initialization
        if self.graph.get(src) is None:
            self.graph[src] = None
        if self.graph.get(dest) is None:
            self.graph[dest] = None
        # Node added to the adjacency list
        node = AdjNode(dest, weight)
        node.next = self.graph[src]
        self.graph.update({src: node})

    def print_graph(self):
        for i in self.graph.keys():
            print("Adjacency list of vertex {}:\n[".format(i), end="")
            temp = self.graph.get(i)
            while temp:
                print(" -> (" + temp.vertex + ", " + temp.weight + ") ", end="")
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
                edges.append([i, temp.vertex, temp.weight])
                temp = temp.next
        return edges
