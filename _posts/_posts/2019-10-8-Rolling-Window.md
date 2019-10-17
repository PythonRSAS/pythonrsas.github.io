---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Rolling Window"
description: Time series data processing using Python and SAS.
author: Sarah Chen
# image: http://drive.google.com/uc?export=view&id=1QCuv6RGm8y1vdPU4DitqOZPIbx8Nw-yM
---

**While we are postponing, life speeds by.**

<!-- > not used for now**Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**. -->


In this and the next two sections, we discuss two important time series processing methods: windowing and resampling.    
 1.   In windowing, statistics are calculated from the windowed rows when “rolling” or “expanding” through each row and frequencies are not changed.   Whereas resampling often changes frequencies of the data via up sampling (higher frequency) or down sampling (lower frequency).  

 2.   Resampling is time-based <span class="coding">.groupby()</span> and requires datetime index.  Whereas, rolling window can be applied to any pandas object, not restricted to those with datetime indices. If the index is not a date, or datetime index, the <span class="coding">on</span> specification must be provided to let pandas know which column to roll on.  
 
Rolling windows in Python and SAS  both can produce statics such as moving average, weighted mean, min, max, standard deviation, sum, rank, etc.  
The <span class="coding">ID</span> variable in SAS <span class="coding">PROC EXPAND</span> is analogous to pandas <span class="coding">datetimeIndex</span> in the context of comparing with pandas <span class="coding">rolling</span>.  However, in <span class="coding">PROC EXPAND</span> the <span class="coding">ID</span> variable must be a SAS datetime variable and is unambiguous.  

Rolling in pandas, however, is implemented both as time-window and count-based, which produce different results when the index is irregular, which could be confusing if not understood properly.  

What we mean by time-window is that the operation is faithful to time, not to observation count.   The causes of the discrepancy or confusion are the <span class="coding">window</span> and/or <span class="coding">min_periods</span> parameters.  This is how it is implemented in pandas 0.19.0+.   Hopefully the developers will improve upon it and make it less ambiguous in the future. 
The <span class="coding">rolling</span> syntax is as followed:
```python
.rolling(
    ['window', 'min_periods=None', 'center=False', 'win_type=None', 'on=None', 'axis=0', 'closed=None'],
)
```
We will go over <span class="coding">window</span>, <span class="coding">min_periods</span>, <span class="coding">center</span>, closed in detail. 
The <span class="coding">window</span> and the <span class="coding">min_periods</span> parameters
From pandas documentation:
    <span class="coding">window</span>: int, or offset
    Size of the moving window. This is the number of observations used for
    calculating the statistic. Each window will be a fixed size.
    If it is an offset, then this will be the time period of each window. Each
    window will be a variable sized based on the observations included in
the time-period. This is only valid for datetime-like indexes.
 
* <span class="coding">min_periods</span>: int, default None
Minimum number of observations in window required to have a value
(otherwise result is NA). 

For a window that is specified by an offset, this will default to 1.
The example below compares count-based window and time-based window for regular (without gaps) datetime index.     In the first example, <span class="coding">rolling</span>(2).sum() returns what we expect from pandas: summing with NaN returns NaN.   In the second example, we see that <span class="coding">rolling</span>(window = '2d').sum()seems to have ignored the NaN.   This seemingly strange behavior is because <span class="coding">min_periods</span> =1 is the default setting for offset window.    

However, in the third example, the result is still the same as Example 2, even if we have specified <span class="coding">min_periods</span>=None.   It seems that for offset windows, the minimum period is 1 unit, even if it is set to None.  

In Example 4, we finally get the same result as Example 1 after setting <span class="coding">min_periods=2</span>.    

Example 5 and 6 are to confirm that as the following conclusion:
For regular dateimeIndex, to get the same results from count-based and time-based windows, remember to specify the same <span class="coding">min_periods</span>, except that for offset windows, the minimum period is 1 unit, even when it is set to None .    
<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df = pd.DataFrame({'x': [0, 1, 2, np.nan, 4]},
                    index=pd.date_range('20200101',
                    periods=5, freq='d'))
>>> df
[Out]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  2.0
2020-01-04  NaN
2020-01-05  4.0

