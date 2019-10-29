---
layout: post
tag : Machine Learning in Practice
category: "machine learning"
title: "Linear Regression Ridge Lasso ElasticNet"
description: Eu est laboris consectetur ut consequat do ullamco ut incididunt incididunt velit laboris nostrud exercitation in velit sit.
author: Sarah Chen
image: https://drive.google.com/uc?id=1crVhO4CHemFakRIxXYYo8HnfO-Z7sc1A
---

In this post, you will learn:

[Ridge, Lasso and Elastic Net](#Ridge,-Lasso-and-Elastic-Net)

[SAS](#SAS)

[Ridge](#Ridge)

[SAS](#SAS)

[Elastic Net](#Elastic-Net)

[SAS](#SAS)

Let's get started. 
<figure>
  <img src="{{ "/images/posts/alex-azabache.jpg" | relative_url }}">
  <figcaption>Photo by Alex Azabache</figcaption>
</figure>

<h3 id="Ridge,-Lasso-and-Elastic-Net">Ridge, Lasso and Elastic Net</h3>

Ridge, Lasso  (aka ‘least absolute shrinkage and selection operator’) and Elastic Net are enhancements or extensions of the OLS.  

They are the most common types of linear model selection methods using regularization. When data meets OLS assumptions, such as no-multicollinearity and linearly correlation between feature and target, we will do just fine with OLS.   

But, in reality, we have many features but often not that many observation , whether in problems such as tumor classifications, signal processing, image analysis, or credit risk management, insurance pricing, telecommunication, healthcare, insurance, retail, education, manufacturing, pharmaceuticals, and so on.   

Real world data almost always has multicollinearity.  With so many features and not quite enough observations, it is easy to overfit while not getting the most accurate model.

Source: Hastie, Tibshirani, & Friedman (2009)

All three methods aim to capture signal over noise. The regression coefficients for unimportant variables are shrunk or reduced to zero which effectively removes them from the model and produces a simpler model that selects only the most important predictors.  

This is the shrinkage process, and is done by treating the model parameters or weights as errors too (since they are kind of wrong too), except we still want them to be useful. They are added to the squared error function (loss function) after being scaled by a penalizing small number, most commonly called lambda , but is called “alpha” in sklearn, and more generally called “tuning parameter”.   

The coefficients are then computed as solutions to minimize the loss function. When lambda/alpha is zero, the algorithm is back to OLS. 
The differences between the three methods are:

•   Ridge:  multiply the sum of squared (L2) coefficients/ parameters/ weights

-   Lasso: coefficients/ parameters/ weights are not squared (L1), but taken as absolute values

-   Elastic net is a linear combination of both ridge and lasso
Limitations of LASSO:

1.  The LASSO is an automated process, which by default does not take into account anything outside of the data. 

2.  If the variables are strongly correlated with each other, the LASSO will arbitrarily select one of them, which may not be what we want.  We may prefer some of the ones that are left out. 

3.  Without a knowledgeble person, the LASSO regression will very likely produce unintuitive models.   

4.  There is no guarantee that the model LASSO selected is the best model.  


To find the model that gives the smallest estimated prediction error, the commonly used metrics are:

o   CP, AIC, SBC (Schwarz Bayesian criterion) (smaller the better)

o   adjusted R-square (larger the better)

o   RMSE

These metrics are computed on train-test-split validation data or k-fold cross validation.  

The rest is finding the right lambda or alpha. Bias increases and variance decrease as lambda increases. Cross validation and out of sample validation both have their advantages and disadvantages, and each has its own errors.    

Furthermore, cross validation can be computationally expensive for very large data. It is best to experiment and not take general guidance for granted.   

Another important detail to remember is to use the methods effectively the independent variables must be standardized to a mean of zero and a standard deviation of one.  Otherwise the penalizing the not fair.   Now we are ready to get into the action.   

<div class="code-head"><span>code</span> Boston Housing Dataset.py</div>
```python
>>> from sklearn.datasets import load_boston
>>> dataset = load_boston()
>>> df = pd.DataFrame(dataset.data, 
columns=dataset.feature_names)
>>> df['MEDV'] = dataset.target
>>> df.isnull().sum()

>>> df.info()
[Out]:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
CRIM       506 non-null float64
ZN         506 non-null float64
INDUS      506 non-null float64
CHAS       506 non-null float64
NOX        506 non-null float64
RM         506 non-null float64
AGE        506 non-null float64
DIS        506 non-null float64
RAD        506 non-null float64
TAX        506 non-null float64
PTRATIO    506 non-null float64
B          506 non-null float64
LSTAT      506 non-null float64
MEDV       506 non-null float64
dtypes: float64(14)
memory usage: 55.4 KB
>>> df.shape
[Out]:  (506, 14)
```
In the example below, we first import the libraries for the three regularizers, all using the built-in cross validation version.  

All these three have their counterparts that do not have built-in cross validation. The data is split into train and test, with 0.3 of the data for testing.  

The random_state seed is set to ensure that the data are randomly split the same way if run again.  After splitting, the training predictors are standardized, and the same standardization parameters from (mean and standard deviation) from training data, sc = StandardScaler().fit(X_train), are used to process testing data.   

<div class="code-head"><span>code</span> Import Libraries and Process Data.py</div>
```python
>>> from sklearn.model_selection import train_test_split
>>> from sklearn.linear_model import LassoLarsCV, RidgeCV, ElasticNetCV
>>> from sklearn.metrics import mean_squared_error
>>> from sklearn.preprocessing import StandardScaler
>>> y = dataset.target

# split data into train and test sets
>>> X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=.3, random_state=123)

# standardize X to have mean=0 and std=1
>>> sc = StandardScaler().fit(X_train)
>>> X_train = sc.transform(X_train)
>>> X_test = sc.transform(X_test) 
```
You can list all the feature names if you like.  But &x saves you the typing if there are hundreds of variables. 

<div class="code-head"><span>code</span> Import Libraries and Split Data in SAS.sas</div>
```sas
PROC IMPORT
 DATAFILE = "/folders/myfolders/data/boston.csv"
 OUT = lib_name.boston
 DBMS = csv
 REPLACE;
 GETNAMES = YES;
 GUESSINGROWS=100;
RUN;
/* method=srs, specifies that the data are to be split using simple random sampling */
>>> PROC SURVEYSELECT DATA= lib_name.boston SEED = 123456  OUTALL OUT=boston METHOD=srs SAMPRATE=0.33;
RUN;
Input Data Set  BOSTON
Random Number Seed  123456
Sampling Rate   0.33
Sample Size 167
Selection Probability   0.33004
Sampling Weight 3.02994
Output Data Set BOSTON

>>> PROC FREQ DATA = boston;
TABLE selected;
RUN;
[Out]: 
Selection Indicator
Selected    Frequency   Percent Cumulative
Frequency   Cumulative
Percent
0   339 67.00   339 67.00
1   167 33.00   506 100.00
>>> PROC CONTENTS DATA=lib_name.boston OUT=meta (KEEP=NAME WHERE=(NAME<>"MEDV")) NOPRINT; 
RUN ; 

>>> PROC SQL;
SELECT name into :X separated by ' '
FROM meta;
QUIT;

>>> DATA train test;
SET boston;
if SELECTED = 0 THEN OUTPUT train;
ELSE OUTPUT test;
RUN;
```
LASSO Regression has various model selection algorithms.  The LAR (aka ‘Least Angle Regression’) is similar to the forward selection method.   

It starts with no predictors in the model and sequentially adds one parameter at each step, terminating at the full least squares solution when all parameters have entered the model. 

At each step, it adds a predictor that is most correlated with the response variable and moves it towards least score estimate until there is another predictor to add to the model that is equally correlated with the model residual.  

Parameter estimates at any step are shrunk and predictors with coefficients that have shrunk to zero are removed from the model and the process starts all over again. We first the LassoLarsCV algorithm sklearn implementation to build regularized OLS model.   

According to the sklearn documentation , the object solves the same problem as the LassoCV object, except that, unlike the LassoCV, it finds the relevant alphas values using the Lars algorithm.  

Therefore, unlike Ridge or other types of Lasso, we do not need to feed it with a list of alphas. Comparing with LassoCV, the advantage of Lars is efficiency when there are fewer observations than features, i.e. wide data.   The disadvantage is that it is more fragile to strong multicollinear datasets.  
Its initial signature is:

```python
'fit_intercept=True', 'verbose=False', 'max_iter=500', 'normalize=True', "precompute='auto'", "cv='warn'", 'max_n_alphas=1000', 'n_jobs=None', 'eps=2.220446049250313e-16', 'copy_X=True', 'positive=False'],
)
```
The n_jobs option asks for number of CPUs to use during the cross validation, and is default at None. You can set n_jobs = -1 to run computations in parallel (if supported by your computer and its OS)

The normalize  option is set to True by default.  This is to ensure that the regressors X will be normalized before regression by subtracting the mean and dividing by the l2-norm (i.e. Euclidean distance).   

If we want to standardize instead of normalize, we are asked to use preprocessing.StandardScaler from sklearn before calling fit on an estimator with normalize=False.   However, this normalize option is ignored if fit_intercept = False . 

In the example followed, we choose to explicitly standardize to highlight the importance of scaling the data before running the regularized regression.   
In the example below, we first instantiate a LassoLarsCV object.  

The option precompute=False tells Python not to use a precomputed matrix. This option would be helpful with very large models, because the precomputed matrix can speed up calculations.   

After fitting the model, we ask to see what is the best alpha value that the model has chosen using model.alpha_.  This attribute cannot be requested before fitting the data because we did not provide the model with any alpha. As the number of non zero coefficients is still thirteen, no coefficients have been reduced to zero at this stage. 

<div class="code-head"><span>code</span> LassoLarsCV in Python sklearn.py</div>
```python
#specify the algorithm; normalize is set to False because we have standardize the data
>>> model=LassoLarsCV(cv=5, precompute=False, normalize=False)
#train and predict
>>> model.fit(X_train,y_train)
>>> print("The best alpha: %.3f" % model.alpha_)
[Out]: The best alpha: 0.013

>>> print("The number of non-zero coefficients is: %d" %(model.coef_ != 0).sum())
[Out]: The number of non-zero coefficients is: 13
>>> y_train_pred = model.predict(X_train)
>>> y_test_pred = model.predict(X_test)

>>> Interpretation = pd.DataFrame({'X':dataset.feature_names, 'Coef':model.coef_})
#Interpretation.sort_values('Coef', inplace=True)
>>> Interpretation.iloc[(-np.abs(Interpretation['Coef'].values)).argsort()]
[Out]:
          X      Coef
12    LSTAT -3.507695
5        RM  3.430050
7       DIS -2.731830
8       RAD  2.073213
10  PTRATIO -2.009655
9       TAX -1.935421
4       NOX -1.530160
0      CRIM -0.889461
1        ZN  0.864564
11        B  0.542693
2     INDUS  0.371024
6       AGE -0.179474
3      CHAS  0.061070
>>> print("Intercept is %.3f" % model.intercept_)
[Out]: 22.762
```
Note:

1.  To avoid information “leakage”, one should split data into train and test before applying standardizing.

2.  One should scale the test data using the same mean and standard deviation that are used to scale the training data. 

3.  In sklearn, preprocessing.StandardScaler() and preprocessing.scale produce the same standarization (z-scores). 

4.  The parameters all have intuitive signs.  This is probably not the case in most real world data.  Features with unintuitive signs would need to be removed in most business problems.  
 
<div class="code-head"><span>code</span> Regression Coefficients Progression for Lasso Paths.py</div>

```python
>>> log10_alphas = -np.log10(model.alphas_)

>>> plt.plot(log10_alphas, model.coef_path_.T, marker ='o', ms=8, alpha =0.5)
>>> plt.axvline(-np.log10(model.alpha_), linestyle='--', label='alpha CV')
>>> plt.ylabel('Model Coefficients')
>>> plt.xlabel('-log(alpha)')
>>> plt.title('%s'%title)
```
Below figure shows the standardized regression coefficient progression (y-axis) as the penalizing weight (x-axis) increases.  The graph is to be read from right to left.   

When alpha is small (hence -log(alpha) is large),  all the coefficients are in the model (right side of the plot).   As alpha increases, the coefficient estimates reduces to be zero one by one. The last one to die is the strongest predictor according to LASSO.  

Figure 5- 5. Regression Coefficients Progression for Lasso Paths
                                        
 
We may want to know beyond just the algorithm produces. For example, we may want to know if crosss validation process was volatile or not across the alphas tested, and across the folds in cross validation. LassoLarsCV provides a few useful attributes for under-the-hood examination:

•   cv_alphas_  are all the values of alpha along the pth for the different folds

•   mse_path_ are all the mean square error on left-out for each fold along the path for the alpha values in cv_alpha_

In the following example, We can look at the mean and standard deviation for the mse.   

<div class="code-head"><span>code</span> LassoLarsCV Average RMSE.py</div>
```python
 model.cv_alphas_.shape
[Out]: (66,)
>>> model.mse_path_.shape
Out: (66,5)
>>> print("Mean mse for Five Folds: %s" % np.mean(model.mse_path_, axis=0))
[Out]:
Mean mse for Five Folds: [28.70498093 41.41581256 33.07936675 39.46361877 29.06355728]
>>> print("Mean mse Across Folds for each alpha: %s" % np.mean(model.mse_path_, axis=1))
# full result omitted due to space
[Out]:
Mean mse Across Folds for each alpha: [22.56337675… 86.08580552 86.175048  ]

>>> index = np.where(model.cv_alphas_ == model.alpha_)
# mses of left-out fold with the least squred errors
>>> model.mse_path_[index, :]
Out:
array([[[16.06621525, 29.09077835, 19.71706883, 28.18076948,
         19.61510104]]])
# mean MSE across 5 folds with the least squared errors
>>> _mse_v = np.mean(model.mse_path_[index, :])
[Out]: mse value: 22.533987
<div class="code-head"><span>code</span> Plot LassoLarsCV Average RMSE for Different Alphas.py</div>
>>> title ="LassoLarsCV Average RMSE for Different Alphas"
# best alpha index value
>>> markers_on = [np.argwhere(model.cv_alphas_==model.alpha_)[0,0]]
# mark the best alpha
>>> plt.plot(model.cv_alphas_, np.mean(model.mse_path_**(1/2), axis=1), linestyle=None, marker='o', ms=5 ,markevery=markers_on)
>>> plt.xlabel("Alpha")
>>> plt.ylabel("Average RMSE for Each CV")
>>> plt.title('%s'%title)
```
In the following example, we compute performance measures of RMSE and R square, and plot the actual target against predicted target. The method model.predict(X_test) is used for calculating predicted target using the stored coefficients, while the method model.score is used to compute R square.  
As expected, RMSE is higher in test data than training data, and R square is lower in test data.  The good thing is that they are not that far off between train and test. 
<div class="code-head"><span>code</span> Lasso Regression Performance Testing and Plotting.py</div>

```python
>>> from sklearn.metrics import mean_squared_error, median_absolute_error

>>> # RMSE from training and test data
>>> train_rmse = (mean_squared_error(y_train, model.predict(X_train)))**(1/2)
>>> test_rmse = (mean_squared_error(y_test, model.predict(X_test)))**(1/2)

>>> print('Training RMSE: %.3f'% train_rmse)
>>> print('Testing RMSE: %.3f'% test_rmse)
[Out]: Training RMSE: 4.494
       Testing RMSE: 5.340

>>> # R-square from Training and test data
>>> rsquared_train=model.score(X_train,y_train)
>>> rsquared_test=model.score(X_test,y_test)

>>> print ('Training R-square: %.3f'% rsquared_train)
>>> print ('Testing R-square: %.3f'% rsquared_test)
[Out]: Training R-square: 0.765
       Testing R-square: 0.647
  
>>> title = "Lasso regression Predicted vs Actual on Test Data"
>>> y_max =np.max(y)
>>> f, ax =plt.subplots(1, 1)
>>> ax.scatter(y_test, y_test_pred, alpha=0.5)
>>> ax.text(5, 40, r'$R^2$=%.2f, RMSE=%.2f' % (rsquared_test ,test_rmse))
# diagonal line
>>> plt.plot([0, y_max], [0, y_max], '-k')
>>> ax.set_ylabel('Predicted')
>>> ax.set_xlabel('Actual')
>>> ax.set_title('%s' %title)
>>> plt.title('%s'%title)
Figure 5- 6. LassoLars Regression Predicted vs Actual on Test Data
```
After we get the best model with the alpha selected by the Lars algorithm, if we are happy with its overall performance (intuition and metrics), we will now use the selected alpha to re-train the model with all the data: 

<div class="code-head"><span>code</span> Lasso Regression Final Model After CV and Train-Test.py</div>

```python
>>> best_alpha = model.alpha_
>>> final_model = LassoLars(alpha=best_alpha)
>>> final_model.fit(X, y)
>>> n_nonzeros = (final_model.coef_ != 0).sum() #9
>>> print("Non-zeros coef: %d" % n_nonzeros)
>>> Interpretation = pd.DataFrame({'X':dataset.feature_names, 'Coef':final_model.coef_})
>>> Interpretation.index = Interpretation.X
>>> Interpretation.sort_values('Coef').T.loc['Coef',:].plot(kind='bar')
```
The final model now can be used for making predictions.  

final_model.predict(new_x)

If we want to control how the alphas are, you can do something like in the example below.  Note that again the xaxis is log10 scale.  That’s why the ticks are evenly spaced even though the labels are in multiples of 10. 

To standardize the predictors, preprocessing function from the sklearn library. The preprocessing.scale function transforms the variable to have a mean of zero and a standard deviation of one, thus putting all the predictors on the same scale. RidgeCV and LassoCV both worked out selecting the best value among a range of values we provide. 

is a shrinkage and variable selection method for linear regression models.  

The main SAS libraries are <span class="coding">PROC GLMSELECT</span>, and while in Python sklearn.linear_model.Lasso. LASSO performs both coefficient estimation and variable selection simultaneously.  

The entire path of LASSO estimates for all values of the shrinkage parameter can be efficiently through a modification of the least angle regression (LARS) algorithm invented by Efron et al. 2003. 

The  least angle regression algorithm, introduced by Efron et al. (2004), to produce a sequence of regression models in which one parameter is added at each step.

The LassoLarsCV function from the sklearn.linear_model library
Predictors with regression coefficients that do not have a value of zero are included in the selected model. Predictors with regression coefficients equal to zero means that the coefficients for those variables had shrunk to zero after applying the LASSO regression penalty, and were subsequently removed from the model. 

So the results show that of the 23 variables, 18 were selected in the final model. If you remember, we standardized the values of our variables to be on the same scale. So we can also use the size of the regression coefficients to tell us which predictors are the strongest predictors of school connectedness. For example, self-esteem and depression had the largest regression coefficients, and were most strongly associated with school connectedness, followed by black ethnicity and GPA. 

Depression and black ethnicity were negatively associated with school connectiveness, and self-esteem and GPA were positively associated with school connectiveness. We can also create some plots so we can visualize some of the results.

For example, we can plot the progression of the regression coefficients through the model selection process. In Python, we do this by plotting the change in the regression coefficient by values of the penalty parameter at each step of the selection process. 

It's important to note that the sklearn library refers to the penalty parameter is alpha although the more conventional term is lambda . We can use the following code to generate this plot.

For creating the plot, I will apply a negative log10 transformation to the alpha values. Simply to make the values easier to read by creating an object m_log_alphas that is equal to the negative of the -np.log10 transformation function applied to the alphas_ attribute from the model results object. 

The alphas_ attribute contains the values of alpha through the model selection process. The first line of code for the plot, sets up the axes, the second line of code asks Python to use the plot function from the mat plot lib library which we imported as plt to plot the transform values of alpha on the horizontal access. And the change in the regression coefficients in the coef_path_ attribute, from the model results object and the y axis. 

The .T asks python to transpose the coef_path_ attribute matrix to match the first dimension of the array of alpha values. I will use the plt.axlvline function to put a dashed vertical line at the -np.log10 transformed alpha value for the selected model. The color equals='k' in quotes tells Python to make the line color black. Finally, I add titles for the two axes and the plot title and run the code.

This plot shows the relative importance of the predictor selected at any step of the selection process, how the regression coefficients changed with the addition of a new predictor at each step, as well as the steps at which each variable entered the model. 

As we already know from looking at the list of the regression coefficients self esteem, the dark blue line, had the largest regression coefficient. It was therefore entered into the model first, followed by depression, the black line, at step two. In black ethnicity, the light blue line, at step three and so on.

Another important plot is one that shows the change in the mean square error for the change in the penalty parameter alpha at each step in the selection process. This code is similar to the code for the previous plot except this time we're plotting the alpha values through the model selection process for each cross validation fold on the horizontal axis, and the mean square error for each cross validation fold on the vertical axis. 

This is done in the first plt.plot function. Where m_log_alphascv, is a negative log10 transformation applied to the alphascv_ attribute for each validation fold, and a cv_mse_path_ is the model results attribute containing the mean square error for each cross validation fold. The colon in quotes here tells Python to plot the folds as dotted lines. 

In the next line of code, I'm asking Python to plot the average mean squared error across all cross-validation folds, and to plot it as a slightly thicker line with equals to black line. I'll use the plt.axvline function to plot a dashed black vertical line at the -np.log10 transformed alpha value for the selected model. Finally, I ask Python to print a legend and add titles for the two axes as well as the plot title and I run the code.

We can see that there is variability across the individual cross-validation folds in the training data set, but the change in the mean square error as variables are added to the model follows the same pattern for each fold. Initially it decreases rapidly and then levels off to a point at which adding more predictors doesn't lead to much reduction in the mean square error. This is to be expected as model complexity increases. 

We can also print the average mean square error in the r square for the proportion of variance in school connectedness. That is explained by the selected model in the training data set and in the test set when the selected model's applied to the test data using the following code. Here we need to import the mean squared error function from the sklearn metrics library to compute the mean square error.

We create an object called train_error which is equal to the mean_squared_error calculation function, then in parentheses, the training data set response variable, tar_train, then a comma, and then model.predict(pred_train). This code tells Python to use the results from the model object to predict the response variable for observations in the training data set. 

We then do the same thing for the test data by using the results from the training set model to calculate the test data mean square error. We use the model.score attribute, which includes the predicted response values for the training, and test data sets for calculating the r square for each set. We then use the print function to print them.

As expected, the selected model was less accurate in predicting school connectedness in the test data, but the test mean square error was pretty close to the training mean square error. This suggests that prediction accuracy was pretty stable across the two data sets. 

The R-square values were 0.33 and 0.31, indicating that the selected model explained 33 and 31% of the variance in school connectedness for the training and test sets, respectively. If we go back to our graph from the bias variance trade-off video that shows what happens to prediction error as a model becomes more complex by adding more predictors. 

We can see that prediction error decreases as more variables are added to the model, and consequently bias is lower. However, we can see from the results of our example, that the reduction in mean squares error became negligible. If we'd had even more predictors in our example to predict school connectiveness. We would likely see something similar to the graph's test curve, showing an increase in both bias and variance. 

The model that is selected as the best model, is the one that falls somewhere in here. It is a point where bias and variance and the test prediction error is lowest. If a model with fewer predictors is chosen, then the model is at risk of being under-chosen. If a model of more predictors is chosen, then the model is at risk of being over-fitted.
Which algorithm is best depends on the type of data.  

<h3 id="SAS">SAS</h3>

SAS <span class="coding">GLMSELECT</span> is a very useful and flexible procedure that …
In the following example, we illustrate with an example that is very similar to what we did with <spa class="coding">LASSOLARSCV</spa> in Python.  

There is fewer lines of code required whereas all the important information are automatically generated, including parameter estimates, standardized parameter estimates, scores and plots.  339 used for training and 167 used for testing.   

Optimal Value of Criterion is at step 12 where the test error is the smallest. The <span class="coding">CHOOSE= CVEX</span> is different from <span class="coding">CHOOSE =CV</span> .If you use <span class="coding">CHOOSE= CV</span>,  the <span class="coding">CVPRESS</span> statistic that is computed by k-fold cross validation uses an ordinary least squares fit, and hence it does not directly depend on the coefficients obtained by the penalized least squares regression.  

You can specify <span class="coding">CHOOSE=CVEX</span> to use k-fold external cross validation. External cross validation directly applies the coefﬁcients obtained by a penalized least squares regression to computing the predicted residual sum of squares.

<div class="code-head"><span>code</span> LASSO Using SAS GLMSELECT Using Cross Validation and Train-Test Split.py</div>
```sas
>>> PROC GLMSELECT DATA = train testdata=test
    PLOTS(STEPAXIS=NORMB) = COEFFICIENTS;
    MODEL medv = &x. /STB SELECTION=LASSO(STOP=NONE CHOOSE = CVEX);
RUN;

Data Set    WORK.TRAIN
Test Data Set   WORK.TEST
Dependent Variable  MEDV
Selection Method    LASSO
Stop Criterion  None
Choose Criterion    External Cross Validation
Cross Validation Method Random
Cross Validation Fold   5
Effect Hierarchy Enforced   None
Random Number Seed  123456

LASSO Selection Summary
Step    Effect
Entered Effect
Removed Number
Effects In  ASE Test ASE    CV PRESS
0   Intercept       1   72.9986 108.5806    24924.2517
1   LSTAT       2   60.9175 91.9883 11474.2970
2   RM      3   38.3337 60.8006 8977.4002
3   PTRATIO     4   25.0661 43.4385 7680.8076
4   TAX     5   24.0131 42.1847 7691.1248
5   B       6   23.6414 41.7138 7534.5225
6   CRIM        7   21.4143 39.1149 7486.3140
7   DIS     8   20.9967 38.5358 7182.8036
8   NOX     9   19.3255 36.3454 6840.3996
9   INDUS       10  19.2364 36.2300 6865.5430
10  ZN      11  19.1894 36.1524 6820.8127
11  CHAS        12  19.0069 35.7675 6872.9614
12  RAD     13  18.4578 35.0417 6487.1362*
13      INDUS   12  17.7496 34.0360 6487.3217
14  AGE     13  17.2888 33.3081 6581.4756
15  INDUS       14  17.2110 33.2180 6578.7295
* Optimal Value of Criterion

Root MSE    4.38108
Dependent Mean  21.96490
R-Square    0.7471
Adj R-Sq    0.7378
AIC 1355.35030
AICC    1356.64659
SBC 1064.08830
ASE (Train) 18.45781
ASE (Test)  35.04166
CV PRESS    6487.13618

Parameter Estimates
Parameter   DF  Estimate    Standardized
Estimate
Intercept   1   27.315946   0
B   1   0.007449    0.075668
CHAS    1   0.134706    0.003884
CRIM    1   -0.063235   -0.069382
DIS 1   -0.869566   -0.203630
INDUS   1   0   0
LSTAT   1   -0.501045   -0.401110
NOX 1   -10.626646  -0.142356
PTRATIO 1   -0.902548   -0.226064
RAD 1   0.054005    0.054820
RM  1   4.000630    0.320524
TAX 1   -0.003028   -0.060041
ZN  1   0.010659    0.027125
```
In the example below MODEL statement specifies the target variable <span class="coding">MEDV</span> and the features denoted by SAS macro &x. As mentioned earlier, you can list all the feature names after the =.  

But &x saves you the typing if there are hundreds of variables especially if you need to refer to them repeatedly. The option <span class="coding">STOP = NONE</span> runs the entire path (the penalizing weight varies from zero to 1) and add all the features until none is left behind.  The Choose = SBC  (Schwarz Bayesian criterion) option produces LASSO Selection Summary table using SBC for each model on the LASSO path (in figure).   

The PLOT option plots the coefficient progression plot as in figure. where the x axis shows the ratio of the L1 norm (i.e. absolute value) of the coefficient with the L1 norm of the least square coefficient.  Since the denominator is actually a constant, we can regard the x-axis as the shrinkage parameter or the reciprocal of the penalizing weight lambda.  

The scale for the horizontal axis, requested by the <span class="coding">STEPAXIS=</span> suboption, is more appropriate for the lasso method than the default step scale in Figure 4 because it expresses the size of the ith step as the 1 norm of the parameters relative to the 1 norm of the parameters at the ﬁnal step.

<div class="code-head"><span>code</span> LASSO Using SAS GLMSELECT Using SBC Criteria.sas</div>

```sas
>>> PROC GLMSELECT DATA = boston (WHERE=(selected=0))
    PLOTS(STEPAXIS=NORMB) = COEFFICIENTS;
    MODEL medv = &x. /SELECTION=LASSO(STOP=NONE CHOOSE = SBC);
RUN;
LASSO Selection Summary
Step    Effect
Entered Effect
Removed Number
Effects In  SBC
0   Intercept       1   1460.2853
1   LSTAT       2   1404.7797
2   RM      3   1253.5834
3   PTRATIO     4   1115.3978
4   TAX     5   1106.6747
5   B       6   1107.2131
6   CRIM        7   1079.4987
7   DIS     8   1078.6478
8   NOX     9   1056.3571
9   INDUS       10  1060.6171
10  ZN      11  1065.6135
11  CHAS        12  1068.1992
12  RAD     13  1064.0883
13      INDUS   12  1044.9999
14  AGE     13  1041.9074*
15  INDUS       14  1046.2043
* Optimal Value of Criterion

Root MSE    4.24007
Dependent Mean  21.96490
R-Square    0.7632
Adj R-Sq    0.7544
AIC 1333.16938
AICC    1334.46568
SBC 1041.90738

LASSO Selection Summary
Step    Effect
Entered Effect
Removed Number
Effects In  SBC
0   Intercept       1   1460.2853
1   LSTAT       2   1404.7797
2   RM      3   1253.5834
3   PTRATIO     4   1115.3978
4   TAX     5   1106.6747
5   B       6   1107.2131
6   CRIM        7   1079.4987
7   DIS     8   1078.6478
8   NOX     9   1056.3571
9   INDUS       10  1060.6171
10  ZN      11  1065.6135
11  CHAS        12  1068.1992
12  RAD     13  1064.0883
13      INDUS   12  1044.9999
14  AGE     13  1041.9074*
15  INDUS       14  1046.2043
* Optimal Value of Criterion
```
The second table is <span class="coding">ANOVA</span> table for the selected model, which is omitted here.  The last table “Parameter Estimates” shows the parameter estimations for the selected model.  Note that the standardized coefficients for the selected model is not available in <span class="coding">PROC GLMSELECT</span>.  We can follow with <span class="coding">REG</span> to get the standardized coefficients. 
We can actually select all selection criterion.  

Note:
1.  LASSO is a convex optimization technique, which allows for very fast computing.  We can get the entire solution path within seconds even with a laptop. 
2.  There are many very convenient options in SAS <span class="coding">GLMSELECT</span>.  For example, if you have categorical features, you can simply put it in a CLASS statement and don't have to do anything else. 

Direct method:
The PARTITION statement splits 2/3 of the data for training and 1/3 of the data for out-of-sample testing.  Output figure top part shows the LASSO coefficient progression for the training data, while the bottom shows the progression of errors (The y-axis “ASE” means “average square error) on the test data along the progression.  

The vertical line shows where the minimum testing error is. This helps us look at the top part of the figure, where the model selection.   We can also look at the plot “Progression of Average Squared Errors”, which shows errors for both training and validation data as the shrinkage parameter changes.  And the selected step is where these two errors are equal.   

However, the problem with train-test split is that the test results is highly dependent on the random split of the data .  

<div class="code-head"><span>code</span> LASSO Using SAS GLMSELECT Using Validation Criteria.sas</div>
```sas
>>> PROC GLMSELECT DATA = prostate
    PLOTS(STEPAXIS=NORMB) = COEFFICIENTS;
    MODEL MEDV = lcavol lweight age lbph svi lcp gleason pgg45/SELECTION=LASSO(STOP=NONE CHOOSE = VALIDATE);
PARTITION FRACTION (VALIDATE=0.33);
RUN;
```
However, the problem with train-test split is that the test results is highly dependent on the random split of the data .    Hence we more commonly use k-fold cross validation.  The default k is 5 in SAS <span class="coding">GLMSELECT</span> but can be changed. 

1.  Randomly partitions data into k equal portions.

2.  Leave out one out of the k parts, and fit model to the k-1 parts

3.  Test the resulting model on the left-out portion from step 2 and record “out-of-sample” error

4.  Repeat the process until every one of the k parts got tested once. 

With it, we include the seed option which allows us to specify a random number seed to ensure that the data are randomly split the same way if I run the code again. The samprate command, tells SAS to split the input data set so that 70% of the observations are designated as training observations, and the remaining 30% are designated as test observations. method=srs, specifies that the data are to be split using simple random sampling. 

And the out all option, tells SAS to include, both, the training and test observations in a single output data set that has a new variable called selected, to indicate whether an observation belongs to the training set, or the test set. I will use the glmselect procedure to test my lasso regression model. data=traintest tells SAS to use the randomly split dataset, and the plots=all option, asks that all plots associated with the lasso regression be printed. 

With it we include the seed option, which allows us to specify a random number seed, which will be used in the cross-validation process. The partition command assigns each observation a role, based on the variable called selected, to indicate whether the observation is a training or test observation. Observations with a value of one on the selected variable, are assigned the role of training observation. 

And observations with a value of zero, are assigned the role of test observation. The model command specifies the regression model for which my response variable, school connected-ness, is equal to the list of the 23 candidate predictor variables. 

After the slash, we specify the options we want to use to test the model. The selection option tells us which method to use to compute the parameters for variable selection. In this example, I will use the LAR algorithm, parameters for variable selection. 

In this example, I will use the <span class="coding">LAR</span> algorithm, which stands for Least Angled Regression. This algorithm starts with no predictors in the model, and adds a predictor at each step. 

It first adds a predictor that is most correlated with the response variable, and moves it towards least square estimate, until there is another predictor that is equally correlated with the model residual. It adds this predictor to the model and starts the least square estimation process over again, with both variables. 

The <span class="coding">LAR</span> algorithm continues with this process until it has tested all the predictors. Perimeter estimates at any step are shrunk, and predictors with coefficients that are shrunk to zero are removed from the model ,and the process starts all over again. 

By default, <spa class="coding">PROC GLMSELECT</spa> uses <span class="coding">CVMETHOD</span>=RANDOM(5) for cross validation

The <span class="coding">choose=cv</span> option, ask SAS to use cross validation to choose the final statistical model. <span class="coding">stop=none</span> ensures that the model doesn't stop running until each of the candidate predictor variables is tested. Finally, <span class="coding">cvmethod=random</span>, and in parentheses, (10) Specifies that I use a K-fold cross-validation method with ten randomly selected folds. 

So, what I'm doing here is using K-fold cross validation, in which the first fold is treated as a validation set, and the model is estimated on the training data set using the remaining nine folds. At each step of the estimation process, a new predictor is entered into the model and the mean square error for the validation fold, is calculated for each of the nine folds, and then averaged. 

The model with the lowest average means square error is selected by SAS as the best model. In lasso regression, the penalty term is not fair if the predictive variables are not on the same scale. Meaning that not all the predictors will get the same penalty. The SAS <span class="coding">GLMSELECT</span> procedure handles this by automatically standardizing the predictor variables, so that they all have a mean equal to zero and a standard deviation equal to one, which places them all on the same scale. Let's go ahead and run the code and take a look at the results.


The <span class="coding">ASE</span> and Test <span class="coding">ASE</span> are the averaged squared error, which is the same as the means square error for the training data and the test data. You can see that at the beginning, there are no predictors in the model. 

Just the intercept. Then variables are entered one at a time in order of the magnitude of the reduction in the mean, or average squared error. So they are ordered in terms of how important they are in predicting school connectedness. According to the lasso regression results, it appears that the most important predictor of school connectedness, was depression. Followed by self esteem and so on. 

You can also see how the average square error declines as variables are added to the model, indicating that the prediction accuracy improves as each variable is added to the model. 

The <span class="coding">CV PRESS</span> shows the sum of the residual sum of squares in the test data set. There's an asterisk at step 16. This is the model selected as the best model by the procedure. You can see that this is the model with the lowest summed residual sum of squares and that adding other variables to this model, actually increases it. 

Finally, you could also see that the training data <span class="coding">ASE</span> continues to decline as variables are added. This is to be expected as model complexity increases. This is an example of the bias variance tradeoff.

If we go back to our graph from the bias variance tradeoff video, it shows what happens to prediction error as a model becomes more complex by adding more predictors. We can see that the decrease in the training <span class=
"coding">ASE</span> means that prediction error decreases as more variables are added to the model, and consequently, bias is lower. 

However, if you look at the curve of the test data, you can see that ,as the model becomes more complex by adding more predictors, both bias and variance increase. The model that is selected by the specified selection criteria as the best model, is the one that falls somewhere in here. It is the point where bias and variance in the test prediction error is lowest. If a model with fewer predictors is chosen, then the model's at risk of being under fitted. 
8:02

If a model with more predictors is chosen, then the model is at risk of being over fitted. SAS also provides some nice plots. The first plot shows the change in the regression coefficients at each step, and the vertical line represents the selected model. 

This plot shows the relative importance of the predictor selected at any step of the selection process, how the regression coefficients changed with the addition of a new predictor at each step. As well as, the steps at which each variable entered the model. For example, as also indicated in the summary table above, depression and self esteem had the largest regression coefficient, followed by engaging in deviant behavior. 

Depression and deviant behavior were negatively associated with school connectedness, and self-esteem was positively associated with school connectedness. The lower plot shows how the chosen selection criterion, in this example <span class="coding">CVPRESS</span>, which is the residual sum of squares summed across all the cross-validation folds in the training set, changes as variables are added to the model. 

Initially, it decreases rapidly and then levels off to a point in which adding more predictors doesn't lead to much production in the residual sum of squares. The next plot shows at which step in the selection process different selection criteria would choose the best model. Interestingly, the other, criteria selected more complex models, and the criterion based on cross validation, possibly selecting an overfitted model. The final plot shows the change in the average or mean square error at each step in the process. 

As expected, the selected model was less accurate in predicting school connectiveness in the test data, but the test average squared error at each step was pretty close to the training average squared error overall. This suggests that prediction accuracy was pretty stable across the two data sets. 

Finally, the output shows the R-Square and adjusted R-Square for the selected model and the mean square error for both the training and test data. It also shows the estimated regression coefficients for the selected model.

<div class="code-head"><span>code</span> LASSO Using SAS GLMSELECT Using Cross Validation Criteria.sas</div>
```sas
>>> PROC GLMSELECT DATA = prostate
    PLOTS(STEPAXIS=NORMB) = COEFFICIENTS;
    MODEL MEDV = lcavol lweight age lbph svi lcp gleason pgg45/SELECTION=LASSO(STOP=NONE CHOOSE = CVEX);
RUN;
```
It has flexibility in customizing selection criteria, and in addition, it allows selection of individual levels of classification effects.  Allows user to impose hierachy among features.  And we can obtain more stable model using the bootstrap model averaging.  Using the CLASS statement you can include categorical features. 

And it model selection for nonparametric models with spline effects! And variable selection between different spline bases functions for numeric features

Example of how to write results for a lasso regression: 

A lasso regression analysis was conducted to identify a subset of variables from a pool of 23 categorical and quantitative predictor variables that best predicted a quantitative response variable measuring school connectedness in adolescents. 

Categorical predictors included gender and a series of 5 binary categorical variables for race and ethnicity (Hispanic, White, Black, Native American and Asian) to improve interpretability of the selected model with fewer predictors. Binary substance use variables were measured with individual questions about whether the adolescent had ever used alcohol, marijuana, cocaine or inhalants. 

Additional categorical variables included the availability of cigarettes in the home, whether or not either parent was on public assistance and any experience with being expelled from school. Quantitative predictor variables include age, alcohol problems, and a measure of deviance that included such behaviors as vandalism, other property damage, lying, stealing, running away, driving without permission, selling drugs, and skipping school. 

Another scale for violence, one for depression, and others measuring self-esteem, parental presence, parental activities, family connectedness and grade point average were also included. All predictor variables were standardized to have a mean of zero and a standard deviation of one.

Data were randomly split into a training set that included 70% of the observations (N=3201) and a test set that included 30% of the observations (N=1701). The least angle regression algorithm with k=10 fold cross validation was used to estimate the lasso regression model in the training set, and the model was validated using the test set. The change in the cross validation average (mean) squared error at each step was used to identify the best subset of predictor variables. 

Figure 1. Change in the validation mean square error at each step 


Of the 23 predictor variables, 18 were retained in the selected model. During the estimation process, self-esteem and depression were most strongly associated with school connectedness, followed by engaging in violent behavior and GPA. Depression and violent behavior were negatively associated with school connectedness and self-esteem and <span class="coding">GPA</span> were positively associated with school connectedness. 

Other predictors associated with greater school connectedness included older age, Hispanic and Asian ethnicity, family connectedness, and parental involvement in activities. Other predictors associated with lower school connectedness included being male, Black and Native American ethnicity, alcohol, marijuana, and cocaine use, availability of cigarettes at home, deviant behavior, and history of being expelled from school. These 18 variables accounted for 33.4% of the variance in the school connectedness response variable.

Grouped LASSO, Adaptive LASSO

Reference:
SAS/STAT® 14.3 User’s Guide The GLMSELECT Procedure
https://documentation.sas.com/api/docsets/statug/14.3/content/glmselect.pdf?locale=en#nameddest=statug_glmselect_overview

Tuning parameter
https://stats.stackexchange.com/questions/126898/tuning-alpha-parameter-in-lasso-linear-model-in-scikitlearn

Least Angle Regression (LAR)
https://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_glmselect_a0000000242.htm

Model selection with PROC GLMSELECT https://blogs.sas.com/content/iml/2019/02/04/model-selection-glmselect.html

Least Angle Regression
Bradley Efron, Trevor Hastie, Iain Johnstone and Robert Tibshirani
https://web.stanford.edu/~hastie/Papers/LARS/LeastAngle_2002.pdf


Least Angle Regression (LAR)

Least angle regression was introduced by Efron et al. (2004). Not only does this algorithm provide a selection method in its own right, but with one additional modification it can be used to efficiently produce LASSO solutions. Just like the forward selection method, the LAR algorithm produces a sequence of regression models where one parameter is added at each step, terminating at the full least squares solution when all parameters have entered the model. 

The algorithm starts by centering the covariates and response, and scaling the covariates so that they all have the same corrected sum of squares. Initially all coefficients are zero, as is the predicted response. The predictor that is most correlated with the current residual is determined and a step is taken in the direction of this predictor. 

The length of this step determines the coefficient of this predictor and is chosen so that some other predictor and the current predicted response have the same correlation with the current residual. At this point, the predicted response moves in the direction that is equiangular between these two predictors. 

Moving in this direction ensures that these two predictors continue to have a common correlation with the current residual. The predicted response moves in this direction until a third predictor has the same correlation with the current residual as the two predictors already in the model.

A new direction is determined that is equiangular between these three predictors and the predicted response moves in this direction until a fourth predictor joins the set having the same correlation with the current residual. This process continues until all predictors are in the model. 

As with other selection methods, the issue of when to stop the selection process is crucial. You can specify a criterion to use to choose among the models at each step with the <span class="coding">CHOOSE=</span> option. You can also specify a stopping criterion with the STOP= option. 

See the section Criteria Used in Model Selection Methods for details for the formulas for evaluating these criteria. These formulas use the approximation that at step  of the <span class="coding">LAR</span> algorithm, the model has  degrees of freedom. See Efron et al. (2004) for a detailed discussion of this so-called simple approximation. 

A modification of LAR selection suggested in Efron et al. (2004) uses the LAR algorithm to select the set of covariates in the model at any step, but uses ordinary least squares regression with just these covariates to obtain the regression coefficients. You can request this hybrid method by specifying the <span class="coding">LSCOEFFS</span> suboption of <span class="coding">SELECTION=LAR</span>.
https://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm#statug_glmselect_a0000000242.htm

<h3 id="Ridge">Ridge</h3>

Ridge regression uses L2 penalizer. The ease of use in sklearn is that there are only a few lines of code one needs to change to switch to a different algorithm/model, sometimes a very different one.  For example, if we want to switch to Lasso, LassoCV, LassoLars,or LarsCV, we just have to import and instantiate it, such as:

``` python
>>> from sklearn.linear_model import RidgeCV
>>> model = RidgeCV()
```
The initial signiture of RidgeCV object is:
```python
RidgeCV(
    ['alphas=(0.1, 1.0, 10.0)', 'fit_intercept=True', 'normalize=False', 'scoring=None', 'cv=None', 'gcv_mode=None', 'store_cv_values=False'],
)
```
•   alphas is the default list of alphas.  As the list of alphas provided by the default has only 3 values, it may be adviserable to run the default version, ad then supply a longer list of alphas closer to the one that was chosen in the first run.  

•   The meanings and workings of 'fit_intercept=True', and 'normalize=False', are exactly the same as LassoLarsCV.  

•   gcv_mode is an optional parameter that allows you to choose a mode to use for Generalized Cross-Validation: {None, 'auto', 'svd', eigen'}

•   cv : is optional for the cross-validation splitting strategy.  The default is None, to use the efficient Leave-One-Out cross-validation (aka “Generalized Cross-Validation” or, “LOOC”, or the “Jackknife”), which is possibly the reason why the Ridge in sklearn does not have a random_state parameter for pseduo random generator seed. It can be set to an integer for k-fold or term.  

<div class="code-head"><span>code</span> Ridge Coefficients as a Function of the Regularization.py</div>
```python
>>> n_alphas = 100
>>> alphas = np.logspace(5, -3, n_alphas)

>>> model  = RidgeCV(cv=5, normalize=False, alphas=alphas)
# fit model
>>> model.fit(X_train,y_train)

>>> print("The best alpha: %.3f" % model.alpha_)
[Out]: The best alpha: 9.112

>>> y_train_pred = model.predict(X_train)
>>> y_test_pred = model.predict(X_test)

>>> # print variable names and regression coefficients
>>> Interpretation = pd.DataFrame({'X':dataset.feature_names, 'Coef':model.coef_})
>>> Interpretation.iloc[(-np.abs(Interpretation['Coef'].values)).argsort()] 
[Out]:
          X      Coef
5        RM  3.453538
12    LSTAT -3.378018
7       DIS -2.543855
10  PTRATIO -1.961803
8       RAD  1.708400
9       TAX -1.595832
4       NOX -1.360119
0      CRIM -0.859517
1        ZN  0.794836
11        B  0.555400
2     INDUS  0.236742
6       AGE -0.231184
3      CHAS  0.100041
>>> print("Intercept is %.3f" % model.intercept_)
[Out]: Intercept is 22.762
<div class="code-head"><span>code</span> Ridge Regression Performance Testing and Plotting.py</div>
>>> train_rmse = (mean_squared_error(y_train, model.predict(X_train)))**(1/2)
>>> test_rmse = (mean_squared_error(y_test, model.predict(X_test)))**(1/2)
>>> print('Training RMSE: %.3f'% train_rmse)
>>> print('Testing RMSE: %.3f'% test_rmse)
[Out]: 
Training RMSE: 4.503
Testing RMSE: 5.347

>>> # R-square from Training and test data
>>> rsquared_train=model.score(X_train,y_train)
>>> rsquared_test=model.score(X_test,y_test)
>>> print ('Training R-square: %.3f'% rsquared_train)
>>> print ('Testing R-square: %.3f'% rsquared_test)
[Out]: 
Training R-square: 0.764
Testing R-square: 0.646

>>> y_max =np.max(y)
>>> title = "Ridge regression Predicted vs Actual on Test Data"
>>> f, ax =plt.subplots(1, 1)
>>> ax.scatter(y_test, y_test_pred, alpha=0.5, color='green'
>>> ax.text(5, 40, r'$R^2$=%.2f, RMSE=%.2f' % (rsquared_test ,test_rmse))

>>> plt.plot([0, y_max], [0, y_max], '-', color='blue')
>>> ax.set_ylabel('Predicted')
>>> ax.set_xlabel('Actual')
>>> ax.set_title('%s' %title)
>>> plt.title('%s'%title)
 
<div class="code-head"><span>code</span> Ridge Coefficients as a Function of the Regularization.py</div>
>>> from sklearn.linear_model import Ridge
# Compute paths
>>> title ="Ridge Coefficients as a Function of the Regularization"
>>> n_alphas = 100
>>> alphas = np.logspace(5, -3, n_alphas)
>>> coefs = []
>>> for a in alphas:
>>>     ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
>>>     ridge.fit(X, y)
>>>     coefs.append(ridge.coef_)

# Display result
>>> ax = plt.gca()
>>> ax.plot(alphas, coefs, marker='o', ms=3, alpha=0.3, ls='')
>>> ax.set_xscale('log')
>>> ax.set_xlim(ax.get_xlim()[::-1])  # reverse axis
>>> plt.xlabel('alpha')
>>> plt.ylabel('weights')
>>> plt.title('')
>>> plt.axis('tight')
>>> plt.title('%s'%title)
```

Figure 5- 7. Ridge Coefficients as a Function of the Regularization
  
<h3 id="SAS">SAS</h3>

Ridge regression is a variant to least squares regression that is sometimes used when several explanatory variables are highly correlated. The "usual" ordinary least squares (OLS) regression produces unbiased estimates for the regression coefficients (in fact, the Best Linear Unbiased Estimates). 

However, when the explanatory variables are correlated, the OLS parameter estimates have large variance. It might be desirable to use a different regression technique, such as ridge regression, in order to obtain parameter estimates that have smaller variance. The trade-off is that the estimates for the ridge regression method are biased.
https://blogs.sas.com/content/iml/2013/03/20/compute-ridge-regression.html

"Let X be the matrix of the independent variables after centering [and scaling]the data, and let Y be a vector corresponding to the [centered]dependent variable. Let D be a diagonal matrix with diagonal elements as in X`X. The ridge regression estimate corresponding to the ridge constant k can be computed as D-1/2(Z`Z + kI)-1Z`Y."  

In addition to the <span class="coding">PROC REG</span> outputs such as ANOVA, Goodness of Fit, Fit Statistics, Parameter Estimates,  Fit Diagnostics, Residual by feature, there is Ridge Analysis and plot.  The output <span class="coding">OUTEST =</span> has each model coefficient, RMSE, with parameter coefficients, and VIF for each feature at each ridge. 

<div class="code-head"><span>code</span> Ridge Regression in SAS.py</div>
```sas
>>> PROC REG DATA=boston (WHERE=(selected=0)) OUTVIF
         OUTEST=coef RIDGE=0 TO 0.15 BY .01;
 MODEL medv = &x.;
RUN;
Figure 5- 6. Ridge Regression Analysis with VIF Progression in SAS
```

<h3 id="Elastic-Net">Elastic Net</h3>

The Elastic Net method bridges the LASSO method and ridge regression. It balances having a parsimonious model with borrowing strength from correlated regressors, by solving the least squares regression problem with constraints on both the sum of the absolute coefficients and the sum of the squared coefficients.
 
 
Source: SAS/STAT 14.3 documentation
From sklearn docstring,         

1 / (2 * n_samples) * ||y - Xw||^2_2   + alpha * l1_ratio * ||w||_1 
 + 0.5 * alpha * (1 - l1_ratio) * ||w||^2_2

If  is set to a very large value or, equivalently, if  is set to 0, then the elastic net method reduces to ridge regression. If  is set to a very large value or, equivalently, if  is set to 0, then the elastic net method reduces to LASSO. If  and  are both large or, equivalently, if  and  are both set to 0, then the elastic net method reduces to ordinary least squares regression.
As stated by Zou and Hastie (2005) , the elastic net method can overcome the limitations of LASSO in the following three scenarios: 

•   Wide data case: when you have more parameters than observations, the LASSO method selects at most n variables before it saturates, because of the nature of the convex optimization problem. This can be a defect for a variable selection method. By contrast, the elastic net method can select more than n variables in this case because of the ridge regression regularization. 

•   If there is a group of variables that have high pairwise correlations, then whereas LASSO tends to select only one variable from that group, the elastic net method can select more than one variable. 

•   Long data case, when there are more observation than parameters, if there are high correlations between predictors, it has been empirically observed that the prediction performance of LASSO is dominated by ridge regression. In this case, the elastic net method can achieve better prediction performance by using ridge regression regularization.

Its initial signature is:

ElasticNetCV(alphas=None, copy_X=True, cv='warn', eps=0.001, fit_intercept=True, l1_ <...> se, precompute='auto',
random_state=None, selection='cyclic', tol=0.0001, verbose=0)

•   The l1_ratio is the weight for L1 penalty, whereas 1- L1_ratio for L2  penalty.   

o   For ``l1_ratio = 1`` it is an L1 penalty.

o   When l1_ratio = 0, the penalty is an L2 penalty.    

o   For ``0 < l1_ratio < 1``, the penalty is a combination of L1 and L2

o   This parameter can be a list, in which case the different values are tested by cross-validation and the one giving the best prediction score is used. 

o   Note that a good choice of list of values for l1_ratio is often to put 
more values close to 1 (i.e. Lasso) and less close to 0 (i.e. Ridge), as in  [.1, .5, .7, .9, .95, .99, 1]

•   The fit_intercept, normalize, precompute, random_state, cv parameters are exactly implemented the same way as in Lasso or Ridge.  
In this example below, we are going to use GridSearchCV with 5-fold cross-validation to tune l1_ratio on the training data X_train and y_train, and then predict on the test set and compute R square and RMSE. 

Fit is on grid of alphas and best alpha estimated by cross-validation. The performance is almost identical to LassoLarsCV for this dataset.   As you can see, the code is almost identical to that for LassoLarsCV.   The best alpha is 0.023 using the 5-fold cross validation.  We used the default l1_ratio of 0.5.  We let the algorithm to choose the best alpha for us. 

<div class="code-head"><span>code</span> ElasticNetCV in sklearn.py</div>
```python
>>> from sklearn.linear_model import ElasticNetCV
>>> l1_ratio = [.5, .9, .95, .99, 1]
# >>> l1_ratio = [0.05, .1, .5, .7,.9, .95, .99, 1]
# >>> alphas=[0.01, 0.05, 0.1, 0.5, 0.8, 0.9, 1],
# >>> model  = ElasticNetCV(alphas=alphas, cv=5, l1_ratio = l1_ratio, random_state=123, normalize=False)
>>> model  = ElasticNetCV(cv=5, random_state=123, normalize=False)
>>> # alpha=1 is LASSO
>>> # alpha=0 is ridge
>>> model.fit(X_train,y_train)
>>> X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=123)
>>> # train & predict
>>> model.fit(X_train,y_train)
>>> y_train_pred = model.predict(X_train)
>>> y_test_pred = model.predict(X_test)
# best alpha
>>> print("The best alpha: %.3f" % model.alpha_)
>>> print("The best weight on L1 penalty (l1_ratio): %.2f" % model.l1_ratio_)
>>> # RMSE from training and test data
>>> train_rmse = (mean_squared_error(y_train, model.predict(X_train)))**(1/2)
>>> test_rmse = (mean_squared_error(y_test, model.predict(X_test)))**(1/2)
>>> print('Training RMSE: %.3f'% train_rmse)
>>> print('Testing RMSE: %.3f'% test_rmse)
>>> # R-square from Training and test data
>>> r2_train=model.score(X_train,y_train)
>>> r2_test=model.score(X_test,y_test)
>>> print ('Training R-square: %.3f'% r2_train)
>>> print ('Testing R-square: %.3f'% r2_test)
>>> y_max =np.max(y)
[Out]: 
Training RMSE: 4.499
Testing RMSE: 5.349
Training R-square: 0.764
Testing R-square: 0.646
>>> print("The best alpha: %.3f" % model.alpha_)
[Out]: The best alpha: 0.023
<div class="code-head"><span>code</span> ElasticNet Regression Predicted vs Actual on Test Data.py</div>
>>> title = "ElasticNet Regression Predicted vs Actual on Test Data"
>>> f, ax =plt.subplots(1, 1)
>>> ax.scatter(y_test, y_test_pred, alpha=0.5)
>>> ax.text(5, 40, r'$R^2$=%.2f, RMSE=%.2f' % (r2_test ,test_rmse))
>>> # diagonal line
>>> plt.plot([0, y_max], [0, y_max], '-k')
>>> ax.set_ylabel('Predicted')
>>> ax.set_xlabel('Actual')
>>> ax.set_title('%s' %title)
>>> plt.title('%s'%title)
Figure 5- 8. ElasticNet Regression Predicted vs Actual on Test Data
```

<h3 id="SAS">SAS</h3>

As earlier, a <span class="coding">TESTDATA=</span> data set is named in the <span class="coding">PROC GLMSELECT</span> statement to test the prediction accuracy of the model on the training samples. 

Because the L2=option is not speciﬁed, <span class="coding">PROC GLMSELECT</span> tries a series of candidate values for the ridge regression parameter. Output 51.6.11 shows the standardized coefﬁcients of all the effects selected at some step of the elastic net method, plotted as a function of the step number, and also the curve of the <span class="coding">CVEXPRESS</span> statistic as a function of the step number.

A comparison between the criterion curves in Output 51.6.10 and Output 51.6.11 shows that the <span class="coding">CVEXPRESS</span> statistic is smoother than the <span class="coding">CVPRESS</span> statistic. Note that the <span class="coding">CVEXPRESS</span> statistic is based on a penalized model, whereas the <span class="coding">CVPRESS</span> statistic is based on an ordinary least squares model. 

Output 51.6.12 shows the “Elastic Net Selection Summary” table, which corresponds to the ridge regression parameter selected by k-fold external cross validation. The elastic net method achieves the smallest <span class="coding">CVEXPRESS</span> score at step 120, and hence the model at this step is selected, resulting in 53 selected effects.

<div class="code-head"><span>code</span> ElasticNet Using SAS GLMSELECT.py</div>
```python
>>> title = "ElasticNet Regression Predicted vs Actual on Test Data"
>>> f, ax =plt.subplots(1, 1)
>>> ax.scatter(y_test, y_test_pred, alpha=0.5)
>>> ax.text(5, 40, r'$R^2$=%.2f, RMSE=%.2f' % (r2_test ,test_rmse))
>>> # diagonal line
>>> plt.plot([0, y_max], [0, y_max], '-k')
>>> ax.set_ylabel('Predicted')
>>> ax.set_xlabel('Actual')
>>> ax.set_title('%s' %title)
>>> plt.title('%s'%title)

Root MSE    4.24007
Dependent Mean  21.96490
R-Square    0.7632
Adj R-Sq    0.7544
AIC 1333.16938
AICC    1334.46568
SBC 1041.90738
ASE (Train) 17.28877
ASE (Test)  33.30813
CVEX PRESS  18.85589

Parameter Estimates
Parameter   DF  Estimate    Standardized
Estimate
Intercept   1   36.229893   0
AGE 1   -0.004686   -0.015006
B   1   0.009059    0.092024
CHAS    1   0.382212    0.011020
CRIM    1   -0.103126   -0.113151
DIS 1   -1.413691   -0.331050
LSTAT   1   -0.495568   -0.396725
NOX 1   -15.719402  -0.210580
PTRATIO 1   -0.967183   -0.242253
RAD 1   0.252704    0.256520
RM  1   3.718813    0.297945
TAX 1   -0.011332   -0.224722
ZN  1   0.033851    0.086145
```