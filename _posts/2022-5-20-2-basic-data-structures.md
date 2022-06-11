---
layout: post
tag : data structure, algorithm, python
category: "Python for SAS"
title: "Basic Algorithms"
description: essentials in algorithms including recursion, and various sorting, such as bubble sort, quick sort, select sort,and search
author: Sarah Chen
image: images/posts/derek-mack.jpg

---
The basic data structures in Python are: dictionary, list, special lists (linked list, stack, queue). 
Basic algorithms: recursion, sorting (select sort, bubble sort, quick sort).

# Recursion
Recursion in algorithm refers to calling a function within its own definition. Many mathematical computations can be defined using recursion.  For example, Taylor expansions, Fibonnaci sequence, and so on. 
[cross-section of a nautilus shell](https://www.maa.org/sites/default/files/images/cms_upload/spiral04457.gif with a superimposed polar coordinate grid. The outer spiral of the shell has been traced with a green curve.
<div class="code-head"><span>code</span>Fibonacci.sas</div>

```sas
DATA fs;
n1 = 0; n2=.;  
i =0; n3 = n2; output;
DO i = 1 TO 10;
    n3 = sum(n1, n2);
    OUTPUT;
    n2 = n1;
    n1 = n3;
END;
RUN;
```

<div class="code-head"><span>code</span>Fibonacci using recursion.py</div>

```py
# recursion: every number is the sum of its proceeding 2 numbers
def fb(n):
    if n<2:
        return 1
    else:
        return fb(n-1) + fb(n-2)
fb(2)
# 3
for i in range(10):
    print(fb(i))
# out: 
1
1
2
3
5
8
13
21
34
55
```

We can write it using for loop even though it is mathematically convenient to express the sequence using recursion.
<div class="code-head"><span>code</span>Fibonacci using recursion.py</div>

```py
def fb_loop(n):
    n0 =0
    n1 =1
    seq = []
    for i in range(10):
        n = n1 + n0
        print(n1)
        seq.append(n)
        n0 = n1
        n1 = n
    return seq
```

Sorting algorithms are extremely important.  In the Women in Mathematics summer program that I participated in Washington DC 2006, the NSA director of mathematics came and gave us a talk on sorting algorithms.  

# Sorting algorithms

## Bubble sort

# bubble sort

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


## Select sort


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
## Quick sort (not in place)
<div class="code-head"><span>code</span>quick_sort_0.py</div>

```python
def qs(a):
    if len(a)< 2:
       return a
    else:
        small = []
        big = []
        pivot = a.pop()
        for i in range(0,len(a)):
            if a[i]> pivot:
                big.append(a[i])
            else:
                small.append(a[i])
    return qs(small)+[pivot] + qs(big)
print(qs(a))
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

# reshape
An useful reshape trick is **<span class="coding">-1</span>**, which is a placeholder that refers to the size of the remaining axis that is to be inferred.

For example, we begin with a 1-d array of length 6, and want to reshape it to (2,3), 2 rows and 3 columns.  By <span class="coding">(2,-1)</span>, we mean: 2 rows and 6/2 columns.  <span class="coding">-1</span> is a placeholder for the inferred <span class="coding">3</span>.  

```python
>>> a = np.array([1,2,3,4,5,6])
>>> a1 = a.reshape(2,-1)
>>> print(a1)
Out:
[[1,2,3]
[4,5,6]]
```

# Outer product
Outer product is also called "cartesian product".  It is every order combination of the two arrays, and multiplied.  The number of elements in the end result is nXm, if the left has n and the right has m elements, respectively. 

In all methods below, my favorite is <span class="coding">reshape</span> because there is nothing extra to remember other than the use of <span class="coding">-1</span>. 

<div class="code-head"><span>code</span>outer product.py</div>

```python
In [1]: x = np.array([1,2,3])

In [2]: y = np.array([2,4])

In [3]: np.outer(x,y)
Out[3]:
array([[ 2,  4],
       [ 4,  8],
       [ 6, 12]])

In [4]: x[:,np.newaxis]*y[np.newaxis,:]
Out[4]:
array([[ 2,  4],
       [ 4,  8],
       [ 6, 12]])

In [5]: x.reshape((-1,1))*y.reshape((1,-1))
Out[5]:
array([[ 2,  4],
       [ 4,  8],
       [ 6, 12]])

In [6]: x.reshape((-1,1))*y.reshape((-1,1)).T
Out[6]:
array([[ 2,  4],
       [ 4,  8],
       [ 6, 12]])

In [7]: np.multiply(x.ravel()[:,np.newaxis],y.ravel()[np.newaxis,:])
Out[7]:
array([[ 2,  4],
       [ 4,  8],
       [ 6, 12]])
```
