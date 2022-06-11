---
layout: post
tag : computer data structure, python
category: "Python for SAS"
title: "Basic data structures"
description: essentials in data structures including stack, queue, linked list. 
author: Sarah Chen
image: images/posts/photos/IMG_0878.JPG

---
In working in financial services, whether credit risk modeing, or insurnace pricing, I did not once need to use knowledge on data structures such as stack, queue.  Surely, I need to know how SAS, Python, and R processes data, in particular when working with large filres.  But the goal was to get insight, build models, and predict/forecast. Working in SAS, all you need to know are the <span class="coding">DATA</span> steps, procedures such as <span class="coding">PROC MEAN</span>, <span class="coding">PROC UNIVARIATE</span> and so on for basic data analysis, and more specific procedures for deeper dives and modeling.  Working in Python, the story was quite similar. You master pandas, maybe a little bit of matplotlib, seaborn, numpy and scipy, statsmodels, and sklearn, you've covered all the basics. 

However, in the machine learning era, the goals and capacities of analytics have far expanded beyond statistics and modeling. Modelers may want to or need to implement the models themselves.  In order to implement models, it is necessary to understand computer science fundamentals on data structures. 

Data structures are defined and built according to varied needs of different data types and algorithms:
Stack is the backbone for all recursive processes in our computers because of its "Last In First Out" rule.  
Queue, the opposite of a stack, is used for queue-jobs because of its "First In First Out" rule. 
Linked list
Doubly linked list
dictionary and hash tables
trees and tries (for word-procssing algo)
heaps and grapsh

# The Big O metric
In order to measure run time efficiency, the big $O$ metric is used. 

In analytic number theory class by my late professor Patrick Gallagher,the big O metric was associated with whether two different representations are aymptotically close. 
![Professor Patrick Gallagher](./images/posts/Gallagher.png)

If $S$ is a set and $f$ and $g$ are functions $S$ →$R$, we say that$f = O(g)$ if there exists an$k > 0$ such that$|f(s)| ≤ Mg(s)$ for all s$∈$S$.  

Therefore,$O(1)$ means some constant (time). Similarly,$O(2)$ or $O(100)$ also mean constant, as long as the number is fixed. 

$O(n)$ means linear as in$k*n$ for some $k>0$.

In computer science, the big $O$ is used as a time efficiency metric for data structure: how much time it takes to do each of the following:
1. Access (to get)
2. Search (to find)
3. Insert (to add)
4. Delete (to remove)

In computer science context, constant time (e.g. O(1)) means that the amound of time it takes to do something (something could be one of the 4 tasks above) is independent of the size of the data.  The size of data$n$ is absent from the$O()$. Constant time is the most efficient but also difficult to achieve. 

Time complexity or run time | $O$ as a function of data size$n$ |Example | Explain
---------|----------|---------|---------
constant |$O(1)$ |indexed data |data size is irrelevant
log n |$O(log(n))$ | binary search |data size is relevant, but unit "cost" decreases as data size increases
linear |$O(n)$ | accessing |time is a linear function of data size
linear*log |$O(nlog(n))$ | | As we can see, its slope ($log(n)+1$) is a positive function of n
power |$O(n**2)$ | inserting/deleting| slope ($2n$) is a positive function of n
exponential |$O(2**n)$ | | the worst in efficiency

In general, those with less flexibility are faster for certain basic tasks. For example, in Python tuple are immutable (cannot add or change) is faster than list (Note that although tuple elements cannot be changed, but a list within a tuple can be changed, for example ([1,2,3],)). 

Some data structures are very inefficient in terms of time, but they are very useful for what they are made to do. 

![time complexity](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Comparison_computational_complexity.svg/330px-Comparison_computational_complexity.svg.png)

# Array
Arrays are lists of similar data. An array of an array is a 2-dimensional array, i.e. matrix. 
- name
- type: the type of data is stored, and all have to be the *same* within one array
- size: it is fixed once it is defined, and **cannot be changed** once created

