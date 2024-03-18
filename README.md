# **MCEaSyIM**
MCEaSyIM is an algorithm that extends EaSyIM, which is an algorithm for the influence maximization problem with single information, to the influence maximization problem with misinformation and correct information.
MCEaSyIM computes a set of seed nodes that approximately maximizes the expected number of active nodes in the early stage of spreading correct information.

We provide code for the MCEaSyIM in Python. Our code requires Python 3 series.

## **Usage**

### **Input file**
**network_sample.txt**

We need file, network_sample.txt, where `network_sample` indicates the name of the network and is arbitrary. 
This file should be placed in `MCEaSyIM/data/`. 
In this file, each line contains two integer.
For example, `0 1` indicates that a directed edge exists from node `0 ` to node` 1`.

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
Calculate the fraction of nodes activated with correct information and computation time for MCEaSyIM.

Go to `MCEaSyIM/py/` and run the following command:


```
python3 MCEaSyIM.py
```
The four arguments are as follows. See also Diffusion_Rule.jpynb for an example.

1. Input either MCIC model (**IC**) or MCWC model (**WC**).
```
Enter the model IC or WC:
```


2. Input the name of the network. For example, if the file `network_sample.txt` is placed in `MCEaSyIM/data/`, one inputs `network_sample`.
```
Enter the base filename:
```


3. Input the number of seed nodes that spread correct information.
```
Enter the base k:
```


4. Input the parameter l. We recommend l = 3.
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

The first file shows the fraction of nodes activated with correct information in the given network.

The second file shows the compiutation time in seconds in the given network.



