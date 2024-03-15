# **MCEaSyIM**
MCEaSyIM is an algorithm that extends EaSyIM[1], which is an algorithm for the influence maximization problem with single information, to the influence maximization problem with misinformation and correct information [2].


MCEaSyIM computes a set of seed nodes that spread correct information to approximately maximize the expected number of active nodes in the early stage of spreading correct information.
## **Requirements**
Require Python 3 series.

We implemented all the algorithms in Python3.

We conducted all the simulations on a Linux server with an AMD EPYC 7502 processor and 125 GB of main memory.

## **Usage**
First, clone this repository:
```
git clone git@github.com:SAKIYAMAbar/MCEaSyIM.git
```

### **Input file**
**network_sample.txt**


We need to files, network_sample.txt, where indicates the name of the network and is arbitrary. This files should be placed in `MCEaSyIM/data/`. In this files, each line contains two integer.
For example, `0 1` indicates that an directed edge exists from node `0 ` to node` 1`

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

### **Run MCEaSyIM**
Calculate the fraction of nodes that were activated with correct information and computation time for MCEaSyIM.

Go to ` MCEaSyIM/py/` and run the following command:


```
python3 MCEaSyIM.py
```
The four arguments are as follows.

1. Select either MCIC model (**IC**) or MCWC model (**WC**).(see Diffusion_Rule.jpynb)
```
Enter the model IC or WC:
```


2. Select the a file, network_sample.txt, where network_sample indicates the name of the network. The file should be placed in `MCEaSyIM/data/ `.
```
Enter the base filename:
```



3. Select the number of seed nodes that spread correct information.
```
Enter the base k:
```



4. Select $l$-step.(see [2] for more details on this parameter.)
```
Enter the base l:
```



### **Output files**
MCEaSyIM_spread_{*model*}_{*filename*}(l={*l*},k={*k*}).csv and MCEaSyIM_runtime_{*model*}_{*filename*}(l={*l*},k={*k*}).csv will be created in the folder `MCEaSyIM/result/`.

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


1.   MCEaSyIM_spread_IC_network_sample(l=3,k=20).csv
2.   MCEaSyIM_runtime_IC_network_sample(l=3,k=20).csv

1 denotes the fraction of the number of nodes that received correct information when $k$ nodes belonging to $A_C$ are selected using MCEaSyIM ($l$=3) when the network is network_sample and the diffusion model is IC.

2 denotes the compiutation time (sec) to select $k$ nodes belonging to $A_C$ using MCEaSyIM ($l$=3) when the network is network_sample and the diffusion model is IC.

## **References**
[1] Sainyam Galhotra, Akhil Arora, and Shourya Roy. Holistic influence maximization: Combining scalability and efficiency
with opinion-aware models. Proc. SIGMOD, pp. 743-758(2016). [[paper]](https://arxiv.org/pdf/1602.03110.pdf)
[2] Takumi Sakiyama, Kazuki Nakajima, and Masaki Aida. Efficient intervention in the spread of misinformation in social networks. Under review (2024).