There are 2 ways to create an array:
- define the entire array along with its elements altogether
- define its size only and populate it later (not possible in base Python although we can do it using numpy)

1. Access: random access use *index* as all elements are indexed, run time is$O(1)$; 
2. Search:$O(n)$, may need to go over each element to find an item from an unsorted array
3. Insert:$O(n)$, because we need to shift the elements, which are after the index where we want to insert the item, to the *'right'* for one space  
4. Delete:$O(n)$, because we need to shift the elements, which are after the index where we want to insert the item, to the *"left"* for one space  

pros | cons
---------|----------
good for storing similar data | data must be the same; size cannot be changed once created 
efficient accessing | insert/delete are not as efficent 

Array elements are stored in contiguous (continuous) memory locations. Its efficiency is in scaling its attributes to all its elements. 

## Array in python
Numpy arrays depends on the numpy library.  Python does not have a native support for arrays, but has a more generic data structure called *list*. 

The following code are from Github repository "Data Structure using Python". 

<div class="code-head"><span>code</span>Array.py</div>

```py
class Array(object):
    ''' sizeOfArray: denotes the total size of the array to be initialized
       arrayType: denotes the data type of the array(as all the elements of the array have same data type)
       arrayItems: values at each position of array
    '''
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    # magic methods to enable indexing
    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if (self.arrayItems[i] == keyToSearch):      # brute-forcing
                return i                                 # index at which element/ key was found

        return -1                                        # if key not found, return -1

    # function for inserting an element
    def insert(self, keyToInsert, position):
        if(self.sizeOfArray > position):
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)

    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.sizeOfArray > position):
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
        else:
            print('Array size is:', self.sizeOfArray)

if __name__ == '__main__':
    a = Array(10, int)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4,7)
    print(len(a))

```
We can use the array class we defined.  For example,

```python
# access
a = Array(100,int)
idx = a.search(0)
print("found at", idx)

a.insert(2,2)
print(a)

```

### Reversing an array

<div class="code-head"><span>code</span>a1_reverseArry.py</div>

```py
import Arrays

def  reversingAnArray(start, end, myArray):
    while(start < end):
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    myArray = Arrays.Array(10)
    myArray.insert(2, 2)
    myArray.insert(1, 3)
    myArray.insert(3, 1)
    print('Array before Reversing:',myArray)
    reversingAnArray(0, len(myArray), myArray)
    print('Array after Reversing:',myArray)

```

### Rotating an array

<div class="code-head"><span>code</span>a2_arrayRotation.py</div>

```py

from Arrays import Array

def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray

def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:',myArray)
    print('After Rotation:',rotation(3, myArray))

    # OUTPUT:
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
```

### Get missing number

<div class="code-head"><span>code</span>a3_findMissing.py</div>

```py

from Arrays import Array

def findMissing(myArray, n):
    n = n - 1
    totalSum = (n * (n + 1)) // 2
    for i in range(0, n):
        totalSum -= myArray[i]

    return totalSum

if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    myArray.delete(4, 4)
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray, len(myArray)))

    # OUTPUT:
    # Original Array: 0 1 2 3 5 6 7 8 9 0
    # Missing Element: 4
```

### Get missing number

<div class="code-head"><span>code</span>a4_odd_number_occurance.py</div>

```py
# Given an array of positive integers. All numbers occur even number of times except one
# number which occurs odd number of times. Find the number in O(n) time & constant space.

# XOR of all elements gives us odd occurring element. Please note that XOR of two elements
# is 0 if both elements are same and XOR of a number x with 0 is x.

# NOTE: This will only work when there is only one number with odd number of occurences.

def printOddOccurences(array):
    odd = 0

    for element in array:
        # XOR with the odd number
        odd = odd ^ element

    return odd

if __name__ == '__main__':
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(printOddOccurences(myArray))      # 4
```
### Check for pair sum

<div class="code-head"><span>code</span>a5_CheckForPairSum.py</div>

