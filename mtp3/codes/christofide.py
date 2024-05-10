import numpy as np
import heapq as hp
from dsu import *
from blossom import *
from hierholzer import *
import re
from sklearn.cluster import KMeans
from kmeans import *
from utils import *

def christo(edges):
    # make the mst
    pq = []
    n = len(edges)
    for i in range(n):
        for j in range(i+1, n):
            hp.heappush(pq, (edges[i][j], [i, j]))

    union = DSU(n)
    mst = []
    mstsum = 0
    while pq:
        wt, a = hp.heappop(pq)
        x, y = a[0], a[1]
        if(union.union(x, y)): 
            mst.append([x, y])
            mstsum += wt
    # print(mstsum)
            
    degree = [0]*n
    for a in mst:
        degree[a[0]]+=1
        degree[a[1]]+=1

    oddnodes = []
    for i in range(n):
        if degree[i]%2: oddnodes.append(i)

    # edit the input file and put the odd nodes alongwith the edges in it
    m = len(oddnodes)
    with open("blossom\input.txt", "w") as f:
        f.write(f"{m} {m*(m-1)//2}\n")
        for i in oddnodes:
            for j in oddnodes:
                if i==j: continue
                f.write(f"{i} {j} {edges[i][j]}\n")

    # matching = get_edges(mwpf())
    matching = mwpf()
    mst += matching
    euler = hierholzer(mst)

    ckt = []
    done = {}
    for node in euler:
        if node in done: continue
        done[node] = 1
        ckt.append(node)
    ckt.append(ckt[0])
    return ckt