---
layout: post
tag : arrays, puzzles
category: education
title: "array puzzles"
description: puzzles that based on arrays
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Review](#review)
  - [Slicing](#slicing)
- [Leetcode 2289. Steps to Make Array Non-decreasing](#leetcode-2289-steps-to-make-array-non-decreasing)
# Review
Arrays have the following time complexity
1. **Access**: random access use *index* as all elements are indexed, run time is $$O(1)$$.  This is the advantage of arrays. 
2. Search:  $$O(n)$$, may need to go over each element to find an item from an unsorted array
3. Insert:  $$O(n)$$, because we need to shift the elements, which are after the index where we want to insert the item, to the *'right'* for one space  
4. Delete:  $$O(n)$$, because we need to shift the elements, which are after the index where we want to insert the item, to the *"left"* for one space  


Action | syntax
---------|----------
 instantiating 1D array| <span class="coding"> [0,1,2,3,4]</span>,  <span class="coding">list(range(5))</span>
 instantiating 2D array| <span class="coding"> [[0,1,2,3,4],[1,2], [0]]</span>, also called "nested list"
 access |  <span class="coding">[0]</span> gives the first element,  <span class="coding">[~0] </span> reverse access| 
 append |  <span class="coding">.append() </span>
 insert |   <span class="coding">.insert(2,100)</span>
 reverse |  <span class="coding">.reverse()</span> in-place, or <span class="coding">reversed(list)</span> returns an iterator

Since accessing array is an $$O(1)$$ operation, it is important to know how to access elements via slicing using <span class="coding">:</span> the slicing operator and other directional operators <span class="coding">-</span> and, to a less extent, <span class="coding">~</span> (reverse direction). 
* <span class="coding">[x:y:z]</span>:
  begin at x, 
  end at y-1, 
  step size z.  
For example <span class="coding">[5:1:-2]</span>  means begin at index 5, end at index 1, with step size -2, i.e. the indices sliced are: 5, 3


**Leetcode 2289. Steps to Make Array Non-decreasing problem:** 
Given a 0-indexed integer array $$A$$. In one step, remove all elements $$A[i]$$ where $$A[i]$$ is less than its left neighbor, return the number of steps performed until nums becomes a non-decreasing array.

* Input: $$[5,3,4,4,7,3,6,11,8,5,11]$$
* Output: 3

Explanation: The following are the steps performed:
- Step 1: $$[5,3,4,4,7,3,6,11,8,5,11]$$ ==> $$[5,4,4,7,6,11,11]$$
- Step 2: $$[5,4,4,7,6,11,11]$$ ==> $$[5,4,7,11,11]$$
- Step 3: $$[5,4,7,11,11]$$ ==> $$[5,7,11,11]$$
- $$[5,7,11,11]$$ is a non-decreasing array. Therefore, we return 3.

This is an easy Leetcode problem.  The intuitive solution is to
Number of steps ct=:0; 
1. record the indice of the elements that are smaller than its immediate left neighbor in [idx]
2. drop those elements A[idx]
3. ct++
4. repeat the above steps until idx is empty

In the following Python implementation, I use a helper function <span class="coding">getIndex</span> to get the list of indices of incongruent elements. It returns a thinner array <span class="coding">[A[i] for i in range(len(A)) if not i in idx]</span> and list of indices (can be empty) of non-congruent elements. 

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
nums = [5,3,4,4,7,3,6,11,8,5,11]
print(getIndex(nums))
print(steps(nums))
# Indices to be removed  [1, 5, 8, 9]
# Indices to be removed  [1, 4]
# Indices to be removed  [1]
# Indices to be removed  []
# 3
nums = [4,5,7,7,13]
print(getIndex(nums))
print(steps(nums))
# Indices to be removed  []
# ([4, 5, 7, 7, 13], [])
# Indices to be removed  []
# 0
```
