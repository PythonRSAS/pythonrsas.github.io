---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Linear Regression II Categorical Data Preparation"
description: Prepare categorical data for linear regression in Python and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0648.JPG
---

<figure> 
   <img src="{{"/images/posts/photos/IMG-0648.jpg"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 

Most datasets outside of image recognition have categorical variables.  In linear regression, they are often converted to dummy variables.

In SAS, <code class="coding">PROC GLM</code>, <code class="coding">PROC GENMOD</code>, <code class="coding">PROC GLMMIX</code> and other regression related procedures handle categorical variables are by the <code class="coding">CLASS</code> statement, which implicitly converts them into dummies.  Only when we use <code class="coding">PRO REG</code> that we would have to explicitly recode them ourselves.   

As the mathematics behind linear regression is linear algebra, categorical variables are generally converted to dummy variables.  

We can use Python pandas <code class="coding">pd.get_dummies</code>, <code class="coding">sklearn.preprocessing.OneHotEncode</code> for convert categorical variables into dummies.  

One common serious error some beginners make is applying OneHotEncode to their entire dataset including numerical variable or Booleans.  

To prepare the data for sklearn LinearRegression, the numerical and categorical should be separately handled.   
-  Numerical: standardize if your model contains *interactions* or *polynomial* terms
-  Categorical:  pd.get_dummies is flexible to use.  while sklearn OneHotEncode is both flexible and more consistent in working with sklearn API.


### Simple example
To illustrate, we will use another simple example in listing below using the toy dataset tips from the seaborn library.  The tips dataset has seven columns, which has both numerical, categorical and ordinal variables.   

<div class="code-head"><span>code</span>Linear Regression on Tips Data.py</div>

```python
>>> tips = sns.load_dataset("tips")
>>> print(tips.head())
```

|    |   total_bill |   tip | sex    | smoker   | day   | time   |   size |
|---:|-------------:|------:|:-------|:---------|:------|:-------|-------:|
|  0 |        16.99 |  1.01 | Female | No       | Sun   | Dinner |      2 |
|  1 |        10.34 |  1.66 | Male   | No       | Sun   | Dinner |      3 |
|  2 |        21.01 |  3.5  | Male   | No       | Sun   | Dinner |      3 |
|  3 |        23.68 |  3.31 | Male   | No       | Sun   | Dinner |      2 |
|  4 |        24.59 |  3.61 | Female | No       | Sun   | Dinner |      4 |


<figure> 
   <img src="{{"/images/posts/linear regression on the anscomebe dataset.png" "width"=20| relative_url}}"> 
   <figcaption>Anscomebe Quartet</figcaption>
</figure> 

<div class="note"><p>
<b>Note</b>: The data was constructed in 1973 by Frank Anscombe (13 May 1918 – 17 October 2001), an English statistician, who had stressed that "a computer should make both calculations and graphs".  He illustrated the importance of visualizing data with four data sets now known as Anscombe's quartet.    Frank Anscombe was brother-in-law to John Tukey.
</p></div>

The four subsets, each with 11 data points, have distinct characteristics despite almost identical statistics in **count, mean, median, standard deviation, and Pearson correlation between x and y**.   If you fit OLS linear regression on them, you get the **same intercept, coefficient, and same p-values** of 0.022 for each of them.  
1. The first set of data appears to be the typical linear relationship and follow the assumption of normality.   
1. The second set of data does not seem normally distributed.  A quadratic line would be a better fit. 
1. The third set of data has perfect linear relationship between x and y, but is affected by one outlier.  Unless the outlier is important to keep, one should consider robust regression. 
1. The fourth set of data does not show any linear relationship between x and y, even though the Pearson linear correlation is large.  

|    |   x_I |   y_I |   x_II |   y_II |   x_III |   y_III |   x_IV |   y_IV |
|---:|------:|------:|-------:|-------:|--------:|--------:|-------:|-------:|
|  0 |    10 |  8.04 |     10 |   9.14 |      10 |    7.46 |      8 |   6.58 |
|  1 |     8 |  6.95 |      8 |   8.14 |       8 |    6.77 |      8 |   5.76 |
|  2 |    13 |  7.58 |     13 |   8.74 |      13 |   12.74 |      8 |   7.71 |
|  3 |     9 |  8.81 |      9 |   8.77 |       9 |    7.11 |      8 |   8.84 |
|  4 |    11 |  8.33 |     11 |   9.26 |      11 |    7.81 |      8 |   8.47 |
|  5 |    14 |  9.96 |     14 |   8.1  |      14 |    8.84 |      8 |   7.04 |
|  6 |     6 |  7.24 |      6 |   6.13 |       6 |    6.08 |      8 |   5.25 |
|  7 |     4 |  4.26 |      4 |   3.1  |       4 |    5.39 |     19 |  12.5  |
|  8 |    12 | 10.84 |     12 |   9.13 |      12 |    8.15 |      8 |   5.56 |
|  9 |     7 |  4.82 |      7 |   7.26 |       7 |    6.42 |      8 |   7.91 |
| 10 |     5 |  5.68 |      5 |   4.74 |       5 |    5.73 |      8 |   6.89 |


