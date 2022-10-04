---
layout: post
tag : array
category: education
title: "Index of the First Occurrence in a String"
description: Leetcode 53. Maximum Subarray
author: Sarah Chen
image: images/posts/photos/farm/IMG-1230.JPG

---
![](../images/posts/photos/farm/IMG-1230.JPG)
- [Problem](#problem)
- [O(n*m) solution](#onm-solution)
- [Reference](#reference)

# Problem 

Problem is from [Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

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
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 

# O(n*m) solution

First, consider edge case.  If length of needle is longer than length of haystack, then return -1. 

Them we scan haystack and stop only if the first letters of haystack and needle match.  We use a helper function <span class="coding">test</span> to test if needle is found at each stop location i. 

<div class="code-head"><span>code</span>needleHaystack.py</div>

```py
def needleHaystack(H, N):
    def test(i):
        res = False
        for j in range(len(N)):
            if H[i+j] == N[j]:
                continue
            else:
                return False
        return True
    if len(N) > len(H): # edge case
        return -1
    for i in range(len(H)):
        if H[i] == N[0]:
            if test(i):
                return i
            else:
                continue
    return -1

haystack = "sadbutsad"
needle = "sad"
print(needleHaystack(haystack, needle))
# 0
haystack = "leetcode"
needle = "leeto"
print(needleHaystack(haystack, needle))
# -1
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
https://home.gamer.com.tw/artwork.php?sn=4871160

[Leetcode 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)