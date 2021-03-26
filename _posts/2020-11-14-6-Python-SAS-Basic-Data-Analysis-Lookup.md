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


|    | Purpose           | SAS                                    | Python                                                       |
|---:|:------------------|:---------------------------------------|:-------------------------------------------------------------|
|  0 | content           | PROC CONTENT                           | df.info(), df.dtypes                                         |
|  1 | summary           | PROC MEANS                             | df.describe()                                                |
|  2 |                   | PROC SUMMARY                           | df.x.describe()                                              |
|  3 |                   |                                        | df.groupby(by=’x’).sum()                                     |
|  7 |                   | PROC SQL                               | df.groupby(by=’x’).count()                                   |
|  8 |                   |                                        | df.groupby(by=’x’).quantile([0.25,0.75])                     |
|  9 |                   |                                        | df.groupby(level=’ind1’)                                     |
| 10 | missing count     | PROC MEANS N NMISS MISSING;            | df.count()                                                   |
| 11 |                   |                                        | df.isnull().sum()                                            |
| 12 |                   | PROC FREQ TABLE /MISSING;              |                                                              |
| 13 | frequency         | PROC FREQ                              | df.describe()                                                |
| 14 |                   |                                        |                                                              |
| 15 |                   | PROC SQL                               | df.value.counts()                                            |
| 17 |                   |                                        | pd.crosstab(df.A, df.B).apply(lambda x: x/x.sum(), axis = 1) |
| 18 | distribution      | PROC UNIVARIATE                        | df.describe(include=[np.number])                             |
| 19 | drop/keep columns | DATA df (drop = col_name);             | df.drop(['x1', 'x2', 'x3'], axis = 1                         |
| 20 |                   |                                        |                                                              |
| 21 |                   | DATA df (keep = col_name);             | df.loc[:, ['x1', 'x2'])                                      |
| 22 | rename            | DATA df (RENAME = (old=new col_name)); | df.columns = ['name1', 'name2', 'name3']                     |
| 23 | sort              | PROC SORT; BY x1 DESCENDING x2;        | df.sort(['x1', 'x2'], ascending = [True, False])             |
| 24 | binning           | PROC RANK;                             | pd.cut(x, [min, cut1, …, cutk, max])                         |
| 25 |                   |                                        |                                                              |
| 26 |                   |                                        | np.digitize(x, [cut1, cut2, …, cutk])                        |
| 27 |                   |                                        |                                                              |
| 28 |                   |                                        | pd.qcut(df.x, n, labels=False)                               |
| 29 | bapping/          | DATA df;                               | df.x.replace(zip(old, new))                                  |
| 30 | replace value     | IF THEN;                               |                                                              |
| 33 | combine datasets  | DATA + MERGE;                          | pd.merge(df1, df2, how=’left’,on=’x’)                        |
| 34 |                   | PROC SQL;                              |                                                              |
| 36 | filter join       | DATA + in;                             | df1[df1.x.isin(df2.x)]                                       |
| 37 |                   | PROC SQL                               | df1[~df1.x.isin(df2.x)]                                      |
