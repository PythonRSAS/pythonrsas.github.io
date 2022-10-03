---
layout: post
tag : array,陣列
category: education
title: "Remove Element"
description: Leetcode 27. Remove Element
author: Sarah Chen
image: images/posts/photos/farm/IMG-1229.JPG

---
![](../images/posts/photos/farm/IMG-1229.JPG)
- [Problem](#problem)
- [Bruter force Counter](#bruter-force-counter)
- [O(1) solution](#o1-solution)

# Problem 

Problem is from [Leetcode 27. Remove Element](https://leetcode.com/problems/remove-element/).
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

# Bruter force Counter
As usual, I use <span class="coding">Counter()</span> for the first brute force solution.  The answer is length of input array minus the count of val. 

<div class="code-head"><span>code</span>remove element.py</div>

```py
from collections import Counter
def removeElement(nums, val):
    A = []
    ct = Counter(nums)
    for k, v in ct.items():
        if k != val:
            A.extend([k] * v)
    A.extend([0]*ct[val]) # reconstruct input array
    print(A)
    return len(nums) - ct[val]

nums = [0,1,2,2,3,0,4,2]
val = 2
# [0, 0, 1, 3, 4, 0, 0, 0]
# 5
```

# O(1) solution

We can use the pointer approach to keep track of location of the latest element that does not equal to val. 

```python

def removeElement(nums, val):
    newTail = 0
    val_ct = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[newTail] = nums[i]
            newTail += 1
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
# 5
```

