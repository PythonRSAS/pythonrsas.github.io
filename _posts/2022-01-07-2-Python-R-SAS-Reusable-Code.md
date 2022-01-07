---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Reusable Code"
description: reusable code in Python, R and SAS 
author: Sarah Chen
image: images/posts/IMG-0681.JPG

---
Work in Progress.  Check back later. 

# Custom Snippets
Using custom snippets helps save time.  Using 3 languages we have a lot of syntax and libraries to remember.  
[how to add a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets).
> `shift + command + p` and type snippets => Select `Preferences`: Open User Snippets 
[snippet generator](https://snippet-generator.app/)

# Run external code
If we have code that we use again and again, let us keep it in a separate piece of code (Calling it a piece of code is a genearal way of saying it, which may have other names such as "module", "function", or "macro" in SAS).  Try not to copy and paste even if "Ctrl C" and "Ctrl V" may be our favorite technology. Copying and pasting code all over the place can make our code much longer (and dreadful sometimes) than needed, and messy. 

**Python** - 2 ways depending on which enviroment I am using.  I often use both Jupyter Notebook and the command line simultaneously. 
- <span class="coding">%run</span> magic command in Jupyter Notebook.  E.g. <span class="coding">%run C:/.../myCode.py</span>
- <span class="coding">python C:/.../myCode.py</span> in command prompt. 

<div class="note"><p>
<b>Note</b>: Imported libraries are cached.  So you import an updated version of the library, it will still be the old one showing up, unless you start a new session.
</p></div>

<div class="note"><p>
<b>Note</b>: NEVER <span class="coding">from libraryName import *</span> It can cause name clashes and all kinds of mysterious bad stuff.
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
