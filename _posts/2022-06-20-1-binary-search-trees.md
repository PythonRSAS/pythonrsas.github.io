---
layout: post
tag : abstract data structure, binary search tree, BST
category: "Python for SAS"
title: "binary search trees"
description: binary search trees abstract data structure, algorithm, and implementation in Python
author: Sarah Chen
image: images/posts/photos/IMG_0876.JPG

---

# Binary search tree

A Binary search tree is a kind of abstract data structure.  It is very intuitive from the mathematical perspective: *divide and conquer*.  For a sorted array/list, if we know that x is bigger than the median, then we don't need to spend time on the left half.  On the right half, we divide and conquer again.

Of course, it is made for doing something better than other data structures :)

<!-- # Compare with (abstract) array
* **Advantages**:
*Fast search*: Unlike arrays (abstract data structure), Binary search trees are resizable at run-time as Binary search tree nodes are stored at *arbitrary locations in memory*.  Fast Insertion and deletion operations because do not need to change the indices of other elements or storage location. 
  
* **Disadvantages**:
* *Slower search*: We cannot access elements in constant time as we do in arrays.  To find a node at position n, we have to start the search at the first (head) node and iterate through via <span class="coding">next</span>. 
* Binary search trees takes more space than the array.  -->


* **Properties**
- Search time is proportional to $$O(h)$$, where $$h$$ is height of tree.

- **height of tree** is the length of the longest path between the root and leaf. In a balanced tree, $$height = log(n)$$
![a balanced binary search tree](../images/posts/binary_search_tree_balanced.PNG)

In the extreme case, as shown below, $$height = n$$.  To correct unbalance, 
  
![an unbalanced binary search tree](../images/posts/binary_search_tree_unbalanced.PNG)

- **height of node** is the length of the longest path between the node and leaf.
  
* **Local rule**  
$$\text{height of node} = $$ $$max{$$\text{height of left child}, \text{height of right child}$$} + 1$$

Whenever we have local rules that depend on the children only, we get constant overhead: store node height for free. 

Our goal is to keep the tree's height small (we want short/bushy trees), quivalently, the heights of the children equal.  Cascading down, it means to keep heights of left and right children of every node to differ by at most $$+-1$$. 

<!-- # Maintein structure of subtree
Data structure augmentation. -->

# Keeping tree balanced
There are many ways to keep trees balanced, AVL is the original method discovered in the 1960s.  AVL trees use node heights (i.e. heights of left and right children).

An AVL tree (named after inventors Adelson-Velsky and Landis in 1962) is a *self-balancing* binary search tree (BST).  

In table Below we compare the abstract data structure of array and Binary search tree:

Compare | array | Binary search tree
---------|----------|---------
 size | fixed at birth | can change from insertion/deletion
 storage | static in continuous block of memory allocated during compile time | dynamic, nodes are located at run time
 ordering/sorting | fast direct access via index  | sequential, transverse from the head node via link (next)
 search | binary and linear search | linear search
 
# Binary search trees uses

They are useful when we need fast insertion and deletion, and when we do not know in advance the size of data, or do not need random access when searching for items.   

![Binary search tree uses](../images/posts/linked_list_uses.jpg)

# Binary search problem

Given a sorted array of integers, we want to find a number, which we call "target".  The code should return the index of target, and return -1 if not found. 

The devide and conquer method is implemented as follows:
1. We begin with the entire array of numbers, defined by the index for the smallest number and the index of the biggest number.         
2. We find the mid point.  Although it seems <span class="coding">small_idx + (big_idx - small_idx) // 2</span> and <span class="coding">(big_idx + small_idx) // 2</span> are equivalent, in computation, they have a subtle difference: the latter may cause overflow (even though it may never happen).
3. 
<div class="code-head"><span>code</span>binary search.py</div>

```py
def bSearch(A, target):
    N = len(A)
    small_idx = 0
    big_idx = N - 1
    while small_idx < big_idx:
        m_idx = small_idx + (big_idx - small_idx) // 2
        if target > A[m_idx]:
            small_idx = m_idx + 1
        elif target < A[m_idx]:
            big_idx = m_idx - 1
        else:
            return m_idx
    return - 1

lt = [1, 2, 5, 7, 8, 10, 20]
print(bSearch(lt, 7))

```

In this implementation, Binary search tree has the following common operations:
* Insert, insert at end, insert at beginning, insert between
* Delete (iterative find and then delete)               
* Search (iterative search)  
* Count number of elements
* Print list   

The <span class="coding">count</span> attribute is convenient because we don't need to go through the entire Binary search tree to get the number of elements.  With each insert, the count increments by 1 whereas delete decreases by 1 with <span class="coding">delete</span>. 

However, this attribute potentially has a problem: if <span class="coding">LinkedList</span> is instantiated without a head, and a head is added later such as in <span class="coding">LL.head = Node("Hello")</span>, its count stays 0.  Therefore, we define count as the number of elements without head. 

<div class="code-head"><span>code</span>linkedList.py</div>