```py
# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose sum is exactly x.

def checkSum(array, sum):
    # sort the array in ascending order
    # new changes : made use of Python's inbuilt Merge Sort method
    # Reason for such change : Worst case Time complexity of Quick Sort is O(n^2) whereas Worst Case Complexity of Merge Sort is O(nlog(n))
    array = sorted(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex] ==  sum):
            return array[leftIndex], array[rightIndex]
        elif(array[leftIndex] + array[rightIndex] < sum):
            leftIndex += 1
        else:
            rightIndex += 1

    return False, False

##def quickSort(array):
##    if len(array) <= 1:
##        return array
##    pivot = array[len(array) // 2]
##    left = [x for x in array if x < pivot]
##    middle = [x for x in array if x == pivot]
##    right = [x for x in array if x > pivot]
##    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    number1, number2 = checkSum(myArray, sum)
    if(number1 and number2):
        print('Array has elements:', number1, 'and', number2, 'with sum:', sum)
    else:
        print('Array doesn\'t have elements with the sum:', sum)

```

## ArrayList

ArrayList is a derivation of array.  It is a *growing* array, where the size can be changed.  It has more functionality than an array, including the following 6 common methods:
- add
- remove
- get
- set
- clear
- toArray

**In Python, arrays and arrayLists are grouped together into a single data structured called "Lists"**. 

# Stack
Like what it sounds like, a stack is a stack of something.  The last one added is the first one out. In life, undo, redo, go back, and etc. are all examples of "stacking".

In computer, stack data structure is used for keeping track of active functions or subroutines. 

Stack is the backbone for all recursive processes in our computers.  Recursive processes are those functions that call themselves within themselves. 

When the function calls itself, the call is aded to a stck of processes, keeping track of active subroutines in code and more. 

<div class="code-head"><span>code</span>stack.py</div>

```py

```


# Queue

Queues are the opposite of stacks.  Queues are "FIFO". 



<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```






# Linked List


A linked List is a data structure used for storing collections of data. A linked list has the following properties.
* Successive elements a re connected by pointers
* The last element points to <span class="coding">\__None__</span> (NULL)
* Can grow or shrink in size during execution of a program
* Can be made just as long as required (until systems memory exhausts)
* Does not waste memory space (but takes some extra memory for pointers)

* Linked lists are linear data structures that hold data in individual objects called nodes. These nodes hold both the data and a reference to the next node in the list.
* Each node contains a value, and a reference (also known as a pointer) to the next node. The last node, points to a null node. This means the list is at its end.
* Linked lists offer some important advantages over other linear data structures. Unlike arrays, they are a dynamic data structure, resizable at run-time. Also, the insertion and deletion operations are efficient and easily implemented.
* However, linked lists do have some drawbacks. Unlike arrays, linked lists aren't fast at finding the __n__th item.To find a node at position __n__, you have to start the search at the first node in the linked list, following the path of references  times. Also, because linked lists are inherently sequential in the forward direction, operations like backwards traversal--visiting every node starting from the end and ending in the front--is especially cumbersome. (__Only sequential search possible__)
* Additionally, linked lists use more storage than the array due to their property of referencing the next node in the linked list.
* Finally, unlike an array whose values are all stored in contiguous memory, a linked list's nodes are at arbitrary, possibly far apart locations in memory.


## Common Operations:
* Insert           
* Insert at end
* Insert at beginning
* Insert between
* Delete                
* Search                
* Indexing
  
# Linked List and Node can be accomodated in separate classes for convenience

<div class="code-head"><span>code</span>linkedList.py</div>

```py
class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;
        
    # function to set data
    def setData(self, data):
        self.data = data;
        
    # function to get data of a particular node
    def getData(self):
        return self.data
    
    # function to set next node
    def setNext(self, next):
        self.next = next
        
    # function to get the next node
    def getNext(self):
        return self.next
    
