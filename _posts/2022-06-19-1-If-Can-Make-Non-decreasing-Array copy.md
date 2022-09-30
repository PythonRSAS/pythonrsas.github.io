---
layout: post
tag : arrays, puzzles, easy
category: education
title: "If Can make Non-decreasing Array"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/IMG_0870.JPG

---
- [Leecode 665. Non-decreasing Array, Easy](#leecode-665-non-decreasing-array-easy)
- [Brute force](#brute-force)
- [A clever not not efficient approach](#a-clever-not-not-efficient-approach)
- [Reference](#reference)


# Leecode 665. Non-decreasing Array, Easy

* Problem:
Given an array nums with n integers, check if it could become non-decreasing by modifying **at most one element**.

The problem is labeled as "Medium", but it actually is very easy. 

* Constraints:

n == nums.length
1 <= n <= 104
-10^5 <= nums[i] <= 10^5

* Example 1:
* Input: nums = [4,2,3]
* Output: true
* Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

* Example 2:
* Input: nums = [4,2,1]
* Output: false

# Brute force

The idea is that if left is larger than right, then let left= right - 1.   Iterate through the input array, if having to do this more than once, then return False else True.  

Even though the solution is veyr easy, I made a mistake in the index range.  Whenever we need to compare adjacent elements, be mindful that $$i+1$$ can be out of range.  Hence, the loop should be $$range(len(A) - 1)$$ instead of $$range(len(A))$$.  

* Complexity:
We have a double loop.  Time complexity is $$O(n^2)$$.  

<div class="code-head"><span>code</span>non_decreasing.py</div>

```py
def non_decreasing(A):
    ct = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]: # if left is larger than right
            A[i] = A[i + 1] - 1
            ct += 1
    if ct > 1:
        return False
    else:
        return True

nums = [4,2,3]
print(non_decreasing(nums))
# True
nums = [4,2,1]
print(non_decreasing(nums))
# False
nums = [1, 2, 3, 3]
print(non_decreasing(nums))
# True
```

* Edge case:
Note that the edge case A[i] = 10^5 and A[i] > A[i +1] is just not possible. So we are okay.  

# A clever not not efficient approach

Below solution came from Leetcode discussion.   It is quite clever and reminds me a little of the linked list cycle detection tortoise-hare fast-slow solution.  It makes two copies of the input arrays <span class="coding">one</span> and <span class="coding">two</span>.  

The idea is that if when we run into the situation of $$A[i] > A[i + 1]$$, we can either reduce the left or increase the right.  If one of them works, then return True else False. 

The reason why it is not efficient is that you have to sort both arrays twice as in <span class="coding">sorted(one)</span> and <span class="coding">sorted(two)</span>. 

<div class="code-head"><span>code</span>non_decreasing.py</div>

```py
def checkPossibility(A):
    """
    :type A: List[int]
    :rtype: bool
    """
    one, two = A[:], A[:]
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            one[i] = A[i + 1]
            two[i + 1] = A[i]
            break
    return one == sorted(one) or two == sorted(two)
```

# Reference

[leetcode solution](https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand)