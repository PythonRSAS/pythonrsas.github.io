---
layout: post
tag : arrays, dp, Chinese
category: education
title: "Steps to make array monotonic"
description: Steps to make array monotonic
author: Sarah Chen
image: images/posts/photos/IMG_0877.JPG

---
![waves](../images/posts/photos/IMG_0877.JPG)

**Leetcode 2289. Steps to Make Array Non-decreasing problem:** 
Given a 0-indexed integer array $$A$$. In one step, remove all elements $$A[i]$$ where $$A[i]$$ is less than its left neighbor, return the number of steps performed until nums becomes a non-decreasing array.

* Input: $$[5,3,4,4,7,3,6,11,8,5,11]$$
* Output: 3

Explanation: The following are the steps performed:
- Step 1: $$[5,3,4,4,7,3,6,11,8,5,11]$$ ==> $$[5,4,4,7,6,11,11]$$
- Step 2: $$[5,4,4,7,6,11,11]$$ ==> $$[5,4,7,11,11]$$
- Step 3: $$[5,4,7,11,11]$$ ==> $$[5,7,11,11]$$
- $$[5,7,11,11]$$ is a non-decreasing array. Therefore, we return 3.

# My solution
My solution is very straightforward. The steps are:

Number of steps ct=:0; 
1. record the indice of the elements that are smaller than its immediate left neighbor in [idx]
2. drop those elements A[idx]
3. ct++
4. repeat the above steps until idx is empty

In the following Python implementation, I use a helper function <span class="coding">getIndex</span> to get the list of indices of incongruent elements. It returns a thinner array <span class="coding">[A[i] for i in range(len(A)) if not i in idx]</span> and list of indices (can be empty) of non-congruent elements. 

When removing elements of arrays in loops, we need to remember that Python lists are mutable.  We need to be *careful not to use index that refer to the older list*.  Therefore, using *list comprehension* is a safe and concise way of removing those non-monontonic elements. 

**Complexity:**
<span class="coding">getIndex()</span> runs a loop.  If we find m indices to remove, then when returning the smaller array, the loop is n - m steps.  We may need to do this close to n times in the worst case when the first element is the largest.  For example [6, 1, 2, 3, 4, 5] takes len(A) - 1 steps.  So the time complexity is $$O(n^2)$$.  

The space complexity is $$O(n)$$.

<div class="code-head"><span>code</span>steps_to_non_decreasing_array.py</div>

```py
def getIndex(A):
    idx = []
    for i in range(0, len(A)-1):
        if A[i] > A[i+1]:
            idx.append(i+1)
    print("Indices to be removed ", idx)
    return ([A[i] for i in range(len(A)) if not i in idx], idx)

def steps(A):
    temp, idxRemove = getIndex(A)
    if idxRemove:
        ct = 1
    else:
        ct = 0
        return ct
    while idxRemove:
        temp, idxRemove = getIndex(temp)
        if idxRemove:
            ct += 1
    return ct
print(steps([5, 3, 4]))
# Indices to be removed  [1]
# Indices to be removed  [1]
# Indices to be removed  []
# 2

nums = [5,3,4,4,7,3,6,11,8,5,11]
print(steps(nums))
# Indices to be removed  [1, 5, 8, 9]
# Indices to be removed  [1, 4]
# Indices to be removed  [1]
# Indices to be removed  []
# 3
nums = [4,5,7,7,13]
print(steps(nums))
# Indices to be removed  []
# ([4, 5, 7, 7, 13], [])
# Indices to be removed  []
# 0
```
My method is very intuitive, but it is not the best in time complexity. 

# A very different approach

