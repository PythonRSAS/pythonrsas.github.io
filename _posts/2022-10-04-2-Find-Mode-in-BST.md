---
layout: post
tag : BST, DFS
category: education
title: "Find Mode in BST"
description: Find mode in sorted array and LeetCode - 501. Find Mode in Binary Search Tree
author: Sarah Chen
image: images/posts/photos/farm/IMG-1930.jpg

---
![](../images/posts/photos/farm/IMG-1930.jpg)
- [Problem 1: 最長連續字母](#problem-1-最長連續字母)
  - [Three-variable solution for arrays](#three-variable-solution-for-arrays)
- [Problem 2: find Mode in Binary Search Tree](#problem-2-find-mode-in-binary-search-tree)
  - [Solution: reduce tree problem to array problem](#solution-reduce-tree-problem-to-array-problem)
  - [Other ways to get the list from tree traversal](#other-ways-to-get-the-list-from-tree-traversal)
- [Work in progress](#work-in-progress)
- [Reference](#reference)

In this post, we explore problems on counting the most frequent consecutive occurence of a number or string.  
Please pardon me if you find the notes messy (still working on it) and send me a message if you see anything that should be corrected.   
# Problem 1: 最長連續字母
題目大意：
輸入有多列，給定一字串（只包含小寫字母）。求該字串中連續出現最多次的字母為何？如果有多個連續出現最多次的，則請找到最早出現的字母。

範例輸入：
abbcc
cciiiiiiiixxxxxxxxxxxxguuuuuuufugpccccccc

範例輸出：
b 2
x 12

解題思維：
**用一個整數變數 C (fast) 當作計數器**（一開始設為 1）、**一個整數變數 M (slow) 當作最大值**，**以及一個字元變數 T 儲存最大值發生時的字元（即所求）**。

跳過字串第一個字元從第二個字元開始，對於第 i 個字元，看第 i - 1 個字元是否與它相同。

如果是，則計數器 C 加 1 ；反之，C 重设为 1.  然后判斷 C 的值跟 M 的大小。如果 M < C ，則 M 更新為 C 之值，然後將 T 設為第 i 個字元。

字串扫完后，字元 T 與整數 M 之值即為所求。

## Three-variable solution for arrays
We use 3 variables: 

C: initialized as 1

M: the maximum count, initialized as 1

T: the letter when the mode occurs. Initialized as the first letter. 

Procedures:
For i in range(1, length of input):
    
    Compare current letter with previous one.  
    
    If they are the same then
        
        C++
    
    If they are not the same then
        
        C restart at 1
    
    If M < C then
        
        M = C and update T to be the current letter

Return M and T

Note that this code can be **used for both strings and arrays**. 
<div class="code-head"><span>code</span>findMode_string.py</div>

```py
def findMode(A):
    C = 1
    M = 1
    T = A[0]
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            C += 1
        else:
            C = 1
        if M < C:
            M = C
            T = A[i]
    return (T, M)
letters = "cciiiiiiiixxxxxxxxxxxxguuuuuuufugpccccccc"
print(findMode(letters))

letters = "abbcc"
print(findMode(letters))
```

The time complexity is O(n), and the space complexity is O(1) as we only have 3 variables keeping track of things.

# Problem 2: find Mode in Binary Search Tree

Problem is from [LeetCode - 501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/). 

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.  給定一棵可重複元素的二元搜尋樹（Binary Search Tree，BST），找到 BST 中所有的眾數（出現最多次的元素）。

If the tree has more than one mode, return them in any order.  
注：如果一個樹有多個眾數，則可以任意順序將它們回傳。

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

## Solution: reduce tree problem to array problem
The idea is to first get the sorted array from inorder traversal.  Then use the same algorithm as Problem 1 to get the mode.

二元搜尋樹有一個特性——其中序探訪. 中序探訪得到的序列為一個已排序好的數列。
BST characteristic: **inorder traversal on BST is equivalent to scanning a sorted array**.  Since it is sorted, the mode is therefore the number that is repeated **consecutively** the most. 

因此，我們就對該樹做中序探訪。由上特性可知**此行為等價於掃過一個排序好的數字陣列**，因此**眾數就變成了連續出現最多次的數字**（因為相同的數字會排在一起.  We have **reduce this mode of binary search tree problem to the problem finding mode in a string (or array)**.  I find this is much easier to work with than mixing the actions simutanously with tree traversals. 

In code below, we use <span class="coding">inorder(root)</span> function to get the list of nodes from inorder traversal of the tree.  Then we use the same function for problem 1 to get the mode from the input array. 

The <span class="coding">inorder</span> function is a recursive function that **returns inorder travesal of the left child list, concatenated with [root.val], and the inorder traversal of the right child list.  The base case returns an empty list**.  

> **Inorder travesal root.val is in the middle, between left and right**. 

The drawback of this inorder retreaval of nodes using **list concatenation is extra cost on space**.  Because it creates a new list at every recursive call.
```python
def inorder(root):
    if root==None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
```

<div class="code-head"><span>code</span>findMode_bf.py</div>

```py
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def findMode(A):
    """
    return mode of consecutive number or letter from input array
    C : fast counter
    M: slow max counter
    """
    C = 1
    M = 1
    T = A[0]
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            C += 1
        else:
            C = 1
        if M < C:
            M = C
            T = A[i]
    return T
def inorder(root):
    """
    inorder traversal that returns the list of visited nodes
    """
    if root==None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
# define the tree
Root = TreeNode(val = 1)        
Root.right = TreeNode(val = 2)
Root.right.left = TreeNode(val = 2)

A = inorder(Root) # get array from inorder traversal
print(findMode(A)) # calling the function
# 2


```
１
　＼
　　２
　／
２


## Other ways to get the list from tree traversal
This is from [stackoverlow](https://stackoverflow.com/questions/49063499/inorder-traversal-of-tree-in-python-returning-a-list).  

Passing the data structure itself is the simplest solution. 

A better solution would be using some **static list**(i. e. a fixed list that would be declared only once). However, in Python we will need to do it by declaring it inside a class.  

Below code has two versions, which are almost identical, except that the first one is inorder, and the second one is preorder.  The other minor difference is that the first one uses only 1 function, and the second one wraps the function call in a function. 

Notice that the preorder recursive call actions for the root node take place before recursive calls for the left and the right.  Whereas in inorder the recursive call actions for the root node take place in between recursive calls for the left and the right.  

<div class="code-head"><span>code</span>inorder2.py</div>

```py
def inorder2(root,A): 
    if root==None:
        return

    inorder2(root.left, A)
    A.append(root.val)
    inorder2(root.right, A)
A = []
inorder2(Root,A)
print(A)


def preorderTraversal(root):
        res = []
        preorder(root, res)       
        return res
def preorder(node, A):
        if not node:
            return
        A.append(node.val)
        preorder(node.left, A)
        preorder(node.right, A)

```

# Work in progress


<div class="code-head"><span>code</span>findMode_dfs.py</div>

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def dfs(node, C, M, prev, res):
#     if not node: # base case
#         return
#     dfs(node.left, C, M, prev, res)
#     print('after left res', res)
#     print("evaluating prev and val", prev, node.val)
#     res = [node.val]
#     if node.val != prev:  # restart the counting
#         C = 1  
#     else:
#         C += 1
#     print("C, M", C, M)
#     print('res', res)
#     if C == M:
#         print("C = M", C, M)
#         res.append(node.val)
#     elif C > M:
#         print("C >M", C, M)
#         res = [node.val]
#         M = C
#     prev = node.val
#     dfs(node.right, C, M, prev, res)
#     print('after right res', res)
# C = 1
# M = 1
# prev = None
# res = []
# dfs(Root, C, M, prev, res)
# ```
```
# Reference

[LeetCode - 501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/)

https://home.gamer.com.tw/artwork.php?sn=4971259

[stackoverlow, inorder traversal of tree in python returning a list](https://stackoverflow.com/questions/49063499/inorder-traversal-of-tree-in-python-returning-a-list)