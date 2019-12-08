from temporal_graph import TemporalGraph

if __name__ == "__main__":
    graph = TemporalGraph()

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

    for e in edges:
        graph.add_edge(e[0], e[1], e[2])

    graph.print_graph()

    print(graph.get_neighbors("a"))

    print(graph.get_edge_neighbor("a", "b"))

'''
    graph = Graph()

    f = open("out.ca-cit-HepPh", "r")
    line = f.readline()
    count = 0
    while line:
        line = f.readline()
        if line != "":
            data = line.split(" ")
            graph.add_edge(data[0], data[1], data[3])
            count = count + 1

    graph.print_graph()
    '''


