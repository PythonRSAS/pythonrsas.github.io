---
layout: post
tag : data structure, greedy algorithm, python, search, dynamic programming
category: "Python for SAS"
title: "Dijkstra algorithm shortest path between"
description: algorithm for finding shortest (or lowest cost) between any two nodes in a graph
author: Sarah Chen
image: images/posts/photos/IMG_0868.JPG

---

# Introduction
Obviously to be able to find the shortest distance or cost between any two nodes in a graph is a very useful thing. 

Dijkstra's algorithm to find the shortest path between two points. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. 

I find it more intuitive if I think in terms of driving from one place to another. I look at the map, and compare the different routes in distance and traffic (plus toll).  I choose the route with the shortest distance (unless traffic is bad).  

<!-- When there are many routes, then I can iteratively  -->

  
# Dijkstra's algorithm
Dijkstra's method has two steps: 
1. Update estimates
2. Choose next node 

Initially all distances are labeled as $$\infinity$$, except the starting node.

<div class="code-head"><span>code</span>Dijkstra.py</div>

```python
import heapq
def minCostConnect(XY) -> int:
    """
    input XY is a set of nodes expressed as list of lists [[x1,y1],..., [x2,y2]]
    build adjacency list, a dictionary with nodes as keys, and their distance to other nodes as values in list [cost, node]
    pick an arbitrary starting point and place it in minH (list of lists, maintained in the min heap data structure order)
    keep track of visited
    as long as visited is not completed, pop the minH for the node with the minimum cost, and add it to the sum.
    for the one that just got popped, push all its adjacent list [cost, node] into minH if the neighbor has not been visited. 
    The visit method is exactly the same as BFS.
    """
    N = len(XY)
    adj = {i:[] for i in range(N)} # i: list of [cost, node]
    print("adj ", adj)
    for i in range(N):
         x1, y1 = XY[i]
         for j in range(i + 1, N): # for loop could be in Dijkstra's algo 
             x2, y2 = XY[j]
             distance = abs(x1 - x2) + abs(y1- y2)
             adj[i].append([distance, j]) # build adjacency list
             adj[j].append([distance, i])
    print("adj ", adj)
    # Dijkstra's
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

# Reference
## Videos
[How Dijkstra's Algorithm Works](https://www.youtube.com/watch?v=EFg3u_E6eHU)
[Graphs: Dijkstra's Minimal Spanning Tree and Dijkstra's Shortest Path](https://www.youtube.com/watch?v=i4W8WgTuGTE&t=288s)
