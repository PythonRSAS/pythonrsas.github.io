---
layout: post
tag : array, puzzles, easy
category: education
title: "Richest Customer Wealth- Max sum of subarrays"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/sf/IMG-0940.JPG

---
![sunset](../images/posts/photos/sf/IMG-0940.JPG)

- [Leetcode 1672. Richest Customer Wealth- Max sum of subarrays](#leetcode-1672-richest-customer-wealth--max-sum-of-subarrays)


The problem comes from Leetcode 1672. Richest Customer Wealth- Max sum of subarrays.

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
