---
layout: post
tag : array, puzzles, easy
category: education
title: "array puzzles comparisons"
description: compare array puzzles that ask for some permutation of the array, and compare puzzles that ask for a number
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Introduction](#introduction)
- [Problems that ask for permutation or rearrangement](#problems-that-ask-for-permutation-or-rearrangement)
  - [1. Leetcode 1389 create a target array in given order.](#1-leetcode-1389-create-a-target-array-in-given-order)
  - [2. Leetcode 1920. Build Array from Permutation](#2-leetcode-1920-build-array-from-permutation)
  - [4. Passing Yearbooks - number of permutations](#4-passing-yearbooks---number-of-permutations)
- [Problems that ask for a number](#problems-that-ask-for-a-number)
  - [Leetcode 1480. Running Sum of 1d Array](#leetcode-1480-running-sum-of-1d-array)
  - [Leetcode 2011. Final Value of Variable After Performing Operations](#leetcode-2011-final-value-of-variable-after-performing-operations)
  - [Leetcode 1672. Richest Customer Wealth- Max sum of subarrays](#leetcode-1672-richest-customer-wealth--max-sum-of-subarrays)
- [Problems that ask for returning index](#problems-that-ask-for-returning-index)
  - [Two Sum](#two-sum)


# Introduction

Many array-based puzzles ask for some rearrangment of the input array.  The key to solve them is **to read carefully what the question asks for**. 

# Problems that ask for permutation or rearrangement

Questions in the most straightforward type are like pseudo code already.  There is zero twist or turns. 

## 1. Leetcode 1389 create a target array in given order.  

Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.

Example:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]

* **Analysis**:

The question asks us to:

put nums[0] in index[0]

put nums[1] in index[1]

put nums[2] in index[2]
...

Until inputs are exhausted.   The index array gives us positions for dynamtically inserting into the new array.  It is **not the final state index**.  (Final state index should be a permutation of distinct integers 0, 1, 2, ..., len(input) - 1. 

* **Solution**:

So we follow the instruction to a tee. 
```Python
def f(nums, index):
    res = []
    for i in range(len(nums)):
        res.insert(index[i], nums[i])
    return res
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(f(nums, index))
# [0, 4, 1, 3, 2]
```

## 2. Leetcode 1920. Build Array from Permutation

Build an array A of the same length where A[i] = nums[nums[i]] for each 0 <= i < nums.length and return it, where 0 <= nums[i] < nums.length, and the elements in nums are distinct.

Example:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]

* **Analysis**:
Compare with the first question,  this one does not give us an index array for dynamic insertion.  Instead, it tells us what the final state should be <span class="coding">A[i] = nums[nums[i]]</span>. 

output[0] = input[input[0]]

output[1] = input[input[1]]
...

Since output can be appended from the value at the 0th position to the last one, we use the <span class="coding">append</span> method. 
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

## 3. Leetcode 1528 Permuation of a string

You are given a string s and an integer array index of the same length. The string s will be shuffled such that **the character at the ith position moves to index[i]** in the shuffled string.

Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode".

* **Analysis**:

Compare with the first question,  this one does also give us an index array.  But the numbers in the indices array are not meant for dynamic insertion positions in the new array.  Rather, it give the final state positions **from the input perspective**.  Because it dictates the final state but the **state is given from the input perspective**, we cannot use <span class="coding">append</span> because the input order and output order are different. 

So, we can **tempararily** create an output array with the same length, then assign the values at each position according to instruction.   If we don't have a temporary output array, we cannot make assignments by index since an empty array does not have any index yet.   What we put into the temporary output array does not matter as long as the length of the array is the same as the output. 

**input[0] = output[indices[0]]**

**input[1] = output[indices[1]]**
...

<div class="code-head"><span>code</span>newString1.py</div>

```py
def newString(s, indices):
    res = list(s) # or res = ['a'] * len(s)
    for i in range(len(s)):
        res[indices[i]] = s[i]  # follow instruction
    return ''.join(i for i in res)
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(newString(s, indices))
# leetcode
```

Since the problem asks for input[0] to be placed in indices[0] of the output, if we can zip these two arrays and then sort it by the values in indices, then we will have the correct output as well, as shown in the second solution for this problem below. 

<div class="code-head"><span>code</span>newString2.py</div>

```py
def newString(s, indices):
    d = dict(zip(indices,s))
    return ''.join(d[key] for key in sorted(d.keys()))

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(newString(s, indices))
# leetcode
```


* **Caution!**

The question is ***NOT*** asking for **output[0] = input[indices[0]]**. 

The state is not given from the output perspective.  Had we solve the problem with the wrong understanding, we would not have the right solutions. 

## 4. Passing Yearbooks - number of permutations

According to [Leetcode discussions](https://leetcode.com/discuss/interview-question/614096/facebook-interview-preparation-question-passing-yearbooks), this problem comes from Facebook recruiting portal

There are n students, numbered from 1 to n, each with their own yearbook.

They would like to pass their yearbooks around and get them signed by other students. You're given a list of n integers arr[1..n], which is guaranteed to be a permutation of 1..n.

Initially, each student is holding their own yearbook. The students will then repeat the following two steps each minute: 
Each student i will first sign the yearbook that they're currently holding (which may either belong to themselves or to another student), and then they'll pass it to student arr[i]. 

It's possible that arr[i] = i for any given i, in which case student i will pass their yearbook back to themselves. Once a student has received their own yearbook back, they will hold on to it and no longer participate in the passing process.

Output array: ith element is equal to the number of signatures that will be present in student i's yearbook once they receive it back.

* Example 1

n = 2

arr = [2, 1]

output = [2, 2]
The first student will sign their own yearbook and pass it to the second, who will also sign it and pass it back to the first student, resulting in 2 signatures. Meanwhile, the second student's yearbook will similarly be signed both by themselves and then by the first student.

* Example 2

n = 2

arr = [1, 2]

output = [1, 1]
Each student will simply pass their yearbook back to themselves, resulting in 1 signature each.


* **Analysis and Simplifying Problem**:
The problem statement is very long, even after I have shortened it. *Because it is very difficult to think with so many words. We should simplify the problem.*   Let's rewrite the question. 

Do we really need the "yearbooks"?   **An immobile student reunites with his yearbook is equivalent to a moving student reuniting with his original position after moving about according to the given order from the given array.**    The yearbook can be substituted with "soul", "mate", or just simply "self".  

If we use initial positions (1, ..., n) to represent students 1 to n, the given array A represent where to go, then, 

Student i at index 0, moves to (A[0] - 1)th index, and moves to (A[A[0] - 1] - 1)th index, ..., until back to index 0. 

Given n students, and array arr, which is a permutation of 1..n.  

Each student i will will move to arr[i], and will stop moving once it has returned to its starting position.  

Output array: number of moves student i will make. 

* **Analysis and Problem Rewrite**:


# Problems that ask for a number

## Leetcode 1480. Running Sum of 1d Array
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
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

# Problems that ask for returning index

## Two Sum


<div class="code-head"><span>code</span>twoSumUnsorted.py</div>

```py

def twoSumUnsorted(nums, target):
    dd = {}
    for idx, num in enumerate(nums):
        if target - num in dd:
            return [idx, dd[target - num]]
        else:
            dd[num] = idx
nums = [2, 3, 4]
target = 6
print(twoSumUnsorted(nums, target))     

nums = [11, 2,  7, 15]
target = 9
print(twoSumUnsorted(nums, target))    
```

