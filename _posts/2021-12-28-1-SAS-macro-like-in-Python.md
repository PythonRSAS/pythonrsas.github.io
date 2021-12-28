---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "SAS macro like in Python"
description: drawing analogies between Python and SAS
author: Sarah Chen
image: images/posts/IMG-0669.JPG

---
We have a lot of code in SAS at work.  I often need to work in Python, R and SAS all together between projects in the same day. 

1. Keyboard shortcuts
2. Import libraries,modules, and import data 
3. Working with the basics
 
## SAS Macro variable like in Python
There are three ways to enter arguments, which are similar to SAS macro variable. 
<div class="code-head"><span>code</span>arguments.py</div>

```py
def foo(x,y,z):
    print("x=" + str(x))
    print("y=" + str(y))
    print("z=" + str(z))
# 3 ways to enter argument (like SAS macrovariable)
# Method: List
mylist = [1,2,3]
foo(*mylist)

Method: tuple
myTuple = (1,2,3)
foo(*myTuple)
# Out
# x=1
# y=2
# z=3
# Method: dictionary
Two **
If we supply two **, it tells Python to use the values in the dictionary and plug into the function.   Whereas if we supply one *, we tell Python to use the keys in the dictionary for the function. 
mydict = {'x':1,'y':2,'z':3}
foo(**mydict)
# same output as the above
One *
def sum(a,b):
    return a+b

values= (1,2)
sum(*values)
# Out 3

values = {'a':1,'b':2}
sum(*values)
#  'ab'
sum(**values)

def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }
s = sum(*values1, **values2)
# will execute as:
s = sum(1, 2, c=10, d=15)

```
