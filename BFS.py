'''
Il seguente codice necessita della libreria graphviz: https://pypi.org/project/graphviz/
usare uno dei seguenti comandi (a scelta) per installare su ambiente Linux
apt-get install graphviz
pip install graphviz
-------------------------------------------------------------------------------------------
Pseudocodice della BFS temporale

Grafo temporale:                G(V,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    sigma(v)
Numero di hop da 's' a 'v':     dist(v)
Predecessore di 'v' nella BFS:  p(v)
Coda:                           Q

Algoritmo BFS:

1)  Inizializzo i vettori 'sigma(v) = inf', 'dist(v) = inf', 'p(v) = NULL', per ogni vertice 'v' in V
    Inizializzo la coda Q vuota

2)  Seleziono il vertice sorgente 's', imposto 'dist(s) = 0', 'p(s) = NULL', sigma(s) = Ts
    Inserisco nella coda Q la tupla (s, dist(s), sigma(s), p(s))

3)  Finche' Q non e' vuota:
        a)  Pop '(u, dist(u), sigma(u), p(u))'

        b)  Definisco 'E(u,v)' l'insieme di archi da 'u' a 'v' t.c. non sono stati attraversati e con 'sigma(u) <= t'

            i)  Selezione dell'arco 'e = (u, v, t)' appartenente ad 'E(u,v)' con tempo 't' minore

            ii) Se 'v' non e' in Q:
                    ossia non e' gia stato visitato, attraverso 'e' e se 'sigma(v) > t'
                    visito 'v' e push di (v, dist(v) = dist(v) + 1, sigma(v) = t, p(v) = u) in Q

            iii)Se 'v' e' in Q:
                    Controllo '(v, dist(v), sigma(v), p(v))'

                    Se 'dist(v) = dist(u) + 1': ('v' e' gia stato visitato da un nodo allo stesso livello)
                        attraverso 'e' e se sigma(v) > t, visito 'v', imposto 'sigma(v) = t' e 'p(v) = u'

                    Se 'dist(v) = dist(u)': ('v' e' gia stato visitato da un nodo al livello superiore)
                        attraverso 'e' e se 'sigma(v) > t', visito 'v',
                        push '(v, dist(v) = dist(u) + 1, sigma(v) = t, p(v) = u)' in Q


'''


# ----------------------- utility functions ---------------------------------
def is_node_present_into_queue(v, queue):
    for item in queue:
        if item[0] is v:
            return item
    return None


def find_edge_with_min_time(E):
    edge_min = E[0]
    for i in range(1, len(E)):
        if E[i].time < edge_min.time:
            edge_min = E[i]
    return edge_min


def update_node_into_queue(queue, occurrence, time, pred):
    count = 0
    for item in queue:
        if item == occurrence:
            queue.remove(item)
            queue.insert(count, (occurrence.name, dist[occurrence.name], time, pred))
            return
        count += 1


# ----------------------- BFS TEMPORALE ---------------------------------
def bfs():
    global current_node, current_tree_node
    while queue:
        queue_item = queue.pop(0)
        current_node = queue_item[0]
        current_tree_node = tree_nodes[current_node]
        for v in graph.get_neighbors(current_node):

            # il predecessore nella BFS non deve essere considerato come vicino
            if v is predecessor[current_node]:
                continue
            # filtra gli archi che non sono stati attraversati e che sono ancora attivi
            filter_function = lambda edge: not edge.is_traversed and sigma[current_node] <= edge.time
            E = list(filter(filter_function, graph.get_edge_neighbor(current_node, v)))
            if len(E) != 0:
                edge_min = find_edge_with_min_time(E)
                occurrence = is_node_present_into_queue(v, queue)
                if not occurrence:
                    edge_min.is_traversed = True
                    if sigma[v] > edge_min.time:
                        new_tree_node = TreeNode(v, edge_min.time)
                        tree_nodes[v] = new_tree_node
                        current_tree_node.add_node(new_tree_node)
                        dist[v] = dist[current_node] + 1
                        sigma[v] = edge_min.time
                        predecessor[v] = current_node
                        queue.append((v, dist[v], sigma[v], predecessor[v]))
                else:
                    if occurrence != None and dist[occurrence[0]] == dist[current_node] + 1:
                        edge_min.is_traversed = True
                        if sigma[v] > edge_min.time:
                            new_tree_node = TreeNode(v, edge_min.time)
                            tree_nodes[v] = new_tree_node
                            current_tree_node.add_node(new_tree_node)
                            sigma[v] = edge_min.time
                            predecessor[v] = current_node
                            update_node_into_queue(queue, occurrence, sigma[v], current_node)
                    elif occurrence != None and dist[occurrence[0]] == dist[current_node]:
                        edge_min.is_traversed = True
                        if sigma[v] > edge_min.time:
                            new_tree_node = TreeNode(v, edge_min.time)
                            tree_nodes[v] = new_tree_node
                            current_tree_node.add_node(new_tree_node)
                            dist[v] = dist[current_node] + 1
                            sigma[v] = edge_min.time
                            predecessor[v] = current_node
                            queue.append((v, dist[v], sigma[v], predecessor[v]))


# ------------------------- IMPORT and GRAPH DEFINITION -------------------------------
from temporal_graph import TemporalGraph
from math import inf
from TreeNode import TreeNode
from draw_tree import draw_tree

graph = TemporalGraph()

# grafo tratto dal paper
edges = [["a", "b", 2],
         ["b", "a", 5],
         ["a", "c", 4],
         ["a", "f", 7],
         ["f", "g", 3],
         ["b", "f", 3],
         ["c", "f", 5]]

for e in edges:
    graph.add_edge(e[0], e[1], e[2])

# ------------- starting time, sigma, dist ecc ------------
starting_time = 0
V = graph.get_nodes()
sigma = {key: inf for key in V}
dist = {key: inf for key in V}
predecessor = {node: None for node in V}
# ------------- updating source ------------
source = V[0]
sigma[source] = starting_time
dist[source] = 0
queue = [(source, 0, starting_time, None)]
# ------------- setting first tree node ------------
tree_node_root = TreeNode(source, starting_time)
current_tree_node = tree_node_root
tree_nodes = {source: tree_node_root}
# ------------------- BFS ------------------
bfs()
draw_tree(tree_node_root, 'BFS')
