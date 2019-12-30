'''

DFS on temporal graphs


Grafo temporale:                G(V,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta

Algoritmo DFS-v2:

1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in V

2) Visito il primo vertice 's' e metto 'delta(s) = Ts'

    a) Dopo la visita di ogni vertice 'u':
        Definisco 'E(u)' come gli insiemi di archi '(u, v, t)', vicini di u,
        che non sono stati ancora attraversati e per cui 'delta(v) <= t'.

        Se E(u) non é vuoto:
            Attraverso l'arco 'e = (u, v, t)' dove 't = max{t : (u, v, t) appartiene ad E(u)}'
            (attraverso l'arco con tempo massimo)
            (in questo caso andiamo al passo b)

        Se E(u) é vuoto:
            Se 'u' é il source vertex terminiamo la DFS,
            altrimenti, consideriamo l'arco (up, u, t) che ci ha permesso di visitare 'u' e
                        effettuiamo il backtrack visitando il predecessore 'up' di 'u'
                        (in questo caso andiamo al passo a)
            (torno al vertice precedente)

    b) Dopo la visita di ogni arco (u, v, t):
        Se 'delta(v) > t' impostiamo 'delta(v) = t' e visitiamo 'v'
        altrimenti nulla
        (in entrambi i casi vado al passo a)

        (Il controllo 'delta(v) > t' é necessario per visitare solo nodi 'v' che hanno delta(v) = inf)


- Complessitá:
    O ( |E| + |V|)


'''


# ----------------------- function definitions ---------------------------------
def find_edge_with_max_time(E):
    edge_max = E[0]
    for i in range(1, len(E)):
        if E[i].time > edge_max.time:
            edge_max = E[i]
    return edge_max


def dfs_v2(current_node):
    global current_tree_node
    while 1:

        # filtra gli archi che non sono stati attraversati e che sono ancora attivi
        filter_function = lambda edge: not edge.is_traversed and sigma[current_node] <= edge.time and \
                                       predecessor[current_tree_node.name] is not edge.destination
        # predecessor[current_tree_node.name] is not edge.destination
        # evita che il predecessore sia considerato come vicino

        E = list(filter(filter_function, graph.get_edge_neighbor(current_node)))
        if len(E) != 0:
            edge_max = find_edge_with_max_time(E)
            edge_max.is_traversed = True
            if sigma[edge_max.destination] > edge_max.time:
                # aggiorna albero DFS con un nuovo nodo
                next_tree_node = TreeNode(edge_max.destination, edge_max.time)
                predecessor[next_tree_node.name] = current_tree_node
                # aggiorno il nodo dell'albero a cui aggiungere elementi nella prossima chiamata ricorsiva
                current_tree_node.add_node(next_tree_node)
                current_tree_node = next_tree_node

                sigma[edge_max.destination] = edge_max.time
                dfs_v2(edge_max.destination)
        else:
            break
    current_tree_node = predecessor[current_tree_node.name]


# ------------------------- IMPORT and GRAPH DEFINITION -------------------------------
from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree

graph = TemporalGraph()

edges = [["a", "b", 1],
         ["a", "b", 6],
         ["b", "a", 8],
         ["b", "c", 4],
         ["b", "c", 7],
         ["c", "b", 6],
         ["a", "f", 3],
         ["a", "f", 7],
         ["f", "c", 5],
         ["f", "h", 2],
         ["f", "g", 8],
         ["g", "a", 9]]

for e in edges:
    graph.add_edge(e[0], e[1], e[2])

# ------------- starting time, sigma, dist ecc ------------
# V:= insieme di tutti i nodi del grafo
# sigma:= dizionario { <nome_nodo> : <ultimo istante in cui è stato visitato> }
starting_time = 2
V = graph.get_nodes()
sigma = {key: inf for key in V}
# ------------- updating source ------------
source = V[0]
sigma[source] = starting_time
# ------------- setting first tree node ------------
tree_node_root = TreeNode(source, starting_time)
predecessor = {node: None for node in V}
current_tree_node = tree_node_root
# ------------------- DFS-v2 ------------------
dfs_v2(source)
draw_tree(tree_node_root, 'DFS_v2')
