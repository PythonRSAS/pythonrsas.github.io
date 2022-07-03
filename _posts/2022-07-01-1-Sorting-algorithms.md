---
layout: post
tag : data structure, algorithm, python
category: "Python for SAS"
title: "Sorting algorithms"
description: quick sort, select sort, bubble sort, merge sort, bucket sort
author: Sarah Chen
image: images/posts/photos/IMG_0871.JPG

---

Sorting algorithms are very important.  In the Women in Mathematics summer program that I participated in Washington DC 2006 during my college junior year, the NSA director of mathematics came and gave us (16 women math college students from around the country) a talk on sorting algorithms.  The fact that he chose to talk about sorting made me realize it is importance.  For examples:

When things are sorted, you can find order much faster, for example, percentiles.  
The [binary search algorithm](2022-06-22-1-binary-search.md) works on a sorted array.  

![Sorting algorithms and time efficiencies](../images/posts/sort.PNG)

# Quick sort

The quick sort algorithm reminds me of binary search.  

In binary search on a sorted array, we half the search range by comparing target with the median of the search range.  

Quick sort works by sorting as if we only care about sorting into two parts: larger and smaller.  The element that is used to split the original array into two parts is commonly called the "pivot".  

Then we apply the same method to each of the two parts, and continue until each of the parts has only 1 element (cannot be splited anymore).  

![quick sort](../images/posts/quickSort.PNG)

![quick sort recursion](../images/posts/quickSort2.PNG)

Below quick sort implementation is simple but not optimized in any way. 

<div class="code-head"><span>code</span>basic quick sort.py</div>

```python
def qs(A):
    N = len(A)
    if N < 2:
       return A
    else:
        L = [] # not inplace
        H = []
        pivot = A.pop() # using the last element instead of random or the "median of three" method
        for i in range(0,len(A)):
            if A[i]> pivot:
                H.append(A[i])
            else:
                L.append(A[i])
    return qs(L)+[pivot] + qs(H)

nums = [100, 3, 9, 1, 0]
print(qs(nums))
# [0, 1, 3, 9, 100]
```
Below quick sort implementation has improvement in space complexity.  

<div class="code-head"><span>code</span>basic quick sort in place.py</div>

```python
def partition(A, l, r):
    i = l - 1
    pivot = A[r] # use the rightmost of range as pivot (not the best method)
    for j in range(l, r):
        if A[j] <= pivot:
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
def quicksort(A, l=0, r = None):
    if r==None:
        r = len(A) - 1
    if l < r:
        pivot = partition(A, l,r)
        quicksort(A, l, pivot-1)
        quicksort(A, pivot+1, r)
    return A
nums = [100, 3, 9, 1, 0]
quicksort(nums,l=0)
```

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
        while A[j]>A[j+1] and j>=0:
            A[j], A[j+1] = A[j+1], A[j]
            j -= 1
    return A

nums = [100, 3, 9, 1, 0]
print(insertionSort(nums))
```

Insertion sort is not super fast because it uses nested loops. It is useful for only small datasets. 

# Merge sort

# Bucket sort (Radix sort)

Radix sort is a very fast sorting algorithm for integers.  Unlike other sorting methods, it does no comparisons. Digits of integers are slotted into their respective buckets (0, 1, 2, 3, ..., 9)

> There is no comparions and no if-else branching

![Bucket sort](../images/posts/bucketSort.PNG)

It is very fast for large quantities of small integers. 

Note the order of operations in <span class="coding">i//10**(digit)%10</span>:
> The exponential is computed first even if you put a space between like <span class="coding">i//10** (digit)%10</span>!
> To avoid any confusion, it may be better to write <span class="coding">i//(10**digit)%10</span>

Also, pay attention to that $$A$$ is modified with each loop. 

**In the first loop, $$A$$ is the input**.
**In all subsequent loops, $$A$$ is the flattened buckets $$B$$**. 

I intentionally print out each step 
```python
def bucketSort(A):
    num_digits = len(str(max(A)))

    for digit in range(0, num_digits):
        B = [[] for i in range(10)] # list of list
        for i in A:
            num = i//10**(digit)%10 
            B[num].append(i)
        # flatten
        A = []
        for i in B:
            A.extend(i)
    return A

A = [4, 9, 100, 1, 598, 0, 8]
print(bucketSort(A))

# [0, 1, 4, 8, 9, 100, 598]
```



# Bubble sort


<div class="code-head"><span>code</span>bubble sort.py</div>

```python
def bs(a):
    sorted= False
    while not sorted:
        sorted = True # for getting out the while loop
        for i in range(0, len(a)-1):
            if a[i]>a[i+1]:
                sorted=False
                a[i], a[i+1] = a[i+1],a[i]
    return a
a = [4,9, 100, 1, 0,8,2]
print(bs(a))
# [0, 1, 2, 4, 8, 9, 100]
```


# Select sort


<div class="code-head"><span>code</span>select sort.py</div>

```python
def ss(a):
    for i in range(0, len(a)-1):
        min_index = i
        for j in range(i,len(a)):
            if a[j]< a[min_index]:
                min_index=j
        a[i],a[min_index] =a[min_index], a[i]

    return **a**
a = [4,9, 100, 1, 0,8,2]
print(ss(a))
# [0, 1, 2, 4, 8, 9, 100]
```

```python

>>> a = 'Hello, how are you'
>>> r = rotate(a,7)
>>> print(r)
Out:
how are youhello,
```

# rotate a numpy array

We can recycle the previous code for rotating a list.  The 2 differences are:
1. use <span class="coding">np.concatenate</span> instead of <span class="coding">+</span>.
2. use <span class="coding">axis=None</span> such that the numbers are joined without using any axis. 

If we have inputs of multiple dimensions, we can just reshape or flatten them, and rotate accordingly to what we want to achieve. 

```python
>>> def rotate_array(a,k):
>>>        if k==0: return a
>>>        k = k%len(a)
>>>        return (np.concatenate((a[k:],a[:k]), axis=None))
>>> a = np.array([1,2,3,4,5,6])
>>> r = rotate_array(a,2)
>>> print(r)
Out:
array([3,4,5,6,1,2])

```

<span class="coding">np.dot</span> as the name implies, gives a dot product.  The result is a single number. 
