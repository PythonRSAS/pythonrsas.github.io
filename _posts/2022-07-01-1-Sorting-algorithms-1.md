---
layout: post
tag : data structure, algorithm, python
category: education
title: "Sorting algorithms-1"
description: selection sort, insertion sort, bubble sort
author: Sarah Chen
image: images/posts/photos/IMG_0871.JPG

---

- [Introduction](#introduction)
- [Insertion sort](#insertion-sort)
- [Select sort](#select-sort)
- [Compare Select sort and Insertion sort](#compare-select-sort-and-insertion-sort)
- [Bubble sort](#bubble-sort)
# Introduction

Sorting algorithms are very important.  In the Women in Mathematics summer program that I participated in Washington DC 2006 during my college junior year, the NSA director of mathematics came and gave us (16 women math college students from around the country) a talk on sorting algorithms.  The fact that he chose to talk about sorting made me realize it is importance.   When things are sorted, you can find what your target much faster.

The [binary search algorithm](2022-06-22-1-binary-search.md) works on a sorted array.  

There are two main types of sorting: by comparison and not by comparion.  All of the sorting methods in this post are by comparion. 

![Sorting algorithms and time efficiencies](../images/posts/sort.PNG)

Note that Python's built-in <span class="coding">list.sort</span> implements the Timsort algorithm, and is faster than most methods. 

# Insertion sort
Insertion sort feels like some kind of depth-first algorithm although it does not have anything to do with trees.

> It starts from left to right.  The leftiest two element chuck gets sorted.  Then three-element chunk gets sorted, and so on. 
![insertion sort](../images/posts/insertionSort.PNG)

> **For each element, compare it with all elements on its left side to find its right insertion point**. As we progress, all elements are in their rightplaces. 

For the element in the 2nd position, compare with its only left neighbor, if it is smaller than its left neighbor, swap.
Now the first two elements are sorted.

Then move on to the next element, the one in the 3rd position, compare it with its immediate left neighbor, swap if needed. 

Because for each element, the first comparison is always with its **immediate left** neighbor, if it is bigger than its immediate left neightbor, then nothing needs to be done because the left side has already been sorted.  Break to get out and move to the next element.

Else then we have to do **all the comparisons** to ensure the new element will be in its proper place so that order is maintained.  **All the comparisons** means it must go 'stepwise' and swap if needed <span class="coding">A[j+1], A[j] = A[j], A[j+1]</span>. 

All we have to do is to translate the above statement to code.  Before typing, we should work out the indices as shown in table below.

Loop pointer | start | end (inclusive) | direction | end + 1 (Python range)
---------|----------|---------|--------|--------
 Outer loop $$i$$ | $$1$$| $$N - 1$$ | L to R| $$N$$
 Inner loop $$j$$ | $$i-1$$ | $$0$$ | R to L | $$-1$$

<div class="code-head"><span>code</span>insertion sort.py</div>

```python
def insertionSort(A):
    N = len(A)
    for i in range(1,N):
        print("\ni is ", i)
        print("A[i] is ", A[i])
        for j in range(i-1, -1, -1): # everyone to the left of i
            print("j is ", j)
            print("A[j] is ", A[j])
            print("A is ", A)
            if A[j+1] >= A[j]:
                break
            else:
                A[j+1], A[j] = A[j], A[j+1]
                print("swapping ", A[j], " and ", A[j+1])
    return A

nums = [100,3,1]
print(insertionSort(nums))

# i is  1
# A[i] is  3
# j is  0
# A[j] is  100
# A is  [100, 3, 1]
# swapping  3  and  100

# i is  2
# A[i] is  1
# j is  1
# A[j] is  100
# A is  [3, 100, 1]
# swapping  1  and  100
# j is  0
# A[j] is  3
# A is  [3, 1, 100]
# swapping  1  and  3
# [1, 3, 100]
```
We can also use a while-loop instead of if-else-loop. 
<div class="code-head"><span>code</span>insertion sort while loop.py</div>

```python
def insertionSort(A):
    N = len(A)
    for i in range(1,N):
        j = i -1
        while A[j] > A[j+1] and j >= 0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A

nums = [100, 3, 9, 1, 0]
print(insertionSort(nums))
```

Insertion sort is not super fast because it uses nested loops. It is useful for only small datasets. 

# Select sort

> Select means to select the smallest from the unsorted (yellow portion)

> The first outer loop returns the "global minimum" from N elements and places it at the first place

> The second outer loop selects the minimum from the remining N - 1 elements, and so on


![selection sort](../images/posts/selectSort.PNG)

<div class="code-head"><span>code</span>selection sort.py</div>

```python
def selectSort(A):
    N = len(A)
    for i in range(0, N-1):
        min_index = i
        for j in range(i,N):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]

    return A
a = [4,9, 100, 1, 0,8,2]
print(selectSort(a))
# [0, 1, 2, 4, 8, 9, 100]
```

In the code below, I print out each step of the double looping to show how it works.

<div class="code-head"><span>code</span>selection sort in detail.py</div>

```python
def selectSort(A):
    N = len(A)
    for i in range(0, N-1):
        min_idx = i
        print("\nmin_idx is ", min_idx)
        for j in range(i, N):
            print("j is ", j)
            print("comparing if A[j] < A[min_idx]:", A[j], "and", A[min_idx])^
            if A[j] < A[min_idx]:
                min_idx = j
                print("min_idx is updated to ", min_idx)
        print("\nswap A[i], A[min_idx]: ", A[i], " and ",  A[min_idx])
        A[i], A[min_idx] = A[min_idx], A[i]
    return A

a = [4, 3, 5, 9, 9, 1, 1, 0]
print(selectSort(a))

# min_idx is  0
# j is  0
# comparing if A[j] < A[min_idx]: 4 and 4
# j is  1
# comparing if A[j] < A[min_idx]: 3 and 4
# min_idx is updated to  1
# j is  2
# comparing if A[j] < A[min_idx]: 5 and 3
# j is  3
# comparing if A[j] < A[min_idx]: 9 and 3
# j is  4
# comparing if A[j] < A[min_idx]: 9 and 3
# j is  5
# comparing if A[j] < A[min_idx]: 1 and 3
# min_idx is updated to  5
# j is  6
# comparing if A[j] < A[min_idx]: 1 and 1
# j is  7
# comparing if A[j] < A[min_idx]: 0 and 1
# min_idx is updated to  7

# swap A[i], A[min_idx]:  4  and  0

# min_idx is  1
# j is  1
# comparing if A[j] < A[min_idx]: 3 and 3
# j is  2
# comparing if A[j] < A[min_idx]: 5 and 3
# j is  3
# comparing if A[j] < A[min_idx]: 9 and 3
# j is  4
# comparing if A[j] < A[min_idx]: 9 and 3
# j is  5
# comparing if A[j] < A[min_idx]: 1 and 3
# min_idx is updated to  5
# j is  6
# comparing if A[j] < A[min_idx]: 1 and 1
# j is  7
# comparing if A[j] < A[min_idx]: 4 and 1

# swap A[i], A[min_idx]:  3  and  1

# min_idx is  2
# j is  2
# comparing if A[j] < A[min_idx]: 5 and 5
# j is  3
# comparing if A[j] < A[min_idx]: 9 and 5
# j is  4
# comparing if A[j] < A[min_idx]: 9 and 5
# j is  5
# comparing if A[j] < A[min_idx]: 3 and 5
# min_idx is updated to  5
# j is  6
# comparing if A[j] < A[min_idx]: 1 and 3
# min_idx is updated to  6
# j is  7
# comparing if A[j] < A[min_idx]: 4 and 1

# swap A[i], A[min_idx]:  5  and  1

# min_idx is  3
# j is  3
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  4
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  5
# comparing if A[j] < A[min_idx]: 3 and 9
# min_idx is updated to  5
# j is  6
# comparing if A[j] < A[min_idx]: 5 and 3
# j is  7
# comparing if A[j] < A[min_idx]: 4 and 3

# swap A[i], A[min_idx]:  9  and  3

# min_idx is  4
# j is  4
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  5
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  6
# comparing if A[j] < A[min_idx]: 5 and 9
# min_idx is updated to  6
# j is  7
# comparing if A[j] < A[min_idx]: 4 and 5
# min_idx is updated to  7

# swap A[i], A[min_idx]:  9  and  4

# min_idx is  5
# j is  5
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  6
# comparing if A[j] < A[min_idx]: 5 and 9
# min_idx is updated to  6
# j is  7
# comparing if A[j] < A[min_idx]: 9 and 5

# swap A[i], A[min_idx]:  9  and  5

# min_idx is  6
# j is  6
# comparing if A[j] < A[min_idx]: 9 and 9
# j is  7
# comparing if A[j] < A[min_idx]: 9 and 9

# swap A[i], A[min_idx]:  9  and  9
# [0, 1, 1, 3, 4, 5, 9, 9]
```


# Compare Select sort and Insertion sort

My graphic summary of the selection sort method looks identical to the one from the insertion sort method.

Both of them grow the sorted from left to right.  

Both of them use double looping.

* Differences:

Select sort **actions in the unsorted (right) side** (yellow).  

Each outer loop ***selects the smallest one from the unsorted side***  and places at the end of the left (sorted) side. 

Insertion sort **actions in the sorted (left)** side (green).  

Each outer loop ***moves the immediate neighbor from the unsorted sorted side*** and uses pair-wise swap (if needed) to find the new *defector* the right insertion point. 

* Insertion sort pointer indexing summary

Loop pointer | start | end (inclusive) | direction | end + 1 (Python range)
---------|----------|---------|--------|--------
 Outer loop $$i$$ | $$1$$| $$N - 1$$ | L to R| $$N$$
 Inner loop $$j$$ | $$i-1$$ | $$0$$ | R to L | $$-1$$

* Select sort pointer indexing summary

Loop pointer | start | end (inclusive) | direction | end + 1 (Python range)
---------|----------|---------|--------|--------
 Outer loop $$i$$ | $$0$$| $$N - 2$$ | L to R| $$N-1$$
 Inner loop $$j$$ | $$i$$ | $$N-1$$ | L to R | $$N$$



# Bubble sort

> With each loop, the largest one from the unsorted (left yellow section) is moved to sorted section (right) while ironing out **local wrinkles**.  

![Bubble sort](../images/posts/bubbleSort.PNG)

> The buble sort is quite similar to **insertion sort** as both use **adjacent pair-wise comparions**, and swaps them into sorted order in each scanning loop. 

Insertion sort moves the immediate neighbor from unsorted (right) to the sorted (left) and shuffles it to its proper insertion point via pair-wise comparision <span class="coding">A[j], A[j+1] = A[j+1], A[j]</span>, bubble sort bubbles the the largest one from the unsorted to the sorted (left to right).  


<div class="code-head"><span>code</span>bubble sort.py</div>

```python
def bubbleSort(A):
    N = len(A)
    sorted = False

    while not sorted:
        sorted = True # for getting out the while loop
        for i in range(0, N -1):
            if A[i] > A[i+1]:
                sorted = False
                A[i], A[i+1] = A[i+1],A[i]
    return A
a = [4, 9, 100, 1, 0, 8, 2]
print(bubbleSort(a))
# [0, 1, 2, 4, 8, 9, 100]
```

In the buble sort code below, I have printed out how the input array gets sorted in each step and each loop.

<div class="code-head"><span>code</span>bubble sort explanation version.py</div>

```python
def bubbleSort(A):
    N = len(A)
    sorted = False
    print(A)
    while not sorted:
        print("\nStarting the loop:")
        sorted = True # for getting out the while loop
        for i in range(0, N -1):
            if A[i] > A[i+1]:
                sorted = False
                A[i], A[i+1] = A[i+1],A[i]
                print(A)
    return A
a = [4, 9, 100, 1, 200, 0, 8, 2]
print(bubbleSort(a))

# [4, 9, 100, 1, 200, 0, 8, 2]

# Starting the loop:
# [4, 9, 1, 100, 200, 0, 8, 2]
# [4, 9, 1, 100, 0, 200, 8, 2]
# [4, 9, 1, 100, 0, 8, 200, 2]
# [4, 9, 1, 100, 0, 8, 2, 200]

# Starting the loop:
# [4, 1, 9, 100, 0, 8, 2, 200]
# [4, 1, 9, 0, 100, 8, 2, 200]
# [4, 1, 9, 0, 8, 100, 2, 200]
# [4, 1, 9, 0, 8, 2, 100, 200]

# Starting the loop:
# [1, 4, 9, 0, 8, 2, 100, 200]
# [1, 4, 0, 9, 8, 2, 100, 200]
# [1, 4, 0, 8, 9, 2, 100, 200]
# [1, 4, 0, 8, 2, 9, 100, 200]

# Starting the loop:
# [1, 0, 4, 8, 2, 9, 100, 200]
# [1, 0, 4, 2, 8, 9, 100, 200]

# Starting the loop:
# [0, 1, 4, 2, 8, 9, 100, 200]
# [0, 1, 2, 4, 8, 9, 100, 200]

# Starting the loop:
# [0, 1, 2, 4, 8, 9, 100, 200]
```



