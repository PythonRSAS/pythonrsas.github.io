---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Time Series Indexing Copy"
description: Time series data processing using Python and SAS.
author: Sarah Chen
image: https://drive.google.com/uc?id=1crVhO4CHemFakRIxXYYo8HnfO-Z7sc1A
---

**While we are postponing, life speeds by.**

<!-- > not used for now**Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**. -->

One of the main uses of Timestamp and Period objects is indexing.   Indexing is so vital to pandas time series operations that lists of Timestamp or Period objects are automatically coerced to <span class="coding">DatetimeIndex</span> and <span class="coding">PeriodIndex</span> respectively when used as index.   Recall from Chapter 4 Indexing and Grouping, that a pandas index is simply a method to label rows.   Python pandas is so powerful and convenient in handling time series that you may want it to be your go-to tool for time series data, especially for financial data. 

SAS users need to be aware that pandas allow duplicate index.  When we perform strict time series analysis, we would need to remove duplicates.  


The most fundamental measures of time are point in time **timestamp** and **intervals** (fixed or variable), and the difference between them **timedelta**.  These objects provide building blocks for comprehensive time series data processes.    [here](https://github.com){:target="_blank"}.

### DatetimeIndex

Pandas <span class="coding">Timestamp</span> is pandas' equivalent to the Python's native <span class="coding">datetime</span>  object and in many cases a pandas Timestamp is interchangeable with Python's datetime object.    Pandas Timestamp  combines the flexibility of datetime and <span class="coding">dateutil</span> and the efficiency of vectorized representation from numpy.datetime64.  
The example below illustrates how a list of objects with mixed formats is automatically coerced to Datetimeindex by .

<div class="code-head"><span>code</span>Pandas DatetimeIndex.py</div>

```python
>>> dates = ['1-02-2020', '4-1-2020','2020-07-04', '4th of July, 2020', '2020-12-31']
>>> pd.to_datetime(dates, dayfirst=False)
[Out]: DatetimeIndex(['2020-01-02', '2020-04-01', 
'2020-07-04', '2020-07-04', '2020-12-31'],
     dtype='datetime64[ns]', freq=None)

```
* From pandas version 0.20.0. there is a new origin parameter for specifying an alternative starting point for creation of a DatetimeIndex.  For example, using 1960-01-01 as the starting date would make pandas dates have the same reference starting date as SAS date
* If you do not specify origin, then the default is origin='unix', which defaults to 1970-01-01 00:00:00.  This is commonly called 'unix epoch' or POSIX time. 
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

As mentioned earlier, pandas is built on top of numpy.  Vectorized operations from numpy can be applied directly on Timestamp object to create a sequence of dates or times, which is automatically coerced into DatetimeIndex object.   This is illustrated in the next example. 
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

### Partial String Indexing
In SAS, subsetting date ranges are performed via <span class="coding">WHERE</span> clause or IF statement in a <span class="coding">DATA</DATA></span> step, or <span class="coding">WHERE</span> clause in <span class="coding">PROC SQL</span>. Since pandas DatetimeIndex has all the basic functions of regular index , you can use the regular index methods to slice and dice DataFrame or Series, and use DatetimeIndex to perform “partial string indexing”.   For example, omitting the day component extracts all rows belong to a particular year or month.   The uses of partial string index are interspersed throughout the remainder of the Indexing section and are identified in the text.

### An Example Using Historical Bitcoin Trade Data
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

>>> df.index.inferred_freq 
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
plot(title="Bitcoin 2018 daily high and low price time series")
```
<figure>
  <img src="{{ "/images/posts/Bitcoin 2018 daily high and low price time series.png" | relative_url }}">
  <figcaption>Figure 1. Bitcoin 2018 daily high and low price time series</figcaption>
</figure>

The next example shows an instance of Period object and illustrates its attributes.  Notice how <span class="coding">freq = </span>  parameter dictates the time span, and how the two Periods differ and even though they are created from the same timestamp.  

<div class="code-head"><span>code</span>Period Object and its Special Attributes.py</div>

```py
>>> period1=pd.Period('2020-01-02', freq='D')
>>> period1
[Out]: Period('2020-01-02', 'D')

>>> period1.ordinal
[Out]: 18263

>>> period1.start_time
[Out]: Timestamp('2020-01-02 00:00:00')
	
>>> period1.end_time
[Out]: Timestamp('2020-01-02 23:59:59-999999999')

>>> period1.to_timestamp()
[Out]: Timestamp('2020-01-02 00:00:00')

>>> period2=pd.Period('2020-01-02', freq='m')
>>> period2
[Out]: Period('2020-01', 'M')

>>> period2.start_time
[Out]: Timestamp('2020-01-01 00:00:00')

>>> period2.end_time
[Out]: Timestamp('2020-01-31 23:59:59-999999999')
```
Most financial reports are on quarterly data.  Many companies have fiscal years that are different from calendar years.  For example, Microsoft's fiscal year starts from July and ends in June.  WalMart's fiscal year starts in February and ends in January. 

You can specify which month to end in a quarter.  The default is <span class="coding">freq='Q-Dec'</span>, which means that period ending time is at the end of the quarter coinciding with calendar year.   The flexibility of quarter in pandas period time span facilitates different reporting and makes it simple and convenient.  

For example, you can convert a column of datetime sequence to quarter end datatime by using <span class="coding">to_period('Q').end_time</span>.  Of course, you can align all timestamps to beginning of quater by <span class="coding">to_period('Q').start_time</span>.  Similarly, you can nomralize a column of dates to their corresponding week, month, or year start or end dates.   This is very useful for merging datasets that have different datetime resolutions. 

<div class="code-head"><span>code</span>Period freq='Q' and Options for Month Ending.py</div>

```python
>>> date1.to_period('Q').end_time
Out: Timestamp('2020-03-31 23:59:59.999999999')
>>> period1=pd.Period('2020-01', freq='Q')
Out: Period('2020Q1', 'Q-DEC')
>>> period1=pd.Period('2020-01', freq='Q-Jan')
>>> period1
Out: Period('2020Q4', 'Q-JAN')
>>> period1.end_time
Out: Timestamp('2020-01-31 23:59:59-999999999')
```

* Various mathematical operations can be performed on Period, such as adding or subtracting an integer.  
* Adding or subtracting two periods is as simple as integer addition and subtraction, if the frequencies are the same.     Finally, you can also convert Period to different frequencies.    

<div class="code-head"><span>code</span>Arithmetic Operations on Period Object.py</div>

```py
>>> period3 = period2 + 12
>>> period3
[Out]: Period('2021-01', 'M')

>>> period3 - period2
[Out]:<12 * MonthEnds>

>>> q = pd.Period('2020Q4')
>>> q + 1
[Out]: Period('2020Q1', 'Q-DEC')

>>> q.asfreq('m', how='start')
[Out]: Period('2020-10', 'M')

>>> q.asfreq('m', how='end')
[Out]: Period('2020-12', 'M')
```

* Period has the same attributes such as <span class="coding">.day</span>, <span class="coding">.dayofweek</span>, <span class="coding">.quarter</span> and so on as Timestamp, but it does not have <span class="coding">.date</span> or <span class="coding">.time</span> attributes the way Timestamp does.  

### Timedelta
Pandas Timedelta is differences in times, expressed in difference units, e.g. days, hours, minutes, seconds. Timedelta is the pandas equivalent of python datetime.timedelta, and is interchangeable with it in most cases. Timedelta are differences in time expressed in different units, such as days, hours, minutes, seconds and can be positive or negative.  Consider Listing 9-11, pandas Timedelta.   The example first shows how Timedelta can be used to increment and Timestamp, then calculates age in years by converting a Timedelta object to an int via the Timedelta.days() method and then divide by 365.   
<div class="code-head"><span>code</span>Pandas Timedelta and Age Calculation.py</div>

```py
>>> pd_ts     = pd.Timestamp('2020-02-14 00:00:00')
>>> pd_td     = pd.Timedelta(days=1, hours=1, minutes=1, 
	seconds=1)
>>> pd_ts - pd_td
[Out]: Timestamp('2020-02-12 22:58:59')
>>> DoB = pd.Timestamp('2000-02-14 07:00:00')
>>> age = (pd.Timestamp.now() - DoB).days/365

```

* Period has the same attributes such as <span class="coding">.day</span>, <span class="coding">.dayofweek</span>, <span class="coding">.quarter</span> and so on as Timestamp, but it does not have <span class="coding">.date</span> or <span class="coding">.time</span> attributes the way Timestamp does.  
