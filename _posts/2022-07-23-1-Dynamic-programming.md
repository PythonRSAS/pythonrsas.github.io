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

In the Fibonaci case, the time complexity is reduced to $$O(n)$$. 

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

Below we compare three different algorithms for this simple problem. 

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
n = 20
t0 = datetime.now()
print(fibDP(n))
print(datetime.now() - t0)

t1 = datetime.now()
print(fibRecurse(n))
print(datetime.now() - t1)

t2 = datetime.now()
print(fibLoop(n))
print(datetime.now() - t2)
# DP
# 6765
# 0:00:00
# Recurse
# 6765
# 0:00:00.016181
# Loop
# 6765
# 0:00:00.015625
```

We should add validation code as below to capture invalid inputs. 

```python
if not(isinstance(n, int) and n > 0):
    raise ValueError(f'positive integer expected, got "{n}"')
```

# Finding the shortest path


# Reference
[CMU lecture](https://www.cs.cmu.edu/~avrim/451f09/lectures/lect1001.pdf)