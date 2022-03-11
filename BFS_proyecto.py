import numpy as np
import plotly.express as px
import time

inicio = time.time()

def bfs(lab, i_s, j_s, i_e, j_e, h):
    #establece el tamaño del laberinto
    width = len(lab[0])
    height = len(lab)

    #q = lista de tuplas
    #Los argumentos son: coordenadas, camino que ha seguido, costo del camino (que es 0 porque es el inicio)
    q = [((i_s, j_s), list(), 0)]

    #diccionario vacío, este tendrá las casillas visitadas junto con su path cost
    visited = {}

    while True:
        #obtiene el primer objeto en la lista 'q' y lo elimina de esta
        state = q.pop(0)
        if state[0] in visited:
            #si la coordenada que se obtuvo ya ha sido visitada, se salta este objeto y continúa al siguiente
            continue

        (i, j) = state[0] #asigna a i,j el valor de la coordenada ubicada en el primer objeto de la tupla
        if (i,j) == (i_e,j_e): #goal check
            path = [state[0]] + state[1] #agrega a path state[0] (la coord final) y state[1] (las coordenadas seguidas anteriormente)
            path.reverse() #invierte la lista para tener el camino tal cual se siguió
            print(state[2])
            return path

        #set the cost
        visited[(i, j)] = state[2]

        #crea la lista vecinos a los que agregará las casillas adyacentes disponibles
        neighbor = list()
        
        #revisa que esté dentro de la matriz, que no exceda el límite de cambio de altura establecido y que no sea una celda ya visitada
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
            next_cost = state[2] + 1 #definir que el siguiente path cost será el mismo + 1 (se aleja 1 del inicio)
            q.append((n, [state[0]] + state[1], next_cost)) #se agrega la coordenada nueva,
            #la lista de los ya recorridos, el costo del lugar siguiente

def printsolution(sol, lab):
    #cambiará los valores de las celdas que forman parte del camino final a 0
    for coord in range(0, len(sol)):
        x = sol[coord][1]
        y = sol[coord][0]
        lab[y][x] = 0

    #mostrar imagen
    fig = px.imshow(lab)
    fig.show()

# MAIN ALGORITHM
mars_map = np.load('mars_map.npy')

i_start = 1175
j_start = 285
i_end = 1135
j_end = 314
h = 0.25

road = bfs(mars_map, i_start, j_start, i_end, j_end, h)
print(road)
printsolution(road, mars_map)

fin = time.time()
print(fin-inicio)