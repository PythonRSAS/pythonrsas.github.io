---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "Python class"
description: What is a class and how to write and use it
author: Sarah Chen
image: images/posts/photos/IMG-0668.JPG

---
![](images/posts/photos/IMG-0668.JPG)

> Only in a Python class did I see clearly that the thinking process is different from SAS.  The design of a class is the essence of object programming and the essence of what makes Python thought process different from SAS.   It is when writing a class that I finally say to myself "Aha, that's kind of new to me!" 


- [a class in Python](#a-class-in-python)
- [def \__init__()](#def-_init_)
- [Class attributes and methods](#class-attributes-and-methods)
  - [Attributes can be defined within class or outside](#attributes-can-be-defined-within-class-or-outside)
- [Parent class and child classes](#parent-class-and-child-classes)
- [Example from modules](#example-from-modules)
  
# a class in Python
A class is a group of things and things associated with that group of things. Using jargon, a class groups objects such as attributes and functions/methods that belong together. ["Classes provide a means of bundling data and functionality together."](https://docs.python.org/3/tutorial/classes.html)  

The closest thing from SAS to Python class is a SAS procedure specifically those that do very specific things.  For example, PROC LOGISTIC, which contains almost all the reusable code that one needs for doing logistic regression in a statical-focused context. 

We may turn some of the routine data analysis code into class. For example, as shown below, we define a class for data description that has one attribute and three methods.  
The one and only attribute is the data itself, like a *parameter* to a function. This "parameter" has 3 "sub-functions".  Or from the SAS users' perspective, 3 macro functions), one for <span class="coding">PROC CONTENTS</span>, one for <span class="coding">PROC MEANS</span> and <span class="coding">PROC FREQ </span> and one for <span class="coding">PROC CORR</span> (sort of). 

<div class="code-head"><span>code</span>data analysis.py</div> 

```python
class DataDescription(object):
    def __init__(self, data): # 第一个 input总是self。即， 一个instance. self = instance.  Can call "self" any name you want
        self.data = data # 类似其他语言的constructor # can call "self" or anything we want.  'self' is because of convention
     # could have written self.values = first, or self.something = first, but it is easier to keep track of if keep the same names
    def data_content(self):
        print(self.data.info())
        print('\ndtypes are: \n', self.data.dtypes)
        print('\ncolumn names are: \n',self.data.columns.tolist())
    def cal_corr(self):
        pearson_corr = self.data.corr(method='pearson')
        spearman_corr = self.data.corr(method='spearman')
        return pearson_corr,spearman_corr
    def descriptive(self):
	    des = self.data.describe(include='all').T
        missing = self.data.isnull().sum().to_frame(name='missing')
	    des= pd.concat([des, missing], axis=1).T
        print(des)
        return des

df = sns.load_dataset('tips')
a = DataDescription(df)
a.data_content()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   total_bill  244 non-null    float64
#  1   tip         244 non-null    float64
# ...
# column names are:
#  ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
a.descriptive()
#         total_bill   tip   sex smoker  day    time  size
# count        244.0 244.0   244    244  244     244 244.0
# ...
# missing          0     0     0      0    0       0     0
a.data_content()
```

# def \__init__()

A class does not have to have an \__init__() method.  But most of the time we like to create objects initialized with a specific initial state. Therefore a class may define a special method named <span class="coding">\__init__()</span>, like this:

![class](/images/posts/class_data.PNG)

When a class defines an <span class="coding">\__init__()</span> method, class instantiation automatically invokes <span class="coding">\__init__()</span> for the newly-created class instance.

# Class attributes and methods

Attributes and methods are terms used often interchangably.  Some refer to anything following the <span class="coding">.</span> as attributes or methods. 

Although we by convention use <span class="coding">self</span> when we define class methods, we can actually call it almost anything, just like we can name variables with any name. 

## Attributes can be defined within class or outside

**Within class definition**

In example below, myClass is defined with 2 attributes: <span class="coding">i</span> and <span class="coding">telescope</span>.  

The attributes defined within class definition **cannot** be deleted using <span class="coding">del</span>.   

**After instantiating**

Outside of class definition, after instantiate an myClass object, we can also give the object new attributes, which is <span class="coding">counter</span> in the example.

The new attribute can be written, used, and deleted. After deleted, we don't find the counter attribute anymore.  They are *easy come and easy go*. 

Notice that although we can define attributes after instantiation anyway we want: .first, .last, .pay, and .X, .Y, .Z.  But this will **not be reusable** because these attributes are specific to this instance, and not to the class. 

Also notice that instead of <span class="coding">self</span>, I first use <span class="coding">martian</span> in a method called <span class="coding">f</span>, and then change it to <span class="coding">venus</span> in another method called <span class="coding">g</span>. 
<div class="code-head"><span>code</span>class attribute.py</div> 

```python
In [2]: class myClass:
   ...:     """A simple example class"""
   ...:     i = 12345
   ...:     telescope = "James Webb"
   ...:     def f(martian):
   ...:         return 'hello Mars'
   ...: 
   ...:     def g(venus):
   ...:         return 'I live on Mars'
   ...: x = myClass()
   ...: 
   ...: print(x.f())
   ...: print(x.g())
   ...:
hello Mars
I live on Mars

In [3]: print(x.i)
   ...: print(x.telescope)
   ...:
12345
James Webb

In [4]: x.counter = 1
   ...: while x.counter < 10:
   ...:     x.counter = x.counter * 2
   ...: print(x.counter)
   ...:
16

In [5]: del x.counter
   ...: print(x.counter)
   ...:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-5-6daa4215855c> in <module>()
      1 del x.counter
----> 2 print(x.counter)

AttributeError: 'myClass' object has no attribute 'counter'

In [6]: del x.f
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-a09835603615> in <module>()
----> 1 del x.f

In [7]: x.f()
Out[7]: 'hello Mars'
```

Below example compares defining attribute/method within class definition and added for an instance of a class. 

<div class="code-head"><span>code</span>class attribute2.py</div> 

```python
# 1. add attritutes for an instance of a class
class Data:
    pass

dt1 = Data()

dt1.data = [1, 2, 3]
dt1.name = "anyName"

print(dt1.data)
print(dt1.name)
print([i**2 for i in dt1.data])

# 2. attritutes defined within class
class Data:
    def __init__(self, data,name):
        self.data = data
        self.name = name
    def square(self):
        self.data = [i**2 for i in self.data]
        

dt1 = Data([1,2,3],'any name')
print(dt1.data)
print(dt1.name)
dt1.square()
print(dt1.data)
```


# Parent class and child classes
<figure>
  <img src="{{ "/images/posts/classes_cats1.PNG" | relative_url }}">
  <figcaption> classes</figcaption>
</figure>

# Example from modules

Examples:
[**turtle** library](https://docs.python.org/3/library/turtle.html):  

The [<span class="coding">RawTurtle</span> class](https://github.com/python/cpython/blob/84975146a7ce64f1d50dcec8311b7f7188a5c962/Lib/turtle.py#L2513), inherites from two parent classes, [TPen](https://github.com/python/cpython/blob/84975146a7ce64f1d50dcec8311b7f7188a5c962/Lib/turtle.py#L2022) and [TNavigator](https://github.com/python/cpython/blob/84975146a7ce64f1d50dcec8311b7f7188a5c962/Lib/turtle.py#L1511).  The TPen class has the drawing part: a drawing [Pen](https://github.com/python/cpython/blob/84975146a7ce64f1d50dcec8311b7f7188a5c962/Lib/turtle.py#L2337) with size, colors, and how to draw.  The TNavigator class groups navigation and movements: position, set X and set Y, forward, backward, degree, radius, and goto, etc. 

Even though the following snippet seems like a very elementary program written by elementary school kids (and yes it was), the module turtle is actually quite complex.   This is an example of reusable code because a child can import the module, start an instance of the class, and do those things that she normally does with drawing, using the language and a computer. 
<div class="code-head"><span>code</span>Turtle.python</div>

```python
""""
reference
# https://github.com/magicmathmandarin/Turtle/blob/master/shapes.py
# https://docs.python.org/3/library/turtle.html
""""
import turtle
v=turtle.Pen()
v.color("blue")

for i in range(0,3):
	v.forward(30)
	v.left(120)
```
[Youtube video by Corey Shafer](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=7s).  