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
- [Similarity 1: unpacking](#similarity-1-unpacking)
  - [When defining a function](#when-defining-a-function)
    - [Positional arguments](#positional-arguments)
- [Similarity 2: any number of arguments](#similarity-2-any-number-of-arguments)
- [One *](#one-)
- [Two **](#two-)
The general idea of entering arguments to a Python function is similar to SAS macro variable for SAS functions, although the details are different. 

The SAS the macro language can be confusing. 

Whereas in Python, things can be confusing in a different sense.  So I will begin with what is similar to SAS, and then explains a more complete picture. 

# Similarity 1: unpacking
In Python, the * and ** can be used in two different context of a function:
1. when defining a function inputs
2. when calling the function

## When defining a function

In Python, 
**\***: mean that the argument can be any length of positional arguments (represented by <span class="coding">*arg</span>) and keyword arguments (represented by **).  
**\***: mean that the argument can be any length of keyword arguments (represented by <span class="coding">*arg</span>) and keyword arguments (represented by **).  

### Positional arguments

Positional arguments are explanatory.  For a refresher in SAS, here is an example from Russ Tyndall's [SAS Blog](https://blogs.sas.com/content/sgf/2017/06/16/using-parameters-within-macro-facility/).  
<div class="code-head"><span>code</span>positional argument.sas</div> 

```sas
%macro test(var1,var2,var3);                                                                                                            
 %put &=var1;                                                                                                                           
 %put &=var2;                                                                                                                           
 %put &=var3;                                                                                                                           
%mend test;                                                                                                                             
 
/** Each value corresponds to the position of each variable in the definition. **/ 
/** Here, I am passing numeric values.                                         **/                                                            
%test(1,2,3)                                                                                                                            
/** The first position matches with var1 and is given a null value.            **/                                                             
%test(,2,3)                                                                                                                             
/** I pass no values, so var1-var3 are created with null values.               **/                                                             
%test()                                                                                                                                 
/** The first value contains a comma, so I use %STR to mask the comma.         **/                                                             
/** Otherwise, I would receive an error similar to this: ERROR: More           **/
/** positional parameters found than defined.                                  **/                                                             
%test(%str(1,1.1),2,3)                                                                                                                  
/** Each value corresponds to the position of each variable in the definition. **/ 
/** Here, I am passing character values.                                       **/                                                            
%test(a,b,c) 
/** I gave the first (var1) and second (var2) positions a value of             **/
/** b and c, so var3 is left with a null value.                                **/                                                             
%test(b,c)
```

For comparison, here is an example in Python.  
<div class="code-head"><span>code</span>positional argument.py</div> 

```python
def test(a,b,c):
    print('var1 =',a, 'var1 =', b,'var1 =',c)
test(1,2,3)
# var1 = 1 var1 = 2 var1 = 3
test( ,2,3)
#   File "<ipython-input-40-977619a1b726>", line 1
#     test( ,2,3)
#           ^
# SyntaxError: invalid synta
test("(1,1,1)",2,3)
# var1 = (1,1,1) var1 = 2 var1 = 3
```
# Similarity 2: any number of arguments

the name that holds the arguments is prefixed with <span class="coding">*</span>, the asterisk (not be mistakened as "asteroid"). 

When the argument is given in the format of a dictionary, <span class="coding">*</span> tells Python to use the keys in the dictionary for the function,  two <span class="coding">**</span>, tells Python to use the values in the dictionary and plug into the function.  We can think of it as if the first <span class="coding">*</span> locates the key, and then the second <span class="coding">*</span> locates the value associated with the key.


 Python | SAS
----------|---------
'keyword', i.e.use the key * | &
use the value: ** | && 

# One *

The object that holds that arguments in Python can be:
- list
- tuple
- dictionary

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