---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "numpy outer product"
description: a few ways to do outer product using numpy
author: Sarah Chen
image: images/posts/derek-mack.jpg

---
One of the advantage of Python over base SAS (of course SAS has other advantages over Python) is matrix operations.  This short post is about a few ways to do outer product using Numpy.  

Outer product is also called "cartesian product".  It is every order combination of the two arrays, and multiplied.  The number of elements in the end result is nXm, if the left has n and the right has m elements, respectively. 

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
