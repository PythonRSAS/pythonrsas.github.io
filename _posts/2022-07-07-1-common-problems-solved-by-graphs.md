---
layout: post
tag : data structure, algorithm, python
category: "Python for SAS"
title: "Common problems solved by graphs"
description: common problems that are solved using graph theory and basic algorithms like BFS and DFS
author: Sarah Chen
image: images/posts/photos/IMG_0869.JPG

---

- [Introduction](#introduction)
- [Problems](#problems)
  - [Shortest path problem](#shortest-path-problem)
  - [Negative cycles](#negative-cycles)
  - [Strongly connected components](#strongly-connected-components)
  - [Traveling salesman problem (TSP)](#traveling-salesman-problem-tsp)
  - [Minimum spanning tree (MST)](#minimum-spanning-tree-mst)
  - [Max flow (MST)](#max-flow-mst)
  - [Bridge](#bridge)
- [Algorithms](#algorithms)
  - [DFS](#dfs)
  - [BFS](#bfs)

# Introduction
Graphs, or networks, are useful for representing relationships. In this post, we learn common problems that are solved using graph theory, and a few of the most well-known algorithms. 

# Problems

## Shortest path problem

Given a weighted graph, find the shorted path from node A to node B with minimal cost (or weight).  

For example, Amazon delivery routes where heavy traffic has large weights.  And in credit risk rating models: **the least (or the most) likely path from rating A to rating B**. 

Algorithms:
- BFS (unweighted graph)
- DIjkstra's
- Bellman-Ford
- Floyd-Warshall,
- A*

## Negative cycles

Detect existence of negative cycles and location.  Negative cycle is like air bubles in a radiator heaters, or blood clots in our bodies, or black markets.  Negative cycle forms a cycle within itself. 

Negative cycles can mean good things too: a safe shelter in a hurricane, an arbitrage opportunity that take advantage of inconsistencies in markets (e.g. foreign exchange). 

Algorithms:
- Bellman-Ford
- Floyd-Warshall
  
## Strongly connected components 

Strongly connected components forms a cycle within itself, where every node in a given cycle can reach every other node in the same cycle.  They are like silos. 

Algorithms:
- Tarjan's
- Kosaraju's

## Traveling salesman problem (TSP) 

Kind of like the 7 bridge problem but with weights (or distances) on the edges.  What is the shortest possible route that he visits each city exactly once and returns to the origin city?

The TSP problem has important applications.  However it is *NP-hard* (computationally difficult). 

Algorithms:
- Held-Karp
- branch and bound, and many othe approximations
- 
## Minimum spanning tree (MST) 

Minimum spanning tree is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.  The MST has many applications. 

Algorithms:
- Kruskal's
- Prim's & Boruvka's
  
## Max flow (MST) 

With an infinite input source, how much "flow" can we push through the network?   Suppose the edges are elevators, escalators at in a building.  Flow represents the number of people can be moved up or down. 


## Bridge

A bridge is a single link between connected components (or local networks). 
Bridges are where the network vulnearabilities or weak points. 

# Algorithms

## DFS

BFS is a way to search graph broadly.   


## BFS

A BFS starts at some arbitrary node and explores its neighbors first **before moving to the next level** of neighbors, in a layer by layer fashion. 

Useful for finding the shortest path. 

BFS uses a *queue* data structure to track which node to visit next. 


<div class="code-head"><span>code</span>BFS.py</div>

```python
graph ={
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'G': []
}

from collections import deque
def bfs(grah, node):
    visited = []
    queue = deque()
    queue.append(node)
    visited.append(node)

    while queue:
        N = queue.popleft()
        print("popped ", N)
        print(grah[N])
        queue.extend(grah[N])
        visited.extend(graph[N])
        # print("\npopped ", N)
        # print(grah[N])
        # for n in graph[N]:
        #     if n not in visited:
        #         queue.append(n)
        #         visited.append(n)

bfs(graph, "A")

# popped  A
# ['B', 'C']
# popped  B
# ['D', 'E', 'F']
# popped  C
# ['G']
# popped  D
# []
# popped  E
# []
# popped  F
# ['H']
# popped  G
# []
# popped  H
# []
```
  