---
layout: post
tag : array, puzzles, easy
category: education
title: "Target Array in the Given Order"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/sf/IMG-0920.JPG

---
![](../images/posts/photos/sf/IMG-0920.JPG)

- [1389. Create Target Array in the Given Order - super easy](#1389-create-target-array-in-the-given-order---super-easy)


# 1389. Create Target Array in the Given Order - super easy
* Summary: this problem is super easy.  Just follow instruction and use <span class="coding">list.insert(where, what)</span>.
>
Using indexing to assign values will not work because indices are repeated.  Use **.insert()**. 

* Problem
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
[0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

* Solution
```python
def newArray(A, B):
    C = []
    for i in range(len(A)):
        C.insert(B[i], A[i])
    return C
print(newArray(nums, index))
```

