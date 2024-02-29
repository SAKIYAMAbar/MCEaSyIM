import matplotlib.pyplot as plt
import numpy as np
import random
import time
import prob
import makedict
import initial
import makeval
import opt
import calc


model=input("Enter the model IC or WC: ")
base_filename = input("Enter the base filename: ")
k = int(input("Enter the base k: "))
length = int(input("Enter the base l: "))
file_name = f"../data/{base_filename}.txt"
graph = prob.from_file(file_name,model)
nodes=graph[0]
edges_M=graph[1]
edges_C=graph[2]
out_degree=graph[3]
n=graph[4]
data=graph[5]
neighbors=makedict.get_all_neighbors(data)
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
initial=initial.initial(edges_M,edges_C,neighbors,I_f,S_f,R_f,selected_nodes,state,n)
selected_nodes1=initial[0]
#print("selected_nodes1",selected_nodes1)
I_f=initial[1]
R_f=initial[3]
S_f=initial[2]
runtimeind=np.zeros(1)
start_time = time.time()  # 現在の時間を取得
Mfvalue=makeval.makevalue(edges_C,neighbors,n,state,k,selected_nodes1,edges_M,length)
end_time = time.time()
runtime = end_time - start_time
runtimeind[0]=runtime
remaining_nodes = [node for node in range(len(state)) if int(state[node]) != -1]
for l in range(chal):
    R_heikin=0
    Rc_heikin=0
    opt1=opt.opt(Mfvalue,k,state)
    for i in range(sim):
        state2=np.copy(state)
        calcR=calc.calc(edges_M,edges_C,neighbors,opt1,I_f,S_f,R_f,k,selected_nodes1,state2,n)
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
