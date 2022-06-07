---
layout: post
tag : computer data structure, python
category: "Python for SAS"
title: "Basic data structures"
description: essentials in data structures including stack, queue, linked list. 
author: Sarah Chen
image: images/posts/derek-mack.jpg

---
In working in financial services, whether credit risk modeing, or insurnace pricing, I did not once need to use knowledge on data structures such as stack, queue.  Surely, I need to know how SAS, Python, and R processes data, in particular when working with large filres.  But the goal was to get insight, build models, and predict/forecast. Working in SAS, all you need to know are the <span class="coding">DAT</span> steps, procedures such as <span class="coding">PROC MEAN</span>, <span class="coding">PROC UNIVARIATE</span> and so on for basic data analysis, and more specific procedures for deeper dives and modeling.  Working in Python, the story was quite similar. You master pandas, maybe a little bit of matplotlib, seaborn, numpy and scipy, statsmodels, and sklearn, you've covered all the basics. 

However, in the machine learning era, the goals and capacities of analytics have far expanded beyond statistics and modeling.

Stack is the backbone for all recursive processes in our computers.  
queue, The opposite of a stack
Linked list
Doubly linked list
dictionary and hash tables
trees and tries (for word-procssing algo)
heaps and grapsh

# The Big O metric
In analytic number theory class by my late professor Patrick Gallagher,the big O metric was associated with whether two different representations are aymptotically close (when the epsilon is )
![Professor Patric Gallagher](/images/posts/Gallagher.PNG)

The “big O” notation: 
If $$S$$ is a set and f and g are functions $$S$$ → $$R$$, we say that $$ f = O(g)$$ if there exists an $$M > 0$$ such that $$|f(s)| ≤ Mg(s)$$ for all s $$∈$$ $$S$$.  Usually the set $$S$$ is taken to be the interval $$[a, ∞)$$ for some sufficiently large $$a ∈ R$$ that is left unstated, or an open interval like
$$(1, 2]$$ if we care about asymptotic behavior near 1.

Therefore, $$O(1)$$ means some constant (time). Similarly, $$O(2)$$ or $$O(100)$$ also mean constant. 

$$O(n)$$ means linear as in $$M*n$$ for some $$M>0$$.

In computer science, the big $$O$$ is used as a time efficiency metric for data structure: how much time it takes to do each of the following:
1. Access (to get)
2. Search (to find)
3. Insert (to add)
4. Delete (to remove)

In computer science context, constant time (e.g. O(1)) means that the amound of time it takes to do something (something could be one of the 4 tasks above) is independent of the size of the data.  The size of data $$n$$ is absent from the $$O()$$. Constant time is the most efficient but also difficult to achieve. 

As VaR (value at risk) is not the only thing we used for measuring market risk, the big $$O$$ is not the only thing either.  But it is very useful. 


Time complexity | $$O$$ as a function of data size $$n$$ | Explain
---------|----------|---------
constant | $$O(1)$$ | data size is irrelevant
log n | $$O(log(n))$$ | data size is relevant, but not less than linearly
linear |$$O(n)$$ | time is a linear function of data size

# Stack

Stack is the backbone for all recursive processes in our computers.  
# Data structures in SAS
In SAS, one can use the list structure and the associated SAS/IML functions to emulate many different data structures, including the following:

Structs. A struct is a collection of named elements called members. The members can be inhomogeneous, which means they do not have to be the same type or size. For example, you could create a list that contains named fields for a person’s name, address, telephone number, and salary. You can use the ListSetName subroutine to assign names to list items.

Stacks. A stack is a linear array in which objects can be inserted and removed only at the beginning of the array. A push operation adds an item to the front of the list; a pop operation removes the item at the front of the list. A stack obeys the last-in first-out principle (LIFO). You can access only the first element of a stack. In the SAS/IML language, you can use the ListGetItem function to implement the pop operation and use the ListInsertItem operation to implement the push operation.

Queues. A queue is a linear array in which objects can be inserted at the end of the array and removed from the beginning of the array. A queue obeys the first-in first-out principle (FIFO) but is otherwise similar to a stack.

Trees. A tree contains nodes and directed edges. A tree starts with a root node. The root node is connected via branches to other nodes, called child nodes. Every node except the root node has exactly one parent node. In SAS/IML, lists can contains sublists. For an example, see the section Construct a Binary Search Tree.

Associative arrays. An associative array (also called a map or a dictionary) is a set of key-value pairs. Elements in an associative array are accessed by specifying the key. In the SAS/IML language, you can use the ListSetName subroutine to assign names to some or all elements. You can then access the elements by name.
# Recursion
