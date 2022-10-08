---
layout: post
tag : ADT, tree traversal
category: education
title: "Binary tree implementation"
description: Binary tree implementations and traversals
author: Sarah Chen
image: images/posts/photos/IMG_0871.JPG

---
  
- [Tree Traversal](#tree-traversal)
- [Tree height](#tree-height)
- [breadth First Traversal](#breadth-first-traversal)
- [Count number of leave nodes](#count-number-of-leave-nodes)
- [Binary trees and arrays](#binary-trees-and-arrays)
- [Root to Leaf Paths](#root-to-leaf-paths)
    - [Tree traversal:](#tree-traversal-1)
    - [Implementing tree traversals:](#implementing-tree-traversals)
- [Reference](#reference)

To implement binary tree, we only need to define the node itself, its value, and left and right attributes.  We can define methods after this. 
<div class="code-head"><span>code</span> treeNode.py</div>

```py
class Node(object):
    def __init__(self, val = None):
        self.left = None
        self.right = None
        self.val = val

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
''' for visualization only
                    1
                /       \
            2            3
        /     \       /     \
    4          5     6       7
'''
```
# Tree Traversal
![tree](../images/posts/tree123.PNG)
Inorder: 4, 2, 5, 1, 6, 3, 7
Postorder: 4, 5, 2, 6, 7, 3, 1
BFS:    1, 2, 3, 4, 5, 6, 7
Preorder: 1, 2, 4, 5, 3, 6, 7
DFS:    same as preorder

# Tree height
We define a recursive function <span class="coding">height</span> for the object.  The height of a tree is max(height(node.left), height(node.right)) + 1, with the base case of 0 when node is None. 
<div class="code-head"><span>code</span> treeHeight.py</div>

```py
def height(node):
    if node is None: # base case
        return 0
    else:
        leftHeight = height(node.left)
        # if node.left:
        #     print("node.left:", node.left.val)
        # print("leftHeight:", leftHeight)
        rightHeight = height(node.right)
        # print("rightHeight:", rightHeight)
        # if node.right:
        #     print("node.right:", node.right.val)
        return max(leftHeight, rightHeight) + 1

''' for visualization only
                    1
                /       \
            2            3
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
height(root)
# leftHeight: 0
# rightHeight: 0
# node.left: 2
# leftHeight: 1
# leftHeight: 0
# rightHeight: 0
# rightHeight: 1
# node.right: 3
# Out[46]: 2
```
# breadth First Traversal
<div class="code-head"><span>code</span> breadthFirstTraversal.py</div>

```py
def breadthFirstTraversal(root):
    if root == None:
        return 0
    else:
        h = height(root)
        for i in range(1, h + 1):
            printBFT(root, i)
def printBFT(root, level):
    if root is None:
        return
    else:
        if level == 1:
            print(root.val, end = ' ')
        elif level > 1:
            printBFT(root.left, level - 1)
            printBFT(root.right, level - 1)

breadthFirstTraversal(root)
# 1 2 3 4 5 6 7

```
# Count number of leave nodes

Leaf nodes are the nodes that do not have any children.

<div class="code-head"><span>code</span> P02_CountLeafNodes.py</div>

```py

from Tree import Node

def countLeafNodes(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)
root = Node(1)
root.setLeft(Node(2))
root.setRight(Node(3))
root.left.setLeft(Node(4))
print('Count of leaf nodes:',countLeafNodes(root))
```
# Binary trees and arrays

<div class="code-head"><span>code</span> P03_TreeFromInorderAndPreorder.py</div>

```py
# Python program to construct tree using inorder and
# preorder traversals

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""Recursive function to construct binary of size len from
   Inorder traversal in[] and Preorder traversal pre[].  Initial values
   of start and end should be 0 and len -1.  The function doesn't
   do any error checking for cases where inorder and preorder
   do not form a tree """
def buildTree(inOrder, preOrder, start, end):
    if (start > end):
        return None

    # Pick current node from Preorder traversal using
    # preIndex and increment preIndex
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return
    if start == end :
        return tNode

    # Else find the index of this node in Inorder traversal
    rootIndex = search(inOrder, start, end, tNode.data)

    # Using index in Inorder Traversal, construct left
    # and right subtrees
    tNode.left = buildTree(inOrder, preOrder, start, rootIndex-1)
    tNode.right = buildTree(inOrder, preOrder, rootIndex+1, end)


    return tNode

# function to search for the index
def search(arr, start, end, value):
    for i in range(start, end+1):
        if arr[i] == value:
            return i

# function to print the contents of the tree in inorder fashion
def inorder(node):
    if node is None:
        return

    # first recur on left child
    inorder(node.left)
    #then print the data of node
    print (node.data, end = ' ')
    # now recur on right child
    inorder(node.right)

# Driver program to test above function
inOrder = ['D', 'B' ,'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

# Static variable preIndex
buildTree.preIndex = 0
root = buildTree(inOrder, preOrder, 0, len(inOrder)-1)

# Let us test the build tree by priting Inorder traversal
print ("Inorder traversal of the constructed tree is")
inorder(root)

```
# Root to Leaf Paths

<div class="code-head"><span>code</span> P04_RootToLeafPaths.py</div>

```py

# Use a path array path[] to store current root to leaf path. Traverse from root to all leaves in top-down fashion.
# While traversing, store data of all nodes in current path in array path[]. When we reach a leaf node, print the path
# array.

class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data

def printPath(node, path = []):
    if node is None:
        return
    path.append(node.data)

    if (node.left is None) and (node.right is None):
        print(' '.join([str(i) for i in path if i != 0]))
    else:
        printPath(node.left, path)
        printPath(node.right, path[0:1])

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)

    printPath(root)

```







<div class="code-head"><span>code</span> P05_InorderPredecessorAndSuccessor.py</div>

```py

# Input: root node, key
#
# Output: predecessor node, successor node
# 1. If root is NULL
#       then return
# 2. if key is found then
#     a. If its left subtree is not null
#         Then predecessor will be the right most
#         child of left subtree or left child itself.
#     b. If its right subtree is not null
#         The successor will be the left most child
#         of right subtree or right child itself.
#     return
# 3. If key is smaller then root node
#         set the successor as root
#         search recursively into left subtree
#     else
#         set the predecessor as root
#         search recursively into right subtree

# Python program to find predecessor and successor in a BST

# A BST node
class Node(object):
    # Constructor to create a new node
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None

    # for finding the predecessor and successor of the node
    def findPredecessorAndSuccessor(self, data):
        global predecessor, successor
        predecessor = None
        successor = None

        if self is None:
            return

        # if the data is in the root itself
        if self.data == data:
            # the maximum value in the left subtree is the predecessor
            if self.left is not None:
                temp = self.left
                if temp.right is not None:
                    while(temp.right):
                        temp = temp.right
                predecessor = temp

            # the minimum of the right subtree is the successor
            if self.right is not None:
                temp = self.right
                while(temp.left):
                    temp = temp.left
                successor = temp

            return

        #if key is smaller than root, go to left subtree
        if data < self.data:
            print('Left')
            self.left.findPredecessorAndSuccessor(data)
        else:
            print('Right')
            self.right.findPredecessorAndSuccessor(data)

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

root = Node(50)
root.insert(30)
root.insert(20)
root.insert(40)
root.insert(70)
root.insert(60)
root.insert(80)

 # following BST is created
 #               50
 #            /     \
 #           30      70
 #          /  \    /  \
 #        20   40  60   80

root.findPredecessorAndSuccessor(70)
if  (predecessor is not None) and (successor is not None):
    print('Predecessor:', predecessor.data, 'Successor:', successor.data)
else:
    print('Predecessor:', predecessor, 'Successor:', successor)

```

### Tree traversal:

Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. The following are the generally used ways for traversing trees.

* Inorder  中序   (left, data, right)
* Preorder  前序 (data, left, right)
* Postorder 後序 (left, right, data)


中序運算式」「後序運算式」

「中序運算式」，即是我們一般會看見的運算式形式。例如：２＋７ * ８，每個運算子都會被運算元所包圍（除非是一元運算子，或是括號）。

「後序運算式」，則是電腦方便運算的運算式形式。例如，上面的２＋７ * ８的後序運算式為２７８ * ＋。而在生成後序運算式時，各個運算子的運算順序已經被考慮進去（包含括號），因此在裡面不會再看到括號的存在。

可是為何有中序、後序之差？這是因為，每個運算式都可化為一個樹，以上面的２＋７ * ８為例，可化為：

![computationTree](../images/posts/computationTree.png)
如上圖，是一個二元樹（每個節點最多兩個子樹）。

我們常見的「中序運算式」便是這棵樹經由「中序探訪」的「路徑」。先走左子樹，接下來是自己，最後再走右子樹。

相似地，「後序運算式」為這棵樹的「後序探訪」。先走左子樹、再右子樹，最後才走根節點。



而中序轉後序不需要真的建一棵二元樹，再用後序探訪找路徑。只需要堆疊，在輸入的時候即可轉變成後序運算式。

以５＋７－８ /（６＋２）* ２為例：
先讀入５，一讀入數字即可把它放進後序運算式的結果之中。現結果為５，堆疊為空。

讀入＋，放進堆疊裡。現結果為５，堆疊裡有＋。

讀入７，結果為５７，堆疊裡有＋。

讀入－，判斷堆疊的頂端元素的優先順序，是否大於等於現在讀入的運算子之優先度。如果是，就一直把堆疊的頂端元素拿出，直到堆疊為空或是不符合為止。最後再放入現有的運算子。現結果為５７＋，堆疊裡有－。

讀入８，結果為５７＋８，堆疊裡有－。

讀入 / ，結果為５７＋８，堆疊裡有－ / 。

讀入（，左括號很特別，要與右括號配對。結果為５７＋８，堆疊裡有－ / （。

讀入６，結果為５７＋８６，堆疊裡有－ / （。

讀入＋，結果為５７＋８６，堆疊裡有－ / （＋。

讀入２，結果為５７＋８６２，堆疊裡有－ / （＋。

讀入），把堆疊的頂端元素拿出，直到遇見（。現結果為５７＋８６２＋，堆疊裡有－ / 。

讀入 * ，結果為５７＋８６２＋ / ，堆疊裡有－ * 。

讀入２，結果為５７＋８６２＋ / ２，堆疊裡有－ * 。

最後把堆疊清空，最終結果即為５７＋８６２＋ / ２ * －，即是題目所求。


### Implementing tree traversals:


<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py
# in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData(), end = ' ')
        inorder(Tree.getRight())
    return

# in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
def preorder(Tree):
    if Tree:
        print(Tree.getData(), end = ' ')
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return 

# in this we first traverse to the leftmost node and then to the rightmost node and then print the data
def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData(), end = ' ')
    return

print('Inorder  Traversal:')
inorder(root)
print('\nPreorder Traversal:')
preorder(root)
print('\nPostorder Traversal:')
postorder(root)      

```

# Reference

[Geeks for Geeks 3-types-of-binary-tree](http://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/)
