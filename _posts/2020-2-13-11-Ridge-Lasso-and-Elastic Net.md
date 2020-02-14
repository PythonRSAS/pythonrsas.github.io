---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Ridge, Lasso and Elastic Net"
description: In progress
author: Sarah Chen
image: images/posts/photos/IMG-0632.jpg
---

**Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia consequuntur, provident nemo soluta similique, maiores sit dicta doloremque facere laudantium [Keras](https://keras.io/){:target="_blank"} Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque neque totam voluptatem porro accusantium id.**

<figure> 
   <img src="{{"/images/posts/photos/IMG-0632.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 
When data meets OLS assumptions, such as no-multicollinearity and linear relationship between feature and target, we will do just fine with OLS.  When we don't have that many variables, overfitting is not that much a concern either.  

**multicollinearity**: While multicollinearity mathmatically is the matter of the covariance matrix and does not cause predictions to be wrong, severe multicollinearity can cause estimates of coefficients to be unstable, or even change signs.  
**overfitting**: the more overfitted a model is to the training data, the less capable it becomes for future data.   With so many features and not quite enough observations, it is easy to overfit while not getting the most accurate model.

One way to reduce overfitting and mitigate mutlicollinearlity is to penalize the weights (coefficients) by adding a function of them to the least squares loss function and to minimize the whole thing.  

constaining the weights adding a scaled (the scaler is a tuning parameter, often called alpha or lambda) sum of the weights (lasso), or sum of squared weights (ridge), or a combination of the weights and squared weights (elastic net) or sum of weighted weights (adatpive lasso), to the objective loss function (recall that OLS objective loss function is to minimize the squared errors).

When lambda/alpha is zero, the algorithm is back to OLS. So, regularized linear regression is a generalized OLS.

For some reason, the added terms are called regularizers. With the regularizers added, the objective function is no longer unbiased.  But the benefit is that we can reduce overfitting and instability of the model
Ridge, Lasso   (aka ‘least absolute shrinkage and selection operator’) and Elastic Net are the most common types of linear model with regularization.

Ridge, Lasso  (aka ‘least absolute shrinkage and selection operator’) and Elastic Net are the most common types of linear model with regularization. 
 - Ridge:  multiply the sum of squared (L2) coefficients/ parameters/ weights
 - Lasso: coefficients/ parameters/ weights are not squared (L1), but taken as absolute values
 - Elastic net is a combination of ridge and lasso

All three methods aim to capture signal over noise.   The regression coefficients for unimportant variables are shrunk or reduced to zero which effectively removes them from the model and produces a simpler model that selects only the most important predictors.

The image below is from Hastie, Tibshirani, & Friedman's book, which reminded me of my first year calculus at Columbia University: the solution of the Lagrangian is when the two contours are tangent to each other. 

<figure> 
   <img src="{{"/images/posts/lasso-ridge.PNG"| relative_url}}" width="600"> 
   <figcaption>Source: Hastie, Tibshirani, & Friedman (2009)</figcaption>
</figure> 


### Illustration of the Problem

Before presenting the solutions, let's illustrate the problem with multicollinearity just for fun, even if we understand it theoretically. 

We are making up 3 variables that are *highly correlated relative to the noise we added*.

Using OLS, we got negative coefficients for the first variable.
   
<div class="code-head"><span>code</span>multicollinearity problem.py</div>

```python
import numpy as np
size = 20
x1 = np.random.random(size)
x2 = x1 + np.random.random(size)
x3 = x1 + np.random.random(size)
y = x1* 0.5 + x2 * 0.4 + x3 *3 + 2*np.random.random(size)
print(np.corrcoef(x1,x2))
# [[1.        0.6526465]
#  [0.6526465 1.       ]]
plt.plot(x1,y, x2,y, x3,y, linestyle="", marker="o")
plt.show()
X = np.vstack((x1,x2,x3)).T
model = LinearRegression()
model.fit(X,y)
print(model.coef_)
# [-0.43193674  1.25814033  2.76525919]
```
<figure>
  <img src="{{ "/images/posts/multicollinearity.PNG" | relative_url }}" width="600">
  <figcaption>A made-up problem</figcaption>
</figure>

### Ridge

Ridge regression is also called L2 regularization.  If you look it up in wikipedia, you will find it as ["Tikhonov-Phillips regularization"](https://en.wikipedia.org/wiki/Tikhonov_regularization), where Tikhonov is the name of Soviet and Russian mathematician Andrey Tikhonov. Tikhonov proposed this method of regularization of ill-posed problems such as multicollinearity in around 1940's.  

In the simplest case, the problem of a near-singular moment matrix (covariance matrix) is dealt with by adding small positive numbers to the diagonals (which are the variances). 

The OLS least square problem becomes the following:
<figure>
  <img src="{{ "/images/posts/ridge.PNG" | relative_url }}" width="600">
  <figcaption>Ridge Regression Least Squares</figcaption>
</figure>

In general, the method provides improved efficiency in parameter estimation problems in exchange for a tolerable amount of bias (see bias–variance tradeoff).

Ridge regression will keep all the variables while reducing (shrink) their sizes.  The higher the shrinkage, the higher the bias, and the lower the variance- there is a trade-off.  

As it was the earliest regularization technique among the three, it is available in SAS PROC REG. 

Listing below would have otherwise been an OLS <code class="coding">PROC REG</code> except with <code class='coding'>RIDEGE =0 TO 0.01 BY 0.001</code>.  <code class='co'>RIDEGE</code> here stands for the scaler to be multiplied to the L2 norms.  When it is 0, it is back to original OLS.  We can specify a set of values to try, and in this case, from 0 to 0.01 with increments of 0.001. 

<div class="code-head"><span>code</span>ridge regression.sas</div>

```sas
ODS GRAPHICS ON;
PROC REG DATA = train OUTVIF OUTEST = b RIDEGE =0 TO 0.01 BY 0.001;
MODEL y = x;
RUN;
```

Python <code class="coding">sklearn.linear_model</code> provides Ridge and RidgeCV classes, where the latter includes cross validation. 

Using ridge regression with alpha of 0.1, we get the coefficients back to the right signs and close to what we expected.  

<div class="code-head"><span>code</span>ridge regression.py</div>

```python
>>> from sklearn.linear_model import Ridge
>>> import numpy as np
>>> model = Ridge(alpha=1.0)
>>> model.fit(X, y)
>>> model.coef_
# Out: array([0.53831271, 0.3955434 , 2.02971427])
```
Since there are no p-value related metrics in sklearn for us to assess quality of the estimates, <code class="coding">RidgeCV</code>, the cross validation version is provided. 

Its use is similar to Ridge or other linear models. 

<div class="code-head"><span>code</span>ridge regression with cross validation.py</div>

```python
>>> from sklearn.linear_model import RidgeCV
>>> model = RidgeCV()
```
The default signiture of <code class="coding">RidgeCV</code> object is:
> RidgeCV(
    ['alphas=(0.1, 1.0, 10.0)', 'fit_intercept=True', 'normalize=False', 'scoring=None', 'cv=None', 'gcv_mode=None', 'store_cv_values=False'],
> )

 - alphas is the default list of alphas.  As the list of alphas provided by the default has only 3 values, it may be adviserable to run the default version, and then supply a longer list of alphas closer to the one that was chosen in the first run.  
 - cv : is optional for the cross-validation splitting strategy.  The default is None, to use the efficient Leave-One-Out cross-validation (aka “Generalized Cross-Validation” or, “LOOC”, or the “Jackknife”).
 - gcv_mode is an optional parameter that allows we to choose a mode to use for Generalized Cross-Validation: {None, 'auto', 'svd', eigen'}

<div class="code-head"><span>code</span>Ridge Regression Coefficients.py</div>

```python
>>> n_alphas = 100
>>> alphas = np.logspace(5, -3, n_alphas)

>>> model  = RidgeCV(cv=5, normalize=False, alphas=alphas)
# fit model
>>> model.fit(X_train,y_train)

>>> print("The best alpha: %.3f" % model.alpha_)
# [Out]: The best alpha: 9.112

>>> y_train_pred = model.predict(X_train)
>>> y_test_pred = model.predict(X_test)

>>> # print variable names and regression coefficients
>>> coefficients = pd.DataFrame({'X':dataset.feature_names, 'Coef':model.coef_})
>>> coefficients.iloc[(-np.abs(coefficients['Coef'].values)).argsort()] 
# [Out]:
#           X      Coef
# 5        RM  3.453538
# 12    LSTAT -3.378018
# 7       DIS -2.543855
# 10  PTRATIO -1.961803
# 8       RAD  1.708400
# 9       TAX -1.595832
# 4       NOX -1.360119
# 0      CRIM -0.859517
# 1        ZN  0.794836
# 11        B  0.555400
# 2     INDUS  0.236742
# 6       AGE -0.231184
# 3      CHAS  0.100041
>>> print("Intercept is %.3f" % model.intercept_)
# [Out]: Intercept is 22.762
```

We can see the coefficient progression as alpha changes as in plot below (view from right to left).

The coefficients shrink gradually to zero once alpha is large enough.  Notice that none of the coefficients goes to zero before others.   This is the characteristic of ridge regression: it keeps all variables.  
<figure>
  <img src="{{ "/images/posts/Ridge Coefficients as a Function of the Regularization.PNG" | relative_url }}" >
  <figcaption>Ridge Coefficients as a Function of the Regularization</figcaption>
</figure>

<div class="code-head"><span>code</span>ridge regression.sas</div>

```sas
PROC IMPORT OUT = lib_name.dsn DATAFILE ="/boston.csv DBMS=csv REPLACE;
RUN;

ODS GRAPHICS ON; 
PROC REG DATA = boston OUTVIF OUTEST = b RIDEGE =0  0.001 0.01 0.1 1 
MODEL MEDV = CRIM ZN INDUS CHAS NOX RM AGE DIS RAD TAX PTRATIO B LSTAT; 
RUN;

ODS GRAPHICS OFF;
 
```
If we look at the output dataset named B, we will see there are two rows of information for each alpha (ridge): one row for coefficients and the other is VIF for each parameter.  
The coefficients from the SAS PROC REG corresponds to exactly the above. 

```python
from sklearn.datasets import load_boston
dataset =load_boston()
X =dataset.data
y=dataset.target
clf = RidgeCV(normalize=True,alphas=[1e-3, 1e-2, 1e-1, 1]).fit(X, y)
clf.coef_
print(clf.alpha_)
print(clf.score(X,y))
print(clf.coef_)
coef =pd.DataFrame(zip(dataset.feature_names,clf.coef_)) #match SAS closely
# 0.01 (alpha)
# 0.7403788769476067  (R square)
```

|    | 0       |             1 |
|---:|:--------|:--------------|
|  0 | CRIM    |  -0.103542    |
|  1 | ZN      |   0.0434058   |
|  2 | INDUS   |   0.00519961  |
|  3 | CHAS    |   2.74631     |
|  4 | NOX     | -16.6256      |
|  5 | RM      |   3.86519     |
|  6 | AGE     |  -0.000341086 |
|  7 | DIS     |  -1.41355     |
|  8 | RAD     |   0.269159    |
|  9 | TAX     |  -0.0105767   |
| 10 | PTRATIO |  -0.934596    |
| 11 | B       |   0.00928759  |
| 12 | LSTAT   |  -0.515911    |

#### Ridge Regression as Classifier

It is worth mentioning that ridge regression (a variant of OLS) can also be used for classifying. 

This classifier is sometimes referred to as a [*Least Squares Support Vector Machines with a linear kernel*](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression).

This classifier first converts binary targets to **{-1, 1}** and then treats the problem as a regression task, optimizing the same objective as above. 

> ["It might seem questionable to use a (penalized) Least Squares loss to fit a classification model instead of the more traditional logistic or hinge losses."](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)

> However in practice all those models can lead to similar cross-validation scores in terms of accuracy or precision/recall, while the penalized least squares loss allows for a very different choice of the numerical solvers with distinct computational performance profiles.

The predicted class corresponds to the sign of the regressor’s prediction, meaning that one class corresponding to predicted positive numbers whereas the other class correspond to predicted negative numbers.  

For multiclass classification, the problem is treated as multi-output regression, and the predicted class corresponds to the output with the highest value.


The <code class="coding">RidgeClassifier</code> can be significantly **faster** than e.g. LogisticRegression with a high number of classes, because it is able to compute the projection matrix only once.

### Lasso

[Lasso](https://en.wikipedia.org/wiki/Lasso_(statistics)) (“least absolute shrinkage and selection operator” was originally introduced in geophysics literature in 1986, and later independently rediscovered and proposed by Robert Tibshirani in 1996, about 50 years after ridge regression. 

It is also known as L1 regularization as the regularizer is L1-norm of the coefficients, multiplied by a scaler. 
<figure>
  <img src="{{ "/images/posts/ols_l1_regularizer.PNG" | relative_url }}" width="400">
  <figcaption>ols_l1_regularizer</figcaption>
</figure>

Unlike ridge regression, which keeps all variables, lasso keeps a subset of them.  
Because of this, lasso is often used for variable or model selection.

Before lasso, stepwise selection was the most popular method for variable selection while ridge was the most popular method for accuracy.  

The advantage of lasso over ridge is model interpretation as only the more important variables are kept.  

However, if several variables are equally important and are highly correlated, lasso will arbitrarily keep one.   So, this can be seen as a disadvantage as well, depending on the model requirements. 

It is worth noting that as a variant of OLS, lasso regularization can be applied to a wide variety of statistical and machine models including generalized linear models. 

#### SAS GLMSELECT
 
Lasso has been available in SAS <code class="coding">PROC GLMSELECT</code> since version 2008 (or possibly earlier). 

SAS PROC GLMSELECT is a powerful and versatile go-to tool for variable/model selection.   It requires few lines of code and provides comprehensive results in tables and plots, and is very well documented.  

Given the choice, we would prefer to use PROC GLMSELECT on lasso over Python (my non-biased opinion as I have used both in depth)

Below is the summary of the main features from SAS/STAT® 14.3 User’sGuide.  It is very impressive.  

**Model speciﬁcation supports**
 - different parameterizations for classiﬁcation features
 - *any degree of interaction* (crossed features) and nested features 
 - hierarchy among features 
 - training, validation, and testing split
 - constructed features including spline and multimember feature 


 **Selection Control provides**
 - multiple feature selection methods 
 - enables selection from a very large number of features (tens of thousands) 
 - offers selection of individual levels of classiﬁcation features 
 - a variety of selection criteria 
 - stopping rules based on a variety of model evaluation criteria 
 - LOOV, k-fold cross validation, and k-fold external cross validation 
 - supports *resampling* and *model averaging* 


**Display and Output produces**
 - plots of selection process 
 - predicted values and residuals 
 - the design matrix 
 - macro variables containing selected models 
 - supports parallel processing of <code class="coding">BY</code> groups 
 - supports multiple <code class="coding">SCORE</code> statements

<figure>
  <img src="{{ "/images/posts/glmselect-selection.PNG" | relative_url }}" width="600">
  <figcaption>SAS PROC GLMSELECT-selection</figcaption>
</figure>

<figure>
  <img src="{{ "/images/posts/glmselect-choose.PNG" | relative_url }}" width="600">
  <figcaption>SAS PROC GLMSELECT-choose</figcaption>
</figure>


The entire path of Lasso estimates for all values of the shrinkage parameter can be efficiently interpolated through the least angle regression (LARS) algorithm proposed by Efron and others around 2004 as an adoption of the “homotopy method” method from Osborne, Presnell, and Turlach (2000).   LARS is how lasso is implemented in SAS GLMSELECT. 

<div class="code-head"><span>code</span>lasso in glmselect.sas</div>

```sas
ODS GRAPHICS ON;
>>> PROC GLMSELECT DATA = train_data
  PLOTS(STEPAXIS=NORMB) = COEFFICIENTS;
  MODEL y = x/SELECTION=LASSO(STOP=NONE CHOOSE = SBC AIC);
RUN;
ODS GRAPHICS OFF;
```




<figure>
  <img src="{{ "/images/posts/constraint_shapes.PNG"| relative_url }}" width="600">
  <figcaption>constraint shapes</figcaption>
</figure>

### Adaptive lasso


More precisely, suppose that the response y has mean zero and the regressors x are scaled to have mean zero and common standard deviation. Furthermore, suppose you can ﬁnd a suitable estimator O ˇ of the parameters in the true model and you deﬁne a weight vector by w D 1=jO ˇj

<figure>
  <img src="{{ "/images/posts/lasso-adaptive.PNG" | relative_url }}" width="400">
  <figcaption>lasso-adaptive</figcaption>
</figure>

, where
 0. Then the adaptive LASSO regression coefﬁcients ˇ D .ˇ1;ˇ2;:::;ˇm/ are the solution to the constrained optimization problem
Model-Selection Methods F 4031
minjjyXˇjj2 subject to
m X jD1
jwjˇjj t


Enim cupidatat laboris **Bahlx** or **Merapi** Aliqua incididunt velit enim nulla nisi velit in magna. Lorem ipsum laboris veniam nostrud proident dolor fugiat . (Commodo irure eiusmod quis elit labor reprehenderit.). So, Ad cupidatat dolore esse nostrud duis deserunt veniam enim nostrud.
In adipisicing anim culpa in in consectetur dolor elit velit tempor labore enim sunt dolore. [here](https://github.com){:target="_blank"}.

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
