import numpy as np
import matplotlib
import plotly.express as px
import time

def extract(lst):
    return [item[0] for item in lst]

heuristic=lambda state : (state[0]-x_end)**2+(state[1]-y_end)**2

def moves(lab, current, visited,h):
    moves=list()
    heu=list()
    path=current[1]
    directions=[(1,0),(1,1),(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    for k in directions:
        newState=(current[0][0]+k[0],current[0][1]+k[1])
        if h>abs(lab[current[0][0]][current[0][1]]-lab[newState[0]][newState[1]]) and newState not in visited:
            moves.append(newState)
            path.append(newState)
            heu.append(heuristic(newState))
    #Return possible moves in order based on the hueristic
    l= [x for _,x in sorted(zip(heu,moves),reverse=True)]
    return l,path


def greedyDFS(lab, i_s, j_s, i_e, j_e, h):
    #current=(i_s,j_s)
    goal=(i_e,j_e)
    
    nextNodes=[((i_s,j_s),list(),heuristic((i_s,j_s)))]
    current=((i_s,j_s),list())
    visited={current[0]}
    i=0
    while i<5000 and not current[0]==goal:
        current=nextNodes.pop()
        #print(str(current[0])+' i:'+str(i))
        visited.add(current[0])
        heu=list()
        directions=[(1,0),(1,1),(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for k in directions:
            newState=(current[0][0]+k[0],current[0][1]+k[1])
            if h>abs(lab[current[0][0]][current[0][1]]-lab[newState[0]][newState[1]]) and newState not in visited and newState not in extract(nextNodes):
                newMove=[newState,current[1]+[newState],heuristic(newState)] 
                nextNodes.append(newMove)
        nextNodes.sort(key=lambda y: y[2],reverse=True)
        #print(str(nextNodes[-1][0])+'  h: '+str(nextNodes[-1][2]))
        i+=1

    return current[1]
        

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
y_end = 1172
x_end = 620
block = 0.25

inicio = time.time()

road = greedyDFS(mars_map, y_start, x_start, y_end, x_end, block)

fin = time.time()

print(road)
print(fin-inicio)
print(printsolution(road, mars_map))
