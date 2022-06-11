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

# Heap



# Data structures in SAS
In SAS, one can use the list structure and the associated SAS/IML functions to emulate many different data structures, including the following:

Structs. A struct is a collection of named elements called members. The members can be inhomogeneous, which means they do not have to be the same type or size. For example, you could create a list that contains named fields for a person’s name, address, telephone number, and salary. You can use the ListSetName subroutine to assign names to list items.

Stacks. A stack is a linear array in which objects can be inserted and removed only at the beginning of the array. A push operation adds an item to the front of the list; a pop operation removes the item at the front of the list. A stack obeys the last-in first-out principle (LIFO). You can access only the first element of a stack. In the SAS/IML language, you can use the ListGetItem function to implement the pop operation and use the ListInsertItem operation to implement the push operation.

Queues. A queue is a linear array in which objects can be inserted at the end of the array and removed from the beginning of the array. A queue obeys the first-in first-out principle (FIFO) but is otherwise similar to a stack.

Trees. A tree contains nodes and directed edges. A tree starts with a root node. The root node is connected via branches to other nodes, called child nodes. Every node except the root node has exactly one parent node. In SAS/IML, lists can contains sublists. For an example, see the section Construct a Binary Search Tree.

Associative arrays. An associative array (also called a map or a dictionary) is a set of key-value pairs. Elements in an associative array are accessed by specifying the key. In the SAS/IML language, you can use the ListSetName subroutine to assign names to some or all elements. You can then access the elements by name.
# Recursion