```py
    
class LinkedList(object):
    # Defining the head of the Binary search tree
    def __init__(self, head = None):
        # if head = None:
        #     self.head = None
        #     self.count = 0
        # else: 
        #     self.head = head
        #     self.count = 1
        self.head = head
        self.count = 0
    # printing the data in the Binary search tree
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
            
    # inserting the node at the beginning
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode # update LinkList head
        self.count += 1 # update count
        
    # inserting the node in between the Binary search tree (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.count += 1 # update count
            
    # inserting at the end of Binary search tree
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode
        self.count += 1 # update count
        
    # deleting an item based on data
    def delete(self, data):
        temp = self.head
        # if data to be deleted is the head
        if (temp.next is not None): 
            if(temp.data == data):
                self.head = temp.next
                self.count -= 1
                temp = None
                return
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next
                
                # node not found
                if temp == None:
                    return
                
                prev.next = temp.next # if found, then drop the node by omiting it from the link
                self.count -= 1
                return
            
    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
    # iterative search return found item instead of True/False
    def search_list(self, node, data):
        while node and node.data != data:
            node = node.next
        return node
            
In [5]: LL = LinkedList()
   ...: LL.head = Node("Hello")
   ...: print("After defining head node")
   ...: LL.printLinkedList()
After defining head node
Hello
 
In [8]: node1 = Node(1)
   ...: LL.head.setNext(node1) 
   ...: print("After inserting 1 after head node")
   ...: LL.printLinkedList()
   ...:
After inserting 1 after head node
Hello 1

In [10]: node2 = Node(2)
    ...: node1.setNext(node2)     
    ...: LL.insertAtStart(4)    
    ...: LL.insertBetween(node1, 5)
    ...: LL.insertAtEnd(6)
    ...: print("After inserting at start, between and end")
    ...: LL.printLinkedList()
    ...:
After inserting at start, between and end
4 Hello 1 5 2 6

In [11]: LL.delete(3)
    ...: print("After deleting 3")
    ...: LL.printLinkedList()
    ...:
After deleting 3
4 Hello 1 5 2

In [12]: print(LL.search(LL.head, 1))
True

In [13]: print("Searching for 'hello'")
    ...: print(LL.search(LL.head, 'hello'))
    ...:
Searching for 'hello'
False

In [14]: print("Searching for 'Hello'")
    ...: found = LL.search_list(LL.head, 'Hello')
    ...: print(found.data)
    ...:
    ...:
Searching for 'Hello'
Hello

```

* In general, __array__ is considered a data structure for which size is fixed at the compile time and array memory is allocated either from __Data section__ (e.g. global array) or __Stack section__ (e.g. local array). 
* Similarly, Binary search tree is considered a data structure for which size is not fixed and memory is allocated from __Heap section__ (e.g. using malloc() etc.) as and when needed. In this sense, array is taken as a static data structure (residing in Data or Stack section) while Binary search tree is taken as a dynamic data structure (residing in Heap section).
* The array elements are allocated memory in sequence i.e. __contiguous memory__ while nodes of a Binary search tree are non-contiguous in memory. Though it sounds trivial yet this is the most important difference between array and Binary search tree. It should be noted that due to this contiguous versus non-contiguous memory, array and Binary search tree are different.

# Implementing doubly Binary search tree

<div class="code-head"><span>code</span>doublyLlinkedList.py</div>

```py
class Node(object):
    # Each node has its data and a pointer that points to next node in the Binary search tree
    def __init__(self, data, next = None, previous = None):
        self.data = data;
        self.next = next;
        self.previous = previous
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
    
    # for inserting at beginning of Binary search tree
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            
    # for inserting at end of Binary search tree
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp
        
    # deleting a node from Binary search tree
    def delete(self, data):
        temp = self.head
        if(temp.next != None):
            # if head node is to be deleted
            if(temp.data == data):
                temp.next.previous = None
                self.head = temp.next
                temp.next = None
                return
            else:
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    temp = temp.next
                if(temp.next):
                    # if element to be deleted is in between
                    temp.previous.next = temp.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None
                else:
                    # if element to be deleted is the last element
                    temp.previous.next = None
                    temp.previous = None
                return
        
        if (temp == None):
            return
        
    # for printing the contents of Binary search trees
    def printdll(self):
        temp = self.head
        while(temp != None):
            print(temp.data, end=' ')
            temp = temp.next
            
dll = DoublyLinkedList()
dll.insertAtStart(1)
dll.insertAtStart(2)
dll.insertAtEnd(3)
dll.insertAtStart(4)
dll.printdll()
dll.delete(2)
print()
dll.printdll()

```

# Binary search tree examples

## Find linkedlist length


<div class="code-head"><span>code</span>a1_findLlinkedListLength.py</div>

```py

import SinglyLinkedList

def checkLength(linkedList):
    count = 0
    temp = linkedList.head
    while(temp != None):
        count += 1
        temp = temp.next

    return count

myLinkedList = SinglyLinkedList.LinkedList()
for i in range(10):
    myLinkedList.insertAtStart(i)
myLinkedList.printLinkedList()
print()
print('Length:', checkLength(myLinkedList))

# OUTPUT:
# 9 8 7 6 5 4 3 2 1 0
# Length: 10
    
```

<div class="code-head"><span>code</span>a2_reverseLlinkedListLength.py</div>

```py
import SinglyLinkedList

def reverseLinkedList(myLinkedList):
    previous = None
    current = myLinkedList.head
    while(current != None):
        temp = current.next
        current.next = previous
        previous = current
        current = temp
    myLinkedList.head = previous


myLinkedList = SinglyLinkedList.LinkedList()
for i in range(10, 0, -1):
    myLinkedList.insertAtStart(i)

print('Original:', end = ' ')
myLinkedList.printLinkedList()
print()
print('Reversed:', end = ' ')
reverseLinkedList(myLinkedList)
myLinkedList.printLinkedList()

# OUTPUT:
# Original: 1 2 3 4 5 6 7 8 9 10
# Reversed: 10 9 8 7 6 5 4 3 2 1

```
