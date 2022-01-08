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

- [basics](#basics)
  - [freqency and frequency plot](#freqency-and-frequency-plot)
    - [Python](#python)
    - [R](#r)
    - [SAS](#sas)
- [summary](#summary)
    - [Linear Regression](#linear-regression)
    - [Random Forest](#random-forest)
    - [Kmeans Clustering](#kmeans-clustering)


# basics
## freqency and frequency plot
### Python
<div class="code-head"><span>code</span>frequency.py</div>

```py
df.x.value_counts()
df.x.value_counts().plot(kind='bar)
```
### R
<div class="code-head"><span>code</span>frequency.r</div>

```r
table(df$x)
barplot(table(df$x))
barplot(table(df$x),horiz=True)
```
### SAS
<div class="code-head"><span>code</span>frequency.sas</div>

```sas
proc freq data=df;
run;
```

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
|                       | PROC SQL                                                                     |                                                              |                                      |
|                       |                                                                              | df.value.counts()                                            |                                      |
|                       |                                                                              |                                                              |                                      |
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
In SAS, use the [Tree procedure](https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.4/statug/statug_tree_examples02.htm)
<div class="code-head"><span>code</span>import data.sas</div>

```sas
title 'Fisher (1936) Iris Data';
ods graphics on;

proc cluster data=sashelp.iris method=twostage print=10
             outtree=tree k=8 noeigen;
   var SepalLength SepalWidth PetalLength PetalWidth;
   copy Species;
run;
proc tree data=tree horizontal lineprinter pages=1 maxh=10;
   id species;
run; 
```