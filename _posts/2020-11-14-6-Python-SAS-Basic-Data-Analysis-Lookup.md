---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python SAS Basic Data Analysis Lookup"
description: comparing essential data analysis functions
author: Sarah Chen
image: images/posts/IMG-0669.JPG

---
Work in Progress.  Check back later. 


| Purpose           | SAS                                    | Python                                                       |
|:------------------|:---------------------------------------|:-------------------------------------------------------------|
| content           | PROC CONTENT                           | df.info(), df.dtypes                                         |
| summary           | PROC MEANS                             | df.describe()                                                |
|                   | PROC SUMMARY                           | df.x.describe()                                              |
|                   |                                        | df.groupby(by=’x’).sum()                                     |
|                   | PROC SQL                               | df.groupby(by=’x’).count()                                   |
|                   |                                        | df.groupby(by=’x’).quantile([0.25,0.75])                     |
|                   |                                        | df.groupby(level=’ind1’)                                     |
| missing count     | PROC MEANS N NMISS MISSING;            | df.count()                                                   |
|                   |                                        | df.isnull().sum()                                            |
|                   | PROC FREQ TABLE /MISSING;              |                                                              |
| frequency         | PROC FREQ                              | df.describe()                                                |
|                   |                                        |                                                              |
|                   | PROC SQL                               | df.value.counts()                                            |
|                   |                                        | pd.crosstab(df.A, df.B).apply(lambda x: x/x.sum(), axis = 1) |
| distribution      | PROC UNIVARIATE                        | df.describe(include=[np.number])                             |
| drop/keep columns | DATA df (drop = col_name);             | df.drop(['x1', 'x2', 'x3'], axis = 1                         |
|                   |                                        |                                                              |
|                   | DATA df (keep = col_name);             | df.loc[:, ['x1', 'x2'])                                      |
| rename            | DATA df (RENAME = (old=new col_name)); | df.columns = ['name1', 'name2', 'name3']                     |
| sort              | PROC SORT; BY x1 DESCENDING x2;        | df.sort(['x1', 'x2'], ascending = [True, False])             |
| binning           | PROC RANK;                             | pd.cut(x, [min, cut1, …, cutk, max])                         |
|                   |                                        |                                                              |
|                   |                                        | np.digitize(x, [cut1, cut2, …, cutk])                        |
|                   |                                        |                                                              |
|                   |                                        | pd.qcut(df.x, n, labels=False)                               |
| bapping/          | DATA df;                               | df.x.replace(zip(old, new))                                  |
| replace value     | IF THEN;                               |                                                              |
| combine datasets  | DATA + MERGE;                          | pd.merge(df1, df2, how=’left’,on=’x’)                        |
|                   | PROC SQL;                              |                                                              |
| filter join       | DATA + in;                             | df1[df1.x.isin(df2.x)]                                       |
|                   | PROC SQL                               | df1[~df1.x.isin(df2.x)]                                      |
