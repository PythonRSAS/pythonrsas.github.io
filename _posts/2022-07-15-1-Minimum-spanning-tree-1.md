---
layout: post
tag : data structure, algorithm, python
category: "Python for SAS"
title: "Common problems solved by graphs"
description: common problems that are solved using graph theory and basic algorithms like BFS and DFS
author: Sarah Chen
image: images/posts/photos/IMG_0869.JPG

---

# Introduction
Minimum spanning tree is a **subset** of the edges of a connected, edge-weighted graph that connects all the nodes together, without any cycles and with the minimum possible total edge weight.  

> Spanning means to connect all nodes. 
> Tree means no cycles. 

Algorithms:
- Kruskal's
- Prim's & Boruvka's
  
# Prim's algorithm
Prim's method somehow reminds me of the [Metropolis algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm) even though I have not read anything that says they are related.   

What it reminds me of are 2 things:
1. Start with an arbitrary node
2. At the node where we are, use a metric to pick the next node.  In Prim's, it is the minimum cost edge.  In Metroplis, it is the one with the highest probability. 


<div class="code-head"><span>code</span>mst_prim.py</div>

```python
import heapq
def minCostConnect(XY) -> int:
    """
    input XY is a set of nodes expressed as list of lists [[x1,y1],..., [x2,y2]]
    build adjacency list, a dictionary with nodes as keys, and their distance to other nodes as values in list [cost, node]
    pick an arbitrary starting point and place it in minH (list of lists, maintained in the min heap data structure order)
    keep track of visited
    as long as visited is not completed, pop the minH for the node with the minimum cost, and add it to the sum.
    for the one that just got popped, push all its adjacent list [cost, node] into minH if the neighbor has not been visited
    """
    N = len(XY)
    adj = {i:[] for i in range(N)} # i: list of [cost, node]
    print("adj ", adj)
    for i in range(N):
         x1, y1 = XY[i]
         for j in range(i + 1, N): # for loop could be in prim's algo 
             x2, y2 = XY[j]
             distance = abs(x1 - x2) + abs(y1- y2)
             adj[i].append([distance, j]) # build adjacency list
             adj[j].append([distance, i])
    print("adj ", adj)
    # Prim's
    sum = 0
    visit = set()
    minH = [[0, 0]] 
    while len(visit) < N:
        cost, i = heapq.heappop(minH) # heappop maintains min heap structure
        if i in visit:
            continue
        sum += cost
        visit.add(i)
        for neiCost, nei in adj[i]:
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei]) # heappush maintains min heap structure
    return sum 

A = [[0,0], [2,2], [3, 10], [5,2], [7,0]]
print(minCostConnect(A))
```

The reason why we can use heapqpop and heapqpush with lists is because it compares the first element of the lists. In the code above, [cost, node], we have placed cost before node in list.  Therefore, only costs are compared, and the minimum cost is popped from the min heap. 
<!-- https://stackoverflow.com/questions/45892736/python-heapq-how-do-i-sort-the-heap-using-nth-element-of-the-list-of-lists -->
# A
<div class="code-head"><span>code</span>lessThan.py</div>

```python
A = [[0,0], [2,2], [3, 10], [5,2], [7,0]]
print(minCostConnect(A))


n = [[1, 5, 93],
    [2, 6, 44],
    [4, 7, 45],
    [6, 3, 12]]
heapq.heapify(n)
print(n)
class MyList(list):
    def __lt__(self, other):
        return self[2] < other[2]

q = [MyList(x) for x in n]
```