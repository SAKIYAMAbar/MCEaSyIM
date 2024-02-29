import numpy as np
import random
def calc(edges_M,edges_C,neighbors,top_k_nodes, I, S, R, k, selected_nodes,state,n):
    Rc=0
    Ic=len(top_k_nodes)
    selected_nodes=top_k_nodes+selected_nodes
    while I!=0 or Ic!=0:
        #selected_nodes = np.array(selected_nodes)
        R += I
        Rc += Ic
        I = 0
        Ic = 0
        selected_nodes_kari = []
        for i in selected_nodes:
            i_state = int(state[i])
            for j in neighbors[i]:
                j_state = int(state[j])
                if i_state == 1 and j_state == 0:
                    ransu = random.uniform(0, 1)
                    if ransu <= edges_C[(i, j)]:
                        state[j] = 1
                        selected_nodes_kari.append(j)
                        Ic += 1
                if i_state == -1 and j_state == 0:
                    ransu = random.uniform(0, 1)
                    if ransu <= edges_M[(i, j)]:
                        state[j] = -1
                        selected_nodes_kari.append(j)
                        I += 1
        selected_nodes = selected_nodes_kari
        S = n - (R + I + Rc + Ic)
        #print("Ic",Ic,"Rc",Rc,"I",I,"R",R,"S",S)
    return R,Rc
