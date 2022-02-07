---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "Reusable Code - Python class"
description: discuss ways to make reusable code in Python and SAS, specifically on Python class
author: Sarah Chen
image: images/posts/photos/IMG-0667.JPG

---
![](images/posts/photos/IMG-0687.JPG)
I often hear some people saying that the reason why we need to switch from SAS to Python is because only in Python we can write reusable code.  That is totally wrong!  You can and should write reusable code in just about any language.  People switch to SAS for other reasons, expenses being one of them. 

In SAS, besides the numerous PROCs (procedures) that are reusable, writing macros (or macro functions) is the de facto method. 

The analogy to SAS macro in Python is functions.  Both SAS macros and Python function take inputs, do something with them, and then either exit after job is done, or return something. 

The real difference, in my opinion, between the two languages from the reusable code perspective is the Python class object.  

If we stay at the function level (the <span class="coding">def</span> level), there is not a whole lot different between SAS and Python.  What you write with a Python <span class="coding">def</span> I can pretty much accomplish the same using a SAS macro. 

# jargons

* **attribute** for any name following a dot. Such as df.shape.   Attributes may be read-only or writable.  This is not available in SAS. 
* **namespace** is a mapping from names to objects.  SAS has namespace too, even though it may have a different name. 

Examples: 
1. the set of built-in names (including functions, and built-in exception names)
2. the global names in a module; and the local names in a function invocation
3. the set of attributes of an object. 

Note that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function <span class="coding">deepnn<span>  — we must prefix it with its module name.
* **scope** of namespace: 
As in SAS, we have global, local and built-in in Python.  At run time, the order that a name is accessed has the following hierchy: 
1. local, if not found, then search the one that it inherits from
2. any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
3. module's global names
4. the outermost scope (searched last) is the namespace containing built-in names

Furthermore, the order Python looks for names at run time: local -> lib (typical vanilla installation modules are in lib) -> site packages (3rd party packages are generally in site-packages).  

