---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "SAS macro variable like in Python"
description: drawing analogies between Python function arguments and SAS macro variables
author: Sarah Chen
image: images/posts/photos/IMG-0683.jpg

---
![](/images/posts/photos/IMG-0683.jpg)
We have a lot of SAS code at work from former colleagues.  We often need to work in Python, R and SAS simultaneously between projects in the same day. 

Python functions are a lot like SAS macros.  What is the analogy to SAS macro variable in Python?

## SAS Macro variable like in Python
There are three ways to enter arguments to a Python function, which are similar to SAS macro variable for SAS functions. 

In SAS, a macro variable is prefixed with <span class="coding">&</span>, the ampersand sign. Whereas in Python, the name that holds the arguments is prefixed with <span class="coding">*</span>, the asterisk (not be mistakened as "asteroid"). 

The object that holds that arguments can be:
- list
- tuple
- dictionary

When the argument is given in the format of a dictionary, <span class="coding">*</span> tells Python to use the keys in the dictionary for the function,  two <span class="coding">**</span>, tells Python to use the values in the dictionary and plug into the function.  We can think of it as if the first <span class="coding">*</span> locates the key, and then the second <span class="coding">*</span> locates the value associated with the key. 

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

# Two **
In SAS the <span class="coding">&&</span> is used on composite macro variable.

Whereas in Python, the <span class="coding">**</span> means the values associated with the keys.  

In a sense it is like in SAS where it is kind of like composite function in math g(f(x)), you plug in f(x) first and then get g(x)).  The first <span class="coding">*</span> gets the keys, 
and the second <span class="coding">**</span> use the keys to get the values. 

The following example illustrates what we talk about. 
```py
mydict = {'x':1,'y':2,'z':3}
sas(**mydict)
# same output as the above
```

<div class="code-head"><span>code</span>arguments_mixed.py</div>

```py
In [1]: def sum(a,b):
   ...:     return a+b
   ...:

In [2]: values=[1,2]

In [3]: sum(*values)
Out[3]: 3

In [4]: values=(1,2)

In [5]: sum(*values)
Out[5]: 3

In [6]: values={'a':1,'b':2}

In [7]: sum(*values)
Out[7]: 'ab'

In [8]: sum(**values)
Out[8]: 3

In [9]: def sum(a, b, c, d):
   ...:     return a + b + c + d
   ...:

In [10]: values1 = (1, 2)
    ...: values2 = { 'c': 10, 'd': 15 }
    ...: s = sum(*values1, **values2)
    ...:

In [11]: s
Out[11]: 28

In [12]: args = (1, 2)
    ...: kwargs={ 'c': 10, 'd': 15 }
    ...: s = sum(*args, **kwargs)
    ...:
    ...:

In [13]: s
Out[13]: 28
```
The last two examples are identical,except that the names of the inputs changed from "value1" and "value2" to "args" and "kwargs", respectively. 

We see "args" and "kwargs" a lot in Python code.  Now that you know they are nothing but some naming convention representing <span class="coding">*</span> and <span class="coding">**</span> bring us: argument, and keyword arguments.  It is completely legal to use any name you want.  But just keep in mind what they commonly represent. 