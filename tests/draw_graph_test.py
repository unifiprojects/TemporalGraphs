from graphviz import Digraph

g = Digraph()

nodes = ["a", "b", "c", "f", "g", "h"]
edges = [["a", "b", "1"],
         ["a", "b", "6"],
         ["b", "a", "8"],
         ["b", "c", "4"],
         ["b", "c", "7"],
         ["c", "b", "6"],
         ["a", "f", "3"],
         ["a", "f", "7"],
         ["f", "c", "5"],
         ["f", "h", "2"],
         ["f", "g", "8"],
         ["g", "a", "9"]]

for node in nodes:
    g.node(node)

for edge in edges:
    start_node = edge[0]
    end_node = edge[1]
    label = edge[2]
    g.edge(start_node, end_node, label, minlen='2', dir="forward")

g.view()
