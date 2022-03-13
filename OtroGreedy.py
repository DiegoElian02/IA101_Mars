import numpy as np
import plotly.express as px
import time



def greedy(lab, i_s, j_s, i_e, j_e, h):
    #distancia heurística: de la posición actual a la meta (pitágoras)
    #lambda es una función anónima, significa que 'heuristic' está en función de i y j
    heuristic = lambda i, j: (i_e - i)**2+(j_e - j)**2

    #obtiene el costo total ( heurística)
    comp = lambda state: state[3]

    #fringe = casillas sin explorar (lista de tuplas). 
    # Los argumentos son: coordenadas, coordenadas previas, costo del camino (que es 0 porque es el inicio) 
    # y costo heurístico.
    fringe = [((i_s, j_s), list(), 0, heuristic(i_s, j_s))]

    #diccionario vacío, este tendrá las casillas visitadas junto con su path cost
    visited = {}

    while True:

        #obtiene el primer objeto de la lista (least distance) y lo elimina de esta
        state = fringe.pop(0)
        if state[0] in visited:
            continue

        ##goal check
        (i, j) = state[0] #asigna a i,j el valor de la coordenada ubicada en el primer objeto de la tupla.
        if (i,j) == (i_e,j_e): #si se llegó a la meta...
            path = [state[0]] + state[1] #agrega a path state[0] (la coord actual) y state[1] (las coordenadas seguidas anteriormente)
            path.reverse() #invierte la lista para tener el camino tal cual se siguió
            print(state)
            return path

        #set the cost
        visited[(i, j)] = state[2] + state[3]

        #explorar el vecino, ocho direcciones
        neighbor = list()

        directions=[(1,0),(1,1),(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] #las 8 direcciones posibles

        for k in directions:
            newState=(i+k[0],j+k[1]) #el nuevo estado posible
            if h>abs(lab[i][j]-lab[newState[0]][newState[1]]) and newState not in visited : #revisa si es posible moverse ahi y si no se ha visitado
                neighbor.append(newState)

        for n in neighbor:
            next_cost = heuristic(n[0],n[1]) #definir que el siguiente path cost será el mismo + 1 (se aleja 1 del inicio)
            fringe.append((n, [state[0]] + state[1], state[2] + 1, next_cost)) #se agrega la coordenada nueva,
            #la lista de los ya recorridos, el costo del lugar siguiente, y el costo heurístico
        
        #print(state) #imprimir moves

        #reorganiza la lista con base en 'comp', es decir, la heuristica
        fringe.sort(key=comp)
    


def printsolution(sol, lab):
    for coord in range(0, len(sol)):
        x = sol[coord][1]
        y = sol[coord][0]
        lab[y][x] = 0
    fig = px.imshow(mars_map)
    fig.show()


# MAIN ALGORITHM
mars_map = np.load('mars_map.npy')

#valores de busqueda
y_start = 1175
x_start = 285
y_end = 1135
x_end = 315
block = 0.25

inicio = time.time()
road = greedy(mars_map, y_start, x_start, y_end, x_end, block)
fin = time.time()

print(road)
print(fin-inicio)
print(printsolution(road, mars_map))

