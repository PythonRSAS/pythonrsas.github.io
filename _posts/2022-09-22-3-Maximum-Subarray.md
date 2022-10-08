---
layout: post
tag : array, dp, recursion, greedy
category: education
title: "Maximum Subarray"
description: The maximum subarray problem and solutions using brute force, greedy,dp and recursion. 
author: Sarah Chen
image: images/posts/photos/farm/IMG-1230.jpg

---
![](../images/posts/photos/farm/IMG-1930.jpg)
- [Maximum profit from buying and selling stocks](#maximum-profit-from-buying-and-selling-stocks)
- [Leetcode problem](#leetcode-problem)
- [Brute force method](#brute-force-method)
  - [1. $$O(n^3)$$](#1-on3)
  - [2. $$O(n^2)$$ solution](#2-on2-solution)
- [$$O(n)$$ Solution: Kadane's algorithm (Fast and Slow method)](#on-solution-kadanes-algorithm-fast-and-slow-method)
- [Computing the best subarray's position](#computing-the-best-subarrays-position)
- [$$O(n^2)$$ and $$O(n*log(n))$$ divide-and-conquer recursion approach](#on2-and-onlogn-divide-and-conquer-recursion-approach)
- [Memorizing method (DP)](#memorizing-method-dp)
- [Reference](#reference)

The maximum subarray is a [well-known problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) in computer science. We discussed its brute force and dynamic programming solutions in [Dynamic programming](https://pythonrsas.github.io/1-Dynamic-programming/#subarray-with-the-greatest-sum).   In this post, we deep dive into this problem using [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) as a test example.  

Please pardon me if you find the notes messy and send me a message if you see anything that should be corrected.  

# Maximum profit from buying and selling stocks
In Introduction to Algorithms (Cormen and others), the problem is presented as follows:
Suppose that you been offered the opportunity to invest in the Volatile Chemical
Corporation. Like the chemicals the company produces, the stock price of the
Volatile Chemical Corporation is rather volatile. You are allowed to buy one unit
of stock only one time and then sell it at a later date. To compensate for this restriction, you are allowed to
learn what the price of the stock will be in the future. Your goal is to maximize
your profit. 

In order to design an algorithm with an $$O(n^2)$$ running time, We want to find a sequence of days over which the net change from the first day to the last is maximum. Instead of looking at the
daily prices, let us instead consider the daily change in price, where the change on
day i is the difference between the prices after day i - 1 and after day i.   We now want to **find the nonempty, contiguous subarray of A whose values have the largest sum**. We call this contiguous subarray
the **maximum subarray**. 



# Leetcode problem

Problem is from [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).  

Given an integer array nums, find the **contiguous** subarray (containing at least one number) which has the largest sum and return its sum.  給定一整數陣列 nums，找到其最大連續子陣列（至少有一個元素）之和，並回傳該總和。

Example 1:
![Example 1:](https://assets.leetcode.com/uploads/2019/12/18/q2-e1.png)

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
[Example 2:](https://assets.leetcode.com/uploads/2019/12/18/q2-e5-.png)

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
# Brute force method
## 1. $$O(n^3)$$ 
Since there are $$\frac{(n+1)*n}{2}$$ subarrays, and each takes $$O(n)$$ to sum, the time complexity is $$O(n^3)$$. 

<div class="code-head"><span>code</span>maxSubarray_bfO3.py</div>

```py
def max_subarray(A):
    maxSum = 0
    for i in range(len(A)): # starting position
        for j in range(i, len(A)): # ending position
            sum = 0
            for k in range(i,j):
                sum += A[k]
                if sum > maxSum:
                    maxSum = sum
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
```
## 2. $$O(n^2)$$ solution
We can improve the above $$O(n^3)$$ solution.
Idea: The sum of A[i..j] can be efficiently calculated as (sum of A[i..j-1]) + A[j].

<div class="code-head"><span>code</span>maxSubarray_bfO3.py</div>

```py
def max_subarray(A):
    maxSum = 0
    for i in range(len(A)): # starting position
        sum = 0
        for j in range(i, len(A)): # ending position
            sum += A[j] #  sum is that of A[i..j]
            if sum > maxSum:
                maxSum = sum
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
```
# $$O(n)$$ Solution: Kadane's algorithm (Fast and Slow method)

The Kadane's algorithm is a simple greedy strategy.  I call it "**Fast and Slow**" because it helps me unify similar approaches.  The method scans through input array exactly once while maintaining two variables: the current sum and the max sum.  The max sum is a function of the current sum. 

1. current sum (*Fast*) is the maximum cumulative sum at the current position in the scan. It is permitted to restart at any position, and choose between to restart at the current index or to cumulate. Formally, current sum = max(current sum + num[i], current sum)

2. max sum (*Slow*) is the best of the all the current sums.  It is only updated when current sum finds a better one.  max sum = max(current sum, max sum)

I adapted the code from  [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Empty_subarrays_admitted). using my fast-slow interpretation. Fast is the one that scans linearly along the input array. Whereas Slow only changes when fast is better. 

<div class="code-head"><span>code</span>maxSubarray_fast_slow.py</div>

```py
def max_subarray(A):
    """Find the largest sum of any contiguous subarray."""
    if A == []:
        raise ValueError('Empty array has no nonempty subarrays')

    slow, fast = 0, 0
    for x in A:
        fast = max(x, fast + x) # choose between restart at x or cumulate from its previous value
        slow = max(slow, fast) # update only if new fast is bigger than slow
    return slow
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
```

There are many variations of the same idea.  For example, the version below does not even bother to keep the two variables and directly modifies the input array to be an array of the fast. 

<div class="code-head"><span>code</span>maxSubarray_fast_slow.py</div>

```py
def max_subarray(A):
    for i in range(len(A)):
        A[i] = max(A[i], A[i-1] + A[i])
    return max(A)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
```
# Computing the best subarray's position
The algorithm can be modified to keep track of the starting and ending indices of the maximum subarray as well.  

$$f$$: fast sum.
$$s$$: slow (the maximum) sum.
$$i$$: ending index of fast.
$$slow/_start$$: starting index of slow.
$$slow/_end$$: ending index of slow.
In time, we normally think of start as larger than end.  But when we look at an array (or a ruler), the start is smaller than the end.  We update slow and its associated indices only when $$f>s$$.  

<div class="code-head"><span>code</span>maxSubarray_positions_fast_slow.py</div>

```py
def max_subarray(A):
    fast_start = 0
    f = s = 0
    slow_start = slow_end = 0  # or: None
    for i in range(len(A)):
        if f + A[i] < 0:
            f_start = i
            f = 0
        else:
            f = f+ A[i]
        if s < f:
            s = f
            slow_start = f_start
            slow_end = i
    return s, slow_start, slow_end
```

The code below is adapted from [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Computing_the_best_subarray's_position).  It is similar to the code above. 

It uses <span class="coding">enumerate</span>get both the current index and number during scan instead of i and A[i].

<span class="coding">fast_end</span>: keeps track of the position of the current number being added or restarted with.  At all times, $$fast\_start <= fast\_end$$.   
We initialize slow_start, slow_end and slow_sum as zero, and update them only when fast_sum is bigger than slow_sum. 

<div class="code-head"><span>code</span>maxSubarray_positions_fast_slow.py</div>

```py
def max_subarray(A):
    """Find a contiguous subarray with the largest sum."""
    slow_sum = 0  # or: float('-inf')
    slow_start = slow_end = 0  # or: None
    fast_sum = 0
    for fast_end, x in enumerate(A):
        if fast_sum <= 0:
            # Start a new sequence at the current element
            fast_start = fast_end
            fast_sum = x
        else:
            # Extend the existing sequence with the current element
            fast_sum += x

        if fast_sum > slow_sum:
            slow_sum = fast_sum
            slow_start = fast_start
            slow_end = fast_end + 1  # the +1 is to make 'slow_end' match Python's slice convention (endpoint excluded)

    return slow_sum, slow_start, slow_end
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
slow_sum, slow_start, slow_end = max_subarray(nums)
nums[slow_start: slow_end]
# [4, -1, 2, 1]
sum(nums[slow_start: slow_end])
# 6
```

[St. Louis University Professor Michael Goldwasser's solutions](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/maxsubarray.py) maintain tuples of (maxSum, starting position, ending position) to keep track of the max sum and the start-end positions.  

<div class="code-head"><span>code</span>maxSubarray_positions_fast_slow.py</div>

```py
def max_subarray(A):
def algorithm4(A):
    """A linear algoirthm based on a simple greedy strategy.

    As we let index i increase, we keep track of two pieces of information:
      * maxhere     which is maximum subarray ending specifically at index i
      * maxsofar    which is maximum subarray for anything from A[0:i]

    Returns tuple designating optimal (maxsum, start, stop).
    """
    n = len(A)
    maxsofar = (0, 0, 0)           # (t, start, stop) such that sum(A[start,stop]) = t
    maxhere = (0, 0)               # (t, start) such that sum(A[start:i]) = t
    for i in range(1, n+1):
        if maxhere[0] + A[i-1] > 0:
            maxhere = (maxhere[0] + A[i-1], maxhere[1])
        else:
            maxhere = (0, i)
        if maxhere[0] > maxsofar[0]:
            maxsofar = (maxhere[0], maxhere[1], i)
    return maxsofar
```
# $$O(n^2)$$ and $$O(n*log(n))$$ divide-and-conquer recursion approach

Section 4.1 of Introduction to Algorithm describes a divide-and-conquer recursion approach. 
![max_subarray_recursion](..\images\posts\max_subarray_recursion.PNG).

The maximum subarray has 3 possible locations: in the left half, in the right half, or in the middle.  We need to consider how to solve the middle section before recurse on the two halves. 

![max_crossing_subarray](..\images\posts\max_crossing_subarray.PNG)
將目前的陣列分作兩半，遞迴左半邊
以及右半邊各自的最大連續子陣列之和。停止條件很簡單，切到剩一個元素的時候直接回傳該元素值。

當求出左右兩邊各自的最大總和 L 、 R 之後，還會有一種情況我們沒有考慮到，也就是橫跨左右兩邊的連續最大。而該值可以藉由從中間開始，往左、往右找最長的總和非遞減數列。而該值 M 就是那兩個數列之和。

所以目前陣列的最大即是 L 、 M 、 R 中的最大值。

而這個方式為 O(n log n)。不過其實分治法一樣可以做到 O(n) ，待補。


可以看到我們的癥結點是在橫跨左右兩半的子陣列。不過仔細觀察後，可以看到它的內容必定是左側的最大後綴和以及右側的最大前綴和所合併而成。

而實際上，一個陣列的最大後綴和、最大前綴和可以在分治的時候順便求得：
假設我們現在要求
最大連續和 M、
最大前綴和 P、
最大後綴和 S、
陣列總和 T、
這四個值。

則對於陣列 nums 我們將其切一半：
設左邊的解為 ML 、 PL 、 SL 、 和 TL
設右邊的解為 MR 、 PR 、 SR 、 和 TR

則我們可以合併左右兩半的解得到
M = max(ML, MR, SL + PR)
P = max(PL, TL + PR)
S = max(SR, TR + SL)
T = TL + TR

而當陣列只有一個元素時，M = P = S = T = 該元素值。

因此時間複雜度 T(n) = 2T(n ÷ 2) + O(1)。根據主定理（Master Theorem），可以看到 T(n) = O(n)。


The following code is from [Professor Michael Goldwasser's course notes](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/maxsubarray.py).  

<div class="code-head"><span>code</span>maxSubarray_recurse.py</div>

```py
def recurse(A, start, stop):
    """Recursion for algorithm3 that only considers implicit slice A[start:stop])."""
    if stop == start:                         # zero elements
        return (0, 0, 0)               
    elif stop == start + 1:                   # one element
        if A[start] > 0:
            return (A[start], start, stop)
        else:
            return (0, start, start)
    else:                                     # two or more elements
        mid = (start + stop) // 2

        # find maximum sum(A[i:mid]) for i < mid
        total = 0
        lmax = (0, mid)                       # (t,i) such that sum(A[i:mid]) = t
        for i in range(mid-1, start-1, -1):
            total += A[i]
            if total > lmax[0]:
                lmax = (total,i)
                
        # find maximum sum(A[mid:j]) for j > mid
        total = 0
        rmax = (0, mid)                       # (t, j) such that sum(A[mid:j]) = t
        for j in range(mid+1, stop+1):
            total += A[j-1]
            if total > rmax[0]:
                rmax = (total,j)

        overlay = (lmax[0]+rmax[0], lmax[1], rmax[1])

        return max(recurse(A, start, mid),
                   recurse(A, mid, stop),
                   overlay)

def algorithm3(A):
    """A divide-and-conquer approach achieving O(n log n) time.

    We find the maximum solution from the left half, the maximum from the right,
    and the maximum solution that straddles the middle.  One of those three is
    the true optimal solution.

    Returns tuple designating optimal (maxsum, start, stop).
    """
    return recurse(A, 0, len(A))
```
# Memorizing method (DP)

Each time when we enounter overlapping subproblems, it is time to consider dynamic programming. 

When we sum the $$ith$$ to the $$jth$$ element, do we really have to start from the beginning $$ith$$?  If we store cumulative sums, then we just have to look it up like we did in the Fibonaci problem. 

<div class="code-head"><span>code</span>number of subarrays DP.py</div>

```py
import itertools
def maxSubArrayDP(A):
    minSum = maxSum = 0
    print(list(itertools.accumulate(A)))
    for runningSum in itertools.accumulate(A):
        minSum = min(minSum, runningSum)
        maxSum = max(maxSum, runningSum - minSum)
    return maxSum
``` 
# Reference
[Introduction to Algorithm, 3rd Edition, 4.1 The maximum-subarray problem](https://sd.blackball.lv/library/Introduction_to_Algorithms_Third_Edition_(2009).pdf)

[Wikipedia Maximum Subarray](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Computing_the_best_subarray's_position
)

https://home.gamer.com.tw/artwork.php?sn=4871160

[Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

[Notes on Maximum Subarray Problem](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/)

[Five algorithmic solutions to the maximum subarray problem (see Bentley's Programming Pearls) by Michael Goldwasser](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/maxsubarray.py)

In case address is changed and link is broken, I have copied all 4 algorithms that Professor Goldwasser posted. 

```python

"""
Five algorithmic solutions to the maximum subarray problem (see Bentley's Programming Pearls).

Author: Michael Goldwasser

Module can be executed as a test harness.

Use -h flag for documentation on usage.
"""

#-----------------------------------------------------------------------
def algorithm1(A):
    """A brute-force algorithm using cubic-time.

    This algorithm tries every possible i < j pair, and computes the
    sum of entries in A[i:j].

    Returns tuple designating optimal (maxsum, start, stop).
    """
    n = len(A)
    maxsofar = (0, 0, 0)                    # (t, start, stop) with sum(A[start:stop]) = t
    for i in range(n):                      # potential start index
        for j in range(i+1, n+1):           # potential stop index
            total = 0
            for k in range(i,j):            # compute sum(A[i:j])
                total += A[k]
            if total > maxsofar[0]:         # if new best, record parameters
                maxsofar = (total, i, j)
    return maxsofar

#-----------------------------------------------------------------------
def algorithm2a(A):
    """A quadratic time approach to brute force by using previous sums.

    Uses fact that sum(A[i:j]) = sum(A[i:j-1]) + A[j-1] to avoid a third nested loop.

    Returns tuple designating optimal (maxsum, start, stop).
    """
    n = len(A)
    maxsofar = (0, 0, 0)                    # (t, start, stop) with sum(A[start:stop]) = t
    for i in range(n):                      # potential start index
        total = 0                           # maintain sum(A[i:j]) as j increases
        for j in range(i+1, n+1):
            total += A[j-1]                 # thus total is now sum(A[i:j])
            if total > maxsofar[0]:
                maxsofar = (total, i, j)
    return maxsofar

#-----------------------------------------------------------------------
def algorithm2b(A):
    """A quadratic time approach to brute force using prefix sums.

    precomputes sum(A[0:j]) for each j.

    That allows for O(1) time computation of sum(A[i:j]) = sum(A[0:j]) - sum(A[0:i])

    Returns tuple designating optimal (maxsum, start, stop).
    """
    n = len(A)

    cumulative = [0] * (n+1)                 # cumulative[i] = sum(A[0:i])
    for i in range(n):
        cumulative[i+1] = cumulative[i] + A[i]
    
    maxsofar = (0, 0, 0)                    # (t, start, stop) with sum(A[start:stop]) = t
    for i in range(n):                      # potential start index
        for j in range(i+1, n+1):
            total = cumulative[j] - cumulative[i]
            if total > maxsofar[0]:
                maxsofar = (total, i, j)
    return maxsofar

#-----------------------------------------------------------------------
def recurse(A, start, stop):
    """Recursion for algorithm3 that only considers implicit slice A[start:stop])."""
    if stop == start:                         # zero elements
        return (0, 0, 0)               
    elif stop == start + 1:                   # one element
        if A[start] > 0:
            return (A[start], start, stop)
        else:
            return (0, start, start)
    else:                                     # two or more elements
        mid = (start + stop) // 2

        # find maximum sum(A[i:mid]) for i < mid
        total = 0
        lmax = (0, mid)                       # (t,i) such that sum(A[i:mid]) = t
        for i in range(mid-1, start-1, -1):
            total += A[i]
            if total > lmax[0]:
                lmax = (total,i)
                
        # find maximum sum(A[mid:j]) for j > mid
        total = 0
        rmax = (0, mid)                       # (t, j) such that sum(A[mid:j]) = t
        for j in range(mid+1, stop+1):
            total += A[j-1]
            if total > rmax[0]:
                rmax = (total,j)

        overlay = (lmax[0]+rmax[0], lmax[1], rmax[1])

        return max(recurse(A, start, mid),
                   recurse(A, mid, stop),
                   overlay)

def algorithm3(A):
    """A divide-and-conquer approach achieving O(n log n) time.

    We find the maximum solution from the left half, the maximum from the right,
    and the maximum solution that straddles the middle.  One of those three is
    the true optimal solution.

    Returns tuple designating optimal (maxsum, start, stop).
    """
    return recurse(A, 0, len(A))

#-----------------------------------------------------------------------
def algorithm4(A):
    """A linear algoirthm based on a simple greedy strategy.

    As we let index i increase, we keep track of two pieces of information:
      * maxhere     which is maximum subarray ending specifically at index i
      * maxsofar    which is maximum subarray for anything from A[0:i]

    Returns tuple designating optimal (maxsum, start, stop).
    """
    n = len(A)
    maxsofar = (0, 0, 0)           # (t, start, stop) such that sum(A[start,stop]) = t
    maxhere = (0, 0)               # (t, start) such that sum(A[start:i]) = t
    for i in range(1, n+1):
        if maxhere[0] + A[i-1] > 0:
            maxhere = (maxhere[0] + A[i-1], maxhere[1])
        else:
            maxhere = (0, i)
        if maxhere[0] > maxsofar[0]:
            maxsofar = (maxhere[0], maxhere[1], i)
    return maxsofar


#-----------------------------------------------------------------------
if __name__ == '__main__':
    from optparse import OptionParser
    import sys
    import time
    import random

    def quit(message=None):
        if message: print(message)
        sys.exit(1)

    parser = OptionParser(usage='usage: %prog [options]')

    parser.add_option('-n', dest='size', type='int', default=512,
                      help='number of elements in data set [default: %default]')
    
    parser.add_option('-a', dest='num_alg', metavar='NUM', type='int', default=5,
                      help='number of algorithms to test [default: %default]')
    
    parser.add_option('-s', dest='seed', type='int', default=None,
                      help='random seed for data set [default: %default]')   

    (options,args) = parser.parse_args()

    if options.size <= 0:
        quit('n must be positive')
    
    if not 1 <= options.num_alg <= 5:
        quit('invalid number of algorithms to test')
    
    if options.seed is None:
        options.seed = random.randrange(1000000) # print('Using seed: {0}'.format(options.seed))
    random.seed(options.seed)

    data = [random.uniform(-100,100) for _ in range(options.size)]
          
    algorithms = (algorithm1, algorithm2a, algorithm2b, algorithm3, algorithm4)

    print('Running tests for {0} algorithms using n={1} and seed={2}'.format(options.num_alg,options.size,options.seed))
    for alg in reversed(algorithms[len(algorithms)-options.num_alg:]):
        start = time.time()
        answer = alg(data)
        end = time.time()
        print("{0:<11} found sum(data[{1}:{2}])={3:.2f} using {4:.3f} seconds of computation".format(
            alg.__name__, answer[1], answer[2], answer[0], (end-start)))
```