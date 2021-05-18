---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Timeseries Modeling"
description: OLS regression, serial correlation correction, robust regression
author: Sarah Chen
image: images/posts/regplot food_yoy and meat_yoy.png

---

This post consists of a few timeseries regression examples from my upcoming book on statistical and machine learning using Python, also to be published by Apress,as my co-authored book [Python for SAS User](https://www.amazon.com/Sarah-Chen/e/B07ZL3Q97B?ref_=dbs_p_pbk_r00_abau_000000).  There are two main categories of models for time series data: 
1. Various variations of OLS type of regression y = a + b*x.  To account for residual serial correlation, Newey-West standard errors may be used. 
2. Time series model, such as ARIMAX, SARIMAX

We will begin with some data analysis and then get into modeling. 

## Data: Food and energy CPI
Looking at economic activity data year over year (or sometimes quarter over quarter) is a routine exercise for analysts who work with macroeconomic data, and business performance data.  Tranformating the target variable using YoY often makes the time series stationary and non-serial correlated.  Stationary target variable makes modeling easier because it is reduces chances of spurious regression and it is easier to isolate problems.  Why?  Let's make an analogy, when you have two objects, it is easier to see what is happening if you keep one object relatively fixed (stationary) instead of both are moving. 

Food and energy (along with housing) are the most important factors in daily life. We use CPI data from FRED for our first example, using <span class="coding">.to_frame().join([meat,energy])</span> to combine the three time series together: urban meat prices, all food prices, and energy prices. 

To avoid seeing too much volatility, we first convert the monthly data to quarterly by using <span class="coding">.resample('Q').mean()</span>, then chain it with <span class="coding">.pct_change(4)</span>.  This gives us a quick way to compare a few time series in year over year change. 

<div class="code-head"><span>code</span>CPI YoY.python</div>

```python
pd.options.display.float_format = '{:10,.1f}'.format 
fred = fred(api_key='your key')
from fredapi import Fred as fred
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
meat=fred.get_series('CWSR0000SAF112')
meat.name ='meat'
food=fred.get_series('CPIUFDNS')
food.name = 'food'
energy=fred.get_series('CUSR0000SEHF')
energy.name = 'energy'
title = "energy,meat and all food CPI"
df = food.to_frame().join([meat,energy]).resample('Q').mean().pct_change(4)
df.plot(figsize=(15,5), alpha=0.8, linewidth=3)
plt.title(title)
# plt.savefig(r".\TimeSeries\images\food_cpi.png")
plt.show()
```
<figure>
  <img src="{{ "/images/posts/energy,meat and all food CPI.png" | relative_url }}">
  <figcaption>energy,meat and all food CPI YoY - Sarah Chen</figcaption>
</figure>

## Data Transform
A variation of YoY transformation is moving average YoY, which first takes moving average before computing year over year. 
Only one line of code is need to accomplish this. Again, <span class="coding">.resample('Q').mean()</span> changes frequency of the data from monthly to quarterly.  <span class="coding">.rolling(4).mean()</span> takes four-quarter moving average, followed by <span class="coding">.pct_change(4)</span> to make it year over year change. 

<div class="code-head"><span>code</span>CPI moving average YoY.python</div>

```python
title = "CPI moving average YoY"
food.to_frame().join([meat,energy]).resample('Q').mean().rolling(4).mean().pct_change(4).plot(figsize=(15,5),linewidth=2, color=[blue, green,'grey'])
plt.title(title,fontdict={'fontsize': 20, 'fontweight': 'bold'})
```
<figure>
  <img src="{{ "/images/posts/CPI moving average YoY.png" | relative_url }}">
  <figcaption>CPI moving average YoY - Sarah Chen</figcaption>
</figure>

If we have many series and cannot plots them in one chart, we may want to use the following code.  To make the plots more informative, we can annotate them with statistics such as historical mean. 
</span> takes four-quarter moving average, followed by <span class="coding">.pct_change(4)</span> to make it year over year change. 

<div class="code-head"><span>code</span>CPI moving average YoY.python</div>

```python
fred_series = ['CWSR0000SAF112','CPIUFDNS','CUSR0000SEHF' ] 
series_names = ['meat','food','energy']
series_dict = dict(zip(fred_series,series_names))
# get series together and save them in a dataframe
s_list =[]
for i in fred_series:
    s = fred.get_series(i)
    s_list.append(s)
s_df = pd.concat(s_list, axis=1) #convert a list of series to dataframe
s_df.columns=series_names
# transform the entire dataframe
s_yoy =s_df.resample('Q').mean().pct_change(4) 
MEAN = s_yoy.mean()

for i in fred_series:
    NAME = series_dict[i]
    title = "CPI " +  NAME + ' '+ i
    fig, ax = plt.subplots(1,1)
    s_yoy[NAME].dropna(axis=0).plot(label=NAME,color=blue, ax=ax)
    left_pos = s_yoy[NAME].first_valid_index()
    right_pos = s_yoy[NAME].last_valid_index() 
    plt.hlines(MEAN[NAME], xmin=left_pos,xmax=right_pos, linestyles=":", alpha=0.3)
    # annotate with historical mean
    ax.text(s_yoy[NAME].first_valid_index(),MEAN[NAME], '$mean: {:.1f}$%'.format(100*MEAN[NAME]))
    plt.hlines(0, xmin=left_pos,xmax=right_pos, lw=4, alpha=0.5, color='white')
    plt.legend(frameon=False)
    plt.title(title)
    plt.show()
```
<figure>
  <img src="{{ "/images/posts/CPI meat CWSR0000SAF112.png" | relative_url }}">
  <figcaption>CPI meat CWSR0000SAF112</figcaption>
</figure>


<div class="Inflation and Deflation Periods in the 20th Century"><p>
<b>Note</b> 

1. 1900 - 1914    The Gold standard and stability
2. 1915 - 1924    Inflation - World War I
3. 1925 - 1939    Deflation - Interwar instability
4. 1949 - 1970    Moderate inflation - Bretton Woods and the Dollar standard
5. 1971 - 1979    Highly variable inflation - Floating exchange rates, OPEC
6. 1980 - 2000    *Disinflation* - Greater central bank independence
</p></div>

**deflation** is a decrease in general price levels throughout an economy. Deflation, which is the opposite of inflation, is mainly caused by shifts in supply and demand. 
**disinflation** is what happens when price inflation slows down temporarily.  Disinflation shows the rate of change of inflation over time.

Because time series transformation is often used in feature engineering in models, we may need to merge the transformed data with the level data. 
<div class="Python notes"><p>
<b>Note</b> When merging data back, it is important to check by looking at the data, and reading the numbers.   Python is easy to use, and is also very easy to make mistake with.    For example, when using <span class="coding">.join</span>, default method is on index, if the series have different frequency, then nothing will be merged. 
</p></div>

<div class="code-head"><span>code</span>YoY and moving average YoY.python</div>

```python
df = food.to_frame().join([meat,energy]).resample('Q').mean()
yoy_df = df.pct_change(4)
ma_yoy_df = df.rolling(4).mean().pct_change(4)
df = df.join(yoy_df, rsuffix='_yoy')
df = df.join(ma_yoy_df, rsuffix='_ma_yoy')
title = "YoY and moving average YoY"
df[['meat_yoy','meat_ma_yoy']].dropna(how='all',axis=0).plot(figsize=(15,5),linewidth=2, color=[blue, green])
plt.title(title,fontdict={'fontsize': 20, 'fontweight': 'bold'})
```
<figure>
  <img src="{{ "/images/posts/YoY and moving average YoY.png" | relative_url }}">
  <figcaption>YoY and moving average YoY - Sarah Chen</figcaption>
</figure>

## Bi-variate Plots Check for Economic Intuition

<div class="code-head"><span>code</span>comparing 2 time series with different axis.python</div>

```python
def plot_2_ts(data, x, y, year):
    '''
    plot 2 time series using secondary axis
    y is plotted with solid blue line
    x is in dotted green line
    annotated with correlation
    year is the beginning year
    '''
    temp = data.loc[str(year):, [x]+[y]].dropna(how='any', axis=0).copy()
    corr = np.round(temp.corr().iloc[0,1],2)
    print("corr \n",corr)
    title = x + " and " + y
    fig, ax1 = plt.subplots(1,1,figsize=(15,5))
    ax2 = ax1.twinx()
    ax1.plot(temp.index, temp[x], color=green, label=x,linestyle=":", lw=3)
    ax2.plot(temp.index, temp[y], color=blue, label=y, lw=3)
    ax1.set_ylabel(x, color=green)
    ax2.set_ylabel(y, color=blue)
    ax2.xaxis.set_major_locator(YearLocator()) #frequency
    ax2.xaxis.set_major_formatter(DateFormatter('%Y'))
    ax2.text(temp.index[2],temp[x].min(), "correlation = %s"%str(corr))
    ax1.tick_params(axis='x', labelrotation = 90)
    ax2.tick_params(axis='x', labelrotation = 90)
    ax1.legend(frameon=False, loc=2)
    ax2.legend(frameon=False, loc=1)
    plt.xticks(fontsize=5)
    plt.title(title,fontsize=20, fontweight ='bold')
plot_2_ts(df, x= "food_ma_yoy", y = "energy_ma_yoy", year=1970)
```
<figure>
  <img src="{{ "/images/posts/food_ma_yoy and energy_ma_yoy.png" | relative_url }}" width ="1500">
  <figcaption>food_ma_yoy and energy_ma_yoy</figcaption>
</figure>

## regression analysis
After preparing the data, we may want to do some simple regression analysis for feature selection.   Below is an example that looks at various lags and leads to find which is the most correlated one with the target.  

<div class="code-head"><span>code</span>regression analysis.python</div>

```python
def regplots(x, y, data):
    df = data[[y,x]].dropna(how='all', axis=0).copy()
    df.rename({y:'y'}, inplace=True, axis=1)
    df['lead1'] = df[x].shift(-1)
    df['lead2'] = df[x].shift(-2)
    df['lead3'] = df[x].shift(-3)
    df['lead4'] = df[x].shift(-4)
    df['lag1'] = df[x].shift(1)
    df['lag2'] = df[x].shift(2)
    df['lag3'] = df[x].shift(3)
    df['lag4'] = df[x].shift(4)
    corrs = np.round(df.corr()['y'][1:],2)
    print("correlation is:/n", corrs)
    cols = [x,'lead4','lead3','lead2','lead1','lag1','lag2','lag3','lag4']
    lwargs = {'color':'grey', 'alpha':0.6}
    lwargs2 = {'color':'k', 'alpha':0.6}
    fig, ax = plt.subplots(3,3, figsize=(15,15))
    sns.regplot(x=df[cols[0]], y=df.y, data=df, ax=ax[0,0],line_kws=lwargs).set_title("%s, corr %s"%(cols[0],str(corrs[cols[0]])))
    sns.regplot(x=df[cols[1]], y=df.y, data=df, ax=ax[0,1],line_kws=lwargs).set_title("%s, corr %s"%(cols[1],str(corrs[cols[1]])))
    sns.regplot(x=df[cols[2]], y=df.y, data=df, ax=ax[0,2],line_kws=lwargs).set_title("%s, corr %s"%(cols[2],str(corrs[cols[2]])))
    sns.regplot(x=df[cols[3]], y=df.y, data=df, ax=ax[1,0],line_kws=lwargs).set_title("%s, corr %s"%(cols[3],str(corrs[cols[3]])))
    sns.regplot(x=df[cols[4]], y=df.y, data=df, ax=ax[1,1],line_kws=lwargs).set_title("%s, corr %s"%(cols[4],str(corrs[cols[4]])))
    sns.regplot(x=df[cols[5]], y=df.y, data=df, ax=ax[1,2],line_kws=lwargs).set_title("%s, corr %s"%(cols[5],str(corrs[cols[5]])))
    sns.regplot(x=df[cols[6]], y=df.y, data=df, ax=ax[2,0],line_kws=lwargs).set_title("%s, corr %s"%(cols[6],str(corrs[cols[6]])))
    sns.regplot(x=df[cols[7]], y=df.y, data=df, ax=ax[2,1],line_kws=lwargs).set_title("%s, corr %s"%(cols[7],str(corrs[cols[7]])))
    sns.regplot(x=df[cols[8]], y=df.y, data=df, ax=ax[2,2],line_kws=lwargs).set_title("%s, corr %s"%(cols[8],str(corrs[cols[8]])))
    title ="regplot %s and %s"%(y,x)
    plt.suptitle(title,fontsize=20, fontweight ='bold')
    plt.subplots_adjust(top=0.925, hspace=0.25)
    plt.savefig(r".\Volume2\TimeSeries\images\%s.png"%title)
regplots(x='meat_yoy',y='food_yoy',data=df)
Out:
correlation is:
meat_yoy   0.690
lead1      0.530
lead2      0.350
lead3      0.190
lead4      0.060
lag1       0.690
lag2       0.630
lag3       0.530
lag4       0.420
```
From the correlation and regression analysis, we see that without lead or lag the correlation between food and meat is the highest.  
<figure>
  <img src="{{ "/images/posts/regplot food_yoy and meat_yoy.png" | relative_url }}">
  <!-- <figcaption>regplot food_yoy and meat_yoy</figcaption> -->
</figure>
Below plots show that food price change is more often a leading indicator for energy price change.  However,
- When the target variable leads a input variable, **the predicted will lag behind the actual**. 
- When target leads a input, we cannot no longer call the input as a "driver", as it implies causality. 

<figure>
  <img src="{{ "/images/posts/regplot food_yoy and energy_yoy.png" | relative_url }}">
  <!-- <figcaption>regplot food_yoy and meat_yoy</figcaption> -->
</figure>

## OLS Regression
We run a simple OLS regression using meat_yoy and energy_yoy to predict food_yoy.   
<div class="code-head"><span>code</span>OLS regression.python</div>

```python
import statsmodels.api as sm
from statsmodels.stats.stattools import durbin_watson
x1 = 'meat_yoy'
x2 = 'energy_yoy'
y =  'food_yoy'
ts = df[[x1,x2,y]].copy()
ts.dropna(how='any', axis =0, inplace=True)
X = ts[[x1,x2]].copy()
X = sm.add_constant(X)
model = sm.OLS(ts[y],ts[[x1,x2]]).fit()
model.summary()
[Out]:
                            OLS Regression Results
==============================================================================
Dep. Variable:               food_yoy   R-squared:                       0.628
Model:                            OLS   Adj. R-squared:                  0.625
Method:                 Least Squares   F-statistic:                     178.5
Date:                Sun, 16 May 2021   Prob (F-statistic):           4.28e-46
Time:                        17:44:34   Log-Likelihood:                 536.07
No. Observations:                 214   AIC:                            -1066.
Df Residuals:                     211   BIC:                            -1056.
Df Model:                           2
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0168      0.002      9.058      0.000       0.013       0.020
meat_yoy       0.3547      0.024     15.009      0.000       0.308       0.401
energy_yoy     0.2186      0.023      9.472      0.000       0.173       0.264
==============================================================================
Omnibus:                       82.989   Durbin-Watson:                   0.222
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              390.244
Skew:                           1.458   Prob(JB):                     1.82e-85
Kurtosis:                       8.939   Cond. No.                         18.3
==============================================================================
```

## Residual Autocorrelation and Stationarity
From the regression results, we see that DW is 0.222.  Ideally DW should be close to 2. A rule of thumb is that test statistic values in the range of 1.5 to 2.5 are relatively normal.  Close to 0 DW means the residual is positively auto-correlated. Close to 4 implies negative autocorrelation. 

Autoregressive relationships are very common in time series.  For example, when prices are increasing, it is likely to increase for a few years.  This is what some may call "momemtum".  
In context such as stock trading, strong autocorrelation shows if there is a momentum factor associated with a stock and a suitable trading strategy may be used to explore the autocorrelation. 

Autocorrelation does not impact coefficient values from OLS.  It impacts the estimate of the errors in significance testing.  Because one of the assumptions for OLS parameter testing is independence of errors, violating this assumption makes the the standard errors smaller than they actuarlly are.  

Similarly, non-stationary residual can make us underestimate standard errors of the coefficent estimates.  We use augmented Dicky-Fuller test to test resdual stationarity.  

<div class="code-head"><span>code</span>OLS regression with Newey-West standard errors.python</div>

```python
from statsmodels.tsa.stattools import adfuller
stationary_test_result = adfuller(model.resid)
print('ADF Statistic: %f' % stationary_test_result[0])
print('p-value: %f' % stationary_test_result[1])
[Out]:
ADF Statistic: -2.178328
p-value: 0.214205
```
There are mainly three methods to correct these problems.  
One of the methods to correct the problem is to use heteroskedasticity and autocorrelation consistent (HAC) standard errors such as Newey-West ( Newey, Whitney K., and Kenneth D. West. “A Simple, Positive Semi-definite, Heteroskedasticity and Autocorrelation Consistent Covariance Matrix”. Econometrica 55.3 (1987): 703–708.) standard errors. By adding <span class="coding">cov_type='HAC'</span> to the fit method.  

In the code below, to add the intercept term, <span class="coding">sm.tools.add_constant(X)</span> is used, which is equivalent to <span class="coding">X = sm.add_constant(X)</span>  The new model summary shows that the standard errors now are larger.  For example, for meat_yoy the std err went from 0.024 to 0.054.  As a result, the coefficient estimate confidence intervals are wider.  

<div class="code-head"><span>code</span>OLS regression with Newey-West standard errors.python</div>

```python
X = ts[[x1,x2]].copy()
sm.OLS(ts[y], sm.tools.add_constant(X)).fit(cov_type='HAC',cov_kwds={'maxlags':2})
model.summary()
[Out]:

                            OLS Regression Results
==============================================================================
Dep. Variable:               food_yoy   R-squared:                       0.628
Model:                            OLS   Adj. R-squared:                  0.625
Method:                 Least Squares   F-statistic:                     43.12
Date:                Sun, 16 May 2021   Prob (F-statistic):           1.98e-16
Time:                        19:24:59   Log-Likelihood:                 536.07
No. Observations:                 214   AIC:                            -1066.
Df Residuals:                     211   BIC:                            -1056.
Df Model:                           2
Covariance Type:                  HAC
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.0168      0.002      8.954      0.000       0.013       0.021
meat_yoy       0.3547      0.054      6.629      0.000       0.250       0.460
energy_yoy     0.2186      0.058      3.751      0.000       0.104       0.333
==============================================================================
Omnibus:                       82.989   Durbin-Watson:                   0.222
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              390.244
Skew:                           1.458   Prob(JB):                     1.82e-85
Kurtosis:                       8.939   Cond. No.                         18.3
==============================================================================
```
Our goal is here is to get the right standard error for the coefficients.    Since the p-values are extremely small even under the Newy-West errors in the presence of serial correlation and/or heteroskedasticity, we can conclude the model estimates are not significantly influenced by serial correlation and therefore appropriate for use.  However, there is always a possibility that the model is not the right one for this data. 

Newey-West standard errors is the simplest serial correlation corrections to implement for a simple OLS because it does not change the model if the parameters are significant.  Depending on model purpose, OLS may be the preferred model, or sometimes we may prefer using a time series ARMA model to correct for autocorrelation. 

## Performance Testing
Before we move on to ARIMAX model, we will conduct performance testings on the OLS model.  

<div class="code-head"><span>code</span>performance testing.python</div>

```python
from statsmodels.tsa.stattools import acf
def accuracy_dict_function(pred, actual):
    resid =pred - actual
    mape = np.mean(np.abs(resid)/np.abs(actual))  # MAPE
    me = np.mean(resid)             # ME
    mae = np.mean(np.abs(resid))    # MAE
    mpe = np.mean((resid)/actual)   # MPE
    rmse = np.mean((resid)**2)**.5  # RMSE
    corr = np.corrcoef(pred, actual)[0,1]   # corr
    acf1 = acf(resid)[1]   # ACF1
    adf_pvalue = adfuller(resid)[1] #STATIONARY
    accuracy_dict = {'mape':mape, 'me':me, 'mae': mae, 
            'mpe': mpe, 'rmse':rmse, 'acf1':acf1, 
            'corr':corr} 
    accuracy_dict = {key: round(accuracy_dict[key],2) for key in accuracy_dict}  # dictionary comprehension to round the values
    return accuracy_dict

# measure model performance
# measure model performance
aic = np.round(model.aic)
dw = np.round(durbin_watson(model.resid),2) # 0.262
r2 = np.round(model.rsquared,2)
ts['p_yoy'] = model.predict()
ts = ts.join(df.food)
df = df.join(ts.p_yoy)
# get predicted level
df['pred'] = df['food'].shift(4)*(1+df['p_yoy'])
df.dropna(subset=['pred','food'], axis=0,inplace=True)
# performance for the backed out level variable
accuracy_dict = accuracy_dict_function(df.pred,df.food)
accuracy_dict
[Out]:
{'mape': 0.01,
 'me': 0.51,
 'mae': 1.77,
 'mpe': 0.0,
 'rmse': 2.44,
 'acf1': 0.87,
 'adf_pvalue': 0.34,
 'corr': 1.0}
# plot
fig, ax = plt.subplots(1,2, figsize=(14,6))
df[[y,'p_yoy']].plot(ax=ax[0], title='YoY',alpha=.8)
df[['food','pred']].plot(ax=ax[1], title='level', alpha=.8)
w1 = df.index[2] #where to put text
h1 = np.min(df[y]) +0.01
# for YoY performance
textstr0 = '\n'.join((
    r'$R^2: %.2f$'%(model.rsquared),
    r'$Durbin-Watson: %.2f$'%(dw),
    r'$AIC: %.2f$'%(aic),
    r'$%s: %.2f$'%(model.params.index[0],model.params[0]),
    r'$%s: %.2f$'%(model.params.index[1],model.params[1])
))
# for the level performance
textstr1 = '\n'.join((
    r'$mape: %.2f$'%(accuracy_dict['mape']),
    r'$mae: %.2f$'%(accuracy_dict['mae']),
    r'$rmse: %.2f$'%(accuracy_dict['rmse']),
    r'$acf1: %.2f$'%(accuracy_dict['acf1']),
    r'$adf_pvalue: %.2f$'%(accuracy_dict['adf_pvalue']),
    r'$corr: %.2f$'%(accuracy_dict['corr']),
))
textstr_lt = [textstr0, textstr1]
props = dict(boxstyle='round', facecolor='white',alpha=0.4)
for i in range(2):
    ax[1].set_xlabel("")
    ax[i].text(.1,.9, textstr_lt[i], fontsize=9, transform=ax[i].transAxes, va='top',bbox=props)
    ax[i].legend(loc='lower center',ncol=2, frameon=False)
```
<figure>
  <img src="{{ "/images/posts/performance_testing.png" | relative_url }}">
</figure>

## ARIMA Models for the Level Taget
Non-seasonal and non-stationary time series can be modeled using ARIMA. An ARIMA model is characterized by 3 terms:
1. p: the order of the AR term (how many lags)
2. d: the number of differencing required to make the time series stationary; use **acf** plot
3. q: the order of the MA term

The statsmodels <span class="coding">statsmodels.tsa.arima_model.ARIMA</span> has the order of <span class="coding">(p,d,q)</span>. So the first term in this ARIMA class is order of AR term, then differencing, and finally MA. 

**PACF** (Partial Autocorrelation) plot: used for identify number of AR terms, i.e. number of lags
 The right order of differencing is the minimum differencing required to get a near-stationary series which roams around a defined mean and the ACF plot reaches to zero fairly quick.
Adjusted Box-Tiao (ABT). In ABT, ARIMAX models with AR terms using the Box-Tiao method.
First of all, since P-value is greater than the significance level, we take difference of the series and plot autocorrelation plot.
Note that because our data has datetime index, we should not use <span class="coding">sharex=True</span>, because datetime index and range index cannot be shared. 
<div class="code-head"><span>code</span>stationary testing.python</div>

```python

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
stationary_result = adfuller(df.food_yoy)
print('ADF Statistic: %f' % stationary_result[0])
print('p-value: %f' % stationary_result[1])
[Out]:
ADF Statistic: -1.780230
p-value: 0.390320
# Original Series
fig, axes = plt.subplots(3, 2,figsize=(15,10) #sharex=False
axes[0, 0].plot(df.food); axes[0, 0].set_title('Level')
plot_acf(df.food, ax=axes[0, 1])

# 1st Differencing
axes[1, 0].plot(df.food.diff()); axes[1, 0].set_title('1st Order Differencing')
plot_acf(df.food.diff().dropna(), ax=axes[1, 1])

# 2nd Differencing
axes[2, 0].plot(df.food.diff().diff()); axes[2, 0].set_title('2nd Order Differencing')
plot_acf(df.food.diff().diff().dropna(), ax=axes[2, 1])
```
The acf plots show that after the first difference, the autocorrelation has dropped a lot.  Although there is still a bit of autocorrelation at lag 1, the first difference is better than the second difference, which went to negative correlation on the first lag.  Therefore we will go with AR 1. 
<figure>
  <img src="{{ "/images/posts/stationary_visual_test.png" | relative_url }}">
</figure>

<div class="code-head"><span>code</span>stationary testing.python</div>

```python

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
stationary_result = adfuller(df.food_yoy)
print('ADF Statistic: %f' % stationary_result[0])
print('p-value: %f' % stationary_result[1])
[Out]:
ADF Statistic: -1.780230
p-value: 0.390320
```

The YoY transformed autocorrelation plot is below. We see that even the YoY transformed price has strong autocorrelation in the first few lags.  This is understandable because price increase/decrease don't just last a quarter, and has momemtum effect.  After the first difference, the data looks stationary but still has a little positive serial correlation at lag 1, but not severa.  We will go with AR 1 as well.   Besides visual examination, we can run some statistical tests as well on the number of differences needed to achieve stationarity. 
<figure>
  <img src="{{ "/images/posts/YoY_stationary_visual_test.png" | relative_url }}">
</figure>

The pmdarima package provides many convenient methods.  Using the ndiffs from pmdarima.arima.utils we see the all three different tests agree on differencing once for food.  For the YoY transformation, ADF and KPSS method concludes 1 differencing, but the PP method says no differencing is needed. 
<div class="code-head"><span>code</span>stationary testing.python</div>

```python
from pmdarima.arima.utils import ndiffs
y = df.food
print("ndiff by Adf Test:", ndiffs(y, test='adf'))
print("ndiff by KPSS:", ndiffs(y, test='kpss'))
print("ndiff by PP:",ndiffs(y, test='pp'))
[Out]:
ndiff by Adf Test: 1
ndiff by KPSS: 1
ndiff by PP: 1

y = df.food_yoy
print("ndiff by Adf Test:", ndiffs(y, test='adf'))
print("ndiff by KPSS:", ndiffs(y, test='kpss'))
print("ndiff by PP:",ndiffs(y, test='pp'))
[Out]:
ndiff by Adf Test: 0
ndiff by KPSS: 1
ndiff by PP: 0
```

We begin with an ARIMA(1,1,1) model.  The ma term ma.L1.D.food is not signficant, which is dropped in the second try in an ARIMA(1,1,0) model. We notice that AIC and BIC dropped, and the p-value for ar.L1.D.food is smaller, which means the ARIMA(1,1,0) is a simpler and more robust model than ARIMA(1,1,1).

<div class="code-head"><span>code</span>ARIMA model.python</div>

```python
from statsmodels.tsa.arima_model import ARIMA
train = df.food
model = ARIMA(train, order=(1, 1, 0)).fit()  
model.summary()
[Out]:
                            ARIMA Model Results
==============================================================================
Dep. Variable:                 D.food   No. Observations:                  213
Model:                 ARIMA(1, 1, 1)   Log Likelihood                -273.430
Method:                       css-mle   S.D. of innovations              0.873
Date:                Sun, 16 May 2021   AIC                            554.860
Time:                        15:14:31   BIC                            568.305
Sample:                    06-30-1968   HQIC                           560.294
                         - 06-30-2021
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
const            1.1184      0.100     11.197      0.000       0.923       1.314
ar.L1.D.food     0.5186      0.204      2.538      0.011       0.118       0.919
ma.L1.D.food    -0.1932      0.241     -0.802      0.422      -0.665       0.279
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.9283           +0.0000j            1.9283            0.0000
MA.1            5.1752           +0.0000j            5.1752            0.0000
-----------------------------------------------------------------------------

model = ARIMA(train, order=(1, 1, 0)).fit()  
model.summary()
[Out]:
                             ARIMA Model Results
==============================================================================
Dep. Variable:                 D.food   No. Observations:                  213
Model:                 ARIMA(1, 1, 0)   Log Likelihood                -273.749
Method:                       css-mle   S.D. of innovations              0.875
Date:                Sun 16 May 2021    AIC                            553.497
Time:                        15:21:19   BIC                            563.581
Sample:                    06-30-1968   HQIC                           557.572
                         - 06-30-2021
================================================================================
                   coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------
const            1.1187      0.092     12.130      0.000       0.938       1.299
ar.L1.D.food     0.3519      0.064      5.491      0.000       0.226       0.477
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            2.8419           +0.0000j            2.8419            0.0000
-----------------------------------------------------------------------------
```
You can find out the required number of AR terms by inspecting the Partial Autocorrelation (PACF) plot.

<div class="code-head"><span>code</span>residual test.python</div>

```python
# residual
residuals =model.resid
from scipy import stats
from scipy.stats import norm
norm_test =stats.anderson(residuals, dist='norm')
stat, p = stats.kstest(residuals, 'norm')
print('p-value: {0: .4f}'.format(p))
[Out]:
p-value:  0.0958

fig, ax = plt.subplots(1,2, figsize=(15,4))
residuals.plot(title="Residuals", ax=ax[0])
sns.distplot(residuals, fit=norm, kde=False, rug=True, ax=ax[1])
plt.title("Distribution")
plt.show()
```

<figure>
  <img src="{{ "/images/posts/ARIMA_residual.png" | relative_url }}">
</figure>

<div class="code-head"><span>code</span>actual vs non-dynamic predicted.python</div>

```python
title = "ARIMA(1,1,0) non-dynamic level actual vs predicted"
model.plot_predict(dynamic=False)
```
The <span class="coding">dynamic=False</span> specification in <span class="coding">.plot_predict</span> uses the in-sample lagged values for prediction, which can make the predicted look better than they actually are. We will get to **out-of-sample testing** in the next section. 

<figure>
  <img src="{{ "/images/posts/ARIMA(1,1,0) non-dynamic level actual vs predicted.png" | relative_url }}">
</figure>

## YoY ARIMA Models

Both the AR and MA terms are significant.  
When we have AR 3, AIC and HQIC increased but BIC dropped slightly.   We will go with AR 2 and see how the residual looks like.   
<div class="code-head"><span>code</span>actual vs non-dynamic predicted.python</div>

```python
from statsmodels.tsa.arima_model import ARIMA
train = df.food_yoy
model = ARIMA(train, order=(2, 1, 0)).fit()  
model.summary()
[Out]:
                            ARIMA Model Results
==============================================================================
Dep. Variable:             D.food_yoy   No. Observations:                  213
Model:                 ARIMA(2, 1, 1)   Log Likelihood                 693.187
Method:                       css-mle   S.D. of innovations              0.009
Date:                Mon, 17 May 2021   AIC                          -1376.375
Time:                        18:32:01   BIC                          -1359.569
Sample:                    06-30-1968   HQIC                         -1369.583
                         - 06-30-2021
====================================================================================
                       coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------------
const            -1.347e-05      0.001     -0.012      0.990      -0.002       0.002
ar.L1.D.food_yoy    -0.3167      0.071     -4.456      0.000      -0.456      -0.177
ar.L2.D.food_yoy     0.1866      0.071      2.635      0.008       0.048       0.325
ma.L1.D.food_yoy     0.9554      0.019     49.319      0.000       0.917       0.993
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1           -1.6171           +0.0000j            1.6171            0.5000
AR.2            3.3147           +0.0000j            3.3147            0.0000
MA.1           -1.0467           +0.0000j            1.0467            0.5000
-----------------------------------------------------------------------------

model = ARIMA(train, order=(3, 1, 0)).fit()  
model.summary()
[Out]:
                             ARIMA Model Results
==============================================================================
Dep. Variable:             D.food_yoy   No. Observations:                  213
Model:                 ARIMA(3, 1, 1)   Log Likelihood                 695.807
Method:                       css-mle   S.D. of innovations              0.009
Date:                Mon, 17 May 2021   AIC                          -1379.613
Time:                        18:40:16   BIC                          -1359.445
Sample:                    06-30-1968   HQIC                         -1371.463
                         - 06-30-2021
====================================================================================
                       coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------------
const            -1.242e-05      0.001     -0.010      0.992      -0.003       0.003
ar.L1.D.food_yoy    -0.3342      0.071     -4.697      0.000      -0.474      -0.195
ar.L2.D.food_yoy     0.2238      0.072      3.108      0.002       0.083       0.365
ar.L3.D.food_yoy     0.1624      0.070      2.311      0.021       0.025       0.300
ma.L1.D.food_yoy     0.9442      0.024     38.951      0.000       0.897       0.992
                                    Roots
=============================================================================
                  Real          Imaginary           Modulus         Frequency
-----------------------------------------------------------------------------
AR.1            1.7650           -0.0000j            1.7650           -0.0000
AR.2           -1.5717           -1.0096j            1.8680           -0.4091
AR.3           -1.5717           +1.0096j            1.8680            0.4091
MA.1           -1.0591           +0.0000j            1.0591            0.5000

title = "ARIMA(2,1,0) YoY actual vs predicted"
model.plot_predict(dynamic=False)
```
<figure>
  <img src="{{ "/images/posts/ARIMA(2,1,0) YoY actual vs predicted.png" | relative_url }}">
</figure>

## Model Validation (Out of Sample Testings)
We have so far worked without any validation, which is certainly wrong.  But we did that to focus on illustrating the individual pieces.  
Now, we will incorpate out of sampel validation in model building. 

<div class="code-head"><span>code</span>out of sample test.python</div>

```python
from statsmodels.tsa.arima.model import ARIMA
# train/test
train = df.food[:200]
test = df.food[200:] # 14 records
model = ARIMA(train, order=(1, 1, 0)).fit()
# Forecast
fc= model.forecast(14, alpha=0.05)  # 95% conf
forecast = model.get_forecast(14)
yhat = forecast.predicted_mean
yhat_conf_int = forecast.conf_int(alpha=0.05)
test_pred = test.to_frame().join([fc,yhat_conf_int])
title = "ARIMA Forecast (level)"
test_pred.plot()
plt.plot(train, label='training')
plt.fill_between(test.index, test_pred['lower food'], test_pred['upper food'], 
                 color='k', alpha=.15)
plt.legend(frameon=False, loc='lower center', ncol=4)

# plot test data and forecast together with training data
title ="ARIMA Forecast and Training Data"
plt.plot(test_pred)
plt.fill_between(test.index, test_pred['lower food'], test_pred['upper food'], 
                 color='k', alpha=.15)
plt.plot(train,label='actual')
```
Using out-of-sample testing, we see that the forecast result is not good as it did not actually capture the upward trend.  The actual food price is close to the 95% upper bound.
<figure>
  <img src="{{ "/images/posts/ARIMA Forecast (level).png" | relative_url }}">
</figure>
The forecast quality is poor. 
<figure>
  <img src="{{ "/images/posts/ARIMA Forecast and Training Data.png" | relative_url }}">
</figure>

