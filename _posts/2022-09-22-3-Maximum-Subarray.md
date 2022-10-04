---
layout: post
tag : array, dp, recursion, greedy
category: education
title: "Maximum Subarray"
description: The maximum subarray problem and solutions using brute force, greedy,dp and recursion. 
author: Sarah Chen
image: images/posts/photos/farm/IMG-1230.jpg

---
![](../images/posts/photos/farm/IMG-1230.JPG)
- [Problem](#problem)
  - [Brute force method](#brute-force-method)
    - [1. $$O(n^3)$$](#1-on3)
    - [2. $$O(n^2)$$ solution](#2-on2-solution)
  - [Kadane's algorithm (Fast and Slow method)](#kadanes-algorithm-fast-and-slow-method)
    - [Computing the best subarray's position](#computing-the-best-subarrays-position)
  - [O(n*log(n)) divide-and-conquer approach](#onlogn-divide-and-conquer-approach)
  - [Memorizing method (DP)](#memorizing-method-dp)
- [Reference](#reference)

The maximum subarray is a [well-known problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem) in computer science. We discussed its brute force and dynamic programming solutions in [Dynamic programming](https://pythonrsas.github.io/1-Dynamic-programming/#subarray-with-the-greatest-sum).   In this post, we deep dive into this problem using [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) as an example. 
![](https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Maximum_Subarray_Visualization.svg/440px-Maximum_Subarray_Visualization.svg.png)

# Problem 

Problem is from [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).  

Given an integer array nums, find the **contiguous** subarray (containing at least one number) which has the largest sum and return its sum.  給定一整數陣列 nums，找到其最大連續子陣列（至少有一個元素）之和，並回傳該總和。

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


## Brute force method

### 1. $$O(n^3)$$ 
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
### 2. $$O(n^2)$$ solution
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

## Kadane's algorithm (Fast and Slow method)

The Kadane's algorithm is a simple greedy strategy.  I call it "**Fast and Slow**" because it helps me unify similar approaches.  The method scans through input array once while maintaining two variables: the current sum and the max sum.  The max sum is a function of the current sum. 

1. current sum (*Fast*) is the maximum cumulative sum at the current position in the scan. It is permitted to restart at any position, and choose between to restart at the current index or to cumulate. Formally, current sum = max(current sum + num[i], current sum)

2. max sum (*Slow*) is the best of the all the current sums.  It is only updated when current sum finds a better one.  max sum = max(current sum, max sum)

I adapted the code from  [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Empty_subarrays_admitted). using my fast-slow interpretation. Fast is the one that scans linearly along the input array. Whereas Slow only changes when fast is better. 

<div class="code-head"><span>code</span>maxSubarray_fast_slow.py</div>

```py
def max_subarray(numbers):
    """Find the largest sum of any contiguous subarray."""
    if numbers == []:
        raise ValueError('Empty array has no nonempty subarrays')

    slow, fast = 0, 0
    for x in numbers:
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
def max_subarray(numbers):
    for i in range(len(numbers)):
        numbers[i] = max(numbers[i], numbers[i-1] + numbers[i])
    return max(numbers)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray(nums))
# 6
```

### Computing the best subarray's position
The algorithm can be modified to keep track of the starting and ending indices of the maximum subarray as well.  The code below is adapted from [Wikipedia](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Computing_the_best_subarray's_position). 

To get both the current index and number during scan is to use <span class="coding">enumerate</span>. 
<span class="coding">fast_end</span>: keeps track of the position of the current number being added or restarted with.  At all times, <span class="coding">fast_fast</span> $$<=$$ <span class="coding">fast_end</span>.

slow_start = slow_end = 0, both of them and slow_sum are updated only when fast_sum is bigger than slow_sum. 

<div class="code-head"><span>code</span>maxSubarray_positions_fast_slow.py</div>

```py
def max_subarray(numbers):
    """Find a contiguous subarray with the largest sum."""
    slow_sum = 0  # or: float('-inf')
    slow_start = slow_end = 0  # or: None
    fast_sum = 0
    for fast_end, x in enumerate(numbers):
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
```

[Professor Michael Goldwasser](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/maxsubarray.py) maintains a tuple of (maxSum, starting position, ending position) 

<div class="code-head"><span>code</span>maxSubarray_positions_fast_slow.py</div>

```py
def max_subarray(numbers):
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
## O(n*log(n)) divide-and-conquer approach

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

## Memorizing method (DP)

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

O(n) 的做法即這題的解法（的前半部分）。



至於進階提及的分治法，則是以下：
將目前的陣列分作兩半，遞迴左半邊以及右半邊各自的最大連續子陣列之和。停止條件很簡單，切到剩一個元素的時候直接回傳該元素值。

當求出左右兩邊各自的最大總和 L 、 R 之後，還會有一種情況我們沒有考慮到，也就是橫跨左右兩邊的連續最大。而該值可以藉由從中間開始，往左、往右找最長的總和非遞減數列。而該值 M 就是那兩個數列之和。

所以目前陣列的最大即是 L 、 M 、 R 中的最大值。

而這個方式為 O(n log n)。不過其實分治法一樣可以做到 O(n) ，待補。

（2021 / 07 / 14 更新）
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



# Reference

[Wikipedia Maximum Subarray](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Computing_the_best_subarray's_position
)
https://home.gamer.com.tw/artwork.php?sn=4871160

[Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

[Notes on Maximum Subarray Problem](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/)

[Five algorithmic solutions to the maximum subarray problem (see Bentley's Programming Pearls) by Michael Goldwasser](https://cs.slu.edu/~goldwamh/courses/slu/csci314/2012_Fall/lectures/maxsubarray/maxsubarray.py)