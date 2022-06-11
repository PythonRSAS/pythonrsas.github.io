---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "numpy outer product"
description: a few ways to do product and outer product using numpy using different ways to reshape
author: Sarah Chen
image: images/posts/derek-mack.jpg

---
One of the advantage of Python over base SAS (of course SAS has other advantages over Python) is matrix operations.  This short post is about a few ways to do product and outer product using Numpy.  

# products
<span class="coding">np.multiply</span> and <span class="coding">*</span> accomplish the same thing. Both multiply element-wise. 

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
