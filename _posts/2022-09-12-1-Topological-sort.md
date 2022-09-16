---
layout: post
tag : algorithm, graph, Khan's algoritm, topological sort, topological ordering
category: education
title: "Topological sort"
description: topological sort and the Khan's algorithm
author: Sarah Chen
image: images/posts/topologicalSortYes.PNG

---
Work in progress
# Problem
Given a directed hierchical structure, how do we flatten it to an array so that the directions are preserved?  

Recall my problem of trying to fly to Beijing, China, while Zero-Covid policy is going on in China, say I have combed through many many flights (edges) and stops (nodes) and have come up with the following possible path.  

![](../images/posts/myTrip.PNG)

How do I write down each of the valid routes in their right order with sentences? 

Before quoting any named algorithm, how would we solve the problem? 

We can write down my starting place first, since it does not have any dependencies. Then we look at where the directed edges lead to, if any of them do not have any dependencies, then we can write it down next. And so forth until we are done. 

My solution seems to resemble Khan's algorithm for topological sort: solving problem layer by layer: start from those that have no dependencies (no incoming edges), remove them and write them down (put them in a queue). Do it to the next batch.

Below images are taken from Washington University Professor Rao's CSE 326 Lecture 20.  The problem is similar, except names of cities have become course numbers.  We want to write down the list of course in their dependency order. 
![](../images/posts/topologicalSortCourses)

![](../images/posts/topologicalSortYes.PNG)

![](../images/posts/topologicalSortNot.PNG)

Here is a different way posing a similar problem:
![](https://en.wikipedia.org/wiki/Talk%3ATopological_sorting#/media/File:LampFlowchart.svg)

# Topological sort

![](../images/posts/topologicalSort_enqueue_deque.PNG)

<div class="code-head"><span>code</span>khans algorithm.py</div>

```py
from collections import deque
from networkx.generators import directed
from networkx.generators import random_graphs

# Make good adjacency list for testing (is DAG)
g = directed.gn_graph(100)
adj_list = g.adjacency_list()

# Make bad adjacency list for testing (is not DAG)
bad_g = random_graphs.fast_gnp_random_graph(100, 0.2, directed=True)
bad_adj_list = bad_g.adjacency_list()

from collections import deque
from networkx.generators import directed
from networkx.generators import random_graphs

# Make good adjacency list for testing (is DAG)
g = directed.gn_graph(100)
adj_list = g.adjacency_list()

# Make bad adjacency list for testing (is not DAG)
bad_g = random_graphs.fast_gnp_random_graph(100, 0.2, directed=True)
bad_adj_list = bad_g.adjacency_list()

def topsort(adj_list):
  def edges(): # Returns list of edges
    return [val for subl in adj_list for val in subl]

  def no_incoming(): # Generates set of all nodes with no incoming edges
    return set(range(0, len(adj_list))) - set(edges())
  
  L = []                       # L <- Empty list that will contain the sorted elements
  S = deque( no_incoming() )   # S <- Set of all nodes with no incoming edges
  
  while len(S) > 0:            # while S is non-empty do
    n = S.pop()                #   remove a node n from S
    L.append(n)                #   insert n into L
    
    for m in adj_list[n]:      #   for each node m with an edge e from n to m do
      adj_list[n].remove(m)    #     remove edge e from the graph
      
      if m in no_incoming():   #     if m has no other incoming edges then
        S.append(m)            #       insert m into S
  
  if len(edges()) > 0:         # if graph has edges then
    raise Exception("Not DAG") #   return error (graph has at least one cycle)
  else:                        # else
    return L                   #   return L (a topologically sorted order)

```

# Cycle detection

Khan's algorithm of topological sort can be used for cycle detection.    

## Leetcode 207. Course Schedule

**Problem**:  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where $$prerequisites[i] = [a_i, b_i]$$ indicates that you must take course $$b_i$$ first if you want to take course $$a_i$$.  For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses. Otherwise, return false.

* Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]

Output: true

* Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]

Output: false.  This is because to take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.  So it is impossible.



<div class="code-head"><span>code</span>course schedule explain version.py</div>