# Example 1
>>> df.rolling(window = 2).sum()
[Out]:
              x
2020-01-01  NaN
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  NaN
2020-01-05  NaN

# Example 2
>>> df.rolling(window = '2d').sum()
[Out]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  2.0
2020-01-05  4.0

# Example 3
>>> df.rolling(window='2d', min_periods=None).sum()
[Out]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  2.0
2020-01-05  4.0

# Example 4
>>> df.rolling(window='2d', min_periods=2).sum()
[Out]:
              x
2020-01-01  NaN
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  NaN
2020-01-05  NaN

# Example 5
>>> df.rolling(window='2d', min_periods=1).sum()
Out[9]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  2.0
2020-01-05  4.0

# Example 6
>>> df.rolling(window=2, min_periods=1).sum()
Out[11]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  2.0
2020-01-05  4.0
```
In the example below makes the comparisons for irregular datetime index.  Contrasting to an integer rolling window, offset window will have variable window length corresponding to the time period.  Again the default for offset window <span class="coding">min_periods</span> is 1.   To see why Example 1 and Example 2 have different results, it may be helpful to look at Example 3, which fills all the missing dates using <span class="coding">.resample('D')</span> function and makes it easier to see how time-based window works.  
<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Irregular DatetimeIndex.py</div>

```python
>>> idx = pd.to_datetime(['2020-01-01', '2020-01-03', '2020-01-05', '2020-01-06','2020-01-08'])
>>> df.index = idx
>>> df
[Out]:
              x
2020-01-01  0.0
2020-01-03  1.0
2020-01-05  2.0
2020-01-06  NaN
2020-01-08  4.0

# Example 1
>>> df.rolling(window=2, min_periods=1).sum()
[Out]:
              x
2020-01-01  0.0
2020-01-03  1.0
2020-01-05  3.0
2020-01-06  2.0
2020-01-08  4.0

# Example 2
>>> df.rolling(window='2d', min_periods=1).sum()
[Out]:
              x
2020-01-01  0.0
2020-01-03  1.0
2020-01-05  2.0
2020-01-06  2.0
2020-01-08  4.0

# Example 3
>>> df.resample('D').mean()
[Out]:
              x
