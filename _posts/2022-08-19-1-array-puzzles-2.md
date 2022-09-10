---
layout: post
tag : arrays, puzzles, easy
category: education
title: "array puzzles"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Review](#review)
  - [Slicing](#slicing)
- [Puzzles](#puzzles)
  - [Leecode 665. Non-decreasing Array, Easy](#leecode-665-non-decreasing-array-easy)
  - [Leetcode 1920. Build Array from Permutation](#leetcode-1920-build-array-from-permutation)
  - [Leetcode 2011. Final Value of Variable After Performing Operations](#leetcode-2011-final-value-of-variable-after-performing-operations)
  - [Leetcode 1672. Richest Customer Wealth- Max sum of subarrays](#leetcode-1672-richest-customer-wealth--max-sum-of-subarrays)
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

## Slicing
Since accessing array is an $$O(1)$$ operation, it is important to know how to access elements via slicing using <span class="coding">:</span> the slicing operator and other directional operators <span class="coding">-</span> and, to a less extent, <span class="coding">~</span> (reverse direction). 
* <span class="coding">[x:y:z]</span>:
  begin at x, 
  end at y-1, 
  step size z.  
For example <span class="coding">[5:1:-2]</span>  means begin at index 5, end at index 1, with step size -2, i.e. the indices sliced are: 5, 3

# Puzzles

## Leecode 665. Non-decreasing Array, Easy

* Problem:
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

The problem is labeled as "Medium", but it actually is very easy. 

* Constraints:

n == nums.length
1 <= n <= 104
-10^5 <= nums[i] <= 10^5

* Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

* Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

* Solution 1: Brute force

Even though the solution is veyr easy, I made a mistake in the index range.  Whenever we need to compare adjacent elements, be mindful that $$i+1$$ can be out of range.  Hence, the loop should be $$range(len(A) - 1)$$ instead of $$range(len(A))$$.  

* Complexity:
We have a double loop.  Time complexity is $$O(n^2)$$.  

```python
def non_decreasing(A):
    ct = 0
    for i in range(len(A) - 1):
        if A[i] > A[i +1]:
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

## Leetcode 1920. Build Array from Permutation

* Problem:
Given a zero-based permutation nums (0-indexed), build an array A of the same length where A[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

* Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.

* Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

* Solution 1:
  
This is a very easy problem.  But more complicated problems may rely on this kind of simple steps. 
```python
nums = [0,2,1,5,3,4]
def buildArray2(nums):
    A = []
    for num in nums:
        A.append(nums[num])
    return A
print(buildArray2(nums))
```

<!-- * Solution 2: https://dev.to/vishnureddys/build-array-from-permutation-solution-to-leetcode-problem-357l I don't quite understand it 
This solution makes use of the modulo. we can store two numbers in one element and extract them at our will. We are given that the range of nums[i] is between 0 to 1000. So we take modulo to be 1001.

As the values in the input array are ranging from 0 to n-1 where $$n$$ is the length of the array, we can simply store the input array value in modulo by $$n$$ and modified value in divide by $$n$$. This solves the problem of adding extra space to our solution.

We make use of the equation nums[i] = nums[i] + (n*(nums[nums[i]]%n)) to store the new values in the nums array. We then divide by n to get the required value to return.

To understand this better, let’s assume an element is a and another element is b, both the elements are less than n. So if an element a is incremented by b*n, the element becomes a + b*n. So, when a + b*n is divided by n, the value is b and a + b*n % n is a.
```python
def buildArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    for i in range(0, len(nums)):
        nums[i]=nums[i]+(n*(nums[nums[i]]%n))
    for i in range(0, len(nums)):
        nums[i] = int(nums[i]/n)
    return nums
``` -->

## Leetcode 1480. Running Sum of 1d Array
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

* Solution 1: Brute force
  
This is a very easy problem.  But more complicated problems may rely on this kind of simple steps. 
1. Since it is a running sum, we need to provide a *starter array*, an empty list, to collect the cumulative sums.   
2. To accumulate sum, we need to provide a *starter sum of 0*. 

```python
def runningSum1(A):
    res = []
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        res.append(sum)
    return res

nums = [1,2,3,4]
print(runningSum1(nums))
```

This solution can be expanded to running product, max, min. 

* Solution 2: [itertools.accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate)
<span class="coding">list(accumulate(A))</span> has [souce code here](https://github.com/python/cpython/blob/main/Modules/itertoolsmodule.c). 

```python
from itertools import accumulate
def runningSum(A):
    return list(accumulate(A))
nums = [1,2,3,4]
print(runningSum(nums))
```
This solution can be expanded to running product using <span class="coding">operator.mul()</span>,  max, min. 
<div class="code-head"><span>code</span>accumulate.py</div>

```py
import operator
def runningProduct(A):
    return list(accumulate(A, operator.mul))
nums = [1,2,3,4]
print(runningProduct(nums))

def runningMax(A):
    return list(accumulate(A, max))
nums = [10,2,3,4]
print(runningMax(nums))
# [10, 10, 10, 10]
```

## Leetcode 2011. Final Value of Variable After Performing Operations 
Super easy. 

* Problem:
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.

* Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

* Constraints:

1 <= operations.length <= 100
operations[i] will be either "++X", "X++", "--X", or "X--".

```python
def operations(A):
    res = 0
    for i in A:
        if i in ["X++","X++"]:
            res += 1
        else:
            res -= 1
    return res

A = ["--X","X++","X++"]
print(operations(A))
```

## Leetcode 1672. Richest Customer Wealth- Max sum of subarrays
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

* Example 1:

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

* Example 2:

Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

* Solution:
Although this is super easy, one should never be careless. It is asking for the maximum of the sums of the subarrays.
We can solve it with one line.
```python
def maxSubSum(A):
    return max([sum(i) for i in accounts])
print(maxSubSum(A))
```
Or we can do it using a for-loop.  

```python
def maxSubSum(A):
    res = 0
    for i in A:
        ith_sum = sum(i)
        if ith_sum > res:
            res = ith_sum
    return res

accounts = [[1,2,3],[3,2,1]]
print(maxSubSum(accounts))
```
