---
layout: post
tag : array,陣列
category: education
title: "Remove Element"
description: Leetcode 27. Remove Element
author: Sarah Chen
image: images/posts/photos/sf/IMG-0908.JPG

---
![](../images/posts/photos/sf/IMG-0908.JPG)
- [Problem](#problem)
- [Counter](#counter)
- [defaultdict](#defaultdict)
- [Dict](#dict)

# Problem 

Problem is from Leetcode 27. Remove Element.
A pair is identical if A[i] == A[j] & i < j. 

* Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Use <span class="coding">collections.Counter</span>, creates a dictionary of frequencies.
Note that because the keys of the dictionary are integers, we **cannot** use <span class="coding">for key, value in Counter(A)</span>. 

All my solutions here are brute force. 
# Counter
Instead, we can use <span class="coding">for value in Counter(A).values()</span>.
```python
from collections import Counter
def countSame(A):
    res = 0
    for v in Counter(A).values():
        if v >= 2:
            res += v * (v - 1) /2
    return int(res)

nums = [1,2,3,1,1,3]
print(countSame(nums))
# 4
```

# defaultdict
Or, if you don't want to use <span class="coding">collections.Counter</span>, and prefer to do your own counting, then use <span class="coding">collections.defaultdict</span>.  It is slightly more convenient to use than plain <span class="coding">dict</span>: can skip the extra step of checking whether a key already existed.

```python
from collections import defaultdict
def numIdenticalPairs(nums):
    ct = defaultdict(int)
    for n in nums:
        ct[n] += 1
    # compute
    res = 0
    for i in ct.values():
        res += i*(i - 1) / 2
    return res
nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))
# 4
```
# Dict

Lastly, we use plain old dictionary and plain old loops. 

``` python
def numIdenticalPairs(ums) -> int:
    pairs = 0
    ct = {}
    for i in nums:
        if i in ct:
            ct[i] += 1
        else:
            ct[i] = 1
    res = 0
    for i in ct.values():
        res += i*(i - 1) / 2
    return res
```
