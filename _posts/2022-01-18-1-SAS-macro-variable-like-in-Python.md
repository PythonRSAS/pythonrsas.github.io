---
layout: post
tag : * function arguments and SAS macro variables
category: "Python for SAS"
title: "SAS macro variable like in Python"
description: drawing analogies between Python function arguments and SAS macro variables
author: Sarah Chen
image: images/posts/photos/IMG-0683.jpg

---
![](/images/posts/photos/IMG-0683.jpg)

Python functions are a lot like SAS macros.  What is the analogy to SAS macro variable in Python?
- [1. When defining a function](#1-when-defining-a-function)
  - [Positional arguments](#positional-arguments)
    - [fixed number of positional arguments](#fixed-number-of-positional-arguments)
    - [Unlimited positional arguments](#unlimited-positional-arguments)
    - [Keyword arguments](#keyword-arguments)
- [2. When calling a function](#2-when-calling-a-function)
- [3. Scan or loop through](#3-scan-or-loop-through)
- [Summary](#summary)
- [Appendix: SAS macro review](#appendix-sas-macro-review)

The general idea of entering arguments to a Python function is similar to SAS macro variable for SAS functions, although the details are different. 
We see "args" and "kwargs" a lot in Python code.  They are naming convention representing <span class="coding">*</span> and <span class="coding">**</span> bring us: 
- positional arguments, and 
- keyword arguments.  
 
 In Python, the *, the asterisk (not be mistakened as "asteroid") and ** can be used in two different context of a function:
1. when defining a function inputs
2. when calling the function
   
When they are used in defining functions, they allow us to use unlimited number of arguments of their respective type.

When used in calling a function, they allow unpacking an iterable (list, tuple, or dictionary).  When used with a dictionary, * represents the key, whereas ** represents the value. 
   
# 1. When defining a function

In Python, 
**\***: mean that the argument can be any length of positional arguments (conventionally written as
*arg).

\**: means that the argument can be any length of keyword arguments (conventionally epresented by <span class="coding">**arg</span>.

## Positional arguments
### fixed number of positional arguments

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

For comparison, here is an example in Python. Except the null value case that raises an error instead of being ignored, Python results are similar to SAS. 
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
The above comparisons were done using a fixed number of arguments. 
### Unlimited positional arguments
For unlimited number of positional arguments, in Python we just add <span class="coding">*</span>. 
<div class="code-head"><span>code</span>unlimited positional argument.py</div> 

```python

def test2(*args
    for n, i in enumerate(args):
        print('var%d='%n,i)
test2(1,2,3,4,5,6)
# var0= 1
# var1= 2
# var2= 3
# var3= 4
# var4= 5
# var5= 6
```
In comparison, for unlimited positional arguments in SAS, the <span class="coding">PARMBUFF</span> option creates a macro variable called <span class="coding">&SYSPBUFF</span> that contains the entire list of parameter values.  This let us pass in a varying number of parameter values. 

Some practical examples are many of the functions in matplotlib.  
```python
plt.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
```
Here, the <span class="coding">* </span> and <span class="coding">**fig_kw </span> allow us to give unlimited positional and keyword arguments, for example, like this one, where <span class="coding">dict()</span> converts an assignment statement into a dictionary.  Using <span class="coding">dict()</span> is easier than typing {}. 
```python
# as in ax.annotate()
textprops=dict(color="w")
# plotting style as in plt.plot()
style = dict(color='k', alpha=0.6)

sns.boxplot(x=tips["total_bill"],
                medianprops={'color':'white'},
                boxprops = dict(linestyle='--', linewidth=3, color='darkgoldenrod'))

```

### Keyword arguments
They are defined with an "=" sign.  This is common in both Python and SAS. 

# 2. When calling a function
> Can only supply it with exactly the same number of parameters as in function, and the same type

I think this is unique to Python. And it can be confusing without an example. 

<div class="code-head"><span>code</span>calling function.py</div> 

```python
def test3(a,b):
    print(a,b)
test3(1,2)
# 1 2

test3(*{'a':1,'b':2})
# a b

test3(**{'a':1,'b':2})
# 1 2
```
When the argument is given in the format of a dictionary, <span class="coding">*</span> tells Python to use the keys in the dictionary for the function,  two <span class="coding">**</span>, tells Python to use the values in the dictionary and plug into the function.  We can think of it as if the first <span class="coding">*</span> locates the key, and then the second <span class="coding">*</span> locates the value associated with the key.

 Python | SAS
----------|---------
'keyword', i.e.use the key * | &
use the value: ** | && 

The object that holds that arguments in Python can be any iterable: list, tuple, and dictionary.

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

In SAS the <span class="coding">&&</span> is used on composite macro variable.

Whereas in Python, the <span class="coding">**</span> means the values associated with the keys.  

In a sense it is like in SAS where it is kind of like composite function in math g(f(x)), you plug in f(x) first and then get g(x)).  The first <span class="coding">*</span> gets the keys, 
and the second <span class="coding">**</span> use the keys to get the values. 

# 3. Scan or loop through
Of course, in SAS, we can also use the <span class="coding">%scan</span> method to process an unlimited number of parameters that are held by one macro variables. 
<div class="code-head"><span>code</span>macro to transform time series.sas</div> 

```sas
%macro ts_transform(dsn);
%do i =2 to &n;
%let var = %scan(%quote(%var_list), &i, " ");
%put &var;
PROC EXPAND DATA = &dsn OUT = transformed METHOD= NONE;
D date;
CONVERT &var. = &var._ma4/TRANSOUT = (MOVAVE 4);  #moving average
CONVERT &var. = &var._cma4/TRANSOUT = (CMOVAVE 4); #center moving average
CONVERT &var. = &var._wma4/TRANSOUT = (MOVAVE 1 2 3 4); #weighted moving average
CONVERT &var. = &var._log/TRANSOUT = (LOG);
CONVERT &var. = &var._1/TRANSOUT = (LAG);
CONVERT &var. = &var._2/TRANSOUT = (LAG, 2);
CONVERT &var. = &var._3/TRANSOUT = (LAG, 3);
CONVERT &var. = &var.1_/TRANSOUT = (LEAD);
CONVERT &var. = &var.2_/TRANSOUT = (LEAD, 2);
CONVERT &var. = &var.3_/TRANSOUT = (LEAD, 3);
RUN;

DATA transformed;
SET transformed;
&var._yoy = DIF4(&var)/&var._4*100;
&var._yoy1 = LAG1(&var._yoy);
&var._qoq = DIF1(&var)/&var._1*100;
&var._qoq1 = LAG1(&var._qoq);
&var._myoy = DIF4(&var._ma4)/&var._ma4*100;
%END;
%MEND;

PROC SQL;
SELECT NAME INTO: v_lt SEPARATED BY " "
FROM DICTIONARY.COLUMNS
WHERE LIBNAME = LOWCASE("sc") AND MEMNAME =  LOWCASE("my_data") AND LOWCASE(NAME) NOT LIKE "%date";
QUIT;
%PUT &v_lt;
PROC SQL;
SELECT NVAR INTO: n 
FROM DICTIONARY.TABLES
WHERE LIBNAME = LOWCASE("sc") AND MEMNAME =  LOWCASE("my_data");
QUIT;
/* run the macro */
%ts_transform(SC.my_data);
```
In Python similar logic that are commonly used.  For example,
```python
countries = ['usa','china',...,'moon']
def country_func(some_list):
    for i in some_list:
        ...
```
# Summary
We see "args" and "kwargs" a lot in Python code.  They are naming convention representing <span class="coding">*</span> and <span class="coding">**</span> bring us: 
- positional arguments, and 
- keyword arguments.  
 
When they are used in defining functions, they allow us to use unlimited number of arguments of their respective type.

When used in calling a function, they allow unpacking an iterable (list, tuple, or dictionary).  When used with a dictionary, * represents the key, whereas ** represents the value. 

# Appendix: SAS macro review
Lastly, the two common ways of using macro variable that holds a flexible number of inputs in SAS is to use 
1. <span class="coding">DATA _NULL_</span> 
2. <span class="coding">PROC SQL</span>
After creating the list, we loop through the list to process operations, and this is often accomplished using a combination of the <span class="coding">%scan</span> function and the <span class="coding">%DO</span>
statements.  

<span class="coding">%scan</span>, and in various combination with <span class="coding">PROC SQL</span>, <span class="coding">INTO</span>, <span class="coding">CALL SYMPUT</span>, <span class="coding">%DO</span>,<span class="coding">&&VAR&I</span> type of syntax. 

The following are from Arthur L. Carpenter [Storing and Using a List of Values in a Macro Variable](https://support.sas.com/resources/papers/proceedings/proceedings/sugi30/028-30.pdf).  To build a macro list:
1. <span class="coding">DATA _NULL_</span>: the character variable <span class="coding"> ALLVAR</span> is used to accumulate the list of variable names, and it is only after all the values are stored in ALLVAR is the macro variable (<span class="coding">&VARLIST</span>) created.

In the example, the list comes from meta data "metaclass" extracted using <span class="coding">PROC CONTENTS</span>. 
<div class="code-head"><span>code</span>macro list using data _null_.sas</div> 

```sas
proc contents data=sashelp.class noprint out=metaclass;
 run;

data _null_;
 length allvars $1000;
 retain allvars ' ';
 set metaclass end=eof;
 allvars = trim(left(allvars))||' '||left(name);
 if eof then call symput('varlist', allvars);
 run;
%put &varlist;
```
2. <span class="coding">PROC SQL</span>.  In this example, we are extracting each kind of the meta data information into a separate macro variable, each holding its respective list of information: name, type and length. 

<div class="code-head"><span>code</span>macro list using proc sql.sas</div> 

```sas
proc sql noprint;
 select name ,type, length
 into :varlist separated by ' ',
 :typlist separated by ' ',
 :lenlist separated by ' '
 from metaclass;
 quit;
%let cntlist = &sqlobs;
%put &varlist;
%put &typlist;
%put &lenlist;
%put &cntlist;
```
