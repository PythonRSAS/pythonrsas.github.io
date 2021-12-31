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

1. Keyboard shortcuts
2. Import libraries,modules, and import data 
3. Working with the basics,frequency and plots
 
# Keyboard shortcuts
When we are used to writing in a language, switching to another one can make use feel slow and dumb.  Having the keyboard shortcuts in hand will allow us to pick up speed easier. 
#### RStudio 
- The pipe operator `%>%` is `Ctrl+Shift+M` (Windows) or `Cmd+Shift+M` (Mac).
- The assignment operator `<-` is `Alt + -` (Windows) or Option + - (Mac).
- `Ctrl+L` to clear all the code from your console.
- `Ctrl+2` and `Ctrl+1` to move the curser back and forth the source editor.
- `Ctrl+Enter` (Windows)To run a line of code from the source editor use  or Cmd+Enter (Mac).
- `Ctrl + ↑` (Windows) to scroll through your command history by clicking  or Cmd + ↑ (Mac). 
- Search a matching subset of the history: type the first few characters and then press `Ctrl/Cmd + ↑`
- Rename all instances of a variable name: highlight one instance of the variable name and then using Code > *Rename in Scope*. This is better than using Edit > Replace and Find because it only looks for whole word matches.
#### VSCode
VSCode is especially useful when we are writing packages or modules
[keyboard shortcuts pdf](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

##### Add custom snippets

[how to add a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets).
> `shift + command + p` and type snippets => Select `Preferences`: Open User Snippets 
[snippet generator](https://snippet-generator.app/)

## Run external code
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

<div class="code-head"><span>code</span>input and output.r</div>

```r
read.table(file,header=TRUE) # default separator is sep=" " is any white space
read.table(file, as.is=TRUE) # as.is=TRUE prevents string values from being converted to factors
read.csv("file", ,header=TRUE) # specifically for .csv files

load("myData.rdata") # load the dataset written with save
write.table(myData, file= "c:/documents/data/myData.csv", sep=',', row.names=F)

data(x) # loads specific dataset

read_feather(path, columns=NULL)
write_feather(x, path)
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
# basics
## freqency and frequency plot
<div class="code-head"><span>code</span>frequency.py</div>

```py
df.x.value_counts()
df.x.value_counts().plot(kind='bar)
```
<div class="code-head"><span>code</span>frequency.r</div>

```r
table(df$x)
barplot(table(df$x))
barplot(table(df$x),horiz=True)
```

# summary


| Purpose           | SAS                                                                          | Python                                                       | R                                    |
|:------------------|:-----------------------------------------------------------------------------|:-------------------------------------------------------------|:-------------------------------------|
| **input**            | PROC IMPORT DATAFILE = " " OUT=df DBMS=CSV REPLACE; GUESSINGROWS=10000; RUN; | pd.read_csv("") # encoding=”cp1252”,encoding=”ISO-8859-1”    | read.table(file, as.is=TRUE)         |
|                   |                                                                              | pd.read_sas("",encoding=”latin-1” )                          | read.csv("", header=TRUE)            |
|                   |                                                                              |                                                              | load() # load data written with save |
| **output**            | PROC EXPORT DATA= df OUTFILE= ""  DBMS=csv REPLACE; RUN;                     | df.to_csv(index=False)                                       | save()                               |
| **content**           | proc contents data = df                                                      | array.ndim, .shape, .size, .dtype, .itemsize, .nbytes        | str(df)                              |
|                   | out = dsList (keep=memname memlabel name label nobs varnum) noprint;run;     |                                                              |                                      |
|                   |                                                                              | df.info(), df.dtypes                                         |                                      |
| **summary**           | PROC MEANS DATA=df NWAY; CLASS species; VAR x1-x6; RUN;                      | df.describe()                                                | summary(dt)                          |
|                   | PROC SUMMARY                                                                 | df.x.describe()                                              |                                      |
|                   | PROC SQL                                                                     | pd.pivot_table()                                             |                                      |
|                   |                                                                              | df.groupby(by=’x’).sum()                                     |                                      |
|                   |                                                                              | df.groupby(by=’x’).count()                                   |                                      |
|                   |                                                                              | df.groupby(by=’x’).quantile([0.25,0.75])                     |                                      |
|                   |                                                                              | df.groupby(level=’ind1’)                                     |                                      |
| **missing count** | PROC MEANS N NMISS MISSING;                                                  | df.count()                                                   |                                      |
|                   |                                                                              | df.isnull().sum()                                            |                                      |
|                   | PROC FREQ TABLE /MISSING;                                                    |                                                              |                                      |
| **frequency**     | PROC FREQ                                                                    | df.describe()                                                |                                      |
|                   | PROC SQL                                                                     |                                                              |                                      |
|                   |                                                                              | df.value.counts()                                            |                                      |
|                   |                                                                              |                                                              |                                      |
|                   |                                                                              | pd.crosstab(df.A, df.B).apply(lambda x: x/x.sum(), axis = 1) |                                      |
| **distribution**  | PROC UNIVARIATE                                                              | df.describe(include=[np.number])                             |                                      |
| **drop/keep columns** | DATA df (drop = col_name);                                                   | df.drop(['x1', 'x2', 'x3'], axis = 1                         |                                      |
|                   | DATA df (keep = col_name);                                                   | df.loc[:, ['x1', 'x2'])                                      |                                      |
| **rename**            | DATA df (RENAME = (old=new col_name));                                       | df.columns = ['name1', 'name2', 'name3']                     |                                      |
| **sort**              | PROC SORT; BY x1 DESCENDING x2;                                              | df.sort(['x1', 'x2'], ascending = [True, False])             |                                      |
| **binning**           | PROC RANK;                                                                   | pd.cut(x, [min, cut1, …, cutk, max])                         |                                      |
|                   |                                                                              | np.digitize(x, [cut1, cut2, …, cutk])                        |                                      |
|                   |                                                                              | pd.qcut(df.x, n, labels=False)                               |                                      |
| **replace value**     | IF THEN;                                                                     |    df.x.replace(zip(old,new))                                            |                                      |
| **combine datasets**  | DATA + MERGE;                                                                | pd.merge(df1, df2, how=’left’,on=’x’)                        |                                      |
|                   | PROC SQL;                                                                    |                                                              |                                      |
| **filter join**       | DATA + in;                                                                   | df1[df1.x.isin(df2.x)]                                       |                                      |
|                   | PROC SQL                                                                     | df1[~df1.x.isin(df2.x)]                                      |                                      |
| **get help**          |                                                                              | object ?                                                     | ?object                              |
| **upgrade library**   |                                                                              | pip3 install --upgrade packageName --user                    |                                      |
| **directory**         | Filename filelist pipe "dir /b /s c:\temp\*.sas";                            | import os                                                    | dir()                                |
|                   | Data _null_; Infile filelist truncover;                                      | os.listdir("")                                               |                                      |
|                   |  Input filename $100.;                                                       |                                                              |                                      |
|                   | Put filename=;Run;                                                           |                                                              |                                      |
| **working directory**  |       |getcwd()       | getwd()                             |
| **change directory**  |       |chdir())       | setwd()                             |

### Summary Statistics:



# Visual Analysis

### frequency barplots

#### simple barplots 
<div class="code-head"><span>code</span>simple bar plot.py</div>

```python
# simple bar plot
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution",
   xlab="Number of Gears")

```

<div class="code-head"><span>code</span>simple bar plot.r</div>

```r
# simple bar plot
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution",
   xlab="Number of Gears")

# simple horizontal bar plot with added labels
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", horiz=TRUE,
  names.arg=c("3 Gears", "4 Gears", "5 Gears"))
