---
layout: post
tag: recursion, dynamic programming, memorize
category: "Python for SAS"
title: "Dynamic programming"
description: dynamic programming to solve overlapping sub-problems in recursion
author: Sarah Chen
image: images/posts/photos/sf/IMG-0956.JPG
---
<figure> 
   <img src="{{"/images/posts/photos/sf/IMG-0956.JPG"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 

> Dynamic programming (DP) is used to eliminate overlapping sub-problems in recursions.  

In comparison with recursion, it reduces time complexity from exponential to polynomial. 

But increases space complexity. 

# What is dynamic programming

Dynamic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s.****

We can see DP in two ways: an algorithm of its own, or as an improvement to recursion on the repetitive call problem. 

On its own, from Wikipedia: [[...] it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively.](https://en.wikipedia.org/wiki/Dynamic_programming).

In computer science, if a problem can be solved *optimally* by breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is said to have *optimal substructure*.

# Problem with naive recursion

The problem with many recursion problems is that they have over-lapping sub-problems.  These redundant calls make these recursion problems exponential in time complexity.  In the case of Fibonaci numbers, it is $$O(2^n)$$. 

As shown in the image from Wikipedia below on the recursive call to the Fibonaci recursion.   There are two $$F_3$$ and $$F_2$$ just for the computation of $$F_5$$.  

$$F_5 = F_4 + F_3$$

$$F_4 = F_3 + F_2$$

$$F_3 = F_2 + F_1$$

The recursion looks like an expanding tree, opposite of binary search tree.   We can guess its time complexity is $$O(2^n)$$. 


![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Fibonacci_dynamic_programming.svg/162px-Fibonacci_dynamic_programming.svg.png)

Below code uses recursion to compute Fibonaci numbers.  When $$n$$ is small, this is not an issue, but it takes longer and longer time when $$n$$ increases. 

<div class="code-head"><span>code</span>fibonanci using recursion.py</div>

```py

def fibRecurse(n):
    if n <= 1:
        return n
    else:
        return fibRecurse(n -1) + fibRecurse(n -2)
```

# How dynamic programming solves the problem

The idea is very simple. If Mr. Bellman did not come up with in 1950s, someone surely would have come up with it before long as well.  

Dynamic programming solves the problem by **remembering** those we have alredy computed so that those overlapped sub-problems do not have to be reworked again and again.  All subproblems only need to be computed once.  When we need them, we look them up from memory in constant time.  

## Top-down DP

In the Fibonaci case, using DP with recursion (top-down approach), the time complexity is reduced to $$O(n)$$, while space complexity goes up to $$O(n)$$ because of memorizing each number. 

Although this problem seems super easy, I did make a few mistakes: 

* **Mistake 1**: I coded <span class="coding">if memo[n]</span>, thinking that it would have worked as boolean.   But no!  It gave me a key error.

* **Mistake 2**:: I coded <span class="coding">memo[n] = memo[n - 1] + memo[n - 2]</span>.  Oops!

In fact, the whole *invention* is **<span class="coding"> memo[n] = fibDP(n -1) + fibDP(n -2)</span>**.

If the nth Fibonaci number is in memo, then return it.  

**Otherwise we recursely compute it and save it to memo** before return it. 

<div class="code-head"><span>code</span>fibonanci using dynamic programming.py</div>

```py

def fibDP(n, memo = {1: 1, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibDP(n -1) + fibDP(n -2)
    return memo[n]
print(fibDP(10))
# 55
```

If we print the memo at the start of the function, we will get the following:

```python
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1}
{1: 1, 2: 1, 3: 2}
{1: 1, 2: 1, 3: 2, 4: 3}
{1: 1, 2: 1, 3: 2, 4: 3, 5: 5}
{1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8}
{1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13}
{1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21}
{1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34}
```

Furthermore, when we call the function again, it remembers all the numbers it previously collected.   

Tying <span class="coding">fibDP?</span>, we see that the function has *grown up*.  

It is still the function we initially defined, but the memo has taken on a life of its own.  That's one of the beauties of dynamic programming:

> **We only need to compute it once**

```python
print(fibDP(2))
# 1
# {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
fibDP?
# Signature: fibDP(n, memo={1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55})
# Docstring: <no docstring>
```

## Bottom-up DP

The bottom-up DP is exactly the same as the top-down DP in compution: it is recursion unwind or unrolled.  It is how we will compute it on the stack.  

The bottom-up DP has one practical advantage: we can **reuse the same memory space for only the last two numbers: current and previous**.  

Current and previous can get us to the next number. 

<div class="code-head"><span>code</span>DP.py</div>

```py

# compare dynamic proramming with recursion and loops

def fibDPLoop(n):   
    if n in {0, 1}:
        return n
    previous, current = 0, 1  # 0 is not a Fibnonaci number
    for _ in range(2, n+1):
        current, previous = previous + current, current
    return current
```

# Run time

Run time can be summarized in this genearal formula:

$$\text{time = Number of subproblems}*\frac{time}{subproblem}$$

Below we compare three different algorithms for this simple problem on their running time.  Recursion is the slowest one by far. 

Note that the iterative loop or bottom-up method has $$O(1)$$ space complexity as we reuse the name to represent the previous number. 

<div class="code-head"><span>code</span>compare algorithms.py</div>

```py

# compare dynamic proramming with recursion and loops
from datetime import datetime
n = 30
print("DP Recusion")
t0 = datetime.now()^M
print(fibDP(n))^M
print(datetime.now() - t0)^M
print("Recursion")
t1 = datetime.now()^M
print(fibRecurse(n))^M
print(datetime.now() - t1)^M
print("DP Loop")
t2 = datetime.now()^M
print(fibDPLoop(n))^M
print(datetime.now() - t2)
# DP Recusion
# 832040
# 0:00:00
# Recursion
# 832040
# 0:00:02.566668
# DP Loop
# 832040
# 0:00:00
```

# Subarray with the greatest sum

We are given an array and asked to find the subarray with the greatest sum.  Note that subarrays need to be contiguous.

Initially I thought, well, why don't we just sum all the positive numbers.  But, no. 

## Number of subarrays

Since the subarray has to be contiguous, we can *look at it as one single element* of the given array. 

One element: $${n\choose 1}$$

Two elements: $${n-1\choose 1}$$

Three elements: $${n-2\choose 1}$$

Four elements: $${n-3\choose 1}$$

k elements: $${n-k+1\choose 1}$$

So, the number of subarrays is $$n + (n-1) + (n-2) + ...+1$$.

That amounts to our familar $$\frac{(n+1)*n}{2}$$

## Brute force method

Since there are $$\frac{(n+1)*n}{2}$$ subarrays, and each takes $$O(n)$$ to sum, the time complexity is $$O(n^3)$$. 

The loop "for i in [0, 1, 2, ..., n-1]" gives the starting index of subarrays.

The loop "for j in [i, ..., n-1]" gives the ending index.

The loop " for k in (i, ..., j) sums the elements of subarrays. 

## Memorizing method (DP)

Each time when we enounter overlapping subproblems, it is time to consider dynamic programming. 

When we sum the $$ith$$ to the $$jth$$ element, do we really have to start from the beginning $$ith$$?  If we store cumulative sums, then we just have to look it up like we did in the Fibonaci problem. 

<div class="code-head"><span>code</span>number of subarrays DP.py</div>

```py
import itertools
def maxSubArrayDP(A):
    minSum = maxSum = 0
    print(list(itertools.accumulate(A)))
    for runningSum in itertools.accumulate(A):
        minSum = min(minSum, runningSum)
        maxSum = max(maxSum, runningSum - minSum)
    return maxSum
```


# Shortest path

From city A to city B, what is the shortest path?   

In between A and B, there are many cities and many choices.  Hence many overlapping subproblems, which means it is a candidate for DP to optimize upon. 

## Recursive thinking
The shortest path reaching B must be the shortest path of reaching one of B's neighbors plus the final leg.  

Which one is it?  We do not know.  We compute all.

Likewise, the shortest path of reaching a neighbor of B, say X, is the shortest path of (reaching X's neighbor + the distance from this neighbor to X).  And so on. 

In code below, the input is a set of nodes expressed as list of lists [[x1,y1],..., [x2,y2]], where $$x_i, y_i$$ are coordinates on the plane.  We use the coordinates to compute distance. 

The distances are stored in a dictionary, which is working as an adjacency list. 

Nodes are represented by $$0, 1, ..., N$$. 

For $$x_i, y_i$$, adj[i] is a list of lists, in the format of <span class="coding">[distance, j]</span> to all neighbors of  $$x_i, y_i$$.   The reason why <span class="coding">[distance, j]</span> instead of <span class="coding">[j, distance]</span> is that we are using the *heapq* moduel.  The <span class="coding">heapq.heappop</span> method by default pops the minimum according to the first number.  So we want to put distance first. 

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
    # build adjacency list of [cost, neighboring node] for all nodes
    adj = {i:[] for i in range(N)} # i: list of [cost, neighboring node]
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
    minH = [[0, 0]]  # starting node, distance to itself is 0
    while len(visit) < N:
        cost, i = heapq.heappop(minH) # heappop maintains min heap structure
        if i in visit:
            continue
        sum += cost
        visit.add(i)
        for neiCost, nei in adj[i]:  # push neighbors of i into minH if they are not yet visited. 
            if nei not in visit:
                heapq.heappush(minH, [neiCost, nei]) # heappush maintains min heap structure
    return sum 

A = [[0,0], [2,2], [3, 10], [5,2], [7,0]]
print(minCostConnect(A))
```

## Bottom-up thinking

Bottom-up thinking is identical to the top-down one, except that we start with A instead of B. 


# Reference
[CMU lecture](https://www.cs.cmu.edu/~avrim/451f09/lectures/lect1001.pdf)