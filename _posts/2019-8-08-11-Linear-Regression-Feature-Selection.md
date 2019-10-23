---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Linear Regression Feature Selection"
description: Eu est laboris consectetur ut consequat do ullamco ut incididunt incididunt velit laboris nostrud exercitation in velit sit.
author: Sarah Chen
image: https://drive.google.com/uc?id=1crVhO4CHemFakRIxXYYo8HnfO-Z7sc1A
---
### Linear Regression
“Simple can be harder than complex: You have to work hard to get your thinking clean to make it simple. But it’s worth it in the end because once you get there, you can move mountains.” 
― Steve Jobs 

Linear models are used in almost everywhere, including in deep learning neural network models .   There are many variations of linear regression models: ordinary least squares linear regression, regularized OLS linear regression fitted by minimizing a penalized version of the least squares cost function, polynomial regression, generalized linear regression, linear models that use different error definitions, linear regression learned using gradient descent, and more.    

In many business contexts, the goal of model selection is interpretability and business intuition with acceptable accuracy.  Linear models are often preferred to other more sophisticated models for its strength in interpretation and stable performance.   It depends on the purpose, you may find Python, R, and SAS are all very useful.  If you are using statistical learning and want results fast and stable.

Before going further, it is important to distinguish linear regression and the least squares approach.   Although the terms "least squares" and "linear model" are closely linked, they are not synonymous.   Linear model refers to model specification being a weighted sum of the parameters for a continuous target variable such as y = a + bx.   Whereas least squares approach is a model fitting method, which is to minimized the sum of squared errors.   

Linear regression models can be fitted in other ways, such as least absolute deviations regression, or by minimizing a penalized version of the least squares cost function as in ridge regression (L2-norm penalty), lasso (L1-norm penalty) and elastic net (L1 and L2).  
Conversely, the least squares approach can be used to fit models that are not linear models. 

We will start small, with a one-feature dataset, and present graphic presentation of linear regression on the four subsets of the Anscomebe quartet  dataset.   

In example below, we use the seaborn library to plot the linear regression plots  on the four stylized subsets of Anscomebe data.  
• The first set of data appears to be the typical linear relationship and follow the assumption of normality.   
• The second set of data does not seem normally distributed.  A quadratic line would be a better fit. 
• The third set of data is linear, but is affected by one outlier.  Unless the outlier is important to keep, one should consider robust regression. 
• The fourth set of data does not show any relationship between x and y, even though the Pearson linear correlation is large.  
<div class="code-head"><span>code</span> Linear Regression on the Anscomebe Quartet Dataset.py</div> 
>>> import seaborn as sns
>>> anscombe = sns.load_dataset("anscombe")
>>> anscomebe.head()
[Out]: 
  dataset     x     y
0       I  10.0  8.04
1       I   8.0  6.95
2       I  13.0  7.58
3       I   9.0  8.81
4       I  11.0  8.33

>>> sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data= anscombe, palette="muted", scatter_kws={"s": 50, "alpha": 1})
Figure 5- 1. Linear Regression on the Anscomebe Dataset
 
In the following example shows that the summary statistics are nearly identical between the four sets of data in the Anscomebe dataset, including mean, median, standard deviation, Pearson linear correlation .   But their rank correlations are quite different, as indicated by the Spearman and Kendall’s tau. 
>>> anscomebe.groupby('dataset')['x','y'].agg([np.mean, 
np.median,np.std]).round(3)
[Out]:
           x                    y
        mean median    std   mean median    std
dataset
I        9.0    9.0  3.317  7.501   7.58  2.032
II       9.0    9.0  3.317  7.501   8.14  2.032
III      9.0    9.0  3.317  7.500   7.11  2.030
IV       9.0    8.0  3.317  7.501   7.04  2.031

<div class="code-head"><span>code</span> Correlations Between x and y from the Anscomebe Quartet Dataset py</div> 
>>> from scipy.stats import pearsonr

>>> for i in ['I','II','III', 'IV']:
>>> print("Pearson linear correlation")
>>> for i in ['I','II','III', 'IV']:
>>>     df = anscomebe[anscomebe.dataset=='%s' %i]
>>>     print("%s :" %i + "%.3f" % pearsonr(df.x,df.y)[0] + " with p-value %.3f" %pearsonr(df.x, df.y)[1])