2020-01-01  0.0
2020-01-02  NaN
2020-01-03  1.0
2020-01-04  NaN
2020-01-05  2.0
2020-01-06  NaN
2020-01-07  NaN
2020-01-08  4.0
```
To avoid getting unexpected result, it is best to try to be Pythonic and be explict as much as possible, especially in working with rolling windows given the dual implementations for count-based window and time-based window, while being mindful of the fact that when using offset window, <span class="coding">min_periods</span> is default to 1 when you specify <span class="coding">min_periods</span>=None.   

While the rolling implementation may not be perfect, the advantage of open source is that you can send your feedback to the developers, fork the pandas repo on Github, improve it and make a pull request to join the collaboration.    

For reference, we note that SAS <span class="coding">PROC EXPAND</span> handles missing values (gaps in <span class="coding">ID</span>) by interpolation or SETMISS to impute missing as how user specifies it (such as SETMISS 0), or set it to missing using the  <span class="coding">TO </span> parameter.   
The <span class="coding">center</span> parameter
From pandas documentation:
    <span class="coding">center</span> : boolean, default <span class="coding">False</span>
The default behavior of rolling window in pandas is looking backward.  This is an intuitive choice as at the most recent data point one can look back into the past.  Moving average is usually calculated using backward window.  Backward looking window calculated statistics has a lagging effect due to all but one of the data points are from the past.
For backward moving window, the width of the time window is shortened at the beginning of the series. 
The lagging effect of backward moving window may be undesirable depending on purpose.  Both Python and SAS have specifications to center rolling window.  The following example below gives an example calculating 60 day moving average and center moving average using the same Bitcoin time series data. 
 
<div class="code-head"><span>code</span> Moving Average Historical Bitcoin Prices using pandas Rolling.py</div>

```python
>>> ma60_center = df.High.rolling(60, center = True)
>>> ma60_back = df.High.rolling(60, center = False)
>>> ma = pd.DataFrame({'price':df.High, '60 day moving 
average': ma60_back.mean(), '60 day center moving average': ma60_center.mean()})
>>> ma.loc['2017':,:].plot(title="daily price, 60-day moving 
average and center moving average") 
```
Figure 9-3. Moving Average Using Rolling Window Backward and Center
 
Note: 
    Many other statistics can be explored.  For example, rolling standard deviation tells how volatility changes over time, and rolling correlation tells how correlations changes over time for specified window. 
When the window width is an odd number, then there is no difference between SAS <span class="coding">PROC EXPAND</span> CMOVAVE and Python pandas center moving averages.   But when the width is an even number, then they are different.  One more lead value than lag value is included in the time window in <span class="coding">PROC EXPAND</span> CMOVAVE.   For example, the result of the <span class="coding">CMOVAVE 4</span> operator is:
SAS:   y_t=(x_(t-1)+x_t+x_(t+1)+ x_(t+2))/4
Whereas pandas rolling(4, center = True) takes one more lag than lead. 
Python: y_t=(x_(t-2)+x_(t-1)+x_t+ x_(t+1))/4
For reference, SAS <span class="coding">PROC EXPAND</span> syntax is as followed.  Other than standard PROC statements, only FROM, CONVERT and <span class="coding">ID</span> are required and the rest are optional.  Upper case is keyword and lower case is user-defined. 
    SAS PROC EXPAND SYNTAX
PROC EXPAND DATA=input_dsn OUT=output_dsn 
FROM=time_interval 
TO=time_interval METHOD=conversion_method; 
BY by_variable(s);
CONVERT old_var =  new_var/OBSERVED=frequency   TRANSFORMIN = (transformation operators)    TRANSFORMOUT = (transformation operators)   OBSERVED= observational_characteristic; 
ID date_var; 
RUN; 

In the example below we provide the example in SAS to perform moving average and center moving average.  As noted before, using <span class="coding">PLOTS=ALL</span> will produce one plot each for the before and after variables. 
<div class="code-head"><span>code</span> Moving Averages in SAS PROC EXPAND.sas</div>

```sas
>>> PROC EXPAND DATA=df METHOD=NONE;
ID date; 
CONVERT price = movave60 /  
TRANSFORMIN=(SETMISS 0) TRANSFORMOUT=(MOVAVE 60);
CONVERT price = cmovave 60 /  
TRANSFORMIN=(SETMISS 0) TRANSFORMOUT=(CMOVAVE 60);
RUN;
```
The <span class="coding">closed</span> Parameter
From pandas documentation,
    <span class="coding">closed</span> : string, default None
Make the interval closed on the 'right', 'left', 'both' or 'neither' endpoints.   For offset-based windows, it defaults to <span class="coding">right</span>.   For fixed windows, defaults to <span class="coding">both</span>. Remaining cases not implemented for fixed windows.
Closed end is only implemented for datetime-like and offset based windows even though rolling is implemented for all pandas objects.   For those who are not familiar with what <span class="coding">closed</span> is referring to, imagine you are standing in time, with the past to your left, and the future to your right, the so-called <span class="coding">closed</span> concerns the following two data points: 
    the observation row itself 
    the leftist/oldest point of the window (if counting from the observation row, then it is the row just before the window)
Left closed means include the oldest point (2).  Right closed means include the newest point (1). 
The different effects of closed are best understood through an example.  In example below, we first create a <span class="coding">datetimeIndex</span> DataFrame, then calculate four second window rolling sum, without specifying closed.   
<div class="code-head"><span>code</span> Different Kinds of Closed Rolling Windows when Time Index is Evenly Spaced.py</div>

```python
>>> df = pd.DataFrame({'x': [1,1,1,1,3]}, index =   
    [pd.Timestamp('20200101 09:00:01'),
     pd.Timestamp('20200101 09:00:02'),
     pd.Timestamp('20200101 09:00:03'),
     pd.Timestamp('20200101 09:00:04'),
     pd.Timestamp('20200101 09:00:05')])
>>> df["default"] = df.rolling('4s').x.sum().astype(int)
>>> df["left"] = df.rolling('4s', closed='left').x.sum()
>>> df["both"] = df.rolling('4s', closed='both').x.sum()
>>> df["right"] = df.rolling('4s', closed='right').x.sum()
>>> df["neither"] = df.rolling('4s', closed='neither').x.sum()
>>> df
[Out]:
                     x  default  left  both  right  neither
2020-01-01 09:00:01  1        1   NaN   1.0    1.0      NaN
2020-01-01 09:00:02  1        2   1.0   2.0    2.0      1.0
2020-01-01 09:00:03  1        3   2.0   3.0    3.0      2.0
2020-01-01 09:00:04  1        4   3.0   4.0    4.0      3.0
2020-01-01 09:00:05  3        6   4.0   7.0    6.0      3.0
```
We now change the last example slightly and run all the above code again.  The output demonstrates that rolling on <span class="coding">datetimeIndex</span> using time frequency, such as '4s' is faithful to time, not to record order count.  Reading or practice through this example will help you understand <span class="coding">datetimeIndex</span>. 
<div class="code-head"><span>code</span> Different Kinds of Closed Rolling Windows when there is Gap in Time Index.py</div>

```python
>>> df = pd.DataFrame({'x': [1,1,1,1,3]}, index =   
    [pd.Timestamp('20200101 09:00:01'),
     pd.Timestamp('20200101 09:00:02'),
     pd.Timestamp('20200101 09:00:03'),
     pd.Timestamp('20200101 09:00:04'),
     pd.Timestamp('20200101 09:00:07')])
>>> df["left"] = df.rolling('4s', closed='left').x.sum()
>>> df["both"] = df.rolling('4s', closed='both').x.sum()
>>> df["right"] = df.rolling('4s', closed='right').x.sum()
>>> df["neither"] = df.rolling('4s', closed='neither').x.sum()
>>> df
[Out]:
                     x  default  left  both  right  neither
2020-01-01 09:00:01  1        1   NaN   1.0    1.0      NaN
2020-01-01 09:00:02  1        2   1.0   2.0    2.0      1.0
2020-01-01 09:00:03  1        3   2.0   3.0    3.0      2.0
2020-01-01 09:00:04  1        4   3.0   4.0    4.0      3.0
2020-01-01 09:00:07  3        4   2.0   5.0    4.0      1.0
```
The <span class="coding">win_type</span> parameter
    <span class="coding">win_type</span> : string, default None.   Provide a window type. If ``None``, all points are evenly weighted.
There are more than a dozen window types implemented in pandas rolling, where the default is <span class="coding">win_type=None</span>, which means all points are evenly weighted . 
The recognized win_types are: <span class="coding">win_type=None</span>, <span class="coding">boxcar</span>, <span class="coding">blackman</span>, <span class="coding">hamming</span>, <span class="coding">bartlett</span>, <span class="coding">parzen</span>, <span class="coding">bohman</span>, <span class="coding">blackmanharris</span>, <span class="coding">nuttall</span>, <span class="coding">barthann</span>, <span class="coding">kaiser</span>, <span class="coding">gaussian</span>, <span class="coding">general_gaussian</span>, <span class="coding">slepian</span>.
In the first example, a triangular window is used by specifying <span class="coding">win_type='triang'</span>.   In the second example,the <span class="coding">boxcar</span> window is also known as rectangular window, which is equivalent to no window type at all.  Therefore it has the same result as Example 6 in the example. 
<div class="code-head"><span>code</span> Using win_type in Rolling Window.py</div>

```python
>>> df = pd.DataFrame({'x': [0, 1, 2, np.nan, 4]},
    ...:                     index=pd.date_range('20200101',^M
    ...:                     periods=5, freq='d'))
>>> df.rolling(window = 2,min_periods=1, 
win_type='triang').sum()
[Out]:
              x
2020-01-01  0.0
2020-01-02  0.5
2020-01-03  1.5
2020-01-04  1.0
2020-01-05  2.0

>>> df.rolling(2,min_periods=1, win_type='boxcar').sum()
[Out]:
              x
2020-01-01  0.0
2020-01-02  1.0
2020-01-03  3.0
2020-01-04  2.0
2020-01-05  4.0
```

