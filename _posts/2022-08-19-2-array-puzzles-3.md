---
layout: post
tag : arrays, puzzles, easy
category: education
title: "array puzzles"
description: easy puzzles that based on arrays from Leetcode
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Leecode 2114. Max number of words in sentences](#leecode-2114-max-number-of-words-in-sentences)
- [Leetcode 1512. Number of identical pairs of numbers in an array](#leetcode-1512-number-of-identical-pairs-of-numbers-in-an-array)
- [Leetcode 1431. If largest if increment by k](#leetcode-1431-if-largest-if-increment-by-k)
- [Leetcode 2011. Final Value of Variable After Performing Operations](#leetcode-2011-final-value-of-variable-after-performing-operations)
- [Leetcode 1672. Max sum of subarrays](#leetcode-1672-max-sum-of-subarrays)
- [1389. Create Target Array in the Given Order - super easy](#1389-create-target-array-in-the-given-order---super-easy)
- [1528. Rearragne String](#1528-rearragne-string)


# Leecode 2114. Max number of words in sentences

* Problem:
Given a list of sentences, find the maximum number of words of all the sentences.

* Constraints:
all lower case and no white space

* Solution 1: Each sentence is an array of words separated with a space.  The number of words is the number of space + 1. 

* Complexity:

```python
def MaxWords1(sentences):
    # i represents a sentence in the list of sentences
    return max([i.count(' ') for i in sentences])
```

* Solution 2: Each sentence is an array of words separated with a space.  Split the sentence into words and count. 

* Complexity:

```python
def MaxWords2(sentences):
    # i represents a sentence in the list of sentences
    return max([len(i.split()) for i in sentences])
```

* Edge case:

# Leetcode 1512. Number of identical pairs of numbers in an array

* Problem:
A pair is identical if A[i] == A[j] & i < j. 

* Example 1:

* Solution 1:
Use <span class="coding">collections.Counter</span>, creates a dictionary of frequencies.
Note that because the keys of the dictionary are integers, we **cannot** use <span class="coding">for key, value in Counter(A)</span>. 

Instead, we can use <span class="coding">for value in Counter(A).values()</span>.
```python
def countSame(A):
    res = 0
    for v in Counter(A).values():
        if v >= 2:
            res += v * (v - 1) /2
    return int(res)
```

# Leetcode 1431. If largest if increment by k

* Solution 1: Use numpy array

```python
def f(A):


nums = [1,2,3,4]
print(f(nums))
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

# Leetcode 2011. Final Value of Variable After Performing Operations 
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

# Leetcode 1672. Max sum of subarrays
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

# 1389. Create Target Array in the Given Order - super easy
* Summary: this problem is super easy.  Just follow instruction and use <span class="coding">list.insert(where, what)</span>.
> Using indexing to assign values will not work because indices are repeated.  Use **.insert()**. 

* Problem
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
[0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

* Solution
```python
def newArray(A, B):
    C = []
    for i in range(len(A)):
        C.insert(B[i], A[i])
    return C
print(newArray(nums, index))
```

# 1528. Rearragne String
* Summary: this problem is super easy.  Just follow instruction and be careful. 

* Problem
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after rearrange per indices.

```python

def newArray(A, B):
    res = []
    for index, alph in enumerate(A):
        res[B[index]] = alph
        return res
```