```
<div class="code-head"><span>code</span>simple bar plot.sas</div>

```sas

```
#### stacked or grouped barplots for > 1 groups
<div class="code-head"><span>code</span>stacked and grouped barplots.py</div>

```pythn
```
<div class="code-head"><span>code</span>stacked and grouped barplots.r</div>

```r
# Stacked Bar Plot with Colors and Legend
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
  xlab="Number of Gears", col=c("darkblue","red"),
  legend = rownames(counts))

# Grouped Bar Plot
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
  xlab="Number of Gears", col=c("darkblue","red"),
  legend = rownames(counts), beside=TRUE)
```

> Bar plots need not be based on counts or frequencies. You can create bar plots that represent means, medians, standard deviations, etc. Use the <span class="coding">aggregate( )</span> function and pass the results to the <span class="coding">barplot( )</span> function.

By default, the categorical axis line is suppressed. Include the option <span class="coding">axis.lty=1</span> to draw it.

With many bars, bar labels may start to overlap. You can decrease the font size using the <span class="coding">cex.names = option</span>. Values smaller than one will shrink the size of the label. Additionally, you can use graphical parameters such as the following to help text spacing:

<div class="code-head"><span>code</span>numerica value barplot.r</div>

```r
# Fitting Labels
par(las=2) # make label text perpendicular to axis
par(mar=c(5,8,4,2)) # increase y-axis margin.

counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", horiz=TRUE, names.arg=c("3 Gears", "4 Gears", "5   Gears"), cex.names=0.8)
```

### relationship between numeric data
<div class="code-head"><span>code</span>relationship between numeric data.py</div>

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(nba[["ast", "fg", "trb"]])
plt.show()
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