This approach is taken from Leetcode hints and [discussion board](https://leetcode.com/problems/steps-to-make-array-non-decreasing/discuss/2085864/JavaC%2B%2BPython-Stack-%2B-DP-%2B-Explanation-%2B-Poem).  It is not as straightforward as my method.  I inserted lots of extra code to explain the process.   Reading the logic alone is not going to be enough.  Run a few small examples will help you a lot. 

Both <span class="coding">dp</span> and <span class="coding">stack</span> are lists.  But <span class="coding">dp</span> has length equal to the input array.  Whereas <span class="coding">stack</span> can have length between 0 and N. 

<span class="coding">dp</span>: used to dynamically update (compute) number of steps A[i] will take to annuhilate/eat smaller ones to its right. 
<span class="coding">stack</span>: used to hold the index of elements (from right to left) and pop the last one.  Of course we don't care to compare index values.  We use <span class="coding">stack.pop</span> or <span class="coding">stack[-1]</span> to pick the element to be compared against.  

We want to scan through the elements only once.  To do that, we start from the rightmost element and work towards the left as <span class="coding">for i in reversed(range(N))</span>.  

Did I ever dream of learning algorithm can improve my wisdom and refresh my Chinese?  It feels great to be able to do that. 

"长江后浪推前浪，世上新人换旧人"

As we are updating <span class="coding">dp</span> from back to front, it kind of makes sense to say 后浪推前浪.  


Let's walk through an example. Given input $$A=[5, 3, 4]$$,
* At the beginning of the loop, stack is empty.  dp is [0, 0, 0].
* $$i$$ is 2, nothing in the stack, <span class="coding">while</span>  condition is not satisfied and dp update action is skipped. stack is [2]
* $$i$$ is 1, stack is [2], <span class="coding">while</span>  condition is not satisfied and dp update action is skipped. stack is [2, 1]
* $$i$$ is 0, looking at the last element $$5$$,  stack is [2, 1], <span class="coding">while</span>  condition is satisfied when compared with A[stack[1]] and dp updates to [1, 0, 0].  Stack is [2].
* At this point, the <span class="coding">while</span> condtion is still satisfied because stack is [2] and 5 is greater than A[stack[2]].  So dp is updated again to be [2, 0, 0]. 
* Finally, the stack is empty.  max(dp) is returned. 

You can walk yourself through the second example of $$A=[5, 4, 3]$$.

The time complexity of this approach is still $$O(n^2)$$ because we have a double loop.  In the worse case, it is $$O(n^2)$$. 

<div class="code-head"><span>code</span>steps_to_non_decreasing_array.py</div>

```py
def totalSteps(A) -> int:
    N = len(A)
    dp = [0] *N
    stack = []
    for i in reversed(range(N)):
        # print("*********************\n")
        # print("i:",i)
        while stack and (A[i] > A[stack[-1]]):
            # print("stack[-1]:", stack[-1])
            # print("Comparing: ", A[i], A[stack[-1]])
            # print("stack: ", stack)
            dp[i] = max(dp[i] + 1, dp[stack.pop()])
            # print("After updating, dp:", dp)
        stack.append(i)
        # print("stack:", stack)
    return max(dp)
totalSteps([5, 3, 4])
# *********************

# i: 2
# stack: [2]
# *********************

# i: 1
# stack: [2, 1]
# *********************

# i: 0
# i: 0
# stack[-1]: 1
# Comparing:  5 3
# stack:  [2, 1]
# After updating, dp: [1, 0, 0]
# i: 0
# stack[-1]: 2
# Comparing:  5 4
# stack:  [2]
# After updating, dp: [2, 0, 0]
# stack: [0]
# Out[95]: 2

totalSteps([5, 4, 3])
# *********************

# i: 2
# stack: [2]
# *********************

# i: 1
# i: 1
# stack[-1]: 2
# Comparing:  4 3
# stack:  [2]
# After updating, dp: [0, 1, 0]
# stack: [1]
# *********************

# i: 0
# i: 0
# stack[-1]: 1
# Comparing:  5 4
# stack:  [1]
# After updating, dp: [1, 1, 0]
# stack: [0]
# Out[97]: 1

totalSteps([6, 1, 2, 3, 4, 5])

nums = [5,3,4,4,7,3,6,11,8,5,11]
print(totalSteps(nums))
```

# Reference
[长江后浪推前浪](https://www.idongde.com/c/732D545aaC926f77.shtml)
《增广贤文》是中国明代时期编写的儿童启蒙书目，集结了中国从古到今的各种格言、谚语，“长江后浪推前浪，世上新人换旧人”就是出自其中，另外还有很多耳熟能详的谚语，例如逢人且说三分话，未可全抛一片心；有意栽花花不发，无心插柳柳成荫；画虎画皮难画骨，知人知面不知心；路遥知马力，日久见人心等等。