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
- [Puzzles](#puzzles)
  - [Leecode 665. Non-decreasing Array, Easy](#leecode-665-non-decreasing-array-easy)
  - [Leetcode 1920. Build Array from Permutation](#leetcode-1920-build-array-from-permutation)
  - [Leetcode 2011. Final Value of Variable After Performing Operations](#leetcode-2011-final-value-of-variable-after-performing-operations)
  - [Leetcode 1672. Richest Customer Wealth](#leetcode-1672-richest-customer-wealth)
  - [Leetcode 2289. Steps to Make Array Non-decreasing](#leetcode-2289-steps-to-make-array-non-decreasing)
  - [Loan balance amortization](#loan-balance-amortization)
  - [Partitioning problem](#partitioning-problem)
  - [Reversing an array](#reversing-an-array)
    - [Rotating an array](#rotating-an-array)
    - [Get missing number](#get-missing-number)
    - [Get missing number](#get-missing-number-1)
    - [Check for pair sum](#check-for-pair-sum)
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

## Leetcode 1672. Richest Customer Wealth
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
## Leetcode 2289. Steps to Make Array Non-decreasing

Problem: You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array.

Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.

Example 2:

Input: nums = [4,5,7,7,13]
Output: 0

Solution:
This problem took me some thinking. 

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



## Loan balance amortization

<span class="coding">list(accumulate(A))</span> can be used to solve more complex problems. 

It seems to be treating the first element in cashflows as balance, and the rest of elements in cashflows as payments. 

<div class="code-head"><span>code</span>accumulate.py</div>

```py
# Amortize a 5% loan of 1000 with 4 annual payments of 90
>>> cashflows = [1000, -90, -90, -90, -90]
>>> list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
[1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
```

## Partitioning problem
We want to partition an array in the following fashion:
Given an element called "pivot" (or the index of it) of the array of integers,  the ones smaller than this number should be placed before this number, and the ones larger than this number after. 

The following solution has time complexity $$O(n)$$ and space complexity $$O(1)$$.  I did this problem a few times.  There are 4 places I found myself making mistakes:
1. indent of the return (or forgot to return)
2. compare with the pivot, not anything else
3. the direction of the range
4. forgot to increment/decrement the pointer indices

<div class="code-head"><span>code</span>partition.py</div>

```py
def partition(pivot_idx, A):
    pivot = A[pivot_idx]
    N = len(A)
    small_idx = 0
    big_idx = N - 1
    print("Pivot is ",A[pivot_idx])
    # move smaller ones to the front
    for i in range(N):
        if A[i] < pivot:
            A[i], A[small_idx] = A[small_idx], A[i]
            small_idx += 1

    # move bigger ones to the front
    for i in reversed(range(N)):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[i], A[big_idx] = A[big_idx], A[i]
            big_idx -= 1

    return A
lt = [0, 1,2,0,2,1,1]
print(partition(3,lt))
```

The following code are from Github repository "Data Structure using Python". 

<div class="code-head"><span>code</span>Array.py</div>

```py
class Array(object):
    ''' sizeOfArray: denotes the total size of the array to be initialized
       arrayType: denotes the data type of the array(as all the elements of the array have same data type)
       arrayItems: values at each position of array
    '''
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    # magic methods to enable indexing
    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if (self.arrayItems[i] == keyToSearch):      # brute-forcing
                return i                                 # index at which element/ key was found

        return -1                                        # if key not found, return -1

    # function for inserting an element
    def insert(self, keyToInsert, position):
        if(self.sizeOfArray > position):
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)

    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.sizeOfArray > position):
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
        else:
            print('Array size is:', self.sizeOfArray)

if __name__ == '__main__':
    a = Array(10, int)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4,7)
    print(len(a))

```
We can use the array class we defined.  For example,

```python
# access
a = Array(100,int)
idx = a.search(0)
print("found at", idx)

a.insert(2,2)
print(a)

```

## Reversing an array

<div class="code-head"><span>code</span>a1_reverseArry.py</div>

```py
import Arrays

def  reversingAnArray(start, end, myArray):
    while(start < end):
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    myArray = Arrays.Array(10)
    myArray.insert(2, 2)
    myArray.insert(1, 3)
    myArray.insert(3, 1)
    print('Array before Reversing:',myArray)
    reversingAnArray(0, len(myArray), myArray)
    print('Array after Reversing:',myArray)

```

### Rotating an array

<div class="code-head"><span>code</span>a2_arrayRotation.py</div>

```py

from Arrays import Array

def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray

def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:',myArray)
    print('After Rotation:',rotation(3, myArray))

    # OUTPUT:
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
```

### Get missing number

<div class="code-head"><span>code</span>a3_findMissing.py</div>

```py

from Arrays import Array

def findMissing(myArray, n):
    n = n - 1
    totalSum = (n * (n + 1)) // 2
    for i in range(0, n):
        totalSum -= myArray[i]

    return totalSum

if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    myArray.delete(4, 4)
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray, len(myArray)))

    # OUTPUT:
    # Original Array: 0 1 2 3 5 6 7 8 9 0
    # Missing Element: 4
```

### Get missing number

<div class="code-head"><span>code</span>a4_odd_number_occurance.py</div>

```py
# Given an array of positive integers. All numbers occur even number of times except one
# number which occurs odd number of times. Find the number in O(n) time & constant space.

# XOR of all elements gives us odd occurring element. Please note that XOR of two elements
# is 0 if both elements are same and XOR of a number x with 0 is x.

# NOTE: This will only work when there is only one number with odd number of occurences.

def printOddOccurences(array):
    odd = 0

    for element in array:
        # XOR with the odd number
        odd = odd ^ element

    return odd

if __name__ == '__main__':
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(printOddOccurences(myArray))      # 4
```
### Check for pair sum

<div class="code-head"><span>code</span>a5_CheckForPairSum.py</div>

```py
# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose sum is exactly x.

def checkSum(array, sum):
    # sort the array in ascending order
    # new changes : made use of Python's inbuilt Merge Sort method
    # Reason for such change : Worst case Time complexity of Quick Sort is O(n^2) whereas Worst Case Complexity of Merge Sort is O(nlog(n))
    array = sorted(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex] ==  sum):
            return array[leftIndex], array[rightIndex]
        elif(array[leftIndex] + array[rightIndex] < sum):
            leftIndex += 1
        else:
            rightIndex += 1

    return False, False

##def quickSort(array):
##    if len(array) <= 1:
##        return array
##    pivot = array[len(array) // 2]
##    left = [x for x in array if x < pivot]
##    middle = [x for x in array if x == pivot]
##    right = [x for x in array if x > pivot]
##    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    number1, number2 = checkSum(myArray, sum)
    if(number1 and number2):
        print('Array has elements:', number1, 'and', number2, 'with sum:', sum)
    else:
        print('Array doesn\'t have elements with the sum:', sum)

```

