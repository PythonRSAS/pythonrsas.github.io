---
layout: post
tag : Array, BST, DFS
category: education
title: "BST to and from Preorder Traversal"
description: Preorder traversal of BST and Construct BST from Preorder Traversal LeetCode - 144 and 1008. 
author: Sarah Chen
image: images/posts/photos/farm/IMG-1931.jpg

---
![](../images/posts/photos/farm/IMG-1931.jpg)
- [Problem 1: 中序以及後序探訪转成前序探訪](#problem-1-中序以及後序探訪转成前序探訪)
- [Problem 2. Postorder from inorder and preorder](#problem-2-postorder-from-inorder-and-preorder)
  - [Brute force: Back to Tree Then Convert to Postorder](#brute-force-back-to-tree-then-convert-to-postorder)
- [Problem 3: Binary Tree Preorder Traversal](#problem-3-binary-tree-preorder-traversal)
  - [Problem 3  LeetCode - 1008. Construct BST from Preorder Traversal](#problem-3--leetcode---1008-construct-bst-from-preorder-traversal)
- [Problem 2: find Mode in Binary Search Tree](#problem-2-find-mode-in-binary-search-tree)
  - [Solution: reduce tree problem to array problem](#solution-reduce-tree-problem-to-array-problem)
  - [Other ways to get the list from tree traversal](#other-ways-to-get-the-list-from-tree-traversal)
- [Work in progress](#work-in-progress)
- [Reference](#reference)

In this post, we explore problems on binary search tree preorder traversal and the reverse: construct BST from preorder traversal. 
先複習一下二元樹的前序、中序、後序探訪，它們的遞迴式依序是：
**前序**：根節點 → 左子樹 → 右子樹
**中序**： 左子樹 → 根節點 → 右子樹
**後序**： 左子樹 → 右子樹 → 根節點

# Problem 1: 中序以及後序探訪转成前序探訪
題目大意：
給定一二元樹的中序以及後序探訪的排列，求此二元樹前序探訪的排列。

此樹的每個節點用相異的大寫字母標記，保證不超過八個節點。

範例輸入：
**中序**：BADC
**後序**: BDCA
範例輸出：
ABCD

解題思維：

我們可以看出**後序排列的最後一個節點即是整棵樹的根節點**。以範例測資為例，中序是 BADC 、後序是 BDCA ，因此：
A 是整棵樹的根節點、 B 是左子樹、 DC 是右子樹。
遞迴求左子樹得左子樹的根節點為 B ；
遞迴求右子樹得右子樹的根節點為 C 、 右子樹的左子樹為 D 。
遞迴求右子樹的左子樹得其根節點為 D 。

因此，前序探訪為 ABCD 。

# Problem 2. Postorder from inorder and preorder
Given Inorder and Preorder traversals of a binary tree, print Postorder traversal.

Example:

Input:
Inorder traversal in[] = {4, 2, 5, 1, 3, 6}
Preorder traversal pre[] = {1, 2, 4, 5, 3, 6}

Output:
Postorder traversal is {4, 5, 2, 6, 3, 1}
## Brute force: Back to Tree Then Convert to Postorder
A naive method is to first construct the tree, then use a simple recursive method to print postorder traversal of the constructed tree.

```python
# Python3 program to print postorder
# traversal from preorder and inorder traversals
def search(A, x, n):
    """
    utility function to search x in
    arrary of size n
    """
	for i in range(n):
		if (A[i] == x):
			return i
	return -1

# Prints postorder traversal from
# given inorder and preorder traversals
def f(IN, PRE, n):
	root = search(IN, PRE[0], n)
	if (root != 0):
		f(IN, PRE[1:n], root)
	if (root != n - 1):
		f(IN[root + 1 : n],
					PRE[root + 1 : n],
					n - root - 1)
	# Print root
	print(PRE[0], end = " ")

In = [ 4, 2, 5, 1, 3, 6 ]
pre = [ 1, 2, 4, 5, 3, 6 ]
n = len(In)
print("Postorder traversal ")
f(In, pre, n)
# Postorder traversal
# 4 5 2 6 3 1
In = [ 4, 2, 5, 1, 3, 12 ]
pre = [ 1, 2, 4, 5, 3, 12 ]
n = len(In)
print("Postorder traversal ")
postOrder(In, pre, n)
```


# Problem 3: Binary Tree Preorder Traversal
[LeetCode - 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

題目大意：
給定一個二元樹的根節點 root ，回傳其節點值之前序探訪（Preorder Traversal）。

限制：
樹中的節點數位於範圍 [0, 100] 中。
-100 ≦ Node.val ≦ 100

進階： 遞迴解顯而易見，那你可以改用迭代的方式解出來嗎？

範例輸入：
![bstPreOrder](..\images\posts\bstPreOrder.JPEG)
輸入： root = [1,null,2,3]
輸出： [1,2,3]

範例 2：
輸入： root = []
輸出： []

解題思維：
**用一個整數變數 C (fast) 當作計數器**（一開始設為 1）、**一個整數變數 M (slow) 當作最大值**，**以及一個字元變數 T 儲存最大值發生時的字元（即所求）**。

跳過字串第一個字元從第二個字元開始，對於第 i 個字元，看第 i - 1 個字元是否與它相同。

如果是，則計數器 C 加 1 ；反之，C 重设为 1.  然后判斷 C 的值跟 M 的大小。如果 M < C ，則 M 更新為 C 之值，然後將 T 設為第 i 個字元。

字串扫完后，字元 T 與整數 M 之值即為所求。

## Problem 3  [LeetCode - 1008. Construct BST from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)

Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
Example 1:

![preorderContructBST](..\images\posts\preorderContructBST.PNG)
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
Example 2:

Input: preorder = [1,3]
Output: [1,null,3]

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 1000
All the values of preorder are unique.

<div class="code-head"><span>code</span>bstFromPreorder.py</div>

```py
def bstFromPreorder(A):
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

[Geeks for Geeks: postorder from given inorder and preorder traversals](https://www.geeksforgeeks.org/print postorder-from-given-inorder-and-preorder-traversals/)

[LeetCode - 144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

[LeetCode - 1008. Construct BST from Preorder Traversal](https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/)


[stackoverlow, inorder traversal of tree in python returning a list](https://stackoverflow.com/questions/49063499/inorder-traversal-of-tree-in-python-returning-a-list)