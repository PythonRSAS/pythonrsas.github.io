---
layout: post
tag : arrays,陣列, two-pointers
category: education
title: "Rearrange Array Elements by Sign"
description: Leetcode 2149 solved by brute force and in-place
author: Sarah Chen
image: images/posts/photos/sf/IMG-0918.JPG

---
![](../images/posts/photos/sf/IMG-0918.JPG)
- [Problem](#problem)
- [My brute forece solution](#my-brute-forece-solution)
- [Simple O(n) solution](#simple-on-solution)
- [Clever O(1) solution but kind of complicated](#clever-o1-solution-but-kind-of-complicated)
- [Reference](#reference)

# Problem 
The first problem is [Leetcode 2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/). 
You are given a 0-indexed integer array nums of even length consisting of an **equal number** of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every **consecutive** pair of integers have **opposite signs**.

For all integers with the same sign, the order in which they were present in nums is preserved.

The rearranged array **begins with a positive integer**.

Return the modified array.
你被給定一個索引值從 0 開始的偶數長度之整數陣列 nums，其由等量的正整數以及負整數組成。

你應重新排列這些元素使得修改後的陣列符合以下條件：
每個相鄰整數有著相反的正負號。
對於同一個正負號的所有整數，它們的順序應保持於原先在 nums 中的順序。
重新排列的陣列開始於一個正整數。

回傳重新排列後滿足以上條件的陣列。

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4].

範例 2：
輸入： nums = [-1,1]
輸出： [1,-1]
解釋：
1 是唯一一個正整數，而 -1 是唯一一個負整數。
因此 nums 將重新排列成 [1,-1]。


# My brute forece solution

As usual, we start with a brute force solution.  Any swapping should be ruled out because the problem says to keep the current order as much as possible. 

We keep 2 arrays, one positive and one negative, and then we zip them up.

<div class="code-head"><span>code</span>rearrange_by_sign_bf.py</div>

```py
def rearrange_by_sign_bf(A):
    positive, negative = [], []
    for i in range(len(A)):
        if A[i] > 0:
            positive.append(A[i])
        else: 
            negative.append(A[i])
    return [x for tupl in zip(positive, negative) for x in tupl]
nums = [3,1,-2,-5,2,-4]
print(rearrange_by_sign_bf(nums))
[3, -2, 1, -5, 2, -4]
```

Note:
<span class="coding">[x for tupl in zip(positive, negative) for x in tupl]</span> is the same as the following double loop:
Or,
```python
res = []
for tupl in zip(positive, negative):
    for x in tupl:
        res.append(x)
```

And the result is also equivalent to the following single loop using <span class="coding">extend</span>.
```python
res = []
for i, j in zip(positive, negative):
    res.extend([i,j])
```

This can also be acommplished by using <span class="coding">iterools.chain.from_iterable</span>.

```python
from itertools import chain
list(chain.from_iterable(zip(positive, negative)))
```

# Simple O(n) solution 

We allocate a new array <span class="coding">A</span>, and maintain 3 pointers: the first two are <span class="coding">pTail</span> and <span class="coding">nTail</span> that keep track of the frontiers of positive and negative integers, respectively.   

When we encounter a positive number, we put it in A[ptail] and increment <span class="coding">pTail</span> by 2. 
When we encounter a negative number, we put it in A[ntail] and increment <span class="coding">nTail</span> by 2. 

<div class="code-head"><span>code</span>removeDuplicate.py</div>

```py
def rearrange_by_sign(num):
    pTail, nTail = 0, 1
    A = [0] * len(nums)
    pTail = 0
    nTail = 1
    for x in nums:
        if x > 0:
            A[pTail] = x
            pTail += 2
        else:
            A[nTail] = x
            nTail += 2
    return A
nums = [3,1,-2,-5,2,-4]
print(rearrange_by_sign(nums))
# [3, -2, 1, -5, 2, -4]
```

# Clever O(1) solution but kind of complicated
解題思維：
其實就跟這題的想法很類似，只是把整個陣列的索引值分成偶數（0 、 2 、 4 、……）以及奇數（1 、 3 、 5 、……）來分別放置正整數以及負整數。也就是，我們掃過一次 nums，每次遇到正整數就是依序放到（實際上是「**交換**」，因為直接取代數值會影響結果）索引值 0 、 2 、 4 、……之位置；相似地，每次遇到負整數就是依序放到索引值 1 、 3 、 5 、……之位置。

To solve it in-place, we cannot make assignments as in the [first Remove Duplicates from Sorted Array problem](2022-06-19-8-Remove-Duplicates-from-Sorted-Array.md) because we have 2 separate streams here.  Making assignments will cause some numbers to appear more than once and some numbers missing. We have to do **swapping**.  

For the first condition, we need to make sure the first number is positive by doing a one-time swapping if needed.  I am not finished yet with this solution. 

<div class="code-head"><span>code</span>removeDuplicate_inplace.py</div>

```py
def rearrange_by_sign(A):
    pTail, nTail = 0, 1
    for i in range(0, len(A)):
        if (i % 2 == 0) & (A[i] > 0):
            A[pTail] = A[i]
            pTail += 2
        elif (i % 2 == 0) & (A[i] < 0):
            A[nTail] = A[i]
            # nTail += 2
        if (i % 2 == 1) & (A[i] > 0):
            A[pTail] = A[i]
            # pTail += 2
        elif (i % 2 == 1) & (A[i] < 0):
            nTail += 2
            A[nTail] = A[i]
    return A
nums = [3,1,-2,-5,2,-4]
print(rearrange_by_sign(nums))

```
# Reference
https://home.gamer.com.tw/artwork.php?sn=5547751


[Leetcode 2149. Rearrange Array Elements by Sign](https://leetcode.com/problems/rearrange-array-elements-by-sign/)
