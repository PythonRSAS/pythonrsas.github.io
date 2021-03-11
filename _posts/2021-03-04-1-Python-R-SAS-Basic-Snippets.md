---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Python R SAS Basic Snippets"
description: A quick lookup for basic tasks in statistical and machine learning using Python, R and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0646.JPG
---
**Century old t-tests formulated to ensure beer quality was formally adopted in statistics and, now, AB testing**

<figure> 
   <img src="{{"/images/posts/photos/IMG-0646.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 

The t-test was developed in early 1900s as an **economical** (small samples) way to check for differences in mean quality of batches of Guinness beer that were small in sample sizes.  William Gosset , the Head Brewer of Guinness and pioneer of modern statistics empirically, by trial and error, found a formula for a t-distributed random variable. 

Gosset was a friend of both Karl Pearson and Ronald Fisher.

It is called the t-test because the test statistics is from a t distribution, which tends to the z (normal) distribution when n is large (when n>30, they are almost identical).  

As William Gosset noted in his original publication [The Probable Error of a Mean](http://seismo.berkeley.edu/~kirchner/eps_120/Odds_n_ends/Students_original_paper.pdf), while it is applicable to samples from population that are normally distributed, "the deviation from "normality must be very extreme to lead to serious error."

Why did he and others focus on population that are normal distributed as opposed to a different kind of distribution?   I guess that's partially due to computational limitations.  

Normal distribution tables and calculus were the best technology at that time.  

The t-test is a type of **signal-to-noise** test. 

### One-sample t-test of the mean
Also called the *"location test"*, the one-sample t-test compares one sample mean to a null hypothesized mean.  

The comparison has to be standardized by something--the standard error the mean (population standard deviation, approximated by sample, devided by square root of sample size)

The t-statistics is more or less defined as followed:

<figure> 
   <img src="{{"/images/posts/t-stat.PNG" width="15" | relative_url}}"> 
   <figcaption>t statistics</figcaption>
</figure> 

The one-sample t-statistics can be interpreted as the **signal-to-noise** ratio, where the numerator is signal (aka “effect size”) and the denominator (standard error of the mean) the noise.  

The larger the numerator, the higher the signal. The higher the variance, the lower the signal to noise ratio.  The signal must be large enough to stand out from the noise for the test result to be significant.  

### Paired t-test
A paired t-test Is just a one-sample t-tests as the difference between paired observations (e.g., before and after) is the test data with null hypothesis that the mean is 0 (i.e. no difference). 
> To determine that the groups are different, the t-value needs to be large enough.

### Two-sample (unpaired) t-test
Unpaired-samples: aka “independent-samples”, “between samples” test if two different groups have the same mean. 
In a 2-sample t-test, the denominator is still the noise.  We can either assume that the variability in both groups is equal or not equal.  Either way, the principle remains the same: we are comparing signal to noise. 

Just like with the 1-sample t-test, for any given difference in the numerator, as we increase the noise value in the denominator, the t-value becomes smaller. 

To determine that the groups are **different**, we need a t-value that is **large enough**.

For details, see [NIST Two-Sample t-Test for Equal Means](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm)

<!-- <div class="code-head"><span>code</span>T-statistics.r</div>

```r
## Read data and save variables. 
y <- matrix(scan("AUTO83B.DAT",skip=25),ncol=2,byrow=T) 
usmpg = y[,1] 
jmpg = y[,2] 
jmpg = jmpg[jmpg!=-999] 
## Perform two-sample t-test. 
z = t.test(usmpg,jmpg,var.equal=TRUE) 
> Case 1: Equal Variances > > Two Sample t-test > > data: usmpg and jmpg > t = -12.6206, df = 326, p-value < 2.2e-16 > alternative hypothesis: true difference in means is not equal to 0 > 95 percent confidence interval: > -11.947653 -8.725216 > sample estimates: > mean of x mean of y > 20.14458 30.48101 
## Find one-tailed and two-tailed critical values. 
qt(.05,z$parameter) 
> -1.649541 
qt(.025,z$parameter) 
> [1] -1.967268 

```
 -->
<div class="note"><p>
<b>Note</b>: T statistics is equivalent to F statistics when there are only two populations/categories. 
</p></div>

### Import and Export Data
A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
import pandas as pd
nba = pd.read_csv("nba_2013.csv")
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
library(readr)
nba <- read_csv("nba_2013.csv")
# export
write.csv(df,"c:\\users\\sarahChen\\filename.csv",row.names=FALSE )
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```
### Create a Dataset
A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
import pandas as pd
nba = pd.read_csv("nba_2013.csv")
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
df<-data.frame(name= c("A","B","C",value=c(1,2,3)))
# export
write.csv(df,"c:\\users\\sarahChen\\filename.csv",row.names=FALSE )
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```

<figure> 
   <img src="{{"/images/posts/Normal_T_Distribution.png"| relative_url}}"> 
   <figcaption>Normal_T_Distribution</figcaption>
</figure> 

### Data Attributes:
1.  Sample and population should not be too skewed in distribution (i.e. very roughly normal)   
2.  Each group should have about the same number of data points.  Comparing large and small groups together may give inaccurate results. 

A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
df.shape
df.info()
df.dtypes()
df.head()
df.tail()

```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
dim(df)
head(df)
tail(df)
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```
### Summary Statistics:
1.  Simulations or shuffling
2.  Non-parametric tests, like the Mann-Whitney rank test  can work with non-normal distributions and ordered-level data.  On the other hand, these tests are also less powerful. 
A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>import data.py</div>

```python
df.mean()
```
To roughly explain the differences in the critical values in the example above for various degrees of  

<div class="code-head"><span>code</span>import data.r</div>

```r
library(purrr)
library(dplyr)
nba %>%
  select_if(is.numeric) %>%
  map_dbl(mean, na.rm = TRUE)
```
<div class="code-head"><span>code</span>import data.sas</div>

```sas
PROC IMPORT 
```

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