[Out]:
Pearson linear correlation
I :0.816 with p-value 0.002
II :0.816 with p-value 0.002
III :0.816 with p-value 0.002
IV :0.817 with p-value 0.002

# spearman rank correlation
>>> print("Spearman rank correlation")
>>> for i in ['I','II','III', 'IV']:
>>>     df = anscomebe[anscomebe.dataset=='%s' %i]
>>>     print("%s :" %i + "%.3f" % spearmanr(df.x,df.y)[0] + " with p-value %.3f" %spearmanr(df.x, df.y)[1])

[Out]: 
Spearman rank correlation
I :0.818 with p-value 0.002
II :0.691 with p-value 0.019
III :0.991 with p-value 0.000
IV :0.500 with p-value 0.117

# Kendal tau correlation
>>> print("Kendal tau correlation")
>>> for i in ['I','II','III', 'IV']:
>>>     df = anscomebe[anscomebe.dataset=='%s' %i]
>>>     print("%s :" %i + "%.3f" % kendalltau(df.x,df.y)[0] + " with p-value %.3f" %kendalltau(df.x, df.y)[1])
[Out]:
Kendal tau correlation
I :0.636 with p-value 0.006
II :0.564 with p-value 0.017
III :0.964 with p-value 0.000
IV :0.426 with p-value 0.114

In the example below below, we first import the data and get an overall statistical summary using PROC MEANS, and get the three types of correlations as in Python.  
<div class="code-head"><span>code</span> Anscomebe Quartet Dataset Using SAS.sas</div> 
>>> PROC IMPORT
 DATAFILE = "/folders/myfolders/data/anscomebe.csv"
 OUT = lib_name.anscomebe (keep=dataset x y)
 DBMS = csv
 REPLACE;
 GETNAMES = YES;
 GUESSINGROWS=40;
RUN;

PROC MEANS DATA= lib_name.anscomebe MAXDEC=2 n std min p25 p50 p75 max;
CLASS dataset;
RUN;

[Out]:
dataset N Obs Variable  N Std Dev Minimum 25th Pctl 50th Pctl 75th Pctl Maximum
I 11  x
y 11
11  3.32
2.03  4.00
4.26  6.00
5.68  9.00
7.58  12.00
8.81  14.00
10.84
II  11  x
y 11
11  3.32
2.03  4.00
3.10  6.00
6.13  9.00
8.14  12.00
9.13  14.00
9.26
III 11  x
y 11
11  3.32
2.03  4.00
5.39  6.00
6.08  9.00
7.11  12.00
8.15  14.00
12.74
IV  11  x
y 11
11  3.32
2.03  8.00
5.25  8.00
5.76  8.00
7.04  8.00
8.47  19.00
12.50

PROC CORR DATA= lib_name.anscomebe PEARSON SPEARMAN KENDALL;
BY dataset;
RUN;

   
We will now dive into linear regression models.     
### Data Background
  For ease of accessibility for readers from different backgrounds  and purpose of illustration, we will use some of the most commonly known datasets that are very small and cleaned. 
super clean, super meaningful features for the era (most real world data is very far from this)
it was well prepared by economists
<div class="code-head"><span>code</span> Boston Housing Dataset.python</div>  
>>> from sklearn.datasets import load_boston
>>> dataset = load_boston()
>>> X, y = dataset.data, dataset.target
>>> df = pd.DataFrame(X, columns = dataset.feature_names)
>>> df['y'] = dataset.target

Feature Names: 
NAME  MEANING
CRIM   Per capita crime rate by town
ZN   Proportion of residential land zoned for lots over 25,000 sq. ft
INDUS  Proportion of non-retail business acres per town
CHAS   Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
NOX  Nitric oxide concentration (parts per 10 million)
RM   Average number of rooms per dwelling
AGE  Proportion of owner-occupied units built prior to 1940
DIS  Weighted distances to five Boston employment centers
RAD  Index of accessibility to radial highways
TAX  Full-value property tax rate per 10,000
PTRATIO  Pupil-teacher ratio by town
B  1000(Bk — 0.63)², where Bk is the proportion of [people of African American descent] by town
LSTAT  Percentage of lower status of the population
MEDV   this is in dataset.target, which is the median value of owner-occupied homes in $1000s
Because this is a super clean and beautifully collected dataset, the most difficult and time-consuming job of data cleaning and analysis steps are skipped.   But don’t you get the idea that model development is this easy.  Please see case study chapters on examples of data cleaning and analysis. 
### Feature Selection
Feature selection is an integral part of model development and model selection, and often it is synonymous with model selection.   It depends not only on model fit but also interpretation and model purpose.  For example, some of the features in the Boston Housing dataset would not be allowed to be in any bank or insurance models as they will be considered discriminatory without question.    Here we will only discuss the common technical aspects as interpretation and model purpose are situation dependent.   

