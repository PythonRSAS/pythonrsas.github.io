---
layout: post
tag : hash table, dict, set
category: "Python for SAS"
title: "hash table"
description: hash table algorithm implementation in Python and the bisect library
author: Sarah Chen
image: images/posts/photos/IMG_0873.JPG

---
> Hash tables can be seen as *indexed arrays* via hash functions. 

- [hash table the basics](#hash-table-the-basics)
  - [Deterministic property](#deterministic-property)
- [Hash tables in Python](#hash-tables-in-python)

# hash table the basics

A hash table is data structure like a Python dictionary. It is designed to store keys (strings), and optionally, with associated values in an **array**.  It is highly efficient for find, insert, and delete. 

A key is stored in the array locations based on its hash code, which is an integer $$\text{hash code}=\text{array index}=f(\text{input key})$$.  

Hash codes are integers that are array indices. 

Hash function maps keys to array indices. 

A good hash function distributes hash codes uniformly through the array locations, which prevents collision as much as possible and promotes fast access, insertion and deletion. 

* Time complexity: find, insert, and delete all in $$O(1)$$ time if we have a good hash function.   

Compare with binary search trees (BSTs), hash tables are more efficient in access (find), insert and delete, as long as we have a good hash function. 

> **same keys must map to the same hash code**.  Although not in any way related, but same keys to a lock should both open it, right? 

$$x=y\Longrightarrowf(x)=f(y)$$

$$\text{Converse is not true}.
In other words, $$f(x)=f(y)\text{, then }x\text{ may or may not}=y$$

## Deterministic property

Hash function (input and output) must be constant (stay the same).  Therefore, many programming languages require hash keys be immutable.  In Python dictionary, keys can be strings or integers, which are immutable. 

# Hash tables in Python

Python has 4 built-in hash table types: *set*, *dict*, *collections.defaultdict*, *collections.Counter*, where a set only stores keys.

Note that <span class="coding">collections.defaultdict</span> is nothing but a <span class="coding">dict</span> with an added option to specify default, so that error can be prevented if key is not found. 


<div class="code-head"><span>code</span>defaultdict.py</div>

```py
from collections import defaultdict
d = defaultdict(str) #default is 0 if key not found
d['OCI']= "other comprehensive income, an accounting category related to AFS"
d["BST"]
# Out
# ''
```