'''

DFS on temporal graphs


Grafo temporale:                G(V,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta

Algoritmo DFS-v1:

1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in V

2) Visito il primo vertice 's' e metto 'delta(s) = Ts'

    a) Dopo la visita di ogni vertice 'u':
        Definisco 'E(u, v)' come gli insiemi di archi '(u, v, t)', vicini di u e diretti verso v,
        che non sono stati ancora attraversati e per cui 'delta(v) <= t'.

        Se esiste un vertice 'v' tale che E(u, v) non é vuoto:
            Attraverso l'arco 'e = (u, v, t)' dove 't = min{t : (u, v, t) appartiene ad E(u,v)}'
            (attraverso l'arco con tempo minore)
            (in questo caso andiamo al passo b)

        Se non esiste un vertice 'v' tale che E(u, v) non é vuoto:
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



- La DFS-v1 puó essere fatta anche utilizzando il max come la DFS-v2

- Complessitá:
    O ( |E| + |V| + X)

    X = Per ogni nodo u, (numero di volte che u é visitato) * (grado in uscita di u)

'''

'''Find the next edge to traverse with minimum time'''


def edge_min(E):
    edge_min = E[0]
    for i in range(1, len(E)):
        if E[i].time < edge_min.time:
            edge_min = E[i]
    return edge_min

def DFSv1(current):
    for v in graph.get_neighbors(current):
        E = list(filter(lambda x: not x.is_traversed and sigma[current] <= x.time, graph.get_edge_neighbor(current, v)))
        if len(E) != 0:
            tmin = edge_min(E)
            tmin.is_traversed = True
            if sigma[tmin.destination] >  tmin.time:
                sigma[tmin.destination] = tmin.time
            DFSv1(tmin.destination)

#--------------------------------------------------------
from temporal_graph import TemporalGraph
from math import inf

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

# da qui parte la DFSv1
starting_time = 2
V = graph.get_nodes()
sigma = {key: inf for key in V}
source = V[0]
sigma[source] = starting_time
DFSv1(source)

all_edges = graph.get_edges()
for e in all_edges:
    print(e)




