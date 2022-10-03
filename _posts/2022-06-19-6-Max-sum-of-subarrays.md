---
layout: post
tag : array, puzzles, easy
category: education
title: "Max sum of subarrays"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/sf/IMG-0922.JPG

---
![](../images/posts/photos/sf/IMG-0922.JPG)

- [Leetcode 1672. Max sum of subarrays](#leetcode-1672-max-sum-of-subarrays)
- [1389. Create Target Array in the Given Order - super easy](#1389-create-target-array-in-the-given-order---super-easy)

# Leetcode 1672. Max sum of subarrays
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

* Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

* Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

* Solution:
Although this is super easy, one should never be careless. It is asking for the maximum of the sums of the subarrays.
We can solve it with one line.
```python
def maxSubSum(A):
    return max([sum(i) for i in accounts])
print(maxSubSum(A))
```
Or we can do it using a for-loop.  

```python
def maxSubSum(A):
    res = 0
    for i in A:
        ith_sum = sum(i)
        if ith_sum > res:
            res = ith_sum
    return res

accounts = [[1,2,3],[3,2,1]]
print(maxSubSum(accounts))
```

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

