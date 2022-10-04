---
layout: post
tag : string
category: education
title: "Index of the First Occurrence in a String"
description: Leetcode 28. Find the Index of the First Occurrence in a String
author: Sarah Chen
image: images/posts/photos/farm/IMG-1230.JPG

---
![](../images/posts/photos/farm/IMG-1230.JPG)
- [Problem](#problem)
- [O(n*m) solution](#onm-solution)
- [More efficient O(n*m) solution](#more-efficient-onm-solution)
- [Use Python in & .index](#use-python-in--index)
- [Reference](#reference)

# Problem 

Problem is from [Leetcode 28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/).

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
回傳字串 needle 第一次在字串 haystack 中出現的索引值。如果 needle 不是 haystack 的一部分則回傳 -1 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"

Output: 0

Explanation: "sad" occurs at index 0 and 6.

The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

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
解題思維：
先判斷字串 needle 的長度，如果是 0 則直接回傳 0；如果大於字串 haystack 的長度，則直接回傳 -1。

剩下的情況就是直接跑過一次 haystack 字串。每遇到一個字元，判斷其與後面的字元組成的字串（要跟 needle 同長度）是不是一樣的字串。如果不是就繼續找下一個字元。如果是就回傳該位置的索引值。

Rooms for improvement:
We don't need to scan all the way to the end: scan to len(H) - len(N) is good enough. 

# More efficient O(n*m) solution

I learned this trick from a user named word_addict from Leetcode Discussion.  We can use slicing to test if needle is found instead of using a helper function to scan through each letter of needle <span class="coding">if H[i:i+len(N)] == N</span>.

<div class="code-head"><span>code</span>needleHaystack.py</div>

```py
def strStr(H, N):
    """
    :type H: str
    :type N: str
    :rtype: int
    """
    for i in range(len(H) - len(N)+1):
        if H[i:i+len(N)] == N:
            return i
    return -1
```

# Use Python in & .index

It seems much ado about nothing that we can just use <span class="coding">in</span> operator in Python. 

<span class="coding">H.index(N)</span> gives us the first index of N in H. 

<div class="code-head"><span>code</span>needleHaystack.py</div>

```py
def strStr(H, N) -> int:
    if N in H:
        return H.index(N)
    else:
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

# Reference
https://home.gamer.com.tw/artwork.php?sn=4867844

[Leetcode 28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)