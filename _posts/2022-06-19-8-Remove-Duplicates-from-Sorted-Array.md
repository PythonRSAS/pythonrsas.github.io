---
layout: post
tag : arrays, two-pointers
category: education
title: "Remove Duplicates from Sorted Array"
description: two Leetcode problems of remove duplicates from sorted array solved by brute force and in-place
author: Sarah Chen
image: images/posts/photos/sf/IMG-0919.JPG

---
![](../images/posts/photos/sf/IMG-0919.JPG)
- [Problem 1](#problem-1)
  - [My brute force O(n) solution](#my-brute-force-on-solution)
  - [Clever O(1) solution](#clever-o1-solution)
- [Problem 2](#problem-2)
  - [My brute force O(n) solution](#my-brute-force-on-solution-1)
  - [Clever O(1) solution](#clever-o1-solution-1)
- [Reference](#reference)

# Problem 1
The first problem is Leetcode 26. Remove Duplicates from Sorted Array. 
Given an integer array nums *sorted in non-decreasing order*, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same.  Return k after placing the final result in the first k slots of nums.

Example 1:

Input: nums = [1,1,2]

Output: 2, nums = [1,2,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.

*It does not matter what you leave beyond the returned k (hence they are underscores)*.

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]

Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.

It does not matter what you leave beyond the returned k (hence they are underscores).

## My brute force O(n) solution

As usual, we start with a brute force solution.  Any swapping should be ruled out because the problem says input is sorted already.  Swapping will mess up the sorted order.  

Using a hashmap to keep track of the unique numbers and their counts surely can solve the problem.  The limitation is the space $$O(n)$$.  

<div class="code-head"><span>code</span>removeDuplicate_bruteforce.py</div>

```py
from collections import Counter
def removeDuplicate_bf(A):
    N = len(A)
    counts = Counter(A)
    A =  list(counts.keys()) + (N-len(counts.keys()))*[0]
    print(A)
    return len(counts.keys())
nums = [1,1,2]
print(removeDuplicate_bf(nums))
# [1, 2, 0]
# 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate_bf(nums))
# [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
# 5
```
## Clever O(1) solution

The clever solution uses two-pointer approach: one pointer loops through input and the other keeps track of unique keys.

The code below uses a pointer <span class="coding">newTail</span> to keep track of the frontier of unique keys.  At position <span class="coding">A[newTail]</span>, it is always the last unique key.  Therefore, we return <span class="coding">newTail + 1</span>.  

How do we enforce this frontier?  We iterate the **loop from 1 to the last place** and compare <span class="coding">A[i]</span> with <span class="coding">A[newTail]</span>.  If we run into a different value from <span class="coding">A[newTail]</span>, then we increment the frontier by 1 and update <span class="coding">A[newTail]</span> to be the latest unique value. 

Since we don't need to worry about those after the k unique values, we are done as soon as our loop has ended. 

<div class="code-head"><span>code</span>removeDuplicate_inplace.py</div>

```py
def removeDuplicates(A):
    if not A:
        return 0
    newTail = 0
    for i in range(1, len(A)):
        if A[i] != A[newTail]:
            newTail += 1 # moves when encounter a new value A[i]
            A[newTail] = A[i] # frontier takes on the new value
            print(A)
    print(A)
    return newTail + 1
nums = [1, 2, 2]
print(removeDuplicates(nums))
# [1, 2, 2]
# [1, 2, 2]
# 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
# [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
# [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
# [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
# [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
# 5
```
# Problem 2

From [Leetcode 80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that **each unique element appears at most twice**. The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums. It does not matter what you leave beyond the returned k (hence they are underscores).


Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

題目意譯：
給定一按非降序排列之整數陣列 nums，原地（In-place）地移除一些重複的元素使得每種元素出現至多兩次。元素之間的相對順序應在移除過程後保持原樣。

由於對於某些語言來說是無法變更陣列的長度的，因此你必須將結果放在 nums 的第一部分。更正式地說，如果移除重複的元素後剩下 k 個元素，則 nums 的前 k 個元素應為最終的結果。在前 k 個元素之後剩下的是什麼將會被忽略。

將最終結果放在 nums 的前 k 個位置後回傳 k。

請勿分配額外的記憶體來宣告另一個陣列。你必須直接原地修改輸入之陣列，並使用 O(1) 的額外記憶體空間。

Example 1:

Input: nums = [1,1,1,2,2,3]

Output: 5, nums = [1,1,2,2,3,_]

Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]

Output: 7, nums = [0,0,1,1,2,3,3,_,_]

Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.


## My brute force O(n) solution
My brute force solution follows the same idea as Problem 1. 

Using a hashmap to keep track of the unique numbers and their counts surely can solve the problem.  The limitation is the space $$O(n)$$.  

I use 2 arrays <span class="coding">keeps</span> and <span class="coding">extras</span>. The first to hold the unique values repeated at most 2 times.  The second to hold the extra repeated. 

<div class="code-head"><span>code</span>removeDuplicate_bruteforce.py</div>

```py
from collections import Counter
def removeDuplicate2_bf(A):
    keeps, extras = [], []
    counts = Counter(A)
    for k, v in counts.items():
        keeps.extend([k]*min(2, v))
        extras.extend([k]*max(0, v - 2))
    A = keeps + extras
    print(A)
    return len(keeps)

nums = [1,1,1,2,2,3]
print(removeDuplicate2_bf(nums))
# [1, 1, 2, 2, 3, 1]
# 5
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate2_bf(nums))
# [0, 0, 1, 1, 2, 2, 3, 3, 4, 1]
# 9
```

## Clever O(1) solution

解題思維：
因為 nums 有按照非降序排列，因此數值相同的元素會被排在一起。因此實際上作法跟這題基本上一致，只是因為現在同一種元素可以出現第二次，因此我們需要額外判斷目前可放置位置 x（使用與該鏈結相同的符號來代表）的前一個位置 x - 1 之元素是否出現過了第二次。假如有出現過第二次的話，則之後再出現也不得放到 x 這個位置，直到換到下一種元素為止。

As before, we maintain 2 pointers: the first <span class="coding">newTail</span> keeps track of the frontier.   There are two cases when newTail is incremented:
1. **Within the same number**: Since each number can be repeated at most twice.  We can increment newTail if we encounter the same number A[i] == A[newTail] $$&$$ A[i] != A[newTail -1] (or equivalently A[newTail] != A[newTail -1]). 
2. **Beyond the same number**: When A[i] != A[newTail] $$&$$ A[newTail] == A[newTail -1] (the unique number has already been appeared two times).
   
<div class="code-head"><span>code</span>removeDuplicate_inplace.py</div>

```py
def removeDuplicates2(A):
    newTail = 0
    for i in range(1, len(A)):
        if (A[i] == A[newTail]) & (A[i] != A[newTail -1]):
            newTail += 1
            continue
        if (A[i] != A[newTail]) & (A[newTail] == A[newTail -1]):
            newTail += 1 # moves when encounter a new value A[i] and old value has been repeated 
            A[newTail] = A[i] # frontier takes on the new value
    print(A)
    return newTail + 1
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates2(nums))
# [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
# 9
# nums = [1,1,1,2,2,3]
# 5
```
# Reference
https://home.gamer.com.tw/artwork.php?sn=5560599


[Leetcode 80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

