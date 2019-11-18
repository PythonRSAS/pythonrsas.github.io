---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Time Series Indexing"
description: Time series data processing using Python and SAS.
author: Sarah Chen
image: images/posts/derek-mack.jpg
---
<!-- image: images/posts/derek-mack.jpg -->
<!-- https://drive.google.com/uc?export=view&id=1qdvZnKpHH8QlnmjJq-l-zE3rajpTyXxm -->
**While we are postponing, life speeds by.**

<!-- > not used for now**Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**. -->

The most fundamental measures of time are point in time **timestamp** and **intervals** (fixed or variable), and the difference between them **timedelta**.  These objects provide building blocks for comprehensive timeseries data processes.  

Recall a pandas index is simply a way to label rows.  One of the main uses of Timestamp and Period objects is indexing.   Lists of Timestamp or Period objects are automatically coerced to <span class="coding">DatetimeIndex</span> and <span class="coding">PeriodIndex</span> respectively when used as index.    Python pandas is powerful and convenient in handling timeseries.  But there are also traps and tips you should be aware in order to avoid errors. 

In this post, you will learn: 

[- DatetimeIndex](#DatetimeIndex)

[- Partial String Indexing](#Partial-String-Indexing)

[- An Example Using Historical Bitcoin Trade Data](#An-Example-Using Historical-Bitcoin-Trade-Data)

[- PeriodIndex](#PeriodIndex)

[- TimeDeltaIndex](#TimeDeltaIndex)

[- Multiindex](#Multiindex)

[- Stack and Unstack](#Stack-and-Unstack)

[- Duplicates in Index](#Duplicates-in-Index)

[- Missing Values](#Missing-Values)
<figure>
  <img src="{{ "/images/posts/derek-mack.jpg" | relative_url }}">
  <figcaption>Photo by Derek Mack</figcaption>
</figure>

Let's get started. 

SAS users need to be aware that pandas allow duplicate index.  When we perform strict timeseries analysis, we would need to remove duplicates.  



<h3 id="DatetimeIndex">DatetimeIndex</h3>

Pandas <span class="coding">Timestamp</span> is pandas' equivalent to the Python's native datetime  object and in many cases a pandas Timestamp is interchangeable with Python's datetime object.    Pandas Timestamp  combines the flexibility of datetime and <span class="coding">dateutil</span> and the efficiency of vectorized representation from numpy.datetime64.  
The example below illustrates how a list of objects with mixed formats is automatically coerced to <span class="coding">Datetimeindex</span> by .

<div class="code-head"><span>code</span>Pandas DatetimeIndex.py</div>

```python
>>> dates = ['1-02-2020', '4-1-2020','2020-07-04', '4th of July, 2020', '2020-12-31']
>>> pd.to_datetime(dates, dayfirst=False)
[Out]: DatetimeIndex(['2020-01-02', '2020-04-01', 
'2020-07-04', '2020-07-04', '2020-12-31'],
     dtype='datetime64[ns]', freq=None)
```
* From pandas version 0.20.0. there is a new <span class="coding">origin</span> parameter for specifying an alternative starting point for creation of a <span class="coding">DatetimeIndex</span>.  For example, using 1960-01-01 as the starting date would make pandas dates have the same reference starting date as SAS date
* If you do not specify origin, then the default is <span class="coding">origin='unix'</span>, which defaults to 1970-01-01 00:00:00.  This is commonly called 'unix epoch' or POSIX time. 
* Pandas represents timestamps in nanosecond resolution.  Hence the time span that can be represented using a 64-bit integer is limited to approximately 584 years.   On the other hand, SAS does not have such limitation  as SAS stores dates as integers, datetime and time as real numbers. 

SAS date or time are stored internally in numbers and represented according to formats user specified.  Example below prints current date, time, and datetime stamps.  
<div class="code-head"><span>code</span>SAS Date Time and Datetime Stamps.sas</div>

```sas
>>> DATA _NULL_;
    d1=DATE();
    t1=TIME();
    dt1=datetime();
    PUT d1 DATE9-;
    PUT t1 TIME10.;
    PUT dt1 DATETIME21.2;
    RUN;
/*20:56:09 09OCT2019 */
```

As mentioned earlier, pandas is built on top of numpy.  Vectorized operations from numpy can be applied directly on Timestamp object to create a sequence of dates or times, which is automatically coerced into <span class="coding">DatetimeIndex</span> object.   This is illustrated in the next example. 
<div class="code-head"><span>code</span>Vectorized Operation on Timestamp.py</div>

```python
>>> date1= pd.Timestamp('2020-01-02')
>>> date1 + pd.to_timedelta(np.arange(3),'D')
Out:  DatetimeIndex(['2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq=None)
```
Base SAS does not have vectorized operations.  To create similar output, one may write a simple loop such as the one below:
<div class="code-head"><span>code</span>SAS Date Time Sequence.sas</div>

```sas
>>> %let start = 02Jan2020;
>>> %let end = 04Jan2020;
>>> DATA _null_;
  DO date="&start"d  to "&end"d;
    PUT date YYMMDD10.;
  END;
  RUN;
```
<h3 id="Partial-String-Indexing">Partial String Indexing</h3>
In SAS, subsetting date ranges are performed via <span class="coding">WHERE</span> clause or <span class='coding'>IF</span> statement in a <span class="coding">DATA</span> step, or <span class="coding">WHERE</span> clause in <span class="coding">PROC SQL</span>. Since pandas <span class="coding">DatetimeIndex</span> has all the basic functions of regular index , you can use the regular index methods to slice and dice DataFrame or Series, and use <span class="coding">DatetimeIndex</span> to perform “partial string indexing”.   

For example, omitting the day component extracts all rows belong to a particular year or month.   The uses of partial string index are interspersed throughout the remainder of the Indexing section and are identified in the text.

<h3 id="An-Example-Using Historical-Bitcoin-Trade-Data">An Example Using Historical Bitcoin Trade Data</h3>

It is time for a real life example.  We use Python library <span class="coding" >pandas_datareader</span> to get historical Bitcoin data from Yahoo Finance.   In example below, we show steps to import, store, reload stored DataFrame and perform index slicing. 
<div class="code-head"><span>code</span> Bitcoin Historical Prices using DatetimeIndex.py</div>

```python
>>> import pandas_datareader.data as pdr
>>> import matplotlib.pyplot as plt
>>> import datetime
>>> df = pdr.get_data_yahoo('BTC-USD', 
start=datetime.datetime(2010, 7, 16), 
end=datetime.date.today())
>>> df.drop('Adj Close', axis=1, inplace=True) 
>>> df.tail()
[Out]:
               High      Low     Open    Close     Volume
Date
2019-08-11  11554.7  11240.4  11549.1  11387.4  229908138
2019-08-12  11439.5  10765.3  11387.4  10872.0  483240069
2019-08-13  10873.4   9924.6  10872.0  10031.9  728247545
2019-08-14  10451.6   9497.1  10031.9  10264.7  840141301
2019-08-17  10381.5  10231.4  10360.4  10256.5   18056754 

>>> <span class="coding">df.index.inferred_freq </span>
#retruns nothing because freq is irregular

# the dates when the maximum took place
>>> df.idxmax(axis=0, skipna=True)
[Out]:
High        2017-12-17
Low         2017-12-17
Open        2017-12-17
Close       2017-12-16
Volume      2017-12-22
dtype: datetime64[ns]

>>> pd.options.display.float_format = '{:20,.1f}'.format 

>>> df1 = df.loc["2017-12-17":"2017-12-22",df.columns.isin(['High','Low'])]
>>> df1
[Out]:
                           High                  Low
Date
2017-12-17               19,871               18,751
2017-12-18               19,221               18,114
2017-12-19               19,022               16,813
2017-12-20               17,814               15,643
2017-12-21               17,302               14,953
2017-12-22               15,824               10,876

>>> df.loc["2018",df.columns.isin(['High','Low'])].
plot(title="Bitcoin 2018 daily high and low price timeseries")
```
<figure>
  <img src="{{ "/images/posts/Bitcoin 2018 daily high and low price timeseries.png" | relative_url }}">
  <figcaption>Figure 1. Bitcoin 2018 daily high and low price timeseries</figcaption>
</figure>

<h3 id="PeriodIndex">PeriodIndex</h3>

Recall that for pandas, a Period is a bounded time segment, i.e. time span, uniform in length with a start and end date with a given frequency and has the associated PeriodIndex, we can define a PeriodIndex directly by using the <span class="coding">pd.PeriodIndex</span> or <span class='coding'>pd.period_range()</span> constructor, which creates a list of periods with frequency specified.   Unlike a <span class="coding">DatetimeIndex</span>, labels for the PeriodIndex are Period objects.    

<div class="code-head"><span>code</span> Constructing PeriodIndex Object using pd.PeriodIndex() and pd.period_range().py</div>

```python
>>> dates = ['2020-01-02', '2020-4-1','2020-07-04', '2020-12-31']
>>> periodIndexDay = pd.PeriodIndex(dates, freq='D')
>>> periodIndexDay
[Out]: PeriodIndex(['2020-01-02', '2020-04-01', '2020-07-04', '2020-12-31'], dtype='period[D]', freq='D')

>>> pd.PeriodIndex(dates, freq='M')
[Out]: PeriodIndex(['2020-01', '2020-04', '2020-07', '2020-12'], dtype='period[M]', freq='M')

>>> pd.PeriodIndex(dates, freq='Q')
[Out]: PeriodIndex(['2020Q1', '2020Q2', '2020Q3', '2020Q4'], dtype='period[Q-DEC]', freq='Q-DEC')

>>> idx = pd.period_range('2020','2022', freq='Q')
>>> idx
[Out]: PeriodIndex(['2020Q1', '2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2',
             '2021Q3', '2021Q4', '2022Q1'],dtype='period[Q-DEC]', freq='Q-DEC')
```
Note:
* We can convert a series of <span class="coding">DatetimeIndex</span> to <span class='coding'>PeriodIndex</span> by the <span class="coding">.to_period()</span> function.  
*  If you have to parse datetime from string format before you convert it to period index, you can use <span class="coding">pd.to_datetime('string', format ='%d-%b-%y'M).dt.to_period('M')</span>
Conversely, <span class='coding'>PeriodIndex</span> can be converted to <span class="coding">DatetimeIndex</span> using either <span class="coding">pd.to_timestamp</span> or <span class="coding">.astype('datetime64[ns]')</span>.  

<div class="code-head"><span>code</span> Converting between Period index and  DatetimeIndex.py</div>

```python
>>> idx.to_timestamp()
[Out]: DatetimeIndex(['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01', '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01', '2022-01-01'], dtype='datetime64[ns]', freq='QS-OCT')
>>> idx.astype('datetime64[ns]') # output is the same as above 
>>> idx.to_timestamp().to_period(freq='Q') # gives the orginal PeriodIndex back
[Out]: PeriodIndex(['2020Q1', '2020Q2', '2020Q3', '2020Q4', '2021Q1', '2021Q2', '2021Q3', '2021Q4', '2022Q1'], dtype='period[Q-DEC]', freq='Q-DEC')
```
As with <span class="coding">Datetimeindex</span>, we can apply “partial string indexing” to PeriodIndex.   The following example shows how convenient it is to subset data by passing a component of a datetime.  
<div class="code-head"><span>code</span> Partial String Indexing using PeriodIndex py</div>

```python
>>> df = pd.DataFrame({'x' :np.random.randint(0, high = 10, size =9)}, index = idx)
>>> df
[Out]: 
        x
2020Q1  6
2020Q2  3
2020Q3  7
2020Q4  4
2020Q1  6
2021Q2  9
2021Q3  2
2021Q4  6
2022Q1  7
>>> df['2020'].sum()
[Out]: 
x    20
dtype: int64
```
<h3 id="TimeDeltaIndex">TimeDeltaIndex</h3>

TimeDeltaIndex is like a series of numbers with day and/or time units. 
TimeDeltaIndex can be created by 
1.  taking the difference of two dates, 
2.  converting using to_timedelta(), or
3.  defining using pd.timedelta_range()

The following example below illustrates each of these methods.  While the examples given are mostly in days for simplicity, there is a very wide range of units that can be used.  

<div class="code-head"><span>code</span> TimedeltaIndex.py</div>

```python
>>> dateTimeIndex = pd.DatetimeIndex(pd.date_range( start='1/1/2020', periods=4, freq='M')) 
>>> dateTimeIndex - dateTimeIndex[0]
[Out]: 
TimedeltaIndex(['0 days', '29 days', '60 days', '90 days'], dtype='timedelta64[ns]', freq=None) 

>>> pd.to_timedelta(np.arange(4),'D') *10
[Out]: 
TimedeltaIndex(['0 days', '10 days', '20 days', '30 days'], dtype='timedelta64[ns]', freq=None)

>>> pd.timedelta_range(start='0 days', periods=3)
[Out]: 
TimedeltaIndex(['0 days', '1 days', '2 days'], dtype='timedelta64[ns]', freq='D') 

>>> pd.timedelta_range(start='5 days', periods=3, freq='24H')
[Out]: 
TimedeltaIndex(['5 days', '6 days', '7 days'], dtype='timedelta64[ns]', freq='24H')
```

For reference, example below shows differencing in SAS datetime.  

<div class="code-head"><span>code</span> SAS Datetime Differencing.sas</div>

```sas  
>>> DATA df;
INPUT startdate DATE9- @11 enddate DATE9-;
Duration=enddate-startdate;
DATALINES;
15dec2020 15dec2020
17oct2020 02nov2020
22jan2021 11mar2021;
>>> PROC PRINT DATA=df;
    FORMAT startdate enddate DATE9-;
  RUN; 
[Out]: 
Obs startdate Enddate Duration
1 15-Dec-19 15-Dec-19 0
2 17-Oct-20 2-Nov-20  16
3 22-Jan-21 11-Mar-21 48
```

<h3 id="Multiindex">Multiindex</h3>

Many timeseries operations cannot be performed if there are duplicated indices.   As mentioned earlier, when the <span class="coding">datetimeindex</span> is irregular, nothing will be returned from <span class="coding">df.index.inferred_freq</span>.  There are multiple ways to remove duplicates in pandas.  When the duplicates are in the columns, <span class="coding">DataFrame.sort_value()</span>, <span class="coding">DataFrame.drop_duplicates()</span>,and <span class="coding">DataFrame.set_index()</span> are the standard procedures to sort, drop duplicate and set index to clean data.   When the duplicates are in <span class="coding">DatetimeIndex</span>, we can use <span class="coding">DataFrame.index.duplicated()</span> to get the array of boolean values of whether an index is a duplicate.  

The <span class="coding">keep = 'first'</span>, <span class="coding">keep = 'last'</span>, or <span class="coding">keep = False</span> option is to mask those duplicates from being identified as True.   By default, for each set of duplicated values, the first occurrence is set to False and all others to True, in effect, keeping the first occurance when you drop duplicates.  To summarize:

• 'first', marking duplicates as True except the first occurrence

• 'last',marking duplicates as True except the last occurrence

• False, marking all duplicates as True

Here is an example of using <span class="coding">DataFrame.index.duplicated()</span>.  Because we use <span class="coding">keep = False</span>, all the duplicated indices are shown, including first and last.  

<div class="code-head"><span>code</span> Checking Duplicated Index.py</div>

```python
>>> df[df.index.duplicated(keep=False)].High
[Out]:
Date
2011-03-27       0.9
2011-03-27       0.9
2012-03-25       4.7
2012-03-25       4.7
2013-03-31     106.0
2013-03-31      93.8
2014-03-30     473.4
2014-03-30     479.0
2015-03-29     248.8
2015-03-29     252.8
2016-03-27     425.4
2016-03-27     427.4
2017-03-26    1048.8
2017-03-26    1004.3
2018-03-25    8521.0
2018-03-25    8690.4
2019-03-31    4164.3
2019-03-31    4129.4
Name: High, dtype: float64
```
<h3 id="Stack-and-Unstack">Stack and Unstack</h3>

Many timeseries operations cannot be performed if there are duplicated indices.   As mentioned earlier, when the <span class="coding">datetimeindex</span> is irregular, nothing will be returned from <span class="coding">df.index.inferred_freq</span>.  There are multiple ways to remove duplicates in pandas.  When the duplicates are in the columns, <span class="coding">DataFrame.sort_value()</span>, <span class="coding">DataFrame.drop_duplicates()</span>,and <span class="coding">DataFrame.set_index() </span>are the standard procedures to sort, drop duplicate and set index to clean data.   When the duplicates are in <span class="coding">DatetimeIndex</span>, we can use <span class="coding">DataFrame.index.duplicated()</span> to get the array of boolean values of whether an index is a duplicate.  

The <span class="coding">keep = 'first'/ 'last' /False</span> option is to mask those duplicates from being identified as True.   By default, for each set of duplicated values, the first occurrence is set to False and all others to True, in effect, keeping the first occurance when you drop duplicates.  

• 'first', marking duplicates as True except the first occurrence

• 'last',marking duplicates as True except the last occurrence

• False, marking all duplicates as True

The following example provides an example of <span class="coding">DataFrame.index.duplicated()</span> using the Bitcoin timeseries data.  Because we use <span class="coding">keep = False</span>, all the duplicated indices are shown, including first and last.  
<div class="code-head"><span>code</span> Checking Duplicated Index.py</div>

```python
>>> df[df.index.duplicated(keep=False)].High
[Out]:
Date
2011-03-27                      1
2011-03-27                      1
2012-03-25                      5
2012-03-25                      5
2013-03-31                    106
2013-03-31                     94
2014-03-30                    479
2014-03-30                    473
2015-03-29                    253
2015-03-29                    249
2016-03-27                    427
2016-03-27                    425
```
<h3 id="Duplicates-in-Index">Duplicates in Index</h3>

Many timeseries operations cannot be performed if there are duplicated indices.   As mentioned earlier, when the <span class="coding">datetimeindex</span> is irregular, nothing will be returned from <span class="coding">df.index.inferred_freq</span>.  There are multiple ways to remove duplicates in pandas.  When the duplicates are in the columns, <span class="coding">DataFrame.sort_value()</span>, <span class="coding">DataFrame.drop_duplicates()</span>,and <span class="coding">DataFrame.set_index</span>() are the standard procedures to sort, drop duplicate and set index to clean data.   When the duplicates are in <span class="coding">DatetimeIndex</span>, we can use <span class="coding">DataFrame.index.duplicated()</span> to get the array of boolean values of whether an index is a duplicate.  

The keep = 'first'/ 'last' /False option is to mask those duplicates from being identified as True.   By default, for each set of duplicated values, the first occurrence is set to False and all others to True, in effect, keeping the first occurance when you drop duplicates.  

• 'first', marking duplicates as True except the first occurrence

• 'last',marking duplicates as True except the last occurrence

• False, marking all duplicates as True

The example below provides an example of <span class="coding">DataFrame.index.duplicated()</span> using the Bitcoin timeseries data.  Because we use <span class="coding">keep = False</span>, all the duplicated indices are shown, including first and last.  
<div class="code-head"><span>code</span> Checking Duplicated Index.py</div>

```python
>>> df[df.index.duplicated(keep=False)].High
[Out]:
Date
2011-03-27                      1
2011-03-27                      1
2012-03-25                      5
2012-03-25                      5
2013-03-31                    106
2013-03-31                     94
2014-03-30                    479
2014-03-30                    473
2015-03-29                    253
2015-03-29                    249
2016-03-27                    427
2016-03-27                    425
2017-03-26                  1,004
2017-03-26                  1,049
2018-03-25                  8,690
2018-03-25                  8,521
Name: High, dtype: float64
```
The following exaple illustrates three simple ways to drop duplicates.  The first two methods use <span class="coding">keep = 'first'</span>, meaning keeping only the first of the duplicates.  The third method uses resample, which is a type of groupby.     As an added bonus, using resample the datetime frequency is set to 'D', which was not set before in the original timeseries imported.  Having a frequency is important for timeseries operations involving the index.  For example, tshift method will give errors if frequency is not set.   More on shifting and resampling in later subsections of this chapter.     
<div class="code-head"><span>code</span> Three Methods for Removing Duplicated DatetimeIndex.py</div>

```python
>>> #Method 1
>>> df = df[~df.index.duplicated(keep='first')] 

>>> #Method 2
>>> df.groupby(df.index).first()

>>> #Method 3
>>> df.resample('D').mean()
```
Note:
Using <span class="coding">groupby</span> or <span class="coding">resample</span>  allows more sophisticated ways of handling duplicates such as keeping the mean or median. 
 
In SAS, many options are available readily for removing duplidates.  In the example below, we use SAS <span class='coding'>PROC TIMESERIES</span> to remove duplicates when we specify the <span class='coding'>INTERVAL</span> parameter to be equal to  <span class='coding'>ID</span> time unit.  Different options are available including how you want to treat missing dates and missing data.   We use <span class="coding">ACCUMULATE = MEDIAN</span> although you can also specify <span class="coding">TOTAL</span>, <span class="coding">AVERAGE</span>, <span class="coding">MINIMUM</span>, <span class="coding">MAXIMUM</span> and etc.  In example below, we use the same data from Bitcoin Prices with <span class='coding'>PROC TIMESERIES</span>.
<div class="code-head"><span>code</span> Removing Duplicated Date using PROC TIMESERIES.sas</div>

```sas
>>> PROC TIMESERIES DATA = history
OUT = timeseries;
ID date 
    INTERVAL = DAY ACCUMULATE = MEDIAN;
    VAR High Low Open Close Adj_close Volume;
RUN;
```
After duplicated dates and times are removed, one can go on performing more time series analysis. 

<h3 id="Missing-Values">Missing Values</h3>

  So far we have not had to deal with missing datetime in using the Bitcoin timeseries because Bitcoin is traded around the world everyday including weekends and holidays.  

  However, many other timeseries have missing datetime either due to weekends/holidays or errors/omissions.    For example, stocks are not traded on weekends or holidays and therefore stocks timeseries will not have any values for those dates.    Furthermore, time-based events may not happen every weekday, for example, large bankruptcies.   In general, there are three types of missing datetime in a timeseries:
1.  Weekend
This can be easily handled via <span class="coding">asfreq('B')</span> or other types of frequency/offset.
2.  Holidays
These can be handled using pandas.tseries.holiday or custom holiday calendar. 
3.  Other causes
These missing can be left as missing or imputed using various methods, for example, <span class='coding'>ffill</span>. 
Missing datetime handling will be demonstrated using a real life example, using historical Apple stock price. 


### Further Reading
- [Python native datetime module](https://docs.python.org/3/library/datetime.html){:target="_blank"}.