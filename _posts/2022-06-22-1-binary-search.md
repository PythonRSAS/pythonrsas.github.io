---
layout: post
tag : binary search algorithm, binary search problems
category: "Python for SAS"
title: "binary search"
description: binary search algorithm implementation in Python and the bisect library
author: Sarah Chen
image: images/posts/photos/IMG_0874.JPG

---

# Binary search the basics

Given a sorted array of integers $$A$$, we want to find a number, which we call "target", or $$x$$  The code should return the index of target, and return $$-1$$ if not found. 

The devide and conquer method is implemented as follows:
1. We begin searching the entire array of numbers, defined by the index for the smallest number and the index of the biggest number.         
2. Compute the mid point index. 
>  <span class="coding">l + (r - l) // 2</span> and <span class="coding">(r + l) // 2</span> are equivalent, in computation, they have a subtle difference: the latter may cause overflow (even though it may never happen) in some languages (not in Python because Python integers are unbounded).
3. We compare the target with the $$A[m]$$:
   1. if the target $$>A[m]$$, then we can disregard the left half $$->$$ <span class="coding">l</span> moves to <span class="coding">m + 1</span>, $$\text{mid point index} + 1$$
   2. else if the target $$<A[m]$$, then we drop the right half $$->$$ <span class="coding">r</span> moves to <span class="coding">m - 1</span>, $$\text{mid point index} - 1$$
   3. else it means the target is equal to $$A[m]$$, we return it and get out of the loop
4. Continue the search from step 1 until loop is exhausted 

> The condition for the <span class="coding">while</span> loop is <span class="coding">while l <= r</span>.  Missing the $$=$$ sign the algorithm will be wrong in this particular set up.  For example, if you search for the boundary values, it would return $$-1$$ erroneously. 

For an one-element array, [1], or [100], the <span class="coding">while</span> loop would not have even run if we did not have the $$=$$ sign because the boundary indices would be the same. 

So, when we check our code, we can test these extreme cases:
* one-element array
* target is one of the boundary values

> Note that if the target is found, it will be returned and the function call will stop immediately. 

<div class="code-head"><span>code</span>binary search.py</div>

```py
def bSearch(A, target):
    N = len(A)
    l = 0
    r = N - 1
    while l <= r:
        m = l + (r - l) // 2 # not writing it as (r + l) // 2 to prevent overflow
        if target > A[m]:
            l = m + 1
        elif target < A[m]:
            r = m - 1
        else:
            return m # return and stop the function
    return - 1

lt = [1, 2, 5, 7, 8, 10, 20]
print(bSearch(lt, 7))

```

## Problem 2: first and last position in sorted array

Now, instead of finding the index of the target (assuming no duplicates), we want to find the first and the last position of the target.  

<div class="code-head"><span>code</span>binary search variation.py</div>

```py
def searchRange(A, target):
    small = bSearch(A, target, True)
    big = bSearch(A, target, False)
    return [small, big]
    
def bSearch(A, target, smallBias):
    ```
    smallbias: True means we are searching for the first & False means searching for the last
    ```
    N = len(A)
    l = 0
    r = N - 1
    idx = -1
    while l <= r:
        m = l + (r - l )//2
        if target > A[m]:
            l = m + 1
        elif target < A[m]:
            r = m - 1
        else:
            idx = m
            # return idx for regular binary bSearch
            if smallBias:
                r = m - 1
            else:
                l = m + 1

    return idx

lt = [1]
lt2 = [1,1,1, 2,2, 5, 7, 8, 10, 20, 30, 100]
print(searchRange(lt, 1))
print(searchRange(lt2, 2))
```    

# The bisect library

The [bisect library](https://docs.python.org/3/library/bisect.html) has some functions that perform variations of binary search. 
> The source code may be most useful as a working example of the algorithm (the boundary conditions are already right!).

The <span class="coding">bisect_left</span> function returns the leftist index of the value we search, if it exist in the input array. If value we search does not exist in the array, then the function gives the index position the insertion point where it would be:
![bisect_left, bisect, bisect_right](../images/posts/bisect.PNG)

The results show that:
1. when x is not in the input array, bisect_left, bisect, and bisect_right all produce the same result: the insertion point
2. when x is in the input array, biset_left gives the index of the leftmost one, while bisect and bisect_right give the index of the number adjacent to the rightmost x. 

<div class="code-head"><span>code</span>bisect.py</div>

```py
from bisect import bisect, bisect_left, bisect_right
In [61]: list1 = [1, 4, 4, 5, 6]
    ...: x = 3
    ...: print(bSearch(list1, x))
    ...: print(bisect_left(list1, x))
    ...: print(bisect(list1, x))
    ...: print(bisect_right(list1, x))
    ...:
-1
1
1
1

In [62]: list1 = [1, 4, 4, 5, 6]
    ...: x = 4
    ...: print(bSearch(list1, x))
    ...: print(bisect_left(list1, x))
    ...: print(bisect(list1, x))
    ...: print(bisect_right(list1, x))
    ...:
2
1
3
3

In [63]: list1 = [1, 4, 4, 5, 6, 6, 6]
    ...: x = 6
    ...: print(bSearch(list1, x))
    ...: print(bisect_left(list1, x))
    ...: print(bisect(list1, x))
    ...: print(bisect_right(list1, x))
    ...:
5
4
7
7

```

The following snippets are modified from the bisect page.


Action | Math expression | Function
---------|----------|---------
 **Locate the leftmost value exactly equal to x**  | $$min\{i\| A[i] = x\}$$| bisect_left(A,x)
 **Find rightmost value less than x** | $$max\{y\|y<x and y\in A\}$$  | A[bisect_left(A,x) - 1]

<div class="code-head"><span>code</span>bisect_derived_functions.py</div>

```py

def find_lt(A, x):
    'Find rightmost value less than x'
    i = bisect_left(A, x)
    if i:
        return A[i-1]
    raise ValueError

def find_le(A, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(A, x)
    if i:
        return A[i-1]
    raise ValueError

def find_gt(A, x):
    'Find leftmost value greater than x'
    i = bisect_right(A, x)
    if i != len(A):
        return A[i]
    raise ValueError

def find_ge(A, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(A, x)
    if i != len(A):
        return A[i]
    raise ValueError