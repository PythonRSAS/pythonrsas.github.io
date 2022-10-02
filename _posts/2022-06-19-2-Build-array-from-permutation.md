---
layout: post
tag : array permutation
category: education
title: "Build array from permutation"
description: array permutation
author: Sarah Chen
image: images/posts/photos/sf/IMG-0938.JPG

---
![waves](../images/posts/photos/sf/IMG-0938.JPG)

- [Intuitive solution](#intuitive-solution)
- [O(1) space complexity solution](#o1-space-complexity-solution)
- [Reference](#reference)

This problem came from Leetcode 1920. Build Array from Permutation. This is a very easy problem.  But more complicated problems may rely on this kind of simple steps. 
Given a zero-based permutation A (0-indexed), build an array A of the same length where 
$$A[i] = A[A[i]]$$ and return it.

Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

# Intuitive solution
The intuitive solution is to follow exactly **what it says** says in $$A[i] = A[A[i]]$$ and build a new array:
0th place of the new array $$A$$: get the key at index $$A[0]$$ index of the old array,
1st place of the new array $$A$$: get the key at index $$A[1]$$ index of the old array 
...

<div class="code-head"><span>code</span>permute array.py</div>

```py
def buildArray2(nums):
    A = []
    for num in nums:
        A.append(nums[num])
    return A
nums = [0,2,1,5,3,4]
print(buildArray2(nums))

```

# O(1) space complexity solution

It seems impossible to solve it in-place: if we follow the instruction, as soon as we change one key to be nums[nums[i]], we would have changed the key of the original array and made it impossible for the instruction to be followed through. 

But there is a way, and it requires a clever math trick. 

$$a + b × n ≡ a (mod n)$$

We can modify the elements of array such that it retains the original key and the future key. 

Because each element of the input array is between $$0$$ and $$N-1$$, it is class representative of modular $$N$$.  

* **retaining the past**: If we add **some multiple** of $$N$$ to the $$nums[i]$$, we can retrieve the original $$nums[i]$$ by mod N. 

* **retaining the future**: Let the "some multiple" be $$nums[nums[i]]$$.  

$$nums[i]  = nums[i] + nums[nums[i]] × N$$

In other words,
**nums[i]  =  original nums[i]  + future nums[i] × N**

This is not exactly true because elements are modified, except the first (possibly one or more) element.  But because this is a linear transformation and a linear transformation of a linear transformation is still a linear transformation. We can get the two parts back! 

So, while keys are being modified while we apply this transformation, each still retains its past and future in compound way.  

So, for each of the transformed nums[i], 
* By taking mod N of the transformed we can retrieve the original nums[i].
* By subtracting nums[i], divide by $$N$$, and take mod N, we get the clean nums[nums[i]]. 

<div class="code-head"><span>code</span>permute array constant space.py</div>

```py
def buildArray(nums):
    N = len(nums)
    # turn the array into a = N *b + r
    for i in range(N):
	    nums[i] = N * nums[nums[i]] + nums[i]

    for i in range(N):
        nums[i] = (nums[i] - nums[i] % N) // N

    for i in range(N):
        nums[i] = nums[i] % N

    return nums
nums = [0,2,1,5,3,4]
print(buildArray(nums))

# def buildArray(nums):
#   N = len(nums)
#   for i, c in enumerate(nums):
#     nums[i] += N * (nums[c] % N)
#   for i,_ in enumerate(nums):
#     nums[i] //= N
#   return nums
```
因為陣列中的數字介於 0 ～ n - 1 中，而這正好可以套入 a 、 b 的位置。因此我們在更動位置 i 時，我們可以將 nums[i] 加上 nums[nums[i]] 乘以 n 後的值。因此此時該位置的值便變成了 nums[i] + nums[nums[i]] × n，當模 n 時我們便可以求得原本位置 i 的數字 nums[i]、而除以 n 取整數便可以得到所求的 nums[nums[i]]。

# Reference
[](https://home.gamer.com.tw/artwork.php?sn=5302636)