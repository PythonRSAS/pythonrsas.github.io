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
- [O(1) solution: assigning](#o1-solution-assigning)
- [O(1) solution: swapping instead of assigning](#o1-solution-swapping-instead-of-assigning)
- [Reference](#reference)

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

<div class="code-head"><span>code</span>remove element_bf.py</div>

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
removeElement(nums, val)
# [0, 0, 1, 3, 4, 0, 0, 0]
# 5
nums = [3,2,2,3]
val = 3
removeElement(nums, val)
# [2, 2, 0, 0]
# 2
```

# O(1) solution: assigning
用一個變數儲存不等於 val 的元素現在應該放在哪個位置。
We can use the pointer approach to keep track of location of the latest element that does not equal to val. 

<div class="code-head"><span>code</span>remove element.py</div>

```py

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
nums = [3,2,2,3]
val = 3
removeElement(nums, val)
# [2, 2, 0, 0]
# 2
```

# O(1) solution: swapping instead of assigning

A guy named klintan from [Leetcode discussion](https://leetcode.com/problems/remove-element/discuss/12584/6-line-Python-solution-48-ms) has a different way of looking at things. He names the two pointers slow and fast.  It uses swapping instead of assignment. I like this solution a lot. 

The <span class="coding">fast</span> pointer sweeps through the input array.  For each element that it encounters that is not equal to val, it throws it to the left.  

<span class="coding">slow</span> is the where the next good number should be placed. In <span class="coding">slow</span> position, it could be a bad one, or it could be good one. When it is moving together with fast in tantem, the swap is just a self-exchange, nothing happens, except both <span class="coding">fast</span> and <span class="coding">slow</span> ++.  When <span class="coding">slow</span> is behind <span class="coding">fast</span>, <span class="coding">slow</span> is holding a bad one.

Whenever <span class="coding">fast</span> finds a good number, it passes it to <span class="coding">slow</span> and removes the bad one from <span class="coding">slow</span>. 


[**0** ,1,2,2,3,0,4,2], slow = 0, fast = 0
$$0 ne 2$$, slow and fast swap (they are the same), slow ++

[0,**1** ,2,2,3,0,4,2], slow = 1, fast = 1
$$1 != 2$$, slow and fast swap (they are the same), slow ++

[0,1,**2** ,2,3,0,4,2], slow = 2, fast = 2
$$2 = 2$$, no swapping

[0,1,2, **2**,3,0,4,2], slow = 2, fast = 3
$$2 = 2$$, no swapping

[0,1,2,2, **3**,0,4,2], slow = 2, fast = 4
$$3 ne 2$$, slow and fast swap, swap the first 2 with 3, slow ++

[0,1,3,2, 2, **0**,4,2], slow = 3, fast = 5
$$0 != 2$$, slow and fast swap, 2 moves to where 0 is,  slow ++

[0,1,3,0 , 2, 2, **4**,2], slow = 4, fast = 6
$$4 != 2$$, slow and fast swap, slow ++

[0,1,3,0 , 4, 2, 2, **2**], slow = 5, fast = 7
$$2 = 2$$, no swapping 

[0,1,3,0 , 4, 2, 2, 2]

<div class="code-head"><span>code</span>remove element fast slow.py</div>

```py
def removeElement(nums, val):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    print(nums)
    return slow
nums = [3,2,2,3]
val = 3
removeElement(nums, val)
# [2, 2, 3, 3]
#  2
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))
# [0, 1, 3, 0, 4, 2, 2, 2]
# 5
```

# Reference
https://home.gamer.com.tw/artwork.php?sn=4866727

[Leetcode 27. Remove Element](https://leetcode.com/problems/remove-element/)