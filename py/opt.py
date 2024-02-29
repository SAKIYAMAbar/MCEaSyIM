import numpy as np
def opt(Mfvalue,k,state):
    top_k_index = list(Mfvalue)[:k]
    for i in range(k):
      ind=int(top_k_index[i])
      state[ind]=1
    return top_k_index
