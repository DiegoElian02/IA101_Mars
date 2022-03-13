import numpy as np
import matplotlib
import plotly.express as px
import queue
import math
import time

inicio = time.time()


def astar(lab, i_s, j_s, i_e, j_e, h):

    #establece el tamaño del laberinto
    width = len(lab[0])
    height = len(lab)

    #distancia heurística: de la posición actual a la meta (pitágoras)
    #lambda es una función anónima, significa que 'heuristic' está en función de i y j
    heuristic = lambda i, j: math.sqrt((i_e - i)**2+(j_e - j)**2)

    #obtiene el costo total (el camino recorrido + heurística)
    comp = lambda state: state[2] + state[3]

    #fringe = casillas sin explorar (lista de tuplas). 
    # Los argumentos son: coordenadas, coordenadas previas, costo del camino (que es 0 porque es el inicio) 
    # y costo heurístico.
    fringe = [((i_s, j_s), list(), 0, heuristic(i_s, j_s))]

    #diccionario vacío, este tendrá las casillas visitadas junto con su path cost
    visited = {}

    while True:

        #obtiene el primer objeto de la lista (least cost) y lo elimina de esta
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
        neighbor = list() #se agregan a la lista de vecinos

        #revisa que esté dentro de la matriz y que sea diferente a la barrera
        if i > 0 and abs(lab[i-1][j] - lab[i][j]) <= h and not(lab[i-1][j] in visited): #subir
            neighbor.append((i-1, j))

        if i < height and abs(lab[i+1][j] - lab[i][j]) <= h and not(lab[i+1][j] in visited): #bajar
            neighbor.append((i+1, j))

        if j > 0 and abs(lab[i][j-1] - lab[i][j]) <= h and not(lab[i][j-1] in visited): #izq
            neighbor.append((i, j-1))

        if j < width and abs(lab[i][j+1] - lab[i][j]) <= h and not(lab[i][j+1] in visited): #der
            neighbor.append((i, j+1))

        if (i > 0 and j > 0) and abs(lab[i-1][j-1] - lab[i][j]) <= h and not(lab[i-1][j-1] in visited): #subir izq
            neighbor.append((i-1, j-1))

        if (i < height and j > 0) and abs(lab[i+1][j-1] - lab[i][j]) <= h and not(lab[i+1][j-1] in visited): #bajar izq
            neighbor.append((i+1, j-1))

        if (i > 0 and j < width) and abs(lab[i-1][j+1] - lab[i][j]) <= h and not(lab[i-1][j+1] in visited): #subir der
            neighbor.append((i-1, j+1))

        if (i < height and j < width) and abs(lab[i+1][j+1] - lab[i][j]) <= h and not(lab[i+1][j+1] in visited): #bajar der
            neighbor.append((i+1, j+1))

        for n in neighbor:
            next_cost = heuristic(n[0],n[1]) #definir que el siguiente path cost será el mismo + 1 (se aleja 1 del inicio)
            fringe.append((n, [state[0]] + state[1], state[2] + 1, next_cost)) #se agrega la coordenada nueva,
            #la lista de los ya recorridos, el costo del lugar siguiente, y el costo heurístico
        
        #print(state) #imprimir moves

        #reorganiza la lista con base en 'comp', es decir, el costo total
        fringe.sort(key=comp)
        print('iter: '+str(i))
    


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
y_start = 1237
x_start = 394
y_end = 1135
x_end = 314
block = 0.25

road = astar(mars_map, y_start, x_start, y_end, x_end, block)
print(road)
print(printsolution(road, mars_map))

fin = time.time()
print(fin-inicio)