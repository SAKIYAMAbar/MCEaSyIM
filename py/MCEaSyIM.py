import matplotlib.pyplot as plt
import numpy as np
import random
import time


def from_file(filename,model):
    data = []  # セットごとのデータを格納するリスト
    max = 0 # ノードの最大値を保持する変数
    with open(filename, "r") as f: # ファイルを開く
        for line in f: # ファイルの各行に対して
            elements = line.split()  # 空白で分割して要素を取得する
            if len(elements) == 2: # 要素が2つであれば
                set_data = (int(elements[0]), int(elements[1])) # 要素を整数に変換してタプルにする
                data.append(set_data) # リストにタプルを追加する
                if max <= int(elements[0]): # ノードの最大値を更新するか判定する
                  max = int(elements[0]) # ノードの最大値を更新する
                if max <= int(elements[1]): # ノードの最大値を更新するか判定する
                  max = int(elements[1]) # ノードの最大値を更新する
    n = max + 1 # ノード数を求める
    nodes = {} # ノードの辞書を作る
    edges_M = {} # カスケードAのエッジの辞書を作る
    edges_C = {} # カスケードBのエッジの辞書を作る
    for i in range(n): # すべてのノードに対して
        nodes[i] = i # ノードの値をノード自身にする
    degree = {}
    for u in range(n):
        degree[u] = 0
    for (u, v) in data:
        degree[u] += 1
        degree[v] += 1
    for tup in data: # リストの各タプルに対して
        if model=="IC":
            edges_M[(tup[0], tup[1])] = 0.1# カスケードAのエッジ (u, v) の重みを入次数で割って求める
            edges_C[(tup[0], tup[1])] = 0.05 # カスケードBのエッジ (u, v) の重みを入次数の2倍で割って求める
            edges_M[(tup[1], tup[0])] = 0.1 # カスケードAのエッジ (v, u) の重みを入次数で割って求める
            edges_C[(tup[1], tup[0])] = 0.05 # カスケードBのエッジ (v, u) の重みを入次数の2倍で割って求める
        if model=="WC":
            edges_M[(tup[0], tup[1])] = 1 / degree[tup[1]] # カスケードAのエッジ (u, v) の重みを入次数で割って求める
            edges_M[(tup[1], tup[0])] = 1 / degree[tup[0]] # カスケードAのエッジ (v, u) の重みを入次数で割って求める
            edges_C[(tup[0], tup[1])] = 1 / (2 * degree[tup[1]]) # カスケードBのエッジ (u, v) の重みを入次数の2倍で割って求める
            edges_C[(tup[1], tup[0])] = 1 / (2 * degree[tup[0]]) # カスケードBのエッジ (v, u) の重みを入次数の2倍で割って求める
    return nodes, edges_M, edges_C,degree,n,data


def get_all_neighbors(data):
    neighbors_dict = {}  # 各ノードの隣接ノードを格納する辞書
    duplicated_neighbors = 0
    selfroop = 0

    for u, v in data:  # カスケードAのエッジのすべてのキーに対して
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


def opt(Mfvalue,k,state):
    top_k_index = list(Mfvalue)[:k]
    for i in range(k):
      ind=int(top_k_index[i])
      state[ind]=1
    return top_k_index



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

model=input("Enter the model IC or WC: ")
base_filename = input("Enter the base filename: ")
k = int(input("Enter the base k: "))
length = int(input("Enter the base l: "))
file_name = f"../data/{base_filename}.txt"
graph = from_file(file_name,model)
nodes=graph[0]
edges_M=graph[1]
edges_C=graph[2]
out_degree=graph[3]
n=graph[4]
data=graph[5]
neighbors=get_all_neighbors(data)
#print(neighbors[0])
#print(neighbors[1])
#print(n)
sim=100
chal=1
R_ratio=np.zeros(chal)
Rc_ratio=np.zeros(chal)
runtimeind=np.zeros(chal)
start =int(n*0.03)
I_f=start
S_f=n-start
R_f=0
random.seed(0)
selected_nodes = random.sample(range(n), start)
state=np.zeros(n)
for i in selected_nodes:
    state[i]=-1
initial=initial(edges_M,edges_C,neighbors,I_f,S_f,R_f,selected_nodes,state,n)
selected_nodes1=initial[0]
#print("selected_nodes1",selected_nodes1)
I_f=initial[1]
R_f=initial[3]
S_f=initial[2]
runtimeind=np.zeros(1)
start_time = time.time()  # 現在の時間を取得
Mfvalue=makevalue(edges_C,neighbors,n,state,k,selected_nodes1,edges_M,length)
end_time = time.time()
runtime = end_time - start_time
runtimeind[0]=runtime
remaining_nodes = [node for node in range(len(state)) if int(state[node]) != -1]
for l in range(chal):
    R_heikin=0
    Rc_heikin=0
    opt1=opt1=opt(Mfvalue,k,state)
    for i in range(sim):
        state2=np.copy(state)
        calcR=calc(edges_M,edges_C,neighbors,opt1,I_f,S_f,R_f,k,selected_nodes1,state2,n)
        R_heikin=R_heikin+calcR[0]
        Rc_heikin=Rc_heikin+calcR[1]
    R_heikin=R_heikin/sim
    Rc_heikin=Rc_heikin/sim
    #print(R_heikin)
    R_ratio[l]=R_heikin/n
    Rc_ratio[l]=Rc_heikin/n
print(Rc_ratio)
print(runtimeind)
np.savetxt(f"../result/MCEaSyIM_{model}_{base_filename}(l={length},k={k}).csv", Rc_ratio, delimiter=",")
np.savetxt(f"../result/MCEaSyIMruntime_{model}_{base_filename}(l={length}).csv", runtimeind, delimiter=",")
