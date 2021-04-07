---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Data Analysis Lookup"
description: comparing Python, R and SAS essential data analysis functions
author: Sarah Chen
image: images/posts/IMG-0669.JPG

---
Work in Progress.  Check back later. 

The first step in any analytic process is import libraries and data. 

## install libraries and data
<div class="code-head"><span>code</span>import libraries.r</div>

```r
install.packages('data.table') #data.table has no dependencies
library(data.table)

install.packages('feather')
library(feather)

install.packages('zoo', dependencies = TRUE)
library(zoo)
```

<div class="code-head"><span>code</span>input and output.r</div>

```r
read.table(file,header=TRUE) # default separator is sep=" " is any white space
read.table(file, as.is=TRUE) # as.is=TRUE prevents string values from being converted to factors
read.csv("file", ,header=TRUE) # specifically for .csv files

load() # load the dataset written with save
data(x) # loads specific dataset

read_feather(path, columns=NULL)
write_feather(x, path)

```
<div class="code-head"><span>code</span>input and output.py</div>

```python
df.mean()
```


<div class="code-head"><span>code</span>input and output.sas</div>

```sas
PROC IMPORT 
```

After having loaded the data, we can use the following to take a quick look before further processings.
<div class="code-head"><span>code</span>firstLook.r</div>

```r
read.table(file,header=TRUE) # default separator is sep=" " is any white space
read.table(file, as.is=TRUE) # as.is=TRUE prevents string values from being converted to factors
read.csv("file", ,header=TRUE) # specifically for .csv files

load() # load the dataset written with save
data(x) # loads specific dataset

str(df) # similar to Python df.info() and SAS proc contents
dim(df)
head(df)
tail(df)
```
<div class="code-head"><span>code</span>firstLook.py</div>

```python
df.mean()
```


<div class="code-head"><span>code</span>firstLook.sas</div>

```sas
PROC IMPORT 
```
## basics


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


