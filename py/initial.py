import random
import numpy as np
def initial(edges_M,edges_C,neighbors,I,S,R,selected_nodes,state,n):
    while (I+R)/n<=0.05:
        R=R+I
        I=0
        selected_nodes_kari=[]
        for i in selected_nodes:
            for j in neighbors[i]:
                if int(state[i])==-1 and int(state[j])==0:
                    random.seed(int(j)*int(i))
                    ransu=random.uniform(0,1)
                    if ransu<=edges_M[(i, j)]:
                        state[j]=-1
                        selected_nodes_kari.append(j)
                        I=I+1
        selected_nodes=selected_nodes_kari
        S=n-(R+I)
        print("I",I,"R",R,"S",S,"(I+R)/n",(I+R)/n)
    return selected_nodes,I,S,R