• Subset selection methods (available in REG, GLMSELECT, HPREG, LOGISTIC, PHREG, HPGENSELECT procedures)
o Forward
o Backward
o Stepwise
• Shrinkage and regularization (GLMSELECT)
o Lasso
o Adaptive LASSO
o Elastic net
• Dimension reduction (PRINCOMP, PLS)
o PCA
o Partial least squares
Unlike the subset selection method, the shrinkage methods do not explicitly select variables.  If shrinkage is large enough, it sets some coefficients to close to zero.  They simultaneous estimate coefficients and reduce overfitting.  
The shrinkage and regularization method is a derivative of the least squares method by adding on linear sum of the coefficients as penalty.  Hence the sum of errors not only depend on the errors due to predictions but also on the size of the coefficients.  This is in effect biased estimator.  
The PROC GLMSELECT has an array of customizing options.   
We will use the well-known Boston Housing dataset to illustrate. 
### Correlation method
While seaborn heatmap is prettier, we use 
<div class="code-head"><span>code</span> Linear Correlation.py</div>   
>>> df.corr().round(2).style.background_gradient()
>>> df.corr().sort_values('y').iloc[:,-1]
[Out]:
LSTAT     -0.74
PTRATIO   -0.51
INDUS     -0.48
TAX       -0.47
NOX       -0.43
CRIM      -0.39
RAD       -0.38
AGE       -0.38
CHAS       0.18
DIS        0.25
B          0.33
ZN         0.36
RM         0.70
y          1.00
Name: y, dtype: float64
>>> corr =df.corr().round(2)
>>> corr['abs_corr']=corr.y.abs().drop('y')
>>> corr_y = corr.sort_values('abs_corr', ascending=False).loc[:,['y']].drop('y',axis=0)
>>> corr_y
[Out]:
            y  
LSTAT   -0.74  
RM       0.70  
PTRATIO -0.51  
INDUS   -0.48  
TAX     -0.47  
NOX     -0.43  
CRIM    -0.39  
AGE     -0.38  
RAD     -0.38   
ZN       0.36   
B        0.33   
DIS      0.25   
CHAS     0.18   

>>> fig, ax = plt.subplots()
>>> mask = np.zeros_like(corr, dtype =np.bool)
>>> mask[np.tril_indices_from(mask)] =True
>>> cmap =sns.diverging_palette(350,150, as_cmap=True)
>>> sns.heatmap(corr,cmap=cmap, linewidths=1, vmin=-1, 
vmax =1, square=True, cbar=True, center=0, ax=ax, mask=mask)
Figure 5- 2. Feature Correlation Heatmap
 
From linear correlation, the most important features are:
LSTAT: Percentage of lower status of the population
RM: Average number of rooms per dwelling
PTRATIO: Pupil-teacher ratio by town
Note:
In linear regression, one of the things to avoid is strong multi-collinearity.  
Correlation Between Features
<div class="code-head"><span>code</span> Correlation Between Features.py</div>   
>>> corr_abs = corr.abs().unstack()
>>> sorted = corr_abs.sort_values(kind="quicksort", ascending=False)
>>> corr_top_pairs = sorted[sorted.values!=1] #has duplicates  
[Out]:
RAD      TAX        0.910228
TAX      RAD        0.910228
NOX      DIS        0.769230
DIS      NOX        0.769230
INDUS    NOX        0.763651
NOX      INDUS      0.763651
AGE      DIS        0.747881
DIS      AGE        0.747881
LSTAT    y          0.737663
y        LSTAT      0.737663
AGE      NOX        0.731470
NOX      AGE        0.731470

