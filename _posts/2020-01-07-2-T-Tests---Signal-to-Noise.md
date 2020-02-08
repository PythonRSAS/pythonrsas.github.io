---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "T Tests - Signal to Noise"
description: Review of t-tests as a signal to noise test, and its "re-branding" as AB testing
author: Sarah Chen
image: images/posts/photos/IMG-0646.JPG
---
**Century old t-tests formulated to ensure beer quality was formally adopted in statistics and, now, AB testing**

<figure> 
   <img src="{{"/images/posts/photos/IMG-0646.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 

The t-test was developed in early 1900s to check for differences in quality of batches of Guinness beer that were small in sample sizes.  William Gosset , the Head Brewer of Guinness and pioneer of modern statistics empirically, by trial and error, found a formula for a t-distributed random variable. 

Gosset was a friend of both Karl Pearson and Ronald Fisher.

It is called the t-test because the test statistics is from a t distribution, which tends to the z (normal) distribution when n is large (when n>30, they are almost identical).  

It is a type of **signal-to-noise** test. 

### One-sample t-test of the mean
Also called the "location test", the one-sample t-test compares one sample mean to a null hypothesized mean.  

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

<div class="code-head"><span>code</span>T-statistics.r</div>

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

<div class="note"><p>
<b>Note</b>: T statistics is equivalent to F statistics when there are only two populations/categories. 
</p></div>

### critical value
A quick review of t-test and critical values is in example below.  The ppf function scipy.stats gives the the 'quantile', which is the critical value for the probability and degree of freedom we specify.

<div class="code-head"><span>code</span>T-statistics.py</div>

```python
from scipy import stats
print('{0:0.3f}'.format(stats.t.ppf(1-0.025, loc=0, scale=1, df=1)))
# 12.706
print('{0:0.3f}'.format(stats.t.ppf(1-0.025, loc=0, scale=1, df=9)))
# 2.262
print('{0:0.3f}'.format(stats.t.ppf(1-0.025, loc=0, scale=1, df=999)))
# 1.962
print('{0:0.3f}'.format(stats.norm.ppf(1-0.025, loc=0, scale=1)))
# 1.960
```
To roughly explain the differences in the critical values in the example above for various degrees of freedom, please see the plot below.  The smaller the degrees of freedom, the probability density curve is more stretched to the two tails.  The larger the degrees of freedom, the closer it is to the normal distribution. 

<div class="code-head"><span>code</span>T-Distributions.py</div>

```python
from scipy import stats
# plot normal Sarah
import numpy as np
import scipy
import pandas as pd
from scipy.stats import norm
import matplotlib.pyplot as plt
n =1000
bins = np.linspace(-10, 10, n) 
fig, ax = plt.subplots()
plt.plot(bins,stats.norm.pdf(bins),label='normal')
plt.plot(bins, stats.t.pdf(bins, loc=0,scale=1,df=1), label='t-dist df=1')
plt.plot(bins, stats.t.pdf(bins, loc=0,scale=1,df=3), label='t-dist df=3')
plt.legend()
plt.title("Normal and T Distributions")
plt.savefig("Normal_T_Distribution",dpi=300)
plt.show()
```

<figure> 
   <img src="{{"/images/posts/Normal_T_Distribution.PNG"| relative_url}}"> 
   <figcaption>Normal_T_Distribution</figcaption>
</figure> 

### Limitations of t-tests:
1.  Sample and population should not be too skewed in distribution (i.e. very roughly normal)   
2.  Each group should have about the same number of data points.  Comparing large and small groups together may give inaccurate results. 

### Overcoming limitations:
1.  Simulations or shuffling
2.  Non-parametric tests, like the Mann-Whitney rank test  can work with non-normal distributions and ordered-level data.  On the other hand, these tests are also less powerful. 


### AB tests
Does mathematics need *new clothes*?  

No.  Only people do.

T tests and other statistical tests have been "re-branded" in Silicon Valley as "AB" test.  