|    | Purpose           | SAS                                                                                                                              | Python                                                                  | R                                    |   Unnamed: 4 | Unnamed: 5   |
|---:|:------------------|:---------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|:-------------------------------------|-------------:|:-------------|
|  0 | input             | PROC IMPORT DATAFILE = " " OUT=df DBMS=CSV REPLACE; GUESSINGROWS=10000; RUN;                                                     | pd.read_csv(r”filename.csv”, encoding=”ISO-8859-1”) # encoding=”cp1252” | read.table(file, as.is=TRUE)         |          nan | nan          |
|    |                   |                                                                                                                                  | pd.read_sas(encoding=”latin-1” )                                        | read.csv("", header=TRUE)            |              |              |
|    |                   |                                                                                                                                  |                                                                         | load() # load data written with save |              |              |
|  1 | directory         | Filename filelist pipe "dir /b /s c:\temp\*.sas";                                                                                | import os                                                               | dir()                                |          nan | nan          |
|    |                   | Data _null_;                                                                                                                     | os.listdir("")                                                          |                                      |              |              |
|    |                   |   Infile filelist truncover;                                                                                                     |                                                                         |                                      |              |              |
|    |                   |   Input filename $100.;                                                                                                          |                                                                         |                                      |              |              |
|    |                   |   Put filename=;                                                                                                                 |                                                                         |                                      |              |              |
|    |                   | Run;                                                                                                                             |                                                                         |                                      |              |              |
|  2 | output            | nan                                                                                                                              | nan                                                                     | save()                               |          nan | nan          |
|  3 | content           | PROC CONTENT                                                                                                                     | nan                                                                     | str(df)                              |          nan | nan          |
|  4 | nan               | nan                                                                                                                              | df.info(), df.dtypes                                                    | nan                                  |          nan | nan          |
|  5 | summary           | PROC MEANS DATA=df NWAY; CLASS species; VAR x1-x6; RUN;                                                                          | df.describe()                                                           | summary(dt)                          |          nan | nan          |
|  6 | nan               | PROC SUMMARY                                                                                                                     | df.x.describe()                                                         | nan                                  |          nan | nan          |
|  7 | nan               | PROC SQL                                                                                                                         | pd.pivot_table()                                                        | nan                                  |          nan | nan          |
|  8 | nan               | nan                                                                                                                              | df.groupby(by=’x’).sum()                                                | nan                                  |          nan | nan          |
|  9 | nan               | nan                                                                                                                              | df.groupby(by=’x’).count()                                              | nan                                  |          nan | a            |
| 10 | nan               | nan                                                                                                                              | df.groupby(by=’x’).quantile([0.25,0.75])                                | nan                                  |          nan | nan          |
| 11 | nan               | nan                                                                                                                              | df.groupby(level=’ind1’)                                                | nan                                  |          nan | nan          |
| 12 | missing count     | PROC MEANS N NMISS MISSING;                                                                                                      | df.count()                                                              | nan                                  |          nan | nan          |
| 13 | nan               | nan                                                                                                                              | df.isnull().sum()                                                       | nan                                  |          nan | nan          |
| 14 | nan               | PROC FREQ TABLE /MISSING;                                                                                                        | nan                                                                     | nan                                  |          nan | nan          |
| 15 | frequency         | PROC FREQ                                                                                                                        | df.describe()                                                           | nan                                  |          nan | nan          |
| 16 | nan               | PROC SQL                                                                                                                         | nan                                                                     | nan                                  |          nan | nan          |
| 17 | nan               | nan                                                                                                                              | df.value.counts()                                                       | nan                                  |          nan | nan          |
| 18 | nan               | nan                                                                                                                              | nan                                                                     | nan                                  |          nan | nan          |
| 19 | nan               | nan                                                                                                                              | pd.crosstab(df.A, df.B).apply(lambda x: x/x.sum(), axis = 1)            | nan                                  |          nan | nan          |
| 20 | distribution      | PROC UNIVARIATE                                                                                                                  | df.describe(include=[np.number])                                        | nan                                  |          nan | nan          |
| 21 | drop/keep columns | DATA df (drop = col_name);                                                                                                       | df.drop(['x1', 'x2', 'x3'], axis = 1                                    | nan                                  |          nan | nan          |
| 22 | nan               | nan                                                                                                                              | nan                                                                     | nan                                  |          nan | nan          |
| 23 | nan               | DATA df (keep = col_name);                                                                                                       | df.loc[:, ['x1', 'x2'])                                                 | nan                                  |          nan | nan          |
| 24 | rename            | DATA df (RENAME = (old=new col_name));                                                                                           | df.columns = ['name1', 'name2', 'name3']                                | nan                                  |          nan | nan          |
| 25 | sort              | PROC SORT; BY x1 DESCENDING x2;                                                                                                  | df.sort(['x1', 'x2'], ascending = [True, False])                        | nan                                  |          nan | nan          |
| 26 | binning           | PROC RANK;                                                                                                                       | pd.cut(x, [min, cut1, …, cutk, max])                                    | nan                                  |          nan | nan          |
| 27 | nan               | nan                                                                                                                              | nan                                                                     | nan                                  |          nan | nan          |
| 28 | nan               | nan                                                                                                                              | np.digitize(x, [cut1, cut2, …, cutk])                                   | nan                                  |          nan | nan          |
| 29 | nan               | nan                                                                                                                              | nan                                                                     | nan                                  |          nan | nan          |
| 30 | nan               | nan                                                                                                                              | pd.qcut(df.x, n, labels=False)                                          | nan                                  |          nan | nan          |
| 31 | bapping/          | DATA df;                                                                                                                         | df.x.replace(zip(old, new))                                             | nan                                  |          nan | nan          |
| 32 | replace value     | IF THEN;                                                                                                                         | nan                                                                     | nan                                  |          nan | nan          |
| 33 | combine datasets  | DATA + MERGE;                                                                                                                    | pd.merge(df1, df2, how=’left’,on=’x’)                                   | nan                                  |          nan | nan          |
| 34 | nan               | PROC SQL;                                                                                                                        | nan                                                                     | nan                                  |          nan | nan          |
| 35 | filter join       | DATA + in;                                                                                                                       | df1[df1.x.isin(df2.x)]                                                  | nan                                  |          nan | nan          |
| 36 | nan               | PROC SQL                                                                                                                         | df1[~df1.x.isin(df2.x)]                                                 | nan                                  |          nan | nan          |
| 37 | get help          | nan                                                                                                                              | object ?                                                                | ?object                              |          nan | nan          |
## SAS Macro variable like in Python
There are three ways to enter arguments, which are similar to SAS macro variable. 
<div class="code-head"><span>code</span>arguments.py</div>

```py
def foo(x,y,z):
    print("x=" + str(x))
    print("y=" + str(y))
    print("z=" + str(z))
# 3 ways to enter argument (like SAS macrovariable)
# Method: List
mylist = [1,2,3]
foo(*mylist)

Method: tuple
myTuple = (1,2,3)
foo(*myTuple)
# Out
# x=1
# y=2
# z=3
# Method: dictionary
Two **
If we supply two **, it tells Python to use the values in the dictionary and plug into the function.   Whereas if we supply one *, we tell Python to use the keys in the dictionary for the function. 
mydict = {'x':1,'y':2,'z':3}
foo(**mydict)
# same output as the above
One *
def sum(a,b):
    return a+b

values= (1,2)
sum(*values)
# Out 3

values = {'a':1,'b':2}
sum(*values)
#  'ab'
sum(**values)

def sum(a, b, c, d):
    return a + b + c + d

values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }
s = sum(*values1, **values2)
# will execute as:
s = sum(1, 2, c=10, d=15)

```


### Summary Statistics:
1.  Simulations or shuffling
2.  Non-parametric tests, like the Mann-Whitney rank test  can work with non-normal distributions and ordered-level data.  On the other hand, these tests are also less powerful. 
A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.


### Visual Analysis
Does mathematics need *new clothes*?  

A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(nba[["ast", "fg", "trb"]])
plt.show()
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
library(GGally)
nba %>%
select(ast, fg, trb) %>%
ggpairs()
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```
### Linear Regression
Does mathematics need *new clothes*?  

A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train[["fg"]], train["ast"])
predictions = lr.predict(test[["fg"]])

import statsmodels.formula.api as sm
model = sm.ols(formula='ast ~ fga', data=train)
fitted = model.fit()
fitted.summary()
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
fit <- lm(ast ~ fg, data=train)
predictions <- predict(fit, test)
summary(fit)
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```
### Random Forest
Does mathematics need *new clothes*?  

A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
from sklearn.ensemble import RandomForestRegressor
predictor_columns = ["age", "mp", "fg", "trb", "stl", "blk"]
rf = RandomForestRegressor(n_estimators=100, min_samples_leaf=3)
rf.fit(train[predictor_columns], train["ast"])
predictions = rf.predict(test[predictor_columns])

from sklearn.metrics import mean_squared_error
mean_squared_error(test["ast"], predictions)
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
library(randomForest)
predictorColumns <- c("age", "mp", "fg", "trb", "stl", "blk")
rf <- randomForest(train[predictorColumns], train$ast, ntree=100)
predictions <- predict(rf, test[predictorColumns])

mean((test["ast"] - predictions)^2)
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```
### Kmeans Clustering
Does mathematics need *new clothes*?  

A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=5, random_state=1)
good_columns = nba._get_numeric_data().dropna(axis=1)
kmeans_model.fit(good_columns)
labels = kmeans_model.labels_
# plotting
from sklearn.decomposition import PCA
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(good_columns)
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
plt.show()
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