# a class in Python
A class is a class,literally.  It is a group of things and things associated with that group of things. Using jargon, a class groups objects such as attributes and functions/methods that belong together. ["Classes provide a means of bundling data and functionality together."](https://docs.python.org/3/tutorial/classes.html)  The closest thing from SAS to Python class is a SAS procedure specifically those that do very specific things.  For example, PROC LOGISTIC, which contains almost all the reusable code that one needs for doing logistic regression in a statical-focused context. 

Only in a Python class did I see clearly that the thinking process is different from SAS.  The design of a class is the essence of object programming and the essence of what makes Python thought process different from SAS.   It is when writing a class that I finally say to myself "Aha, that's something that SAS does not provide, at least not in open scene, and that's kind of new to me!" 

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

We may turn some of the routine data analysis code into class.
<div class="code-head"><span>code</span>data analysis.py</div> 

```python
class DataDescription(object):
    def __init__(self, data):
        self.data = data
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
#  2   sex         244 non-null    category
#  3   smoker      244 non-null    category
#  4   day         244 non-null    category
#  5   time        244 non-null    category
#  6   size        244 non-null    int64
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.4 KB
# None

# dtypes are:
#  total_bill     float64
# tip            float64
# sex           category
# smoker        category
# day           category
# time          category
# size             int64
# dtype: object

# column names are:
#  ['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size']
a.descriptive()
#         total_bill   tip   sex smoker  day    time  size
# count        244.0 244.0   244    244  244     244 244.0
# unique         NaN   NaN     2      2    4       2   NaN
# top            NaN   NaN  Male     No  Sat  Dinner   NaN
# freq           NaN   NaN   157    151   87     176   NaN
# ...
#         total_bill   tip   sex smoker  day    time  size
# count        244.0 244.0   244    244  244     244 244.0
# unique         NaN   NaN     2      2    4       2   NaN
# top            NaN   NaN  Male     No  Sat  Dinner   NaN
# freq           NaN   NaN   157    151   87     176   NaN
# mean        19.786 2.998   NaN    NaN  NaN     NaN  2.57
# std          8.902 1.384   NaN    NaN  NaN     NaN 0.951
# ...
# 75%         24.127 3.562   NaN    NaN  NaN     NaN   3.0
# max          50.81  10.0   NaN    NaN  NaN     NaN   6.0
# missing          0     0     0      0    0       0     0
a.data_content()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   total_bill  244 non-null    float64
# ...

# dtypes are:
# total_bill     float64
# tip            float64
# sex           category
```

# step by step examples
The following are my notes from watching [Corey Shafer](https://www.youtube.com/watch?v=ZDa-Z5JzLYM&t=7s).  

## version 0
Nothing is defined for the class Employee.  It is still a valid class.  

The purpose of this example is about the point of **reusable code**.   

Notice that we can define various attributes anyway we want: we can perfectly define .first, .last, .pay, and .X, .Y, .Z, and write a program that does something.  But this will **not be reusable**. 

<div class="code-head"><span>code</span>Employee version 0.python</div>

```python
class Employee:
    pass
# a class is a blueprint for creating instances
emp_1 = Employee()
emp_1.first = 'sarah'
emp_1.last = 'chen'
emp_1.pay = 500000 # I would like to make this much 
In [3]: emp_1
Out[3]: <__main__.Employee at 0x1698e004588>

In [4]: emp_1.first
Out[4]: 'sarah'

In [5]: emp_1.raise_amount = 1.05

In [6]:  myRaise = emp_1.pay*(emp_1.raise_amount-1)^M
   ...: myRaise
   ...:
Out[6]: 25000.000000000022
```
## version 1

<div class="code-head"><span>code</span>Employee version 1.python</div>

```python
class Employee: # 第一个 input总是self。即， 一个instance. self = instance.  Can call "self" any name you want
    def __init__(self, first, last, pay): # 类似其他语言的constructor # can call "self" or anything we want.  'self' is because of convention
        self.first = first  # could have written self.fname = first, or self.fn = first, but it is easier to keep track of if keep the same names
        self.last = last
        self.email = first + '.' + last +'@company.com'

emp_1 = Employee('sarah', 'chen', 500000)
#  这麻烦得很。每次要type这么多
print(emp_1.email)
print('{} {}'.format(emp_1.first, emp_1.last))
# 所以，我门给它个method
sarah.chen@company.com
sarah chen
```
## version 2

<div class="code-head"><span>code</span>Employee version 2.python</div>

```python
class Employee:
    def __init__(self, first, last, pay): # 类似其他语言的constructor # can call "self" or anything we want.  'self' is because of convention
        self.first = first  # could have written self.fname = first, or self.fn = first, but it is easier to keep track of if keep the same names
        self.last = last
        self.email = first + '.' + last +'@company.com'
    def fullname(self):
        # return ('{} {}'.format(emp_1.first, emp_1.last))
        return ('{} {}'.format(self.first, self.last))
# 现在
print(emp_1.fullname()) # 注意fullname 是method，不是attribute，所以必须加括号
```
<div class="code-head"><span>code</span>dir.python</div>

```python
In [11]: dir(Employee)
Out[11]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'fullname']
 ```

## version 3

<div class="code-head"><span>code</span>Employee version 3.python</div>

```python
 
# version 3
class Employee:
    def __init__(self, first, last, pay): # 类似其他语言的constructor # can call "self" or anything we want.  'self' is because of convention
        self.first = first  # could have written self.fname = first, or self.fn = first, but it is easier to keep track of if keep the same names
        self.last = last
        self.email = first + '.' + last +'@company.com'
        self.pay = pay
    def fullname(self):
        # return ('{} {}'.format(emp_1.first, emp_1.last))
        return ('{} {}'.format(self.first, self.last))
    def apply_raise(self):
        self.pay = int(self.pay* 1.04)
emp_1 = Employee('sarah', 'chen', 500000)
emp_1.apply_raise()
print(emp_1.pay) 
```
## version 4

<div class="code-head"><span>code</span>Employee version 3.python</div>

```python
# 现在我们想把raise percent 作为一个 class variable
# version 4 method 用 class variable 以 self. 的形式， 而非 className. 的形式
class Employee:
    raise_amount = 1.04 # raise percent 作为一个 class variable
    def __init__(self, first, last, pay): # 类似其他语言的constructor # can call "self" or anything we want.  'self' is because of convention
        self.first = first  # could have written self.fname = first, or self.fn = first, but it is easier to keep track of if keep the same names
        self.last = last
        self.email = first + '.' + last +'@company.com'
        self.pay = pay
    def fullname(self):
        # return ('{} {}'.format(emp_1.first, emp_1.last))
        return ('{} {}'.format(self.first, self.last))
    def apply_raise(self):
        self.pay = int(self.pay* self.raise_amount)  # ！！！ 必须用 self.raise_amount 或 Employee.raise_amount 
emp_1 = Employee('sarah', 'chen', 500000)
emp_2 = Employee('sam', 'Poola', 500000)

print(emp_1.__dict__)
# In [25]: print(emp_1.__dict__)
# {'first': 'sarah', 'last': 'chen', 'email': 'sarah.chen@company.com', 'pay': 500000}
emp_1.raise_amount = 1.10
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 1.04
# 1.1  # !!! 注意！！！
# 1.04  emp_2 还是class 的raise_amount
```


One of the most intuitive way writings about how a class roughly works is the "Python for Kids" book I read years ago but still review from time to time. 
<figure>
  <img src="{{ "/images/posts/classes_cats1.PNG" | relative_url }}">
  <figcaption> classes</figcaption>
</figure>

# reuse code
If we have code (either we wrote somewhere or we copied) that we use again and again, let us keep it in a separate piece of code (Calling it a piece of code is a genearal way of saying it, which may have other names such as "module", "function", or "macro" in SAS).  Try not to copy and paste even if "Ctrl C" and "Ctrl V" may be our favorite technology. Copying and pasting code all over the place can make our code much longer (and dreadful sometimes) than needed, and messy. 

**Python** - 2 ways depending on which enviroment I am using.  I often use both Jupyter Notebook and the command line simultaneously. 
- <span class="coding">%run</span> magic command in Jupyter Notebook.  E.g. <span class="coding">%run C:/.../myCode.py</span>
- <span class="coding">python C:/.../myCode.py</span> in command prompt. 

<div class="note"><p>
<b>Note</b>: Imported libraries are cached.  So you import an updated version of the library, it will still be the old one showing up, unless you start a new session.
</p></div>

<div class="note"><p>
<b>Note</b>: NEVER NEVER <span class="coding">from libraryName import *</span> It can cause name clashes and all kinds of mysterious bad stuff.
</p></div>

**SAS**  

Import and run a piece of external code in SAS is easy.  Say we have a few lines of code contained in "step0_libnames_options.sas" that specifies options, directories and a few macro variables for our project.  We can call it to task by using the <span class="coding">%include </span> statement.

<div class="code-head"><span>code</span>step0_libnames_options.sas</div>

```sas
options mprint mlogic symbolgen compress=binary;
options varlidvarname=any;
libname newdata "c:\users\sc\newdata";
%let outpath = A:\sc\output;
```
There are many ways to use the <span class="coding">%include </span> statement. Below is a simple example.  Remember that what we are calling needs to be in quotes. 
<div class="code-head"><span>code</span>import external code.sas</div>

```sas
%let code_dir = "c:\users\sc\code";
%include "&code_dir.\step0_libnames_options.sas";
```
