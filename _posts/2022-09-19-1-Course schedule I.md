---
layout: post
tag : algorithm, graph, Khan's algoritm, topological sort, topological ordering, cycle detection, DAG, leetcode, course schedule, graphlib, networkX
category: education
title: "Course schedule I"
description: topological sort, DFS, Khan's algorithm and cycle detection
author: Sarah Chen
image: images/posts/topologicalSortYes.PNG

---
- [Leetcode 207. Course Schedule](#leetcode-207-course-schedule)
- [Appendix](#appendix)
- [Reference](#reference)

# Leetcode 207. Course Schedule

**Problem**:  There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where $$prerequisites[i] = [a_i, b_i]$$ indicates that you must take course $$b_i$$ first if you want to take course $$a_i$$.  For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1. Return true if you can finish all courses. Otherwise, return false.

* Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]

Output: true

* Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]

Output: false.  This is because to take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.  So it is impossible.

One of the solutions is to use topological sort with DFS.  The

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

Below is the shorter version of the course schedule code in this post. 
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

# Reference

[Washington University CSE 326 Lecture 20: Topo-Sort and Dijkstra’s Greedy Idea](https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf)

[Depth-First Search](https://courses.engr.illinois.edu/cs473/sp2017/notes/06-dfs.pdf)

[Arthur Khan, Topological sorting of large networks, Communications of the ACMVolume 5 Issue 11 Nov. 1962 pp 558–562](https://dl.acm.org/doi/10.1145/368996.369025)

[NetworkX](https://networkx.org/documentation/latest/auto_examples/basic/plot_simple_graph.html#sphx-glr-auto-examples-basic-plot-simple-graph-py)

[Wiki Talk Topological Sorting](https://en.wikipedia.org/wiki/Talk%3ATopological_sorting)
 
[Topological Sort Kahn's algorithm BFS or DFS](https://stackoverflow.com/questions/69523839/topological-sort-kahns-algorithm-bfs-or-dfs)