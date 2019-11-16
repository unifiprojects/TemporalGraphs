'''

DFS on temporal graphs


Grafo temporale:                G(V,E)
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


















