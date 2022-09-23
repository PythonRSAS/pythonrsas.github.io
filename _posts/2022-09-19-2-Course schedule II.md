---
layout: post
tag : algorithm, graph, Khan's algoritm, topological sort, topological ordering, cycle detection, DAG, leetcode, course schedule
category: education
title: "Course schedule II"
description: topological sort, DFS, Khan's algorithm and cycle detection
author: Sarah Chen
image: images/posts/topologicalSortYes.PNG

---
- [Compare with Floyd's algorithm for topological sort](#compare-with-floyds-algorithm-for-topological-sort)
- [Appendix](#appendix)


## Leetcode 210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

<div class="code-head"><span>code</span>course schedule II.py</div>

```py
from collections import defaultdict

def build_graph(edges, n):
    g = defaultdict(list)
    for i in range(n):
        g[i] = []
    for a, b in edges:
        g[b].append(a)
    return g

def topsort(g, n):
    # -- Step 1 --
    indeg = [0] * n
    for u in g:
        for v in g[u]:
            indeg[v] += 1


    # -- Step 2 --
    q = []
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    # -- Step 3 and 4 --
    result = []
    while q:
        x = q.pop()
        result.append(x)
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)

    return result

def courses(n, edges):
    g = build_graph(edges, n)
    ordering = topsort(g, n)
    # -- Step 5 --
    has_cycle = len(ordering) < n
    return [] if has_cycle else ordering
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