### Variable Selection
Python sklearn doesn't have a forward selection algorithm. However, it does provide recursive feature elimination, which is a greedy feature elimination algorithm similar to sequential backward selection.   Suggest hypotheses about the causes of observed phenomena
1.  Support the selection of appropriate statistical tools and techniques
2.  Provide a basis for further data collection through surveys or experiments
 Statistics and visual analysis both are key tools.
https://datascience.stackexchange.com/questions/937/does-scikit-learn-have-forward-selection-stepwise-regression-algorithm
 
Method Description Forward selection Starts with no effects in the model and adds effects Forward swap Before adding an effect, makes all pairwise swaps of in-model and out-of-model effects that improve the selection criterion Backward elimination Starts with all effects in the model and deletes effects Stepwise selection Starts with no effects in the model and adds or deletes effects Least angle regression Starts with no effects and adds effects; at each step, O ˇs shrink toward zero Lasso Constrains the sum of absolute O ˇs; some O ˇs are set to zero, others shrink toward zero





### Linear Regression and Least Squares

Before going further, it is important to distinguish linear regression and the least squares approach.   

Although the terms "least squares" and "linear model" are closely linked, they are not synonymous.   Linear model refers to model specification being a weighted sum of the parameters for a continuous target variable such as y = a + bx.   Whereas least squares approach is a model fitting method, which is to minimized the sum of squared errors.   

Linear regression models can be fitted in other ways, such as least absolute deviations regression, or by minimizing a penalized version of the least squares cost function as in ridge regression (L2-norm penalty), lasso (L1-norm penalty) and elastic net (L1 and L2).  

Conversely, the least squares approach can be used to fit models that are not linear models. 