class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None
        
    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
            
    # inserting the node at the beginning
    def insertAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode
            
    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode
        
    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
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
                
                prev.next = temp.next
                return
            
    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)
            
if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                   # create the head node
    node2 = Node(2)
    List.head.setNext(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.setNext(node3)                # node2's next --> node3
    List.insertAtStart(4)                   # node4's next --> head-node --> node2 --> node3
    List.insertBetween(node2, 5)     # node2's next --> node5
    List.insertAtEnd(6)
    List.printLinkedList()
    print()
    List.delete(3)
    List.printLinkedList()
    print()
    print(List.search(List.head, 1))

```

* In general, __array__ is considered a data structure for which size is fixed at the compile time and array memory is allocated either from __Data section__ (e.g. global array) or __Stack section__ (e.g. local array). 
* Similarly, linked list is considered a data structure for which size is not fixed and memory is allocated from __Heap section__ (e.g. using malloc() etc.) as and when needed. In this sense, array is taken as a static data structure (residing in Data or Stack section) while linked list is taken as a dynamic data structure (residing in Heap section).
* The array elements are allocated memory in sequence i.e. __contiguous memory__ while nodes of a linked list are non-contiguous in memory. Though it sounds trivial yet this is the most important difference between array and linked list. It should be noted that due to this contiguous versus non-contiguous memory, array and linked list are different.

<div class="code-head"><span>code</span>doublyLlinkedList.py</div>

```py
class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None, previous = None):
        self.data = data;
        self.next = next;
        self.previous = previous
        
class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
    
    # for inserting at beginning of linked list
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
            
    # for inserting at end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = newNode
        newNode.previous = temp
        
    # deleting a node from linked list
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
        
    # for printing the contents of linked lists
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

## Linked list examples

### Find linkedlist length


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

if __name__ == '__main__':
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


if __name__ == '__main__':
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

<div class="code-head"><span>code</span>a2_reverseLlinkedListLength.py</div>

```py

# Linked List and Node can be accomodated in separate classes for convenience

class Node(object):
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data;
        self.next = next;

    # function to set data
    def setData(self, data):
        self.data = data;

    # function to get data of a particular node
    def getData(self):
        return self.data

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next

class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    # inserting the node at the beginning
    def insertAtStart(self, data):
        if self.head == None:
            newNode = Node(data)
            self.head = newNode
        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode

    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode

    # inserting at the end of linked list
    def insertAtEnd(self, data):
        newNode = Node(data)
        temp = self.head
        while(temp.next != None):         # get last node
            temp = temp.next
        temp.next = newNode

    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
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

                prev.next = temp.next
                return

    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)

if __name__ == '__main__':
    List = LinkedList()
    List.head = Node(1)                # create the head node
    node2 = Node(2)
    List.head.setNext(node2)           # head node's next --> node2
    node3 = Node(3)
    node2.setNext(node3)               # node2's next --> node3
    List.insertAtStart(4)              # node4's next --> head-node --> node2 --> node3
    List.insertBetween(node2, 5)       # node2's next --> node5
    List.insertAtEnd(6)
    List.printLinkedList()
    print()
    List.delete(3)
    List.printLinkedList()
    print()
    print(List.search(List.head, 1))

```

# Tree

* A tree is a data structure similar to a linked List but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. Tree is an example of non-linear data structures. A tree structure is a way of representing the **hierarchical** nature of a structure in a graphical form.
* The **root** of the tree is the node with no parents. There can be at most one root node in a tree.
* The _edge_ refers to the link from parent to child.
* A node with NO children is called _leaf_ node.
* Children of same parent are called _siblings_.
*  Manipulate hierarchical data.
* Make information easy to search (see tree traversal).
* Manipulate sorted lists of data.
* As a workflow for compositing digital images for visual effects.
* Router algorithms
* Form of a multi-stage decision-making (see business chess).

