---
layout: post
tag: recursion, dynamic programming, memorize
category: education
title: "Dynamic programming"
description: dynamic programming to solve repetitive calls (overlapping sub-problems) in recursion
author: Sarah Chen
image: images/posts/photos/sf/IMG_0957.jpg
---
<figure> 
   <img src="{{"/images/posts/photos/sf/IMG_0957.jpg"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 


> Dynamic programming (DP) is used to eliminate repetitive calls (overlapping sub-problems) in recursions.  

In comparison with recursion, it reduces time complexity from exponential to polynomial. 

But increases space complexity. 

# What is dynamic programming

Dynamic programming is both a mathematical optimization method and a computer programming method. The method was developed by Richard Bellman in the 1950s.

We can see DP in two ways: an algorithm of its own, or as an improvement to recursion on the repetitive call problem. 

On its own, from Wikipedia: [In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points in time do often break apart recursively. Likewise, in computer science, if a problem can be solved optimally by breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is said to have optimal substructure.](https://en.wikipedia.org/wiki/Dynamic_programming).

# Problem with recursion

The problem with some recursion problems is that they have over-lapping sub-problems.  These redundant calls make these recursion problems exponential in time complexity.  In the case of Fibonaci numbers, it is $$O(2^n)$$. 

As shown in the image from Wikipedia below on the recursive call to the Fibonaci recursion.   There are two $$F_3$$ and $$F_2$$ just for the computation of $$F_5$$.  

$$F_5 = F_4 + F_3$$

$$F_4 = F_3 + F_2$$

$$F_3 = F_2 + F_1$$

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

Dynamic programming solves the problem by remembering those we have alredy computed.  When we need them, we look them up in constant time so that they don't need to be computed again.  

In the Fibonaci case, the time complexity is reduced to $$O(n)$$, while space complexity goes up to $$O(n)$$. 

<div class="code-head"><span>code</span>fibonanci using dynamic programming.py</div>

```py

def fibDP(n, cache = {}):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
    elif n not in cache:
        cache[n] = fibDP(n -1) + fibDP(n -2)
    return cache[n]
```

## Compare run time

Below we compare three different algorithms for this simple problem on their running time.  Recursion is the slowest one by far. 

Note that the iterative loop or bottom-up method has $$O(1)$$ space complexity as we reuse the name to represent the previous number. 

<div class="code-head"><span>code</span>compare algorithms.py</div>

```py

# compare dynamic proramming with recursion and loops

def fibLoop(n):   
    if n in {0, 1}:
        return n
    
    F_1, F = 0, 1
    for _ in range(2, n+1):
        F_1, F = F, F_1 + F
    return F

from datetime import datetime
n = 30
print("DP")
t0 = datetime.now()^M
print(fibDP(n))^M
print(datetime.now() - t0)^M
print("Recursion")
t1 = datetime.now()^M
print(fibRecurse(n))^M
print(datetime.now() - t1)^M
print("Loop")
t2 = datetime.now()^M
print(fibLoop(n))^M
print(datetime.now() - t2)
# DP
# 832040
# 0:00:00
# Recursion
# 832040
# 0:00:02.566668
# Loop
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

So, the number of subarrays is $$n + (n-1) + (n-2) + ...+1$$
That amounts to our familar $$\frac{(n+1)*n}{2}$$

## Brute force method

Since there are $$\frac{(n+1)*n}{2}$$ subarrays, and each takes $$O(n)$$ to sum, the time complexity is $$O(n^3)$$. 

The loop "for i in [0, 1, 2, ..., n-1]" gives the starting index of subarrays.

The loop "for j in [i, ..., n-1]" gives the ending index.

The loop " for k in (i, ..., j) sums the elements of subarrays. 

## Memorizing method (DP)

Each when we enounter overlapping subproblems, it is time to consider dynamic programming. 

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


# Finding the shortest path


# Reference
[CMU lecture](https://www.cs.cmu.edu/~avrim/451f09/lectures/lect1001.pdf)