'''

BFS on temporal graphs

Grafo temporale:                G(V,E)
Source vertex:                  s
Tempo di inizio:                Ts
Vettore dei tempi di visita:    delta(v)
Numero di hop da 's' a 'v':     dist(v)
Predecessore di 'v' nella BFS:  p(v)
Coda:                           Q

Algoritmo BFS:

1)  Inizializzo i vettori 'delta(v) = inf', 'dist(v) = inf', 'p(v) = 0', per ogni vertice 'v' in V
    Inizializzo la coda Q vuota

2)  Visito il primo vertice 's', imposto 'dist(s) = 0', 'p(s) = 0'
    Push nella coda Q di (s, dist(s), delta(s), p(s))

3)  While Q is not empty:
        a)  Pop '(u, dist(u), delta(u), p(u))'

        b)  Definisco 'E(u,v)' l'insieme di archi da 'u' a 'v', non ancora attraversati e con 'delta(u) <= t'

            i)  Selezione dell'arco 'e = (u, v, t)' appartenente ad 'E(u,v)' con tempo 't' minore

            ii) Se 'v' non é in Q:
                    ossia non é gia stato visitato, attraverso 'e' e se 'delta(v) > t'
                    visito 'v' e push di (v, dist(v) = dist(v) + 1, delta(v) = t, p(v) = u) in Q

            iii)Se 'v' é in Q:
                    Controllo '(v, dist(v), delta(v), p(v))'

                    Se 'dist(v) = dist(u) + 1': ('v' é gia stato visitato da un nodo allo stesso livello)
                        attraverso 'e' e se delta(v) > t, visito 'v', imposto 'delta(v) = t' e 'p(v) = u'

                    Se 'dist(v) = dist(u)': ('v' é gia stato visitato da un nodo al livello superiore)
                        attraverso 'e' e se 'delta(v) > t', visito 'v',
                        push '(v, dist(v) = dist(u) + 1, delta(v) = t, p(v) = u)' in Q


'''


