# Applications of trees
*  Manipulate hierarchical data.
* Make information easy to search (see tree traversal).
* Manipulate sorted lists of data.
* As a workflow for compositing digital images for visual effects.
* Router algorithms
* Form of a multi-stage decision-making (see business chess).

# Binary Tree
* A tree is called _binary tree_ if each node of the tree has zero, one or two children.
* Empty tree is also a valid binary tree.

Types of binary trees:
1. **Full binary tree**:
A Binary Tree is full if every node has 0 or 2 children. Following are examples of full binary tree.
2. **Complete binary tree**:
A Binary Tree is complete Binary Tree if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
3. **Perfect Binary Tree**:
A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.
4. **Balanced Binary Tree**:
A binary tree is balanced if height of the tree is O(Log n) where n is number of nodes. For Example, AVL tree maintain O(Log n) height by making sure that the difference between heights of left and right subtrees is 1. Red-Black trees maintain O(Log n) height by making sure that the number of Black nodes on every root to leaf paths are same and there are no adjacent red nodes. Balanced Binary Search trees are performance wise good as they provide O(log n) time for search, insert and delete.
5. **A degenerate (or pathological) tree**:
A Tree where every internal node has one child. Such trees are performance-wise same as linked list.

For visualizations:
http://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/

For properties:
http://www.geeksforgeeks.org/binary-tree-set-2-properties/

### Binary tree implementation:


