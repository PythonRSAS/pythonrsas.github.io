---
layout: post
tag : computer data structure, python
category: "Python for SAS"
title: "Linked list"
description: array in Python, actually it is about list
author: Sarah Chen
image: images/posts/photos/IMG_0877.JPG

---

# Linked List

A linked list is a data structure,  like a chain of objects, called *nodes*, each points to the next except the last one, which points to <span class="coding">\__None__</span> (NULL).  

![what is a linked list](./images/posts/linked_list.JPG)

* Can change size during execution of a program
* Can be arbitrarily long, up to memory size
* Does not waste memory space (but takes some extra memory for pointers)

![linked list uses](../images/posts/linked_list_uses.jpg)
# Compare with (abstract) array
* Unlike abstract data structure arrays, they are resizable at run-time. Also, the insertion and deletion operations are efficient and easily implemented.
* Unlike arrays, linked lists are *slow* at finding the <span class="coding">__n__th</span> item.To find a node at position  <span class="coding">__n__</span>, we have to start the search at the first (head) node and iterate through via <span class="coding">next</span>. 
* Linked lists takes more space than the array.  Compare with an array whose values are all stored in contiguous memory, a linked list's nodes are at arbitrary locations in memory.

# Linked list implementation
In this implementation, linked list and Node are defined in separate classes.  It has the following common operations:
* Insert, insert at end, insert at beginning, insert between
* Delete (iterative find and then delete)               
* Search (iterative search)  
* Print list           
<!-- * Indexing -->
  
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
    # iterative search return found item instead of True/False
    def search_list(self, node, data):
        while node and node.data != data:
            node = node.next
        return node
            
In [5]: LL = LinkedList()^M
   ...: LL.head = Node("Hello")^M
   ...: print("After defining head node")
   ...: LL.printLinkedList()
After defining head node
Hello
 
In [8]: node1 = Node(1)^M
   ...: LL.head.setNext(node1) ^M
   ...: print("After inserting 1 after head node")^M
   ...: LL.printLinkedList()
   ...:
After inserting 1 after head node
Hello 1

In [10]: node2 = Node(2)^M
    ...: node1.setNext(node2)     ^M
    ...: LL.insertAtStart(4)    ^M
    ...: LL.insertBetween(node1, 5)^M
    ...: LL.insertAtEnd(6)^M
    ...: print("After inserting at start, between and end")^M
    ...: LL.printLinkedList()^M
    ...:
After inserting at start, between and end
4 Hello 1 5 2 6

In [11]: LL.delete(3)^M
    ...: print("After deleting 3")^M
    ...: LL.printLinkedList()
    ...:
After deleting 3
4 Hello 1 5 2

In [12]: print(LL.search(LL.head, 1))
True

In [13]: print("Searching for 'hello'")^M
    ...: print(LL.search(LL.head, 'hello'))
    ...:
Searching for 'hello'
False

In [14]: print("Searching for 'Hello'")^M
    ...: found = LL.search_list(LL.head, 'Hello')^M
    ...: print(found.data)
    ...:
    ...:
Searching for 'Hello'
Hello

```

* In general, __array__ is considered a data structure for which size is fixed at the compile time and array memory is allocated either from __Data section__ (e.g. global array) or __Stack section__ (e.g. local array). 
* Similarly, linked list is considered a data structure for which size is not fixed and memory is allocated from __Heap section__ (e.g. using malloc() etc.) as and when needed. In this sense, array is taken as a static data structure (residing in Data or Stack section) while linked list is taken as a dynamic data structure (residing in Heap section).
* The array elements are allocated memory in sequence i.e. __contiguous memory__ while nodes of a linked list are non-contiguous in memory. Though it sounds trivial yet this is the most important difference between array and linked list. It should be noted that due to this contiguous versus non-contiguous memory, array and linked list are different.

# Implementing doubly linked list

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

# Linked list examples

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
