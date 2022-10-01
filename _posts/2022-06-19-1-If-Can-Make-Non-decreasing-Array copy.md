---
layout: post
tag : arrays, puzzles, easy
category: education
title: "If Can make Non-decreasing Array"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/IMG_0680.JPG

---
- [Leecode 665. Non-decreasing Array, Easy](#leecode-665-non-decreasing-array-easy)
- [My simple brute force](#my-simple-brute-force)
- [A clever not not efficient approach](#a-clever-not-not-efficient-approach)
- [Compare 2 solutions](#compare-2-solutions)
- [Reference](#reference)

![non-decreasing](../images/posts/photos/IMG_0680.JPG)
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

# My simple brute force

The idea is that if left is larger than right, then let left=right. This smoothes the bump.  Iterate through the input array, if having to do this more than once, then return False else True.  

*** Complexity**:
We have a double loop.  Time complexity is $$O(n^2)$$.  

<div class="code-head"><span>code</span>myCheckPossibility.py</div>

```py
def myCheckPossibility(A):
    ct = 0
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]: # if left is larger than right
            A[i] = A[i + 1]
            ct += 1
    if ct > 1:
        return False
    else:
        return True

print(myCheckPossibility([2, 4, 2, 3]))

nums = [4,2,3]
print(myCheckPossibility(nums))
# True
nums = [4,2,1]
print(myCheckPossibility(nums))
# False
nums = [1, 2, 3, 3]
print(myCheckPossibility(nums))
# True
```

We got the correct answers for all the test cases.  So why is it wrong?

Consider $$[5, 5, 2, 2, 2]$$. 

Even though the solution is veyr easy, I made a mistake in the index range.  Whenever we need to compare adjacent elements, be mindful that $$i+1$$ can be out of range.  Hence, the loop should be $$range(len(A) - 1)$$ instead of $$range(len(A))$$. 



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
# Compare 2 solutions
The solution from leetcode discussion board is more work as it uses two <span class="coding">sorted</span>. 

Let's do a comparison:
```python
import random
from datetime import datetime
from numpy import random as npr

nSamples = 100
npr.seed(1234)

nums_lt = [[np.random.randint(0, 10) for i in range(5)] for j in range(nSamples)]

t0 = datetime.now()
myRes = [myCheckPossibility(i) for i in nums_lt]
mytime = datetime.now() - t0

t1 = datetime.now()
hisRes = [checkPossibility(i) for i in nums_lt]
histime = datetime.now() - t1

compare = pd.DataFrame({'myRes':myRes, 'hisRes':hisRes,'nums_lt':nums_lt })
compare[compare.myRes != compare.hisRes]

for nums in nums_lt:
    if myCheckPossibility(nums)  checkPossibility(nums):
        print(nums)
        print("my:", myCheckPossibility(nums))
        print("his:",checkPossibility(nums) )
```
The very bizzare thing is that when I ran the code initially, it was showing erroneous results.  But after 3 or 4 times of running the same code, none is returned and everything is correct.  This is something I am still trying to figure out exactly where it went wrong. 

# Reference

[leetcode solution](https://leetcode.com/problems/non-decreasing-array/discuss/106816/Python-Extremely-Easy-to-Understand)