### OLS from Scratch
The OLS in one variable can be solved in linear algebra, or beginning calculus, or, with a few more steps, even middle school algebra. 

<figure> 
   <img src="{{"/images/posts/ols_1_feature.png"| relative_url}}"> 
   <figcaption>One Variable OLS Solution</figcaption>
</figure>

<div class="code-head"><span>code</span>OLS from Scratch.py</div>

```python
def ols(x, y):
  n = np.size(df.y)
  m_x = np.mean(df.x)
  m_y = np.mean(df.y)
  xy = np.sum((df.x - m_x)*(df.y - m_y))
  xx = np.sum((df.x - m_x)**2)
  b1 = xy/xx
  b0 = m_y - b1*m_x
  print("dataset %s" %i)
  print("intercept:  {0:0.3f}".format(b0))
  print("coefficient: {0:0.3f} \n".format(b1))
for i in ['I','II','III', 'IV']:
  df = anscombe[anscombe.dataset=='%s' %i]
  ols(df.x, df.y) 
#  Out:
#  dataset I
# intercept:  3.000
# coefficient: 0.500

# dataset II
# intercept:  3.001
# coefficient: 0.500

# dataset III
# intercept:  3.002
# coefficient: 0.500

# dataset IV
# intercept:  3.002
# coefficient: 0.500
```

### OLS from sklearn
The sklearn.LinearRegression class is a wrapper around the [lstsq function](https://github.com/scipy/scipy/blob/v1.4.1/scipy/linalg/basic.py#L1047-L1246) from <code class="coding">scipy.linalg</code>. 
```python
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)
```
It is quite basic, with basically two options other than copy_X and n_jobs.   

The two options are intuitive if we understand the formula for the solution of weights in OLS loss function: 
 -	<span class="coding">fit_intercept</span>: bool, optional, default True.  Whether to calculate the intercept for this model. If set to False, no intercept will be used in calculations (i.e. **data is assumed to be centered** already, in other words, the mean of the data is subtracted from each data point).   Visually, the fitted line will pass through the origin, if set to False.
 -	<span class="coding">normalize</span>: bool, optional, default False.  This parameter is ignored when <span class="coding">fit_intercept</span> is set to False.   If True, the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm.  If we wish to standardize, please use <span class='coding'>sklearn.preprocessing.StandardScaler</span> before calling <span class="coding">fit</span> on  an estimator with <span class="coding">normalize=False</span>.

<div class="code-head"><span>code</span>OLS LinearRegression.py</div>

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
X =df.x.values.reshape(-1,1) #reshape to 2-dimensional
y =df.y.values
# instantiate the LinearRegression object and fit data
model = LinearRegression()
model.fit(X, y)
# model parameters
print('Coefficient(s): ', (*['{0:0.3f}'.format(i) for i in model.coef_]),sep='\n' ) # using separator would be convenient when 
print('Intercept:{0:0.3f}'.format(model.intercept_))
# model predictions
y_pred = model.predict(X)
print("Mean squared error: %.2f"
      % mean_squared_error(y, y_pred))
print('R square: %.2f' % r2_score(y, y_pred)) 
alpha=0.8
title ='OLS Regression for Anscomebe Dataset 1'
f, ax =plt.subplots(1, 1)
plt.rcParams["figure.figsize"] = (5,5)
ax.plot(X, y,  alpha=alpha, linestyle='None', marker='o')
ax.text(4,10, r'$R^2$=%.2f MSE=%.2f' % (r2_score(y, y_pred) ,mean_squared_error(y, y_pred)))
ax.text(4,8.5, 'Intercept:   {0:0.2f}'.format(model.intercept_))
ax.text(4,9,   'Coefficient:{0:0.2f}'.format(model.coef_[0]))
ax.plot(X, y_pred, alpha=alpha)
ax.set_title('%s' %title)
ax.set_ylabel('y')
ax.set_xlabel('X')
plt.savefig("images/%s.png"%title,dpi=300, tight_layout=True)
plt.clf()
plt.close()
# Out:
# Coefficient(s):
# 0.500
# Intercept:3.000
# Mean squared error: 1.25
# R square: 0.67
```
<figure> 
   <img src="{{"/images/posts/OLS Regression for Anscomebe Dataset 1.png"| relative_url}}"> 
   <figcaption>OLS linear regression on Anscomebe</figcaption>
</figure>

1.	When requesting R square using <code class="coding">r2_score</code>, the order matters. It should be r2_score(y_actual, y_pred).   The actual value goes first, then the predicted.  We will get a wrong result if the order is not followed.  
2.	In case we did not know it already, the square of the pearson correlation coefficient is R square for the one-feature case.   So next time if we have doubts about which implementation of OLS, sklearn or statsmodel, is correct, this could be one of your testing tools.

### OLS Using Statsmodels
To get p-values and other statistical metrics like those from SAS and R, we use the Python statsmodels library. 

<div class="code-head"><span>code</span>OLS Regression Using Statsmodels.py</div>

```python
import statsmodels.formula.api as smf
df = anscombe.loc[anscombe.dataset=='I',['x','y']]
smod = smf.ols(formula ='y~ x', data=df)
result = smod.fit()
print(result.summary())
```
For plain OLS, we recommend we use <code class="coding">statsmodels.formula.api</code> instead of <code class="coding">statsmodels.api</code>, even though their names sound similar.   The formula api uses the <code class="coding">patsy</code> package to convert data and formula into matrices.  The latter requires adding a column of constants to the array of independent variables commonly denoted as “X”.

### OLS Using SAS
SAS is the king of statistical analysis.  It outputs tons of information for just a few lines of code.       
<div class="code-head"><span>code</span>OLS Regression Using SAS.sas</div>

```sas
PROC REG DATA = df (WHERE=(dataset='I'));
MODEL y=x;
RUN;
```
<figure> 
   <img src="{{"/images/posts/sas_ols.png"| relative_url}}"> 
   <figcaption>OLS via SAS</figcaption>
</figure>
Diagnostics are important too!  

The outputs show that the model is the right type of model for this data, and that the parameter coeffcient is trustworthy.  For new data coming from the same population, we can apply this model with confidence. 
<figure> 
   <img src="{{"/images/posts/sas_ols_diagnostics.png"| relative_url}}"> 
   <figcaption>OLS via SAS</figcaption>
</figure>
<figure> 
   <img src="{{"/images/posts/ols_1_feature_fit.png"| relative_url}}"> 
   <figcaption>SAS OLS Fit Plot</figcaption>
</figure>

If we add just one line of code <code class="coding">BY dataset;</code>, we get the OLS for each of the Anscombe quartet.  There are many other options too.

### Less perfect case
We will apply the same algorithm to the second subset of the Anscombe quartet.   The code is exactly the same.   

As noted in the introduction, the subsets have identical statistics in count, mean, median, standard deviation, and Pearson correlation between x and y.  

Because it has same intercept, same coefficient, and even the p-values of 0.022, many would have thought this was the perfect model.  But this is probably not the right model for this data, which we could tell by looking at the data at the onset, or by examining the residual diagnostics as shown in SAS output below. 

The residual plot shows that the OLS assumptions do not stand.  From the figure below, we see that the residule plot looks like a parabola and does not look anyway close to random along the predicted, which does not support assumptions of OLS: linear relationship, homoscedasticity, and independence.  

Without diagnostics or visual analysis of the data, it would have been hard to tell any potential problems if we look at statistics and performance scores only.  

We should probably transform the variable, for example, using power transform (note that y = a + bx^2 is still linear regression)
<figure> 
   <img src="{{"/images/posts/ols_1_feature_fit_poor.png"| relative_url}}"> 
   <figcaption>Not a Good Fit</figcaption>
</figure>

<div class="code-head"><span>code</span>Residual Visual Test.py</div>

```python
df = anscombe.loc[anscombe.dataset=='II',['x','y']]\
.copy()
X =df.x.values.reshape(-1,1)
y =df.y.values
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

def residual_visual_test(y, y_pred):
    resid = y - y_pred
    fig, ax = plt.subplots(1,1)
    ax.scatter(y_pred, resid)
    ax.set_title('Residuals vs. Predicted Values')
    ax.set(xlabel='Predicted', ylabel='Residuals')
    ax.plot([min(y_pred)-1, max(y_pred)+1],[0,0],'--k',lw=5,alpha=0.4)
    plt.savefig(r"./images/Residual Visual Test.png", dpi=300)

residual_visual_test(y, y_pred)   
```
<figure> 
   <img src="{{"/images/posts/Residual Visual Test.png" "width"=8 "height"=5| relative_url}}"> 
   <figcaption>Residual Visual Test</figcaption>
</figure>


### More
OLS is old and fundamental.  Its coefficients can be summarized as a dot product normalized by the vector space of the input features.   

To do it correctly, the assumptions should not be too far off.  Checking the fit diagnostics is a way to see if the assumptions are met.

If the assumptions are far from true, we have many other ways besides basic OLS.  