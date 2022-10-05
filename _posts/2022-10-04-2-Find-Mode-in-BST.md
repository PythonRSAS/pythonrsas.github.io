---
layout: post
tag : BST, DFS
category: education
title: "Find Mode in BST"
description: LeetCode - 501. Find Mode in Binary Search Tree
author: Sarah Chen
image: images/posts/photos/farm/IMG-1230.jpg

---
![](../images/posts/photos/farm/IMG-1930.jpg)
- [A different mode finding problem](#a-different-mode-finding-problem)
- [Problem](#problem)
- [Brute force method O(n log(n))](#brute-force-method-on-logn)
- [Solution](#solution)
- [Reference](#reference)

In this post, we deep dive into this problem [LeetCode - 501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/). 

Please pardon me if you find the notes messy (still working on it) and send me a message if you see anything that should be corrected.   
# A different mode finding problem
題目大意：
輸入有多列，每列給定一字串（只包含小寫字母）。求該字串中連續出現最多次的字母為何？如果有多個連續出現最多次的，則請找到最早出現的字母。

範例輸入：
abbcc
cciiiiiiiixxxxxxxxxxxxguuuuuuufugpccccccc

範例輸出：
b 2
x 12

解題思維：
用一個整數變數 C 當作計數器（一開始設為 1）、一個整數變數 max 當作最大值，以及一個字元變數 T 儲存最大值發生時的字元（即所求）。

跳過字串第一個字元從第二個字元開始，對於第 i 個字元，看第 i - 1 個字元是否與它相同。

如果是，則計數器 C 加 1 ；反之，判斷 C 的值跟 max 的大小。如果 max < C ，則 max 更新為 C 之值，然後將 T 設為第 i - 1 個字元；其他的情況，max 與 T 更新。

字串掃完之後，因為最後一個連續的字元尚未判斷過其與 max 的大小。所以仿照上面的做法去判斷以及更新 max 之值。此時字元 T 與整數 max 之值即為所求。


# Problem 

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.  給定一棵可重複元素的二元搜尋樹（Binary Search Tree，BST），找到 BST 中所有的眾數（出現最多次的元素）。

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

Example 1:

Input: root = [1,null,2,2]
Output: [2]

範例測資：
給定 BST 為 [1,null,2,2]，
１
　＼
　　２
　／
２
回傳 [2]。

Example 2:

Input: root = [0]
Output: [0]

# Brute force method O(n log(n))

<div class="code-head"><span>code</span>findMode_bf.py</div>

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
```

# Solution
二元搜尋樹有一個特性——其中序探訪（這題有說明中序探訪的意思）得到的序列為一個已排序好的數列。

因此，我們就對該樹做中序探訪。由上特性可知此行為等價於掃過一個排序好的數字陣列，因此眾數就變成了連續出現最多次的數字（因為相同的數字會排在一起）

<div class="code-head"><span>code</span>findMode_bf.py</div>

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
```

# Reference

[LeetCode - 501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

https://home.gamer.com.tw/artwork.php?sn=4971259
