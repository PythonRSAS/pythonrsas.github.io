---
layout: post
tag : array, puzzles, easy
category: education
title: "Running Sum of 1d Array"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/sf/IMG-0939.JPG

---
![waves](../images/posts/photos/sf/IMG_0939.JPG)

- [Leetcode 1480. Running Sum of 1d Array](#leetcode-1480-running-sum-of-1d-array)
- [Leetcode 2011. Final Value of Variable After Performing Operations](#leetcode-2011-final-value-of-variable-after-performing-operations)


## Leetcode 1480. Running Sum of 1d Array
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

* Solution 1: Brute force
  
This is a very easy problem.  But more complicated problems may rely on this kind of simple steps. 
1. Since it is a running sum, we need to provide a *starter array*, an empty list, to collect the cumulative sums.   
2. To accumulate sum, we need to provide a *starter sum of 0*. 

```python
def runningSum1(A):
    res = []
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        res.append(sum)
    return res

nums = [1,2,3,4]
print(runningSum1(nums))
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