<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py
class Node(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.data = data
    
    # for setting left node
    def setLeft(self, node):
        self.left = node
    
    # for setting right node
    def setRight(self, node):
        self.right = node
        
    # for getting the left node
    def getLeft(self):
        return self.left
    
    # for getting right node
    def getRight(self):
        return self.right
    
    # for setting data of a node
    def setData(self, data):
        self.data = data
        
    # for getting data of a node
    def getData(self):
        return self.data
    
root = Node(1)
root.setLeft(Node(2))
root.setRight(Node(3))
root.left.setLeft(Node(4))
''' This will a create like this 
                    1
                /       \
            2            3
        /
    4
'''
```
<div class="code-head"><span>code</span> BinarySearchTree.py</div>

```py
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()

```








<div class="code-head"><span>code</span> ListViewUsingTree.py</div>

```py
# sample object
class Sample:
    def __init__(self, data_description, node_id, parent_id=""):
        self.data_description = data_description
        self.node_id = node_id
        self.parent_id = parent_id


# Node structure (Basically N-ary Tree)
class Node:
    def __init__(self, data):
        self.data = Sample(data['data_description'], data['node_id'], data['parent_id'])
        self.children = []


class Tree:
    def __init__(self, data):
        self.Root = data

    def insert_child(self, root, new_node):

        #  if the list item's parent_id is equal to the current node it will append the node in their child array.

        if root.data.node_id == new_node.data.parent_id:
            root.children.append(new_node)

        # else it will check all the node and their children list whether the parent_id is same.

        elif len(root.children) > 0:
            for each_child in root.children:
                # it will create a recursive call for all nodes to treate as a root and search for all its child_list nodes
                self.insert_child(each_child, new_node)

    def print_tree(self, root, point):
        print(point, root.data.node_id, root.data.parent_id, root.data.data_description)
        if len(root.children) > 0:
            point += "_"
            for each_child in root.children:
                self.print_tree(each_child, point)


data = {'data_description': 'Sample_root_1', 'node_id': '1', 'parent_id': ''}
data1 = {'data_description': 'Sample_root_2', 'node_id': '2', 'parent_id': '1'}
data2 = {'data_description': 'Sample_root_3', 'node_id': '3', 'parent_id': '1'}
data3 = {'data_description': 'Sample_root_4', 'node_id': '4', 'parent_id': '2'}
data4 = {'data_description': 'Sample_root_5', 'node_id': '5', 'parent_id': '3'}
data5 = {'data_description': 'Sample_root_6', 'node_id': '6', 'parent_id': '4'}
data6 = {'data_description': 'Sample_root_7', 'node_id': '7', 'parent_id': '4'}

a = Tree(Node(data))
a.insert_child(a.Root, Node(data1))
a.insert_child(a.Root, Node(data2))
a.insert_child(a.Root, Node(data3))
a.insert_child(a.Root, Node(data4))
a.insert_child(a.Root, Node(data5))
a.insert_child(a.Root, Node(data6))
a.print_tree(a.Root, "|_")

# |_ 1  Sample_root_1
# |__ 2 1 Sample_root_2
# |___ 4 2 Sample_root_4
# |____ 6 4 Sample_root_6
# |____ 7 4 Sample_root_7
# |__ 3 1 Sample_root_3
# |___ 5 3 Sample_root_5


```


<div class="code-head"><span>code</span> P01_BreadthFirstTraversal.py</div>

```py

class Node(object):
    def __init__(self, data = None):
        self.leftChild = None
        self.rightChild = None
        self.data = data

def height(node):
    if node is None:
        return 0
    else:
        leftHeight = height(node.leftChild)
        rightHeight = height(node.rightChild)

        if leftHeight > rightHeight:
            return leftHeight + 1
        else:
            return rightHeight + 1

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
            print(root.data, end = ' ')
        elif level > 1:
            printBFT(root.leftChild, level - 1)
            printBFT(root.rightChild, level - 1)

if __name__ == '__main__':
    root = Node(1)
    root.leftChild = Node(2)
    root.rightChild = Node(3)
    root.leftChild.leftChild = Node(4)

    breadthFirstTraversal(root)


```





<div class="code-head"><span>code</span> P02_CountLeafNodes.py</div>

```py

# leaf node is the one which does not have any children

from Tree import Node

def countLeafNodes(root):
    if root is None:
        return 0
    if(root.left is None and root.right is None):
        return 1
    else:
        return countLeafNodes(root.left) + countLeafNodes(root.right)

if __name__ == '__main__':
    root = Node(1)
    root.setLeft(Node(2))
    root.setRight(Node(3))
    root.left.setLeft(Node(4))

    print('Count of leaf nodes:',countLeafNodes(root))

```







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

if __name__ == '__main__':
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

Unlike linear data structures (Array, Linked List, Queues, Stacks, etc) which have only one logical way to traverse them, trees can be traversed in different ways. Following are the generally used ways for traversing trees.

* Inorder     (left, data, right)
* Preorder   (data, left, right)
* Postorder (left, right, data)

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













# Heap




<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```











<div class="code-head"><span>code</span> Binary tree implementation.py</div>

```py


```





# Data structures in SAS
In SAS, one can use the list structure and the associated SAS/IML functions to emulate many different data structures, including the following:

Structs. A struct is a collection of named elements called members. The members can be inhomogeneous, which means they do not have to be the same type or size. For example, you could create a list that contains named fields for a person’s name, address, telephone number, and salary. You can use the ListSetName subroutine to assign names to list items.

Stacks. A stack is a linear array in which objects can be inserted and removed only at the beginning of the array. A push operation adds an item to the front of the list; a pop operation removes the item at the front of the list. A stack obeys the last-in first-out principle (LIFO). You can access only the first element of a stack. In the SAS/IML language, you can use the ListGetItem function to implement the pop operation and use the ListInsertItem operation to implement the push operation.

Queues. A queue is a linear array in which objects can be inserted at the end of the array and removed from the beginning of the array. A queue obeys the first-in first-out principle (FIFO) but is otherwise similar to a stack.

Trees. A tree contains nodes and directed edges. A tree starts with a root node. The root node is connected via branches to other nodes, called child nodes. Every node except the root node has exactly one parent node. In SAS/IML, lists can contains sublists. For an example, see the section Construct a Binary Search Tree.

Associative arrays. An associative array (also called a map or a dictionary) is a set of key-value pairs. Elements in an associative array are accessed by specifying the key. In the SAS/IML language, you can use the ListSetName subroutine to assign names to some or all elements. You can then access the elements by name.

