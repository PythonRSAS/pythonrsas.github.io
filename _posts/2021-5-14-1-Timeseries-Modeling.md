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
<figure>
  <img src="{{ "/images/posts/regplot food_yoy and energy_yoy.png" | relative_url }}">
  <figcaption>regplot food_yoy and meat_yoy</figcaption>
</figure>

