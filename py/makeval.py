import numpy as np
def makevalue(edges_C,neighbors,n,state,k,selectednodes,edges_M,l):
    remaining_nodes = set([node for node in range(len(state)) if int(state[node]) != -1])
    selectednodes=set(selectednodes)
    ns={u:{v for v in neighbors[u] if state[v]!=-1} for u in remaining_nodes}
    mns={u:{v for v in neighbors[u] if state[v]!=-1} for u in selectednodes}
    start=1
    top_k_nodes =set()
    pm=np.ones((n,l))
    for i in range(l-1):
            if i==0:
                for u in selectednodes:
                    for v in mns[u]:   #内包表記,#neighbors[u]かつint(state[v]) != -1のsetを先に記述
                            pm[v][i]=pm[v][i]*(1-edges_M[(u, v)])
            else:
                for u in remaining_nodes:
                    for v in ns[u]:
                            pm[v][i]=pm[v][i]*(1-edges_M[(u, v)]*(1-pm[u][i-1]))
    while start<=k:
        Mvalue=np.zeros((n,l))
        for i in range(l):
            max=0
            max_index=0
            for u in remaining_nodes:
                for v in ns[u]:
                        if v not in top_k_nodes:
                            if i==0:
                                Mvalue[u][i]+=edges_C[(u, v)]
                            else:
                                Mvalue[u][i]+=edges_C[(u, v)]*(1+pm[v][i-1]*Mvalue[v][i-1])
                if i==l-1 and max< Mvalue[u][l-1]:
                    max=Mvalue[u][l-1]
                    max_index=u
        top_k_nodes.add(max_index)
        print("top_k_nodes",top_k_nodes)
        remaining_nodes.remove(max_index)
        start+=1
        #print(top_k_nodes)
    return top_k_nodes
