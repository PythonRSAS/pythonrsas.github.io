---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Linear Regression II Categorical Data Preparation"
description: Prepare categorical data for linear regression
author: Sarah Chen
image: images/posts/photos/IMG-0648.JPG
---

<figure> 
   <img src="{{"/images/posts/photos/IMG-0648.jpg"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 

Most datasets outside of image recognition have categorical variables.  In linear regression, they are often converted to dummy variables.

In SAS, <code class="coding">PROC GLM</code>, <code class="coding">PROC GENMOD</code>, <code class="coding">PROC GLMMIX</code> and other regression related procedures handle categorical variables are by the <code class="coding">CLASS</code> statement, which implicitly converts them into dummies.  Only when we use <code class="coding">PRO REG</code> that we would have to explicitly recode them ourselves.   

As the mathematics behind linear regression is linear algebra, categorical variables are generally converted to dummy variables.  

For non-regularized linear regression, perfect multicollinearity must be avoided. That's why categorical column is encoded into k-1 binary columns, where the kth level can be represented by a vector of zeros and it goes to the intercept.  

While most SAS procedures and R take care of encoding behind the scene, to prepare the data for sklearn, the numerical and categorical should be separately handled.   
-  Numerical: standardize if our model contains *interactions* or *polynomial* terms
-  Categorical:  Python pandas <code class="coding">pd.get_dummies</code> and <code class="coding">sklearn.preprocessing.OneHotEncode</code> can be used to convert categorical variables into dummies.

pd.get_dummies is flexible to use.  Whereas sklearn OneHotEncode is both flexible and consistent in with sklearn API.

### Simple example
To illustrate, we will use another simple example in listing below using the toy dataset tips from the seaborn library.  The tips dataset has seven columns, which have numerical, categorical and ordinal variables.   We first load the data and get some information.  The “size” column is ordinal coded in integers, which we assume whose sizes have meaning and won’t encode them into dummies.   

<div class="code-head"><span>code</span>Tips Data.py</div>

```python
tips = sns.load_dataset("tips")
print(tips.shape)
# [Out]: (244, 7)
print(tips.info())
# [Out]:
# tips.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 244 entries, 0 to 243
# Data columns (total 7 columns):
# total_bill    244 non-null float64
# tip           244 non-null float64
# sex           244 non-null category
# smoker        244 non-null category
# day           244 non-null category
# time          244 non-null category
# size          244 non-null int64
# dtypes: category(4), float64(2), int64(1)
# memory usage: 7.2 KB
print(tips.head())
```

|    |   total_bill |   tip | sex    | smoker   | day   | time   |   size |
|---:|-------------:|------:|:-------|:---------|:------|:-------|-------:|
|  0 |        16.99 |  1.01 | Female | No       | Sun   | Dinner |      2 |
|  1 |        10.34 |  1.66 | Male   | No       | Sun   | Dinner |      3 |
|  2 |        21.01 |  3.5  | Male   | No       | Sun   | Dinner |      3 |
|  3 |        23.68 |  3.31 | Male   | No       | Sun   | Dinner |      2 |
|  4 |        24.59 |  3.61 | Female | No       | Sun   | Dinner |      4 |

### pd.get_dummies
<code class="coding">pd.get_dummies(tips[['sex','smoker', 'day', 'time']],drop_first=True)</code> takes inputs such as numpy array, Series, or DataFrame and returns dummy-coded data.  

<div class="code-head"><span>code</span>One Line Encoding.py</div>

```python
tips_encoded =pd.get_dummies(tips, drop_first=True)
```
It is very convenient.   But if want to be more explicit, we can do the following:
<div class="code-head"><span>code</span>Explicit Encoding.py</div>

```python
# or equivalently but more explicitly
cate_var = tips.select_dtypes(exclude=['number']).\
  columns.tolist()
tips_enc = pd.get_dummies(tips,\
 columns=cate_var,drop_first=True)
print(tips_enc.columns.tolist())
# Out:['total_bill', 'tip', 'size', 'sex_Female', 'smoker_No', 'day_Fri', 'day_Sat', 'day_Sun', 'time_Dinner']

```
<code class="coding">drop_first = True</code> is used otherwise the X matrix would have been singular.  Let's look at the deails:
```python
tips_cate=pd.get_dummies(tips[['sex','smoker', 'day', 'time']], drop_first=True)
print(tips_cate.head())
```
Here is the result:

