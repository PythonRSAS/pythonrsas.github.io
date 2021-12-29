---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "SAS macro variable like in Python"
description: drawing analogies between Python and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0683.JPG

---
We have a lot of code in SAS at work.  I often need to work in Python, R and SAS all together between projects in the same day. 


## SAS Macro variable like in Python
There are three ways to enter arguments to a Python function, which are similar to SAS macro variable for SAS functions. 

In SAS, a macro variable is prefixed with <span class="coding">&</span>. Whereas in Python, the name that holds the arguments is prefixed with <span class="coding">*</span>. 

The object that holds that arguments can be:
- list
- tuple
- dictionary
With one *, we tell Python to use the keys in the dictionary for the function. 
If we supply two **, it tells Python to use the values in the dictionary and plug into the function.   

<div class="code-head"><span>code</span>arguments.py</div>

```py
>>> # 3 ways to enter argument (like SAS macrovariable)
>>> def sas(x,y,z):
>>>     print("x=" + str(x))
>>>     print("y=" + str(y))
>>>     print("z=" + str(z))
>>> # Method: List
>>> mylist = [1,2,3]
>>> sas(*mylist)
x=1
y=2
z=3
>>> #### Method: tuple
>>> myTuple = (1,2,3)
>>> sas(*myTuple)
```
# Method: dictionary
Two **

mydict = {'x':1,'y':2,'z':3}
sas(**mydict)
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
