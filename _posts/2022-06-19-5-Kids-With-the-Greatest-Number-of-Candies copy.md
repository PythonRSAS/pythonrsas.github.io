---
layout: post
tag : arrays, puzzles, easy
category: education
title: "Kids With the Greatest Number of Candies"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/sf/IMG_0923.JPG

---
![](../images/posts/photos/sf/IMG_0923.JPG)

- [Leetcode 1672. Max sum of subarrays](#leetcode-1672-max-sum-of-subarrays)
- [1389. Create Target Array in the Given Order - super easy](#1389-create-target-array-in-the-given-order---super-easy)

This post is for my young sweet child, who likes candies and sweets. 

This problem is [Leetcode 1431](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/).   There are n kids with candies. You are given an integer array candies, where each $$candies[i]$$ represents the number of candies the $$ith$$ kid has, and an integer *extraCandies*, denoting the number of **extra candies** that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

```python
def kidsWithCandies(candies, extraCandies) -> List[bool]:
    gauge = max(candies) - extraCandies 
    return [candy >= gauge for candy in candies]
```

This solution can be expanded to running product, max, min. 

* Solution 2: [itertools.accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate)
<span class="coding">list(accumulate(A))</span> has [souce code here](https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c). 

```python
from itertools import accumulate
def runningSum(A):
    return list(accumulate(A))
nums = [1,2,3,4]
print(runningSum(nums))
```
This solution can be expanded to running product using <span class="coding">operator.mul()</span>,  max, min. 
<div class="code-head"><span>code</span>accumulate.py</div>

```py
import operator
def runningProduct(A):
    return list(accumulate(A, operator.mul))
nums = [1,2,3,4]
print(runningProduct(nums))

def runningMax(A):
    return list(accumulate(A, max))
nums = [10,2,3,4]
print(runningMax(nums))
# [10, 10, 10, 10]
```

