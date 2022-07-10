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
  - [Compare iterative DFS and BFS](#compare-iterative-dfs-and-bfs)

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

Algorithms:
DFS

# Algorithms

## DFS

![DFS](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Depth-first-tree.svg/375px-Depth-first-tree.svg.png)
It is quite instructive to read the [pesudo code from Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search) and traverse manually to really understand this algorithm.  

It goes as deep as possible before bouncing back to span the left sub-tree, and then to the next child of the root node and plunge all the way again, and then bounce back to span the right sub-tree. 

> procedure DFS(G, v) is

>    label v as discovered

>    for all **directed** edges from v to w that are in G.adjacentEdges(v) do

>        if node w is not labeled as discovered then

>            recursively call DFS(G, w)

The DFS algorithm can be written using recursion with only 4 lines of code (excluding the return statement).  

Note that <span class="coding">if node not in visited</span> is important for undirected graph.  Without it, the recursion will never stop. 

The <span class="coding">discovered</span> in the psudo code is the list <span class="coding">visited</span> in the code.  We could have used a set for visited, but a set would not show the order of traversal.  

<div class="code-head"><span>code</span>DFS.py</div>

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
# or
graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['B','H'],
    'G': ['C', 'I'],
    'H': ['E'],
    'G': ['C']
}
def dfs(G, startNode,visited):
    # initial value
    if startNode not in visited:
        visited.append(startNode)
    # recurse
    for node in G[startNode]:
        if node not in visited:
            dfs(G, node, visited)
    return visited
print(dfs(graph, 'A', []))
# ['A', 'B', 'D', 'E', 'F', 'H', 'C', 'G']
``` 

The DFS can also be written using iteratively with short length, using psudo code from Wikipedia. 


> procedure DFS_iterative(G, v) is

>     let S be a stack

>     S.push(v)

>     while S is not empty do

>         v = S.pop()

>         if v is not labeled as discovered then

>             label v as discovered

>             for all edges from v to w in G.adjacentEdges(v) do 

>                 S.push(w)
The iterative DFS and the recursive DFS visit the neighbors of each node in the opposite order from each other: the first neighbor of v visited by the recursive variation is the first one in the list of adjacent edges, while in the iterative variation the first visited neighbor is the last one in the list of adjacent edges. 

In other words, while both are depth-first, the recursive goes from left to right whereas the iterative goes from right to left. 

<div class="code-head"><span>code</span>DFS.py</div>

```python
def dfs_iterative_r_to_l(G, startNode):
    # initialize
    visited = []
    S = list(startNode)
    while S:
        node = S.pop()
        if node not in visited:
            visited.append(node)
        # for all edges from v to w in G.adjacentEdges(v)
        for node in G[node]:
            if node not in visited:
                S.append(node)
    return visited
print(dfs_iterative_r_to_l(graph, 'A'))
# ['A', 'B', 'D', 'E', 'F', 'H', 'C', 'G']
```
DSF can be used for:
- Solving puzzles with only one solution, such as mazes.
- Finding connected components.
- Topological sorting.
- Finding the bridges of a graph.

## BFS

A BFS starts at some arbitrary node and explores its neighbors first **before moving to the next level** of neighbors, in a layer by layer fashion. 

BFS is a way to search graph broadly, and useful for finding the shortest path. 

BFS uses a *queue* data structure to track which node to visit next because the traversal is first in and first out (**FIFO**).  

In code below, I use **deque** in to keep track of the queue.  Deques are a generalization of stacks and queues.

From Python documentation: [Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.](https://docs.python.org/3/library/collections.html#deque-objects)

> Though list objects support similar operations, they are **optimized for fast fixed-length operations** and incur $$O(n)$$ memory movement costs for <span class="coding">pop(0)</span> and <span class="coding">insert(0, v)</span> operations which change both the size and position of the underlying data representation.

I could have used <span class="coding">extend</span> method instead of a for-loop to append each neighbor one by one because <span class="coding">extend</span> is much faster.  But there is no method that is the opposite of <span class="coding">extend</span> to pop multile items simutaneously.   So I stay with the for-loop. 

What the <span class="coding">bfs</span> function does is to visit nodes **layer by layer, and from left to right**. 

1. place starting node to the queue
2. while anything is in queue, pop the first item from the queue. 
3. if what's popped out has not been visited yet, add it to the
4.  <span class="coding">visited</span> is a set instead of a list. 


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
def bfs(G, startNode):
    # initialize
    Q = deque(startNode)
    visited = set()
    traversal = []

    while Q: # do until no more node left
        node = Q.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            Q.extend(G[node])
        
    return traversal

print(bfs(graph, 'A'))

``` 
Although the input graph is represented as if it is a directed graph, the BFS works fine if just as well.  
```python
graph ={
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E', 'F'],
    'C': ['A', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['B','H'],
    'G': ['C', 'I'],
    'H': ['E'],
    'G': ['C']
}
```
> The negative side is that we have to do more membership tests.  For example, when we are at the $$B$$ node, we have to ask if $$A$$ was in the <span class="coding">visited</span> even though we just came from A. 

## Compare iterative DFS and BFS

The non-recursive implementation is similar to breadth-first search but differs from it in two ways:

it uses a stack instead of a queue, and
it delays checking whether a vertex has been discovered until the vertex is popped from the stack rather than making this check before adding the vertex.
If G is a tree, replacing the queue of the breadth-first search algorithm with a stack will yield a depth-first search algorithm. For general graphs, replacing the stack of the iterative depth-first search implementation with a queue would also produce a breadth-first search algorithm, although a somewhat nonstandard one.[7]

