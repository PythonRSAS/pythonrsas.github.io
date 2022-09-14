---
layout: post
tag : algorithm, graph, Khan's algoritm, topological sort, topological ordering
category: education
title: "Topological sort"
description: topological sort and the Khan's algorithm
author: Sarah Chen
image: images/posts/topologicalSortYes.PNG

---

# Problem
Given a directed hierchical structure, how do we flatten it to an array so that the directions are preserved?  

Recall my problem of trying to fly to Beijing, China, given so many flights (edges) and stops (nodes), what are the valid routes? How do I write each of the valid routes in their right order with sentences? 

![](../images/posts/Air-route-network-connected-with-PEK-in-2018.jpg)

Below is taken from a course slide.  The problem is similar, except names of cities have become course numbers.  We want to write down the list of course in their dependency order. 
![](../images/posts/topologicalSortCourses)


![](../images/posts/topologicalSortYes.PNG)

![](../images/posts/topologicalSortNot.PNG)

Here is a different way posing a similar problem:
![](https://en.wikipedia.org/wiki/Talk%3ATopological_sorting#/media/File:LampFlowchart.svg)

Before quoting any named algorithm, how would we solve the problem?  

We can write down the destination first, since it does not have any dependencies. Then we look at its "children", if any of them do not have any dependencies, then we can write it down next. And so forth. 

To make problem as simple as possible (albeit unrealistic), I would focus on monetary cost only and pick one of the cities, say Beijing, as my destination.  And since tickets are usually sold as round trip prices, they can be treated as undirected edges in a graph. 

Then I will get the routes for each airlines that currently flies to Beijing, costs of tickets and associated datetime. Let's say Tokyo, Hong Kong, London, Seul, NYC and a few others. The costs are $1000, $500, $9000, $20000.  Although from NYC the flight is non-stop, the cost is very high.   So I choose the cheapest, which is Hong Kong.  Next, I get the data for all the reachable places from Hong Kong and their respective cost and time.  If Hong Kong to Tokyo is $300.  Then I will update the cost from Beijing to Tokyo to be $800 ($500 + $300) to replace the original price of $1000.  

I will continue this method until I reversely track the path to NYC, where I am currently.  In the process of acquiring data and updating costs of getting to the cities, I would have known the cheapest costs to each and every place from source. 

My solution seems to resemble Dijstra's algorithm: solving problem layer by layer: starting from a single source, pick the best one among all the reachable ones.  In each layer, update all previous ones if needed and pick the best one to move on until reaching the destination.  

# Topological sort

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

# Compare with Floyd's algorithm for topological sort


# Bellman-Ford algorithm
Bellman-Ford is a single source shortest path (SSSP) algorithm for weighted directed graph.  But Bellman-Ford is not the ideal SSSP because of time complexity $$O(E*V)$$.  

Like Dijkstra's algorithm, [Bellman–Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm) uses updating, in which approximations to the correct distance are replaced by better ones until they eventually reach the solution. In both algorithms, the approximate distance to each node is always an overestimate of the true distance, and is replaced by the minimum of its old value and the length of a newly found path. 

However, Dijkstra's algorithm uses a priority queue to greedily select the closest node that has not yet been processed, and performs this update process on all of its **outgoing edges**; by contrast, the Bellman–Ford algorithm **updates all the edges**, and does this $$V-1$$ times, where $$V$$ is the number of nodes in the graph. In each of these repetitions, the number of nodes with correctly calculated distances grows, from which it follows that eventually all nodes will have their correct distances. This method allows the Bellman–Ford algorithm to be applied to a wider class of inputs than Dijkstra. The intermediate answers depend on the order of edges relaxed, but the final answer remains the same.


## Bellman-ford updating all edges method

For this problem, we cannot apply Bellman-Ford naively because of at most k stops. 

I like to convert the information given into a table, G.  

start | destination| price
---------|----------|---------
 0 | 1 | 100
 1 | 2 | 100
 0 | 2 | 500

We will use the info from the given table to update prices to all nodes, collected in an array X. 

So, given G, where we start (origin) and where we want to go (target), we want to update X for the cheapest price, k times. 

We use a double-loop.  The outer loop is k+1 times; the inner scans through the edges. 

For this problem, it is critical that we make a copy of X in each outer loop: <span class="coding">tmpX = X.copy()</span> because we want to update X only once at the end of each outer loop, and the fact that we need to check the current price (before updating) from the X table:

```python
if X[s] == float("inf"):
    continue
```

And,
```python
if tmpX[d] > X[s] + p:
    tmpX[d] = X[s] + p
```
<div class="code-head"><span>code</span>cheapest_upto_k_stops_non_greedy.py</div>

```py
def findCheapestPrice(n, G, origin, target, k) -> int:
    # n= number of nodes in graph
    # G=graph represented with compact list of list (compact matrix)
    X = [float("inf")] * n # X= list of prices to all nodes
    X[origin] = 0 # starting place
    for i in range(k + 1):
        tmpX = X.copy()
        for s, d, p in G:
            # s=source, d=destination (edges), p=price
            # print("s, d, p:",s, d, p)
            if X[s] == float("inf"):
                continue
            if tmpX[d] > X[s] + p:
                tmpX[d] = X[s] + p
        X = tmpX # update only once per full scan
    return -1 if X[target] == float('inf') else X[target]

# examples
n = 3
G = [[0,1,100],[1,2,100],[0,2,500]]
origin = 0
target = 2
k = 1
print("The cheapest price is ", findCheapestPrice(n, G, origin, target, k))
# s, d, p: 0 1 100
# s, d, p: 1 2 100
# s, d, p: 0 2 500
# s, d, p: 0 1 100
# s, d, p: 1 2 100
# s, d, p: 0 2 500
# The cheapest price is 200

# example 1
n = 4
G = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
origin = 0
target = 3
k = 1
print("The cheapest price is ", findCheapestPrice(n, G, origin, target, k))
# s, d, p: 0 1 100
# s, d, p: 1 2 100
# s, d, p: 2 0 100
# s, d, p: 1 3 600
# s, d, p: 2 3 200
# s, d, p: 0 1 100
# s, d, p: 1 2 100
# s, d, p: 2 0 100
# s, d, p: 1 3 600
# s, d, p: 2 3 200
# The cheapest price is  700
```

# Future reading

[Bellman Ford](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

[Interview with Dijkstras](https://cacm.acm.org/magazines/2010/8/96632-an-interview-with-edsger-w-dijkstra/fulltext?mobile=false)

[Washington University CSE 326 Lecture 20: Topo-Sort and Dijkstra’s Greedy Idea](https://courses.cs.washington.edu/courses/cse326/03wi/lectures/RaoLect20.pdf)

[Wiki Talk Topological Sorting](https://en.wikipedia.org/wiki/Talk%3ATopological_sorting)
 
