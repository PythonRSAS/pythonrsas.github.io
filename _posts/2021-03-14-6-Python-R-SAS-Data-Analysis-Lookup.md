---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Data Analysis Lookup"
description: comparing Python, R and SAS essential data analysis functions
author: Sarah Chen
image: images/posts/IMG-0669.JPG

---
Work in Progress.  

![](/images/posts/IMG-0669.JPG)
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
|                       | PROC FREQ TABLE /MISSING;                                                    |                                                              |                                      |
| **frequency**         | PROC FREQ                                                                    | df.describe()                                                |                                      |
|                       |                                                                              | df.value.counts()                                            |                                      |
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

