---
layout: post
tag : abstract data structure, ADT
category: education
title: "Basic data structures"
description: essentials in data structures including stack, queue, linked list. 
author: Sarah Chen
image: images/posts/photos/IMG_0878.JPG

---
  
- [Array](#array)
- [Stacks and queues](#stacks-and-queues)
- [Linked List](#linked-list)
- [Graphs](#graphs)
- [Tree](#tree)
- [Reference](#reference)


In the machine learning and artificial intelligence era, it is necessary to understand basic abstract data structures, and why we need them. 

Data structures are defined and built according to varied needs of different data types and algorithms. 

 
# Array
Arrays are lists of similar data. An array of an array is a 2-dimensional array, i.e. matrix. 
- name
- type: the type of data is stored, and all have to be the *same* within one array
- size: it is fixed once it is defined, and **cannot be changed** once created

There are 2 ways to create an array:
- define the entire array along with its elements altogether
- define its size only and populate it later (not possible in base Python although we can do it using numpy)

1. Access: random access use *index* as all elements are indexed, run time is$$O(1)$$; 
2. Search:$$O(n)$$, may need to go over each element to find an item from an unsorted array
3. Insert:$$O(n)$$, because we need to shift the elements, which are after the index where we want to insert the item, to the *'right'* for one space  4. Delete:$$O(n)$$, because we need to shift the elements, which are after the index where we want to insert the item, to the *"left"* for one space  

pros | cons
---------|----------
good for storing similar data | data must be the same; size cannot be changed once created 
efficient accessing | insert/delete are not as efficent 

Array elements are stored in contiguous (continuous) memory locations. Its efficiency is in scaling its attributes to all its elements. 

ArrayList is a derivation of array.  It is a *growing* array, where the size can be changed.  It has more functionality than an array, including the following 6 common methods:
- add
- remove
- get
- set
- clear
- toArray

Numpy arrays depends on the numpy library.  Python does not have a native support for arrays, but has a more generic data structure called *list*. 


**In Python, arrays and arrayLists are grouped together into a single data structured called "Lists"**. 

# Stacks and queues
Like what it sounds like, a stack is a stack of something.  The last one added is the first one out. In life, undo, redo, go back, and etc. are all examples of "stacking".
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

![stack push and pop](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Lifo_stack.svg/700px-Lifo_stack.svg.png)

In computer, stack data structure is used for keeping track of active functions or subroutines. 

Stack is the backbone for all recursive processes in our computers.  Recursive processes are those functions that call themselves within themselves. 

When the function calls itself, the call is aded to a stck of processes, keeping track of active subroutines in code and more. 

Queues are the opposite of stacks.  Queues are "FIFO". 

# Linked List

[Linked lists](https://en.wikipedia.org/wiki/Linked_list#History) were developed in 1955–1956, by Allen Newell, Cliff Shaw and Herbert A. Simon at RAND Corporation as the primary data structure for their Information Processing Language. IPL was used by the authors to develop several early artificial intelligence programs, including the Logic Theory Machine, the General Problem Solver, and a computer chess program. 

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


# Graphs
For example, social media networks, map of paths between cities.  From point A to point B there are many paths or connections. The relationship of graphs are **many-to-many**, not linear one-to-one. 
![graph](https://pythonrsas.github.io/images/posts/myTrip.PNG)


# Tree

![org chart](https://www.ayoa.com/templates/wp-content/uploads/sites/5/2020/11/Company-organizational.jpg)
The boss is in charge of a bunch of heads of departments.  The head of a department is in charge of a bunch of managers.  The manager of a team is in charge of a bunch of employees, and so on.   The relationship between boss to staff is **one-to-many**.  Hierchical data is represented by a special type of trees,

A tree is a data structure **similar to a linked List** but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. 

Tree is an example of non-linear data structures. A tree structure is a way of representing the **hierarchical** nature of a structure in a graphical form.

* The **root** of the tree is the node with no parents. **There can be at most one root node in a tree**.
* The _edge_ refers to the link from parent to child.
* A node with NO children is called _leaf_ node.
* Children of same parent are called _siblings_.

**Applications of trees**
* Manipulate hierarchical data.
* Make information easy to search (see tree traversal).
* Manipulate sorted lists of data.
* As a workflow for compositing digital images for visual effects.
* Router algorithms
* Form of a multi-stage decision-making (see business chess).


# Reference
[wikipedia](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))