```py
def canDo(numCourses, prerequisites) -> bool:
  # numCourses: int, prerequisites: List[list[int]]
  adjList = {i: [] for i in range(numCourses)}
  for c, p in prerequisites:
    adjList[c].append(p)
  for k, v in adjList.items():
    print(k, v)

  visiting = set()
  def dfs(c):
    print("**************************\n%s"%c)
    if c in visiting:
      print("%s already visited, cycle detected!"%c)
      return False # cannot do it
    if adjList[c] == []:
      print("%s has no dependency/neighbor"%c)
      return True
    visiting.add(c)
    print("Adding %s to visiting"%c)
    for p in adjList[c]:
      print("checking on neighbor of %s: %s "%(c, p))
      if not dfs(p):
        return False
    print("completed visit of %s and removing it"%c)
    visiting.remove(c)
    adjList[c] = []
    return True
  for c in range(numCourses):
    if not dfs(c):
      return False
  print("Final adjList:", adjList)
  return True
```

```python
print("\n\n")
numCourses = 2
prerequisites = [[1, 0]]
print(canDo(numCourses, prerequisites))
# 0 []
# 1 [0] 
# **************************
# 0
# 0 has no dependency/neighbor
# **************************
# 1
# Adding 1 to visiting
# checking on neighbor of 1: 0
# **************************
# 0
# 0 has no dependency/neighbor
# completed visit of 1 and removing it
# Final adjList: {0: [], 1: []}
# True
```   


```python
print("\n\n")
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(canDo(numCourses, prerequisites))

# 0 [1]
# 1 [0]
# **************************
# 0
# Adding 0 to visiting
# checking on neighbor of 0: 1
# **************************
# 1
# Adding 1 to visiting
# checking on neighbor of 1: 0
# **************************
# 0
# 0 already visited, cycle detected!
# False
```

![](../images/posts/directedGraph.PNG)

```python
print("\n\n")
numCourses = 5
prerequisites = [[0,1],[0,2], [1, 3], [1,4], [3, 4]]
print(canDo(numCourses, prerequisites))
0 [1, 2]
1 [3, 4]
2 []
3 [4]
4 []
# **************************
# 0
# Adding 0 to visiting
# checking on neighbor of 0: 1
# **************************
# 1
# Adding 1 to visiting
# checking on neighbor of 1: 3
# **************************
# 3
# Adding 3 to visiting
# checking on neighbor of 3: 4
# **************************
# 4
# 4 has no dependency/neighbor
# completed visit of 3 and removing it
# checking on neighbor of 1: 4
# **************************
# 4
# 4 has no dependency/neighbor
# completed visit of 1 and removing it
# checking on neighbor of 0: 2
# **************************
# 2
# 2 has no dependency/neighbor
# completed visit of 0 and removing it
# **************************
# 1
# 1 has no dependency/neighbor
# **************************
# 2
# 2 has no dependency/neighbor
# **************************
# 3
# 3 has no dependency/neighbor
# **************************
# 4
# 4 has no dependency/neighbor
# Final adjList: {0: [], 1: [], 2: [], 3: [], 4: []}
# True
```



# Compare with Floyd's algorithm for topological sort

# Appendix

Code for plotting the directed group. If we want undirected graph, use <span class="coding">nx.Graph()</span> instead. 
<div class="code-head"><span>code</span>simple directed graph.py</div>

```py
import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(3, 4)
# explicitly set positions
pos = {0: (-4, 0), 2: (1, -2), 1: (3, 0),  3: (10, 0), 4: (12, -2)}
options = {
    "font_size": 36,
    "node_size": 3000,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 5,
    "width": 5,
}
nx.draw_networkx(G, pos, **options)
# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
```

Below are the shorter version of the course schedule code in this post. 
<div class="code-head"><span>code</span>course schedule.py</div>

```py
def canDo(numCourses, prerequisites) -> bool:
  # numCourses: int, prerequisites: List[list[int]]
  adjList = {i: [] for i in range(numCourses)}
  for c, p in prerequisites:
    adjList[c].append(p)
  visiting = set()
  def dfs(c):
    if c in visiting:
      return False # cannot do it
    if adjList[c] == []:
      return True
    visiting.add(c)
    for p in adjList[c]:
      if not dfs(p):
        return False
    visiting.remove(c)
    adjList[c] = []
    return True
  for c in range(numCourses):
    if not dfs(c):
      return False
  return True
```
# Future reading

[Washington University CSE 326 Lecture 20: Topo-Sort and Dijkstra’s Greedy Idea](https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf)

[Wiki Talk Topological Sorting](https://en.wikipedia.org/wiki/Talk%3ATopological_sorting)
 
