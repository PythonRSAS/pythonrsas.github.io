---
layout: post
tag : abstract data structure, python
category: education
title: "The flag partition"
description: sorting into 3 buckets that look like 3 bands in the Dutch, French, 
author: Sarah Chen
image: images/posts/tricolors.PNG

---
- [The Dutch flag partitioning problem](#the-dutch-flag-partitioning-problem)

![flag](../images/posts/tricolors.PNG) 
# The Dutch flag partitioning problem
We want to partition an array in the following fashion:
Given an element called "pivot" (or the index of it) of the array of integers,  the ones smaller than this number should be placed before this number, and the ones before than this number after. 

The following solution has time complexity $$O(n)$$ and space complexity $$O(1)$$.  I did this problem a few times.  There are 4 places I found myself making mistakes:
1. indent of the return (or forgot to return)
2. compare with the pivot, not anything else
3. the direction of the range
4. forgot to increment/decrement the pointer indices

<div class="code-head"><span>code</span>flag_partition.py</div>

```py
def flag_partition(pivot_idx, A):
    pivot = A[pivot_idx]
    N = len(A)
    small_idx = 0
    big_idx = N - 1
    print("Pivot is ",A[pivot_idx])
    # move smaller ones to the front
    for i in range(N):
        if A[i] < pivot:
            A[i], A[small_idx] = A[small_idx], A[i]
            small_idx += 1

    # move bigger ones to the front
    for i in reversed(range(N)):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[i], A[big_idx] = A[big_idx], A[i]
            big_idx -= 1

    return A
lt = [0, 1,2,0,2,1,1]
print(flag_partition(3,lt))
```