|    |   sex_Female |   smoker_No |   day_Fri |   day_Sat |   day_Sun |   time_Dinner |
|---:|-------------:|------------:|----------:|----------:|----------:|--------------:|
|  0 |            1 |           1 |         0 |         0 |         1 |             1 |
|  1 |            0 |           1 |         0 |         0 |         1 |             1 |
|  2 |            0 |           1 |         0 |         0 |         1 |             1 |
|  3 |            0 |           1 |         0 |         0 |         1 |             1 |
|  4 |            1 |           1 |         0 |         0 |         1 |             1 |

The dummy-coded DataFrame has new column names that are intuitive.  But sometimes we want different names than what come with default.  

<div class="code-head"><span>code</span>Custom Prefix.py</div>

```python
pd.get_dummies(tips[['sex','smoker']],\
 drop_first=True,prefix=['gender','cigarettes']).head()
```

|    |   gender_Female |   cigarettes_No |
|---:|----------------:|----------------:|
|  0 |               1 |               1 |
|  1 |               0 |               1 |
|  2 |               0 |               1 |
|  3 |               0 |               1 |
|  4 |               1 |               1 |

Other options: 
1.  If we prefer float instead of integers in the result, we could specify dtype=float in the function call. 
2.  If we want to encode columns that are floats or integers into dummies, we can do that by specifying it with the columns=[] option, which does not restrict data type. 

### OneHoteEncode
From version 0.22 +, OneHotEncoder in sklearn.preprocessing has drop option. 
For example, OneHotEncoder(drop='first') works like pd.get_dummies(drop_first=True). 

Because it is so convinient, one common serious error some beginners make is applying OneHotEncode to their entire dataset including numerical variable or Booleans. 
<div class="code-head"><span>code</span>OLS Regression with Both Categorical and Numeric Features Using Statsmodels.py</div>

```python
from sklearn.preprocessing import OneHotEncoder                                                                                                                        
enc = OneHotEncoder(handle_unknown='error',drop='first')
enc.fit(tips[cate_var])
tips_cate = enc.transform(tips[cate_var]).toarray()
print(tips_cate.shape)
# (244, 6)
# tips_num = tips[['total_bill','size']]
tips_num = tips.drop('tip', axis =1).select_dtypes('number')
y = tips['tip'].values.copy()
x = np.concatenate([tips_num, tips_cate],axis=1)
print(x.shape)
# (244, 8)

```
### statsmodels
Using statsmodels formula interface is convenient for data with categorical features due to the workings of patsy behind the scene: categorical variables will automatically treated as categorical variables and all necessary steps will be taken cared without any explicit encoding.  

The <code class="coding">C()</code> notation surrounding the categorical variable names are actually not needed unless the columns are integers rather than strings.  

For example, if we use ‘size’ in the model and wish to treat it as categorical then we would need to have it as <code class="coding">C(size)</code> because the values are integers.      

<div class="code-head"><span>code</span>OLS Regression with Both Categorical and Numeric Features Using Statsmodels.py</div>

```python
import statsmodels.formula.api as smf
df_train, df_test = train_test_split(tips, test_size = 0.25, random_state=1)
smod = smf.ols(formula = 'tip~ total_bill + C(sex) + C(smoker) + C(day) + C(time)', data=df_train)
result = smod.fit()
print(result.summary()) #Note that the performance metrices are based on the training data.
# make predictions on the test data
y_pred = result.predict(df_test[['total_bill','sex','smoker','day','time']])
# getting performance on test data
print("Test data mean squared error: %.2f"
      % mean_squared_error(df_test.tip, y_pred))
 # [Out]: Test data mean squared error: 1.38
print('R square: %.2f' % r2_score(df_test.tip, y_pred))
# [Out]: R square: 0.45

```

### SAS
For reference, we illustrate how it is done in SAS.       
<div class="code-head"><span>code</span>OLS with Categorical Variable Using PROC GLM.sas</div>

```sas
proc glm data=tips;
   class sex smoker day time;         
   model tips = sex smoker day time total_bill size/ solution;
   ods select ParameterEstimates;
quit;
```
If we want to use PROC REG instead, then we will need to encode the dummies.

<div class="code-head"><span>code</span> PROC REG.sas</div>

```sas
proc glmmod data=tips outdesign=GLMDesign outparm=GLMParm NOPRINT;
   class sex smoker day time;
   model tips = sex smoker day time total_bill size;
run;
proc print data=GLMDesign; run;
proc print data=GLMParm; run;
ods graphics off;
proc reg data=GLMDesign;
   DummyVars: model tips = COL2-COL6 total_bill size;
   ods select ParameterEstimates;
quit;
/* same analysis by using the CLASS statement */
proc glm data=tips;
   class sex BP_Status;              /* generates dummy variables internally */
   model tips = sex smoker day time total_bill size/ solution;
   ods select ParameterEstimates;
quit;
```

