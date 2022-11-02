---
layout: post
tag : python
category: education
title: "tuples reviewed"
description: review basics on Python data type tuples
author: Sarah Chen
image: images/posts/photos/7bridges.JPG

---

- [tuples](#tuples)
  - [tuples are like lists](#tuples-are-like-lists)
  - [Use with dictionary](#use-with-dictionary)
  - [Return a tuple of values in a function](#return-a-tuple-of-values-in-a-function)
- [namedtuple](#namedtuple)

# tuples
Some notes below are adapted from the book [Think Python](https://www.greenteapress.com/thinkpython/html/thinkpython013.html). 

## tuples are like lists

Tuples are like lists, except tuples are immutable, and they don't use square brackets. 

Note that tuples are immutable meaning that you cannot modify it by assignment such as x[0] = 100.  But you can add elements to it just like you do to a list.  Note that it is like list means that you can do things like:
```python
x = (1, 2)
x += (3, 4)
x
# 1, 2, 3, 4
```

A tuple is a ***comma-separated list of values***, which **can be any type**, and they are indexed by integers, so in that respect tuples are a lot like lists. 

**Most list operators also work on tuples**. The bracket operator <span class="coding">[]</span> for indexing, and the slicing operator <span class="coding">:</span>. 

> Tuple as function return values: allows us to return multiple values, a function can only return one value, but if the value is a tuple, the effect is the same as returning multiple values. 

> Use <span class="coding">zip</span>, a built-in function, to take two or more sequences and “zips” them into a list of tuples. For example, we can zip a list of country, and a list of capitals associated with the countries. 

```python
t = 'a', 'b', 'c', 'd', 'e'
```
Although it is not necessary, it is common to enclose tuples in parentheses:

```python
>>> t = ('a', 'b', 'c', 'd', 'e')
```
## Use with dictionary

**.items:** Dictionaries have a method called <span class="coding">items</span> that returns an iterator, a list of tuples, where each tuple is a key-value pair.

**Use as dictionary keys:** tuples are often used as dictionary keys.
For example, dictionary[last_name, first_name].  The key <span class="coding">last_name, first_name</span> is a tuple. 

## Return a tuple of values in a function
A function can return multiple values by return a tuple. 
For example, I am using the function below to return mean, median, and the latest value of input data, which is a dataframe of timeseries index with datetime. 

```python
def get_stats(df):
    Mean = df.mean()[0]
    Median = df.median()
    Latest = df.sort_index(ascending=False).iloc[0,0]
    return(Mean, Median, Latest)
```
# namedtuple
A [namedtuple](https://docs.python.org/3/library/collections.html?highlight=counter#collections.namedtuple) object is a new tuple subclass with a name we give it. 

The new subclass is used to create tuple-like objects that have fields *accessible by the <span class="coding">.</span>* notation as well as inherited tuple attributes such as indexable and iterable. 
In code below, we define a Graph class. <span class="coding">help(G)</span>

```python
help(G)
# Help on Graph in module __main__ object:
# class Graph(builtins.tuple)
#  |  Graph(vertice, edge, weights)
#  |
#  |  Graph(vertice, edge, weights)
#  |
#  |  Method resolution order:
#  |      Graph
#  |      builtins.tuple
#  |      builtins.object

G[0]
# ['A', 'B', 'C', 'D']
G.vertice
# ['A', 'B', 'C', 'D']
```
