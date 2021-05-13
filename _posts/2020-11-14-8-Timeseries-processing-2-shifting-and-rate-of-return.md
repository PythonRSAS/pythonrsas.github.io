---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Timeseries processing 2-shifting and rate of return"
description: Shifting, percent change and rate of return
author: Sarah Chen
image: images/posts/S&P 500 Historical Prices and Returns.png

---

This post consists of a few timeseries examples from my upcoming book on statistical and machine learning using Python, also to be published by Apress,as my co-authored book [Python for SAS User](https://www.amazon.com/Sarah-Chen/e/B07ZL3Q97B?ref_=dbs_p_pbk_r00_abau_000000)

## Shifting Time series
Shifting timeseries is needed when we process data across time.   For example, when we compute daily percent change, we are comparing each time point with the one from the day before, <span class="coding">diff(1)/shift(1)</span>.  On the other hand, when comparing with something from tomorrow, we would need <span class="coding">diff(-1)/shift(-1)</span>, where -1 means to go forward into the future.  Oh well.   

In working with data with strong seasonality, we may use year over year.  In the case of quarterly data, a common metric for measuring rate of change without seasonality is <span class="coding">diff(4)/shift(4)</span>. 

There are two main shifting methods in pandas: <span class="coding">shift()</span> and <span class="coding">tshift()</span>. The difference between them is that <span class="coding">shift()</span> shifts the data whereas <span class="coding">tshift()</span> shift the index.   Both can take positive or negative integers to specify number of shifting periods, where positive integer results in lagging and negative number results in leading.    

Under the hood, <span class="coding">tshift()</span> is reindexing the time index.  If you get an error, you should check whether there are *duplicates* in the datetime index or whether your datetime index has a *frequency*.  


## Economic data year over year (Yoy) example: Food and energy CPI
Looking at economic activity data year over year (or sometimes quarter over quarter) is a routine exercise for analysts who work with macroeconomic data, and business performance data.  
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

1. 1900 - 1914    The Gold standard and stability
2. 1915 - 1924    Inflation - World War I
3. 1925 - 1939    Deflation - Interwar instability
4. 1949 - 1970    Moderate inflation - Bretton Woods and the Dollar standard
5. 1971 - 1979    Highly variable inflation - Floating exchange rates, OPEC
6. 1980 - 2000    *Disinflation* - Greater central bank independence

**deflation** is a decrease in general price levels throughout an economy. Deflation, which is the opposite of inflation, is mainly caused by shifts in supply and demand. 
**disinflation** is what happens when price inflation slows down temporarily.  Disinflation shows the rate of change of inflation over time.

Because time series transformation is often used in feature engineering in models, we may need to merge the transformed data with the level data. 
<div class="note"><p>
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

## regression analysis
After preparing the data, we may want to do some simple regression analysis.   Below is an example  
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
```
<figure>
  <img src="{{ "/images/posts/regplot food_yoy and meat_yoy.png" | relative_url }}">
  <figcaption>regplot food_yoy and meat_yoy</figcaption>
</figure>

We now use S&P 500 data to show a few more examples. 
## Example: S&P 500 Historical Prices and Returns

### S&P 500
The S&P 500 Index is a market-value-weighted index of the 500 largest U.S. publicly traded companies. The index is widely regarded as the best gauge of large-cap U.S. equities.  

Mutual funds and ETFs that track S&P Index are part of most passive investors’ portfolio.  

The snippet below shows steps to import, and find the dates with the extreme values, and perform index slicing on the dates and type of data.   We use the pandas_datareader library (version 0.8.1) to get historical S&P 500 stock index data from Yahoo Finance.  Other libraries such as quandl will work just as well.  

The function <span class="coding">pdr.get_data_yahoo</span> takes three inputs: symbol, start date and end date, with the default end as today's date.   <span class="coding">df.idxmax(axis=0, skipna=True)</span> returns the dates with the highest value in every column, which shows that the highest S&P 500 took place on February 19, 2020, although the highest trading volume occurred on October 10, 2008 during the last Financial crisis.    

On the other hand, the historical lowest occurred in 1974 .    The 1973–74 stock market crash caused a bear market between January 1973 and December 1974, which was one of the worst stock market downturns since the Great Depression.      The partial indexing <span class="coding">df.loc["2000":,'Close'].idxmin()</span> tells us the lowest price since year 2000 happened on September 9, 2009 during the last Financial Crisis.   The timestamp of the lowest historical since 1970, and the timestamp of the lowest value in the Financial Crisis are used in the <span class="coding">ax.axvline</span> to plot the vertical dashed lines.   

<div class="code-head"><span>code</span>S&P Historical Values and Extremes.python</div>

```python
 pd.options.display.float_format = '{:10,.1f}'.format 
 import matplotlib.pyplot as plt
 import datetime
 start = datetime.datetime(1970, 1, 1)
 end=datetime.date.today() # today is 04-18-2020
 import pandas_datareader.data as pdr
 df = pdr.get_data_yahoo('^GSPC', start=start, end=end)
 df.tail()
[Out]:
                 High        Low       Open      Close    Volume  Adj Close
Date
1970-01-02       93.5       91.8       92.1       93.0   8050000       93.0
1970-01-05       94.2       92.5       93.0       93.5  11490000       93.5
1970-01-06       93.8       92.1       93.5       92.8  11460000       92.8
1970-01-07       93.4       91.9       92.8       92.6  10010000       92.6
1970-01-08       93.5       92.0       92.6       92.7  10670000       92.7

 df.idxmax(axis=0, skipna=True)
[Out]:
High        2020-02-19
Low         2020-02-19
Open        2020-02-20
Close       2020-02-19
Volume      2008-10-10
Adj Close   2020-02-19
dtype: datetime64[ns]

 df.idxmin(axis=0, skipna=True)
[Out]:
High        1974-10-04
Low         1974-10-04
Open        1974-10-04
Close       1974-10-03
Volume      1970-05-11
Adj Close   1974-10-03
dtype: datetime64[ns]
```
Let's plot the data and highlight those dates with the lowest prices. 
```python
price_min = df.Close.idxmin()
financial_crisis =df.loc["2000":,'Close'].idxmin(axis=0, skipna=True)
plt.style.use('default')
fig, ax = plt.subplots(1,1, figsize=(12,5))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
df.Close.plot( color='mediumseagreen', ax=ax)
ax.axvline(price_min, color ='red', alpha=0.7, dashes=(5, 2, 1, 2), linewidth=1.0)
ax.axvline(financial_crisis, color ='red', alpha=0.7, dashes=(5, 2, 1, 2), linewidth=1.0)
plt.legend(loc='upper left', frameon=False)
plt.ylabel("Closing Price $")
plt.grid(color='lightgrey', linestyle='-.', linewidth=0.7)
plt.tight_layout()
```


<figure>
  <img src="{{ "/images/posts/S&P 500.png" | relative_url }}">
  <figcaption>S&P 500 Historical Prices - Sarah Chen</figcaption>
</figure>

### Daily returns
Now we look at daily returns. <span class="coding">df.Close.diff(1)/df.Close.shift(1)</span> is how we would compute daily return. The convenient <span class="coding">pct_change</span> function gives the same results. 
<div class="code-head"><span>code</span>Rate of daily return.python</div>

```python
# daily return
 rets = df.Close.pct_change()
 rets_manual = df.Close.diff(1)/df.Close.shift(1)
np.testing.assert_allclose(rets_manual,rets,rtol=1e-5)
```

Then we use the <span class="coding">nsmallest()</span> function to get those dates when the largest price decline happened.  The date with the lowest daily return was 1987-10-19, which was the *Black Monday*, one of the worst stock crashes in history.   The two that followed was on March 16 and 12, 2020, due to the Covid-19 pandemic lockdown. The fourth was the  2008-10-15 of the Financial Crisis.   

The <span class="coding">nlargest()</span> function give those dates when the largest price jump happened. The biggest jumps happened right before or after to the largest drop.   It seems that investors changed their minds overnight.  

Anyhow, those are the times with great economic uncertainty and volatility.  
<div class="code-head"><span>code</span>S&P Largest Daily Falls and Jumps.python</div>

```python
nsmallest = rets.nsmallest(4)
print(nsmallest)
Out:
Date
1987-10-19   -0.205
2020-03-16   -0.120
2020-03-12   -0.095
2008-10-15   -0.090
Name: Close, dtype: float64

 nlargest = rets.nlargest(5)
 print(nlargest)
Out:
Date
2008-10-13   0.116
2008-10-28   0.108
2020-03-24   0.094
2020-03-13   0.093
1987-10-21   0.091
Name: Close, dtype: float64
```
We plot historical prices and with the worst days in S&P history annotated. 
<div class="code-head"><span>code</span>plot historical prices.python</div>

```python
# ploting
style = dict(size=11, color='k')
plt.style.use('default') 
title = "S&P 500 Historical Prices and Returns"
fig, ax1 = plt.subplots(1,1, figsize=(12,8))
ax2 = ax1.twinx()
ax1.spines['top'].set_visible(False)
ax1.plot(df.index, df.Close,color='mediumseagreen',alpha=0.5 )
ax2.plot(rets.index, rets,color='grey',alpha=0.3)
ax2.axhline(0, color='grey')
ax2.text(nsmallest.index[1],nsmallest[1], "Covid-19 ", ha='center', **style)
ax2.text(nsmallest.index[3], nsmallest[3], "financial crisis ", ha='center', **style)
ax2.text(Black_Monday, rets.loc[Black_Monday], "Black Monday", ha='center', **style)
ax2.text(Internet_Bubble, -0.15, "Internet Bubble", ha='center', **style)
plt.title(title,fontsize=16)
ax1.spines['bottom'].set_color('grey')
ax1.spines['left'].set_color('grey')
ax1.spines['right'].set_color('grey')
ax2.spines['right'].set_color('grey')
ax2.spines['bottom'].set_color('grey')
ax2.spines['left'].set_color('grey')
ax1.set_ylabel("Closing Price $",color='mediumseagreen',fontsize=12)
ax2.set_ylabel('Daily Return', color='k',fontsize=12)
ax2.set_ylim(-0.25,0.25)
```
<figure>
  <img src="{{ "/images/posts/S&P 500 Historical Prices and Returns.png" | relative_url }}">
  <figcaption>S&P 500 Historical Prices and Returns - Sarah Chen</figcaption>
</figure>

### Monthly returns
To get monthly return, our first instinct might have been using <span class="coding">freq='M'</span>.    But since the data only occurs on business days, then we need to use the prefix <span class="coding">B</span> for the frequency.  Otherwise the result can be incorrect. 

<div class="code-head"><span>code</span>Rate of monthly return.python</div>

```python
#monthly return
 df.Close.pct_change(freq='BM').dropna().tail(2)
Out: 
Date
2020-09-30   -0.039
2020-10-30   -0.028
Name: Close, dtype: float64

 oct = df.loc['2020-10-30','Close']
 sep = df.loc['2020-09-30','Close']
 aug = df.loc['2020-08-31','Close']
 (oct-sep)/sep
Out: -0.02766578622137972
 (sep-aug)/aug
Out: -0.03922797017842309
```
### Annual returns
Annual return or percent change year over year is commonly used in all industries.  The easiest is to use <span class="coding">pct_change(freq='Y')</span> or <span class="coding">pct_change(freq='BY')</span> function.   You need to be careful to use the correct frequency otherwise the results will likely be incorrect. 

In example below, we compute and plot annual returns of S&P 500 since 1970.   Because <span class="coding">pct_change(freq='BY')</span>  is only for full years, it will not work for the latest year to date.   Although there are other ways of handling it, here we will use the year to date as if we had a full year.  Thus, the annual return for 2020 is <span class="coding">return_2020 = adj_close[-1]/adj_close.loc['2020-01-02']-1</span>.  
<div class="code-head"><span>code</span>Annual Returns.python</div>

```python
 adj_close = pdr.get_data_yahoo('^GSPC', start=start, end=date.today())['Adj Close']
 title = "Annual Returns"
 Annual_return = adj_close.pct_change(freq='BY').dropna().asfreq('BY')
 return_2020 = adj_close[-1]/adj_close.loc['2020-01-02']-1
# pretend we had a full year already in 2020
 idx = pd.date_range(date(2020,1,1),date(2020,12,31), freq='BA-DEC' )
 Annual_return = Annual_return.append(pd.Series(return_2020,index=idx))
# plot
 fig, ax = plt.subplots(1,1, figsize=(12,5))
 ax.spines['top'].set_visible(False)
 ax.spines['right'].set_visible(False)
 ax = plt.bar(Annual_return.index.year, Annual_return,alpha=0.5)
 plt.axhline(Annual_return.mean(), color='r', linestyle='--')
```
Figure shows the annual return from 1970 to 2020.  The horizontal dashed line is the average of annual returns.
<figure>
  <img src="{{ "/images/posts/Annual Returns.png" | relative_url }}">
  <figcaption>S&P Annual Returns - Sarah Chen</figcaption>
</figure>
Before 1984, investing in the S&P 500 stock market seem hardly worth it: roller-coaster-like returns with -29.7% in 1974 and 31.1% in 1975 while the safe 10-year Treasury was averaging between 6% and 12.5%.  
In 1982, the return from S&P500 was 14.8% when average 10-year Treasury yield was 13.0%.   
In quite several years the S&P 500 annual return was terribly negative when one could have gotten safe returns from the government bond.   
But after the Financial Crisis in 2009, the stock market annual returns have stayed positive except 2018 and 2020.  
<figure>
  <img src="{{ "/images/posts/S&P 500 Annual Return vs Average 10-Year Treasury.png" | relative_url }}">
  <figcaption>S&P 500 Annual Return vs Average 10-Year Treasury - Sarah Chen</figcaption>
</figure>

History shows us that even investing in the S&P 500 does not always yield great returns.  If we invested on 2000-03-24, the best day of S&P stock prices before 2001, and hold it for twenty years until 2020-02-19, its peak before the market crash prior to the Financial Crisis, our annual rate of return would have been a not-so-amazing 4%.   When computing returns over a period, we usually use adjusted closing price instead of closing price.  We will compute annualized return and continuous annual return.  

In the next example we compute annualized return and continuous annual return.  History shows us that investing in the S&P 500 does not always yield great returns.  If we invested on 2000-03-24, the best day of S&P stock prices before 2001, and held it for about twenty years until the all-time high on 2020-11-14, the annual rate of return would have been a not-so-amazing 4%.    

If you are curious enough to check what was the S&P on 2020-03-24, the twenty-year anniversary, you will find a disappointing 2447, yielding 2.4% annual return.  

Timing is so important. 

When computing returns over a period, adjusted closing price is used.    For those who are following, the peak before coronas virus pandemic was 3386.150 on Feb 19, 2020.   The index went to 3585, about 200 points higher than the peak before the pandemic. 

<div class="code-head"><span>code</span>Annual Rate of Return and Continuous Return.python</div>

```python
 df = pdr.get_data_yahoo('^GSPC', start=datetime(1970,1,1), end=datetime(2020,11,14)['Adj Close']
 df.nlargest(2)
Out:
Date
2020-11-13   3585.150
2020-09-02   3580.840
Name: Adj Close, dtype: float64
 df[:'2001'].nlargest(1)
Out: 
Date
2000-03-24   1527.460
 n = df.idxmax().year-df[:'2001'].idxmax().year #20 years
 Annual_return = (df.max()/df[:'2001'].max())**(1/n)-1
 print("{0:.2%}".format(Annual_return))
Out: 4.36%

 continuous_return = np.log(df.max()/df[:'2001'].max())/n
 print("{0:.2%}".format(continuous_return))
Out: 4.27%
```

We run a statistical test to see whether returns are normal. The test result shows that return is far from being normal.  Alternative tests (not shown) will come to the same conclusion.  

<div class="code-head"><span>code</span>S&P 500 Daily Return Normality Test.python</div>

```python
 from scipy.stats import norm
 norm_test =stats.anderson(rets.dropna(), dist='norm')
 stat, p = stats.kstest(rets.dropna(), 'norm')
 print('p-value: {0: .4f}'.format(p))
Out: 0.0000
 sns.distplot(x, fit=norm, kde=False, rug=True)
```
<figure>
  <img src="{{ "/images/posts/Figure 1- 9. Distribution of Return.png" | relative_url }}">
  <figcaption>S&P 500 Daily Return Normality Test - Sarah Chen</figcaption>
</figure>

