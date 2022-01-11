---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Data Analysis Lookup"
description: comparing Python, R and SAS essential data analysis functions
author: Sarah Chen
image: images/posts/photos/IMG-0682.jpg

---
Work in Progress.  

![](images/posts/photos/IMG-0682.jpg)
- [summary](#summary)
- [Custom Snippets](#custom-snippets)
- [Run external code](#run-external-code)
# summary

| Purpose               | SAS                                                                          | Python                                                       | R                                    |
| :-------------------- | :--------------------------------------------------------------------------- | :----------------------------------------------------------- | :----------------------------------- |
| **input**             | PROC IMPORT DATAFILE = " " OUT=df DBMS=CSV REPLACE; GUESSINGROWS=10000; RUN; | pd.read_csv("") # encoding=”cp1252”,encoding=”ISO-8859-1”    | read.table(file, as.is=TRUE)         |
|                       |                                                                              | pd.read_sas("",encoding=”latin-1” )                          | read.csv("", header=TRUE)            |
|                       |                                                                              |                                                              | load() # load data written with save |
| **output**            | PROC EXPORT DATA= df OUTFILE= ""  DBMS=csv REPLACE; RUN;                     | df.to_csv(index=False)                                       | save()                               |
| **content**           | proc contents data = df                                                      | array.ndim, .shape, .size, .dtype, .itemsize, .nbytes        | str(df)                              |
|                       | out = dsList (keep=memname memlabel name label nobs varnum) noprint;run;     |                                                              |                                      |
|                       |                                                                              | df.info(), df.dtypes                                         |                                      |
| **summary**           | PROC MEANS DATA=df NWAY; CLASS species; VAR x1-x6; RUN;                      | df.describe()                                                | summary(dt)                          |
|                       | PROC SUMMARY                                                                 | df.x.describe()                                              |                                      |
|                       | PROC SQL                                                                     | pd.pivot_table()                                             |                                      |
|                       |                                                                              | df.groupby(by=’x’).sum()                                     |                                      |
|                       |                                                                              | df.groupby(by=’x’).count()                                   |                                      |
|                       |                                                                              | df.groupby(by=’x’).quantile([0.25,0.75])                     |                                      |
|                       |                                                                              | df.groupby(level=’ind1’)                                     |                                      |
| **missing count**     | PROC MEANS N NMISS MISSING;                                                  | df.count()                                                   |                                      |
|                       |                                                                              | df.isnull().sum()                                            |                                      |
|                       | PROC FREQ; TABLE /MISSING;                                                    |                                                              |                                      |
| **frequency**         | PROC FREQ;TABLE value;                                                      | df.describe()                                                |                                      |
|                       |                                                                              | df.value.counts            ()                                            |         |PROC SQL; SELECT COUNT(X) AS CT GROUPBY value; 
|                       |                                                                              | pd.crosstab(df.A, df.B).apply(lambda x: x/x.sum(), axis = 1) |                                      |
| **distribution**      | PROC UNIVARIATE                                                              | df.describe(include=[np.number])                             |                                      |
| **drop/keep columns** | DATA df (drop = col_name);                                                   | df.drop(['x1', 'x2', 'x3'], axis = 1                         |                                      |
|                       | DATA df (keep = col_name);                                                   | df.loc[:, ['x1', 'x2'])                                      |                                      |
| **rename**            | DATA df (RENAME = (old=new col_name));                                       | df.columns = ['name1', 'name2', 'name3']                     |                                      |
| **sort**              | PROC SORT; BY x1 DESCENDING x2;                                              | df.sort(['x1', 'x2'], ascending = [True, False])             |                                      |
| **binning**           | PROC RANK;                                                                   | pd.cut(x, [min, cut1, …, cutk, max])                         |                                      |
|                       |                                                                              | np.digitize(x, [cut1, cut2, …, cutk])                        |                                      |
|                       |                                                                              | pd.qcut(df.x, n, labels=False)                               |                                      |
| **replace value**     | IF THEN;                                                                     | df.x.replace(zip(old,new))                                   |                                      |
| **combine datasets**  | DATA + MERGE;                                                                | pd.merge(df1, df2, how=’left’,on=’x’)                        |                                      |
|                       | PROC SQL;                                                                    |                                                              |                                      |
| **filter join**       | DATA + in;                                                                   | df1[df1.x.isin(df2.x)]                                       |                                      |
|                       | PROC SQL                                                                     | df1[~df1.x.isin(df2.x)]                                      |                                      |
| **get help**          |                                                                              | object ?                                                     | ?object                              |
| **upgrade library**   |                                                                              | pip3 install --upgrade packageName --user                    |                                      |
| **directory**         | Filename filelist pipe "dir /b /s c:\temp\*.sas";                            | import os                                                    | dir()                                |
|                       | Data _null_; Infile filelist truncover;                                      | os.listdir("")                                               |                                      |
|                       | Input filename $100.;                                                        |                                                              |                                      |
|                       | Put filename=;Run;                                                           |                                                              |                                      |
| **working directory** |                                                                              | getcwd()                                                     | getwd()                              |
| **change directory**  |                                                                              | chdir())                                                     | setwd()                              |


# Custom Snippets
Using custom snippets helps save time.  Using 3 languages we have a lot of syntax and libraries to remember.  
[how to add a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets).
> `shift + command + p` and type snippets => Select `Preferences`: Open User Snippets 
[snippet generator](https://snippet-generator.app/)

# Run external code
If we have code that we use again and again, let us keep it in a separate piece of code (Calling it a piece of code is a genearal way of saying it, which may have other names such as "module", "function", or "macro" in SAS).  

Try not to copy and paste even if "Ctrl C" and "Ctrl V" may be our favorite technology. Why?  Because copying and pasting code all over the place can make our code much longer (and dreadful sometimes) than needed, and messy. 

**Python** - 2 ways depending on which enviroment I am using.  I often use both Jupyter Notebook and the command line simultaneously. 
- <span class="coding">%run</span> magic command in Jupyter Notebook.  E.g. <span class="coding">%run C:/.../myCode.py</span>
- <span class="coding">python C:/.../myCode.py</span> in command prompt. 

<div class="note"><p>
<b>Note</b>: Imported libraries are cached.  So you import an updated version of the library, it will still be the old one showing up, unless you start a new session.
</p></div>

<div class="note"><p>
<b>Note</b>: NEVER <span class="coding">from libraryName import *</span> It can cause name clashes and all kinds of mysterious bad stuff.
</p></div>


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


<div class="code-head"><span>code</span>import libraries.r</div>

```r
install.packages('data.table') #data.table has no dependencies
library(data.table)

install.packages('zoo', dependencies = TRUE)
library(zoo)
```
