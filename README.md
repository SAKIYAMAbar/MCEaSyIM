# **MCEaSyIM**
MCEaSyIM is an algorithm that extends EaSyIM[1], an algorithm for the influence maximization problem in terms of single information, to the influence maximization problem in terms of multi information.
(multi information represents **correct information** and **misinformation**)


MCEaSyIM computes $A_{\text{C}}$ (Initial seed nodes that spread correct information) that approximately maximizes the expected number of active nodes in the diffusion of correct information between time $t = r+1$ and $t = r + l$, where $l$ is an input of the algorithm.

## **Python**
### **•Requirements**
Require Python 3 series.

We implemented all the algorithms in Python3.

We conducted all the simulations on a Linux server with an AMD EPYC 7502 processor and 125 GB of main memory.

## **Usage**
First, clone this repository:
```
git clone git@github.com:SAKIYAMAbar/MCEaSyIM.git
```

### **•Inputfile**
**network_sample.txt**


We need to files, network_sample.txt, where indicates the name of the network and is arbitrary. This files should be placed in `MCEaSyIM/data/`. In this files, each line contains two integer.
For example, `0 1` indicates that an edge exists between node `0 `and node` 1`

**Example**


```
0 1
0 2
0 3
1 4
1 5
2 3
2 6
```

### **•Calculate using MCEaSyIM**
Calculate the number of users who received correct information and computation time using MCEaSyIM.

Go to ` MCEaSyIM/py/` and run the following command:


```
python3 MCEaSyIM.py
```
The four arguments are as follows.

1. Select either the Independent Cascade model (**IC**) or the Weighted Cascade model (**WC**).(see Diffusion_Rule.jpynb)
```
Enter the model IC or WC:
```


2. Select the name of the network.
```
Enter the base filename:
```



3. Select the number of initial $k$ seed nodes that spread the correct information($A_\text{C}$).
```
Enter the base k:
```



4. Select nodes to spread correction information considering up to $l$-step.
```
Enter the base l:
```



### **Output files**
MCEaSyIM_{*model*}_{*filename*}(l={*l*},k={*k*}).csv and MCEaSyIMruntime_{*model*}_{*filename*}(l={*l*},k={*k*}).csv will be created in the folder `MCEaSyIM/result/`.

For example, if one runs
```
python3 MCEaSyIM.py
```

```
Enter the model IC or WC: IC
```
```
Enter the base filename: network_sample
```
```
Enter the base k: 20
```

```
Enter the base l: 3
```

the following two files will be stored in `MCEaSyIM/result/`:


1.   MCEaSyIM_IC_network_sample(l=3,k=20).csv
2.   MCEaSyIMruntime_IC_network_sample(l=3,k=20).csv

1 denotes the fraction of the number of nodes that received correct information when $k$ nodes belonging to $A_C$ are selected using MCEaSyIM ($l$=3) when the network is network_sample and the diffusion model is IC.

2 denotes the compiutation time (sec) to select $k$ nodes belonging to $A_C$ using MCEaSyIM ($l$=3) when the network is network_sample and the diffusion model is IC.

## **References**
[1] Sainyam Galhotra, Akhil Arora, and Shourya Roy, Holistic influence maximization: Combining scalability and efficiency
with opinion-aware models, Proc. SIGMOD, 2016, pp. 743-758.[[paper]](https://arxiv.org/pdf/1602.03110.pdf)




