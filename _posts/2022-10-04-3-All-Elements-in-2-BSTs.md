---
layout: post
tag : BST, Merge Sort
category: education
title: "All Elements in 2 BSTs"
description: Leetcode 1305. All Elements in Two Binary Search Trees
author: Sarah Chen
image: images/posts/photos/farm/IMG-2256.jpg

---
![](../images/posts/photos/farm/IMG-2256.jpg)
- [Problem](#problem)
- [Brute force method O(n log(n))](#brute-force-method-on-logn)
- [O(n) solution](#on-solution)
- [Reference](#reference)

In this post, we deep dive into this problem [Leetcode 1305. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/).  

Please pardon me if you find the notes very basic. 

# Problem 

Problem is from [Leetcode 1305. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3],
Output: [0,1,1,2,3,4]
![allElements2BST](..\images\posts\allElements2BST.PNG)

Example 2:

Input: root1 = [1,null,8], root2 = [8,1],
Output: [1,1,8,8]
 
# Brute force method O(n log(n))
n 代稱兩棵樹的節點總數
把兩棵樹探訪過一次並將所有數字放到一個新的陣列後再排序，也就是 O(n log n) 的作法以外.

<div class="code-head"><span>code</span>allElements_2BST.py</div>

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
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
# define the trees
# root1 = [2,1,4], root2 = [1,0,3]
Root1 = TreeNode(val = 1)        
Root.right = TreeNode(val = 4)
Root.right.left = TreeNode(val = 2)
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
def preorder(root):
    """
    inorder traversal that returns the list of visited nodes
    """
    if root==None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


A = inorder(Root) # get array from inorder traversal
print(findMode(A)) # calling the function

def inorder2(root,A): 
    if root==None:
        return

    inorder2(root.left, A)
    A.append(root.val)
    inorder2(root.right, A)
A = []
inorder2(Root,A)
print(A)

```

# O(n) solution
解題思維：
以前有提及過 BST 的中序探訪（Inorder Traversal）是一個排序的數列，再加上我們知道怎麼在線性時間內合併兩個已排序之數列成為另一個已排序之數列. See [Merge Sort and Recursion](https://pythonrsas.github.io/1-Merge-Sort-and-Recursion/）。因此，我們只需要兩次中序探訪加上線性的合併，便可以在 O(n) 之間把兩棵樹的數字合併成一個按升序排列的數列。

# Reference

[Leetcode 1305. All Elements in Two Binary Search Trees](https://leetcode.com/problems/all-elements-in-two-binary-search-trees/)

https://home.gamer.com.tw/artwork.php?sn=5550149

[Merge Sort and Recursion](https://pythonrsas.github.io/1-Merge-Sort-and-Recursion/）