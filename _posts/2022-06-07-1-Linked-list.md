---
layout: post
tag : data structure
category: education
title: "Linked list"
description: linked list as an abstract data structure and implementation in Python
author: Sarah Chen
image: images/posts/linked_list.jpg

---
Arrays are stored in contiguous blocks of memory in a compuater.  In C, array sizes are fixed.  This creates the need to have a data structure that allows data being stored in different places of a computer and are connected via pointers.  That is linked list. 

Linked lists were developed in 1955–1956, by Allen Newell, Cliff Shaw and Herbert A. Simon at RAND Corporation as the primary data structure for their Information Processing Language. IPL was used by the authors to develop several early artificial intelligence programs.

A linked list is a kind of abstract data structure,  like a chain of objects, called *nodes*, each points to the next except the last one, which points to <span class="coding">\__None__</span> (NULL). 

# Compare with (abstract) array
* **Advantages**:
* *Fast insertion/deletion*: Unlike arrays (abstract data structure), linked lists are resizable at run-time as linked list nodes are stored at *arbitrary locations in memory*.  Fast Insertion and deletion operations because do not need to change the indices of other elements or storage location. 
  
* **Disadvantages**:
* *Slower search*: We cannot access elements in constant time as we do in arrays.  To find a node at position n, we have to start the search at the first (head) node and iterate through via <span class="coding">next</span>. 
* Linked lists takes more space than the array. 

![what is a linked list](../images/posts/linked_list.jpg)

In table Below we compare the abstract data structure of array and linked list:

Compare | array | linked list
---------|----------|---------
 size | fixed at birth | can change from insertion/deletion
 storage | static in continuous block of memory allocated during compile time | dynamic, nodes are located at run time
 ordering/sorting | fast direct access via index  | sequential, transverse from the head node via link (next)
 search | binary and linear search | linear search

Linked lists are preferable over arrays when we need **constant-time insertions/deletions** from the list (such as in real-time computing where time predictability is absolutely critical) and we don't need random access to any elements
# Linked lists uses

They are useful when we need fast insertion and deletion, and when we do not know in advance the size of data, or do not need random access when searching for items.   

![linked list uses](../images/posts/linked_list_uses.jpg)
# Linked list implementation in Python
Given the flexibility of Python lists, Python does not have a native support for linked list.  So we need to build the node class first and then implement linked list. 
In this implementation, linked list has the following common operations:
* Insert, insert at end, insert at beginning, insert between
* Delete (iterative find and then delete)               
* Search (iterative search)  
* Count number of elements
* Print list   

Each node is an *independent object that can contain anything*. 
        
<!-- * Indexing -->  
<div class="code-head"><span>code</span>node.py</div>

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
        return self.datalin
    
    # function to set next node
    def setNext(self, next):
        self.next = next
        
    # function to get the next node
    def getNext(self):
        return self.next
```

The <span class="coding">count</span> attribute is convenient because we don't need to go through the entire linked list to get the number of elements.  With each insert, the count increments by 1 whereas delete decreases by 1 with <span class="coding">delete</span>. 

However, this attribute potentially has a problem: if <span class="coding">LinkedList</span> is instantiated without a head, and a head is added later such as in <span class="coding">LL.head = Node("Hello")</span>, its count stays 0.  Therefore, we define count as the number of elements without head. 

<div class="code-head"><span>code</span>linkedList.py</div>

```py
    
class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self, head = None):
        # if head = None:
        #     self.head = None
        #     self.count = 0
        # else: 
        #     self.head = head
        #     self.count = 1
        self.head = head
        self.count = 0
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
        self.head = newNode # update LinkList head
        self.count += 1 # update count
        
    # inserting the node in between the linked list (after a specific node)
    def insertBetween(self, previousNode, data):
        if (previousNode.next is None):
            print('Previous node should have next node!')
        else:
            newNode = Node(data)
            newNode.next = previousNode.next
            previousNode.next = newNode
            self.count += 1 # update count
            
    # inserting at the end of linked list
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
# Reference
[The quest for the fastest linked list by Johny’s Software Lab](https://johnysswlab.com/the-quest-for-the-fastest-linked-list/)

[Linked List, Wikipedia](https://en.wikipedia.org/wiki/Linked_list)

[Stackoverflow, when-to-use-a-linked-list-over-an-array-array-list](https://stackoverflow.com/questions/393556/when-to-use-a-linked-list-over-an-array-array-list)