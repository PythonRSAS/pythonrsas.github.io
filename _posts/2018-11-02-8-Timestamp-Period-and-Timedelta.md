---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Timestamp, Period and Timedelta"
description: Time series data processing using Python and SAS.
author: Sarah Chen
image: images/posts/sean-o.jpg

---

 

[Timestamp](#Timestamp)

[Period](#Period)

[Timedelta](#Timedelta)

Let's get started.
<figure>
  <img src="{{ "/images/posts/sean-o.jpg" | relative_url }}">
  <figcaption>Photo by Sean O</figcaption>
</figure>

The most fundamental measures of time are point in time (time stamp) and intervals (fixed or variable), and the difference between them, timedelta.  These objects provide building blocks for comprehensive time series data processes.  

The most fundamental measures of time are point in time **timestamp** and **intervals** (fixed or variable), and the difference between them **timedelta**.  These objects provide building blocks for comprehensive time series data processes.    [here](https://github.com){:target="_blank"}.

<h3 id="Timestamp">Timestamp</h3>

Pandas <span class="coding">Timestamp</span> is pandas' equivalent to the Python's native <span class="coding">datetime</span>  object and in many cases a pandas Timestamp is interchangeable with Python's datetime object.    Pandas Timestamp  combines the flexibility of datetime and <span class="coding">dateutil</span> and the efficiency of vectorized representation from numpy.datetime64.  


<div class="code-head"><span>code</span>Timestamp Object and Attributes.py</div>

```python
 import pandas as pd
 date1= pd.Timestamp('2020-01-02 8:30:00')
Out: Timestamp('2020-01-02 08:30:00')

 date1.time()
Out: datetime.time(8, 30)
 date1.date()
Out: datetime.date(2020, 1, 2)
 date1.year
Out: 2020
 date1.month
Out: 1
 date1.day
Out: 2
 date1.dayofweek
Out: 3

```
* From pandas version 0.20.0. there is a new origin parameter for specifying an alternative starting point for creation of a DatetimeIndex.  For example, using 1960-01-01 as the starting date would make pandas dates have the same reference starting date as SAS date
* If you do not specify origin, then the default is origin='unix', which defaults to 1970-01-01 00:00:00.  This is commonly called 'unix epoch' or POSIX time. 
* Pandas represents timestamps in nanosecond resolution.  Hence the time span that can be represented using a 64-bit integer is limited to approximately 584 years.   On the other hand, SAS does not have such limitation  as SAS stores dates as integers, datetime and time as real numbers. 

SAS date or time are stored internally in numbers and represented according to formats user specified.  Example below prints current date, time, and datetime stamps.  
<div class="code-head"><span>code</span>SAS Date Time and Datetime Stamps.sas</div>

```sas
 DATA _NULL_;
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
 date1= pd.Timestamp('2020-01-02')
 date1 + pd.to_timedelta(np.arange(3),'D')
Out:  DatetimeIndex(['2020-01-02', '2020-01-03', '2020-01-04'], dtype='datetime64[ns]', freq=None)
```
Base SAS does not have vectorized operations.  To create similar output, one may write a simple loop such as the one below:
<div class="code-head"><span>code</span>SAS Date Time Sequence.sas</div>

```sas
 %let start = 02Jan2020;
 %let end = 04Jan2020;
 DATA _null_;
  DO date="&start"d  to "&end"d;
    PUT date YYMMDD10.;
  END;
  RUN;

```

<h3 id="Period">Period</h3>

While a Timestamp represents a point in time, a Period represents a time span or segment, or commonly known as interval to SAS users.   Periods are non-overlapping time segments uniform in length. 
Some might wonder why we need period if we have Timestamp, or vice versa.   The answer is that point, and period represent different perspectives on how we think of time and record data in time, which result in different attributes.  For example, we can talk about GDP produced from a period of a year, or stock price at a point of time.   Period has <span class="coding">start_time</span> and <span class="coding">end_time</span>  attributes while Timestamp does not.     Period can be used to check if a specific event occurs within a certain period.  
The next example shows an instance of Period object and illustrates its attributes.  Notice how <span class="coding">freq = </span>  parameter dictates the time span, and how the two Periods differ and even though they are created from the same timestamp.  

<div class="code-head"><span>code</span>Period Object and its Special Attributes.py</div>

```py
 period1=pd.Period('2020-01-02', freq='D')
 period1
[Out]: Period('2020-01-02', 'D')

 period1.ordinal
[Out]: 18263

 period1.start_time
[Out]: Timestamp('2020-01-02 00:00:00')
	
 period1.end_time
[Out]: Timestamp('2020-01-02 23:59:59-999999999')

 period1.to_timestamp()
[Out]: Timestamp('2020-01-02 00:00:00')

 period2=pd.Period('2020-01-02', freq='m')
 period2
[Out]: Period('2020-01', 'M')

 period2.start_time
[Out]: Timestamp('2020-01-01 00:00:00')

 period2.end_time
[Out]: Timestamp('2020-01-31 23:59:59-999999999')
```
Most financial reports are on quarterly data.  Many companies have fiscal years that are different from calendar years.  For example, Microsoft's fiscal year starts from July and ends in June.  WalMart's fiscal year starts in February and ends in January. 

You can specify which month to end in a quarter.  The default is <span class="coding">freq='Q-Dec'</span>, which means that period ending time is at the end of the quarter coinciding with calendar year.   The flexibility of quarter in pandas period time span facilitates different reporting and makes it simple and convenient.  

For example, you can convert a column of datetime sequence to quarter end datatime by using <span class="coding">to_period('Q').end_time</span>.  Of course, you can align all timestamps to beginning of quater by <span class="coding">to_period('Q').start_time</span>.  Similarly, you can nomralize a column of dates to their corresponding week, month, or year start or end dates.   This is very useful for merging datasets that have different datetime resolutions. 

<div class="code-head"><span>code</span>Period freq='Q' and Options for Month Ending.py</div>

```python
 date1.to_period('Q').end_time
Out: Timestamp('2020-03-31 23:59:59.999999999')
 period1=pd.Period('2020-01', freq='Q')
Out: Period('2020Q1', 'Q-DEC')
 period1=pd.Period('2020-01', freq='Q-Jan')
 period1
Out: Period('2020Q4', 'Q-JAN')
 period1.end_time
Out: Timestamp('2020-01-31 23:59:59-999999999')
```

* You can perform various mathematical operations on Period, such as adding or subtracting an integer, which is simpler than using the pd.offset object. 
* Adding or subtracting two periods is as simple as integer addition and subtraction, if the frequencies 
are the same.     Finally, you can also convert Period to different frequencies.    

<div class="code-head"><span>code</span>Arithmetic Operations on Period Object.py</div>

```py
 period3 = period2 + 12
 period3
[Out]: Period('2021-01', 'M')

 period3 - period2
[Out]:<12 * MonthEnds>

 q = pd.Period('2020Q4')
 q + 1
[Out]: Period('2020Q1', 'Q-DEC')

 q.asfreq('m', how='start')
[Out]: Period('2020-10', 'M')

 q.asfreq('m', how='end')
[Out]: Period('2020-12', 'M')
```

* Period has the same attributes such as <span class="coding">.day</span>, <span class="coding">.dayofweek</span>, <span class="coding">.quarter</span> and so on as Timestamp, but it does not have <span class="coding">.date</span> or <span class="coding">.time</span> attributes the way Timestamp does.  

<h3 id="Timedelta">Timedelta</h3>

Pandas Timedelta is differences in times, expressed in difference units, e.g. days, hours, minutes, seconds. Timedelta is the pandas equivalent of python datetime.timedelta, and is interchangeable with it in most cases. Timedelta are differences in time expressed in different units, such as days, hours, minutes, seconds and can be positive or negative.  Consider the following examle, pandas Timedelta.   The example first shows how Timedelta can be used to increment and Timestamp, then calculates age in years by converting a Timedelta object to an int via the Timedelta.days() method and then divide by 365.   
<div class="code-head"><span>code</span>Pandas Timedelta and Age Calculation.py</div>

```py
 pd_ts     = pd.Timestamp('2020-02-14 00:00:00')
 pd_td     = pd.Timedelta(days=1, hours=1, minutes=1, 
	seconds=1)
 pd_ts - pd_td
[Out]: Timestamp('2020-02-12 22:58:59')
 DoB = pd.Timestamp('2000-02-14 07:00:00')
 age = (pd.Timestamp.now() - DoB).days/365

```

* Period has the same attributes such as <span class="coding">.day</span>, <span class="coding">.dayofweek</span>, <span class="coding">.quarter</span> and so on as Timestamp, but it does not have <span class="coding">.date</span> or <span class="coding">.time</span> attributes the way Timestamp does.  
