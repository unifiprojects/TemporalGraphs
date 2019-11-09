'''

DFS on temporal graphs


Grafo temporale:                G(V,E)
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta

Algoritmo DFS-v1:

1) Inizializzo i 'delta(v) = inf', per ogni vertice 'v' in V

2) Visito il primo vertice 's' e metto 'delta(s) = Ts'

    a) Dopo la visita di ogni vertice 'u':
        Definisco 'E(u, v)' come l'insieme di archi '(u, v, t)', vicini di u, che non sono stati ancora attraversati
        e per cui 'delta(v) <= t'.

        Se E(u, v) non é vuoto:


        Se E(u, v) é vuoto:



    b) Dopo la visita di ogni arco


'''