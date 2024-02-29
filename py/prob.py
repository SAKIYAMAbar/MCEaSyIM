def from_file(filename,model):
    data = [] 
    max = 0 
    with open(filename, "r") as f: 
        for line in f: 
            elements = line.split()  
            if len(elements) == 2: 
                set_data = (int(elements[0]), int(elements[1])) 
                data.append(set_data) 
                if max <= int(elements[0]): 
                  max = int(elements[0]) 
                if max <= int(elements[1]): 
                  max = int(elements[1]) 
    n = max + 1 
    nodes = {} 
    edges_M = {} 
    edges_C = {} 
    for i in range(n): 
        nodes[i] = i 
    degree = {}
    for u in range(n):
        degree[u] = 0
    for (u, v) in data:
        degree[u] += 1
        degree[v] += 1
    for tup in data: # リストの各タプルに対して
        if model=="IC":
            edges_M[(tup[0], tup[1])] = 0.1
            edges_C[(tup[0], tup[1])] = 0.05 
            edges_M[(tup[1], tup[0])] = 0.1 
            edges_C[(tup[1], tup[0])] = 0.05 
        if model=="WC":
            edges_M[(tup[0], tup[1])] = 1 / degree[tup[1]] 
            edges_M[(tup[1], tup[0])] = 1 / degree[tup[0]] 
            edges_C[(tup[0], tup[1])] = 1 / (2 * degree[tup[1]]) 
            edges_C[(tup[1], tup[0])] = 1 / (2 * degree[tup[0]]) 
    return nodes, edges_M, edges_C,degree,n,data
