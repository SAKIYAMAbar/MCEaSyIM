import numpy as np
def get_all_neighbors(data):
    neighbors_dict = {} 
    duplicated_neighbors = 0
    selfroop = 0

    for u, v in data:  
        if u not in neighbors_dict:
            neighbors_dict[u] = []
        if v not in neighbors_dict:
            neighbors_dict[v] = []
        if u == v:
            selfroop += 1
            #print(u, v)
        if v in neighbors_dict[u]:
            duplicated_neighbors += 1
        neighbors_dict[u].append(v)
        neighbors_dict[v].append(u)
    return neighbors_dict