enim sunt dolore. [here](https://github.com){:target="_blank"}.

### Dolor pariatur velit velit parluptate nulla cupidatat.

In consequat anim sunt excepteur. [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning){:target="_blank"} problem.

<figure>
  <img src="{{ "/images/posts/laptop.jpg" | relative_url }}">
  <figcaption>Figure 1. Generic Laptop Screen</figcaption>
</figure>

Lorem ipsum deserunt consequat. **java tengh** Ad ex quis dolor oe esse qui. (**random** or **lorem values**). Lorem ipsum dolor sit amet, sicing elit. Error autem dolor dolores, Modi temporibus aitis? (**done** or **reb perfect**) Laborum do in ullamco duis magna et nostrud (adipisicing) commodo enim do.

Ex voluptate. **Blablasdf** and **Rdfdsgga**.

* **Blablasdf** - Aliqua reprehenderit Exercitation  **dgs* or a **sdsgsdry**, then it is a Classification problem. *Ex: Predicting the name of a flower species.*
* **Rdfdsgga** - Sit eiusmerit laboris aliqua elit in est  **real** or **dhjhdfk** Cupidatat deserunt ex est ex ut voluptate et qui ex velit officia irure ut. *Ex: Anim eu reprehenderit nulla sunt ut laboris.*

Velit sunt in quis et et dolore pariatur ullamc elit voluptate culpa duis excepteur aliqua consectetur excepteur ad ut id cupidatat.

<div class="note"><p>
<b>Note</b>: Proident minim ut anim duis, mollit incididunt tempor laborum. <a href="https://www.coursera.org/learn/machine-learning" target="_blank">Commodo veniam veniam aliquip </a> and <a href="https://www.coursera.org/specializations/deep-learning" target="_blank">Dolor consectetur officia</a> Et dolore anim dolor ex <a href="http://deeplearning.stanford.edu/tutorial/" target="_blank">Stanford University's</a>.
</p></div>

Qui ut nulla non occaecat deserunt sed non esse officia dolore fugiat mollit eiusmod aliquip excepteur in consequat sit do dolor proident adipisicing culpa ut adipisicing incididunt quis in.

### Sint ex magna incididunt in ir

> Ut magna Consequat aute volupthenderit incididunt consequat amet. **Dfsd** and **Rfskldf Posoe**.

 Consequat aute volupthenderit! Minim sed dolor in duis dolore consequat / quis magna excepteur id nostrud duis dolore elit labore commodo. Quis aliquip laboris magna in anim id do sit sint. Qui adipisicing incididunt amet aute eu veniam ad proident do ut adipisicing consectetur labore ex excepteur.

* **Afsdd kifdgll** - Lorem, ipsum, nostrud ut, sed in aliqua do .
* **Asdfsdfsd ksohk** - Deserunt, qislla, culpa, laborum, fugiat.
* **Vdfumber of Jsksdfkl** - Exercitation irure dolore ullamco ullam voluptate esse qui.
* **Klsdlf of slll** - Tgkdfg lfgfgd fgkgdfl.
* **Ius ksdf fddd** - Exercitation eiusmod non in minim aliqua occaecat ut.

Reprehenderit ut [Google](https://www.google.com/){:target="_blank"} Excepteur sunt nisi anim. Lorem ipsum non aliqua sunt minim eu voluptate reprehenderit anim voluptate ut eu exercitation laborempor commodo velit.(last column in the dataset). Anim esse **Fugiat labore** Dolore consequat tempor deserunt.

* **1 = yes!** Excepteur et dolor commodo adipisicing s occaecat dolor.
* **0 = no!** tExcepteur et dolor no commodo adipisicing s occaecat dolor.

Nostrud ex non ea do elit dolore ut enim adipisicing cillum commodo sit proident quis Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta ipsa, ratione illo eius deleniti odio ipsum doloremque ut atque, recusandae asperiores enim accusantium distinctio quaerat blanditiis quidem, eaque ab voluptates.

<div class="code-head"><span>code</span>sample-from-python-org.py</div>

```python
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
fib(1000) = train_test_split(X, Y, test_size=0.33, random_state=seed)
```

* Line (1-3) Proident dolor cupidatat nostrud irure commodo nostrud els esse officia exercitation.
* Line (4-7) Sit irure ut ut id do culpa ullamco qui est.

### Nulla proident dolor cupidatat  deserunt eiusmod eu id ex.

Lorem ipsum sint ut labore fugiat eiusmod voluptate exercitana culpa dolore sit sint enim. Lorem ipsum in velit ex laborinisi dolor laboris sed do enim sit eu <span class="coding">Odkfsdy</span> dfsdgg.

We will use the above Deep Neural Network architecture which has a **sdfsdle yutm xvwe**, **2 pire xaq**.

Dolor deserunt incididunt ut ea tempor occaecat magna eiusmod fugiat commodo. Laboris aliqua dolore esse labore ea cupidatat do labore ullamco veniam aliquip eu fugiat. Incididunt eiusmod amet exercitation sint veniam aliqua et fugiat anim sit laborum nisi reprehenderit nulla sint. Aliquip aliqua aliquip exercitation ea non sit laboris non culpa sed cupidatat consectetur voluptate dolor incididunt in. In ad tempor culpa cillum in magna est veniam in aliqua anim.

Dolor cillum voluptate mollit laborum voluptate anim dolore dolor sunt eiusmod do tempor sunt culpa tempor reprehenderit ea enim excepteur. Ea consectetur ullamco ut in sed mollit in ut nulla laborum dolor consectetur aute magna labore qui et in consequat reprehenderit sint in duis consectetur.

<div class="code-head"><span>code</span>from-doc-site.py</div>

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

* Line (1), Lorem ipsum culpa labore  <span class="coding">import</span> Est occaecat ad laboris eimodo ut exercitation culpa ex.
* Line (2), Pariatur consectetur ut mollit in eu esse :
  * <span class="coding">[8]]</span>: Im occaecat aliquip eiusmod cupidatat in velit aute magna cupidatat
  * <span class="coding">raw</span>: Lorem ipsum ullamco est dolore magna ut pariatur exercitation ea esse anim labore.
  * <span class="coding">data</span>: specify whether <span class="coding">uniform</span> or  <span class="coding">normal</span>.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo quas ipsam, magnam vel architecto cumque deserunt inventore autem voluptatem minus molestias fuga unde corporis soluta quisquam sapiente consequatur, aut tempora labore id repellat omnis harum? Eveniet velit laboriosam, quas optio, enim iure nesciunt repudiandae hic temporibus facilis, corporis maxime qui quis esse nam? Quod, enim, odio? Sapiente blanditiis quisquam voluptatem fuga quod fugit molestiae illum dolor itaque id ipsam, quasi, quae repellendus error placeat impedit maxime qui nobis est veritatis.
