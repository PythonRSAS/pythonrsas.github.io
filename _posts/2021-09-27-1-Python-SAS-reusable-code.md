---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python SAS Reusable Code"
description: discuss ways to make reusable code in Python and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0667.JPG

---
We often hear some people saying that the reason why we need to switch from SAS to Python is because only in Python we can write reusable code.  That is totally wrong!  You can and should write reusable code in just about any language.

In SAS, besides the numerous PROCs (procedures) that are by definition reusable, writing macros (or macro functions) is the defacto method. 

The analogy to SAS macro in Python is functions.  Both SAS macros and Python function take inputs, do something with them, and then either exit after job is done, or return something. 

The real difference, in my opinion, between the two languages from the reusable code perspective is the Python class object.  

If we stay at the function level (the <span class="coding">def</span> level), there is not a whole lot different between SAS and Python.  What you write with a Python <span class="coding">def</span> I can pretty much accomplish the same using a SAS macro. 

# a class in Python
A class is indeed a class, please do take it literally.  A class is a group of things and things associated with that group of things. Classes are groupings of attributes and functions/methods that belong together.  Looking at it this way, then the closest thing from SAS is a SAS procedure specifically those that do very specific things.  For example, PROC LOGISTIC, which contains almost all the reusable code that one needs for doing logistic regression in a statical-focused context. 

Only in a Python class we see clearly that the thinking process is different from SAS.  The design of a class is the essense of object programming and the essense of what makes Python thought process different from SAS.   It is when writing a class that I finally say to myself "Aha, that's something that SAS does not provide, at lease not in open scene, and that's kind of new to me!" 


The most intuitive way for me to remember (or visualize) how class roughly works is what I read from the "Python for Kids" book. 
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


<div class="code-head"><span>code</span>import libraries.py</div>

```python
import pandas as pd
```

<div class="code-head"><span>code</span>import libraries.r</div>

```r
install.packages('data.table') #data.table has no dependencies
library(data.table)

install.packages('feather')
library(feather)

install.packages('zoo', dependencies = TRUE)
library(zoo)
```

To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
library(cluster)
set.seed(1)
isGoodCol <- function(col){
  sum(is.na(col)) == 0 && is.numeric(col)
}
goodCols <- sapply(nba, isGoodCol)
clusters <- kmeans(nba[,goodCols], centers=5)
labels <- clusters$cluster
# plotting
nba2d <- prcomp(nba[,goodCols], center=TRUE)
twoColumns <- nba2d$x[,1:2]
clusplot(twoColumns, labels)
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```