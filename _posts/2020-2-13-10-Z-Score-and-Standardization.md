---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Z Score and Standardization"
description: review of z-score and standardization, and how to do them in python and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0649.jpg
---
<figure> 
   <img src="{{"/images/posts/photos/IMG-0649.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 
Z-scores are linearly transformed data values having a **mean of zero and a standard deviation of 1**.  

Their names are related to the **standard normal tables**.  Remember, less than 60 years ago, that's all the technology that 99.9% of mathematicians, scientists and statisticians had.  

They are scores with a common standard. This standard is a mean of zero and a standard deviation of 1.     

Z-scores measure the distance of a data point from the mean in terms of the standard deviation, and retains the shape properties of the original data set (i.e. same skewness and kurtosis, which we just covered in the previous section).

Z-scores allow us to compare different data.   For example, GDP growth rate of a country is 3%.  Is it good or bad amongst peer group countries?   If I am told that its z-score is 1.5, then I know it is very good because it is 1.5 standard deviation above the mean. 

While z-scores are not necessarily normally distributed, many random variable distributions are normal.  

Standardizing normal distributions makes them standard normal distribution, which are easily interpretable.  

For example, it's well known that some 2.5% of values are larger than two and some 68% of values are between -1 and 1. 

If a variable is roughly normally distributed, z-scores will roughly follow a standard normal distribution. 

For z-scores, by definition, a score of 1.5 means “1.5 standard deviations higher than average”.   If a variable also follows a standard normal distribution, then we also know that 1.5 roughly corresponds to the 95th percentile. 

The linear transformation of data into z-score is also called standardizing.  Standardizing data is often a prerequisite in data analysis, statistical modeling and machine learning, which includes algorithms such as nearest neighbors, neural networks (and hence all deep learning), support vector machines, principal components analysis, linear discriminant analysis and more.  

The importance is due to the fact that if a feature has a variance that is orders of magnitude larger than others, it might dominate the objective function and make the estimator unable to learn from other features correctly.   
While z-score standardization can be easily coded from scratch using numpy, pandas, or even base Python, we can use readily available functions from <code class='coding'>scipy.stats</code> and sklearn. 

In Listing below, we first load the familiar Iris dataset via sklearn and standardize all the features by using the default method from preprocessing.scale.

<div class="code-head"><span>code</span>Standarize Data Using sklearn. preprocessing.py</div>

```python
 from sklearn.datasets import load_iris
 from sklearn import preprocessing
 iris = load_iris()
 X = iris.data
 stdz_X = preprocessing.scale(X)

#verify result is as expected with mean of 0 and std of 1
 np.mean(stdz_X, axis=0)
# [Out]: array([-0.000, -0.000, -0.000, -0.000])
 np.std(stdz_X, axis=0)
# [Out]: array([1.000, 1.000, 1.000, 1.000])
```

We can achieve the same result using StandardScaler from sklearn.preprocessing, as show in Listing below:

<div class="code-head"><span>code</span>Standarize Data Using sklearn.preprocessing StandardScaler.py</div>

```python
 from sklearn.preprocessing import StandardScaler
 StandardScaler().fit_transform(X)
 stdz_X[0,:]
# [Out]: array([-0.901, 1.019, -1.340, -1.315])
# the following does not change the result even though We have tried to replace the standard deviation with the degree of freedom adjusted one. 
 sc = StandardScaler()
 sc.fit(X)
 sc.std_ = np.std(X, axis=0, ddof=1)
 stdz_X = sc.fit_transform(X)
 stdz_X[0,:]
# [Out]: array([-0.901, 1.019, -1.340, -1.315])

```

Alternatively, a more flexible method is to use scipy.stats.  While the default behavior is provided as scipy.stats.zscore(a, axis=0, ddof=0), which will give we the same result as sklearn, note that both axis and degree of freedom adjustment can be made as shown in Listing below.  

The first standardization with ddof =0 gives the same result as in sklearn.   The second standardization is different due to ddof =1.  

<div class="code-head"><span>code</span>Calculate zscore Using scipy.stats.py</div>

```python
 from scipy import stats
 stdz_X = stats.zscore(X,axis=0, ddof =0)
 stdz_X[0,:]
# [Out]: array([-0.901, 1.019, -1.340, -1.315])
 stdz_X = stats.zscore(X,axis=0, ddof =1)
 stdz_X[0,:]
# [Out]: array([-0.898, 1.016, -1.336, -1.311])
```
For reference, Listing below shows standardization in SAS using <code class="coding">PROC STDIZE</code> and <code class="coding">PROC STANDARD</code>. 
<div class="code-head"><span>code</span>Standardize Data in SAS PROC STDIZE.sas</div>

```sas
 PROC STDIZE DATA=lib_name.iris 
OUT=iris_stdz 
METHOD=MEAN;
RUN;
```
<div class="code-head"><span>code</span>Standardize Data in SAS PROC STANDARD.sas</div>

```sas
 PROC STANDARD DATA=lib_name.iris MEAN=0 STD=1 
OUT=iris_stdz;
RUN;
```
