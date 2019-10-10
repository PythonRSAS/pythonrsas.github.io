---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Timestamp, Period and Timedelta"
description: Time series data processing using Python and SAS.
author: Sarah Chen
image: https://drive.google.com/uc?id=1crVhO4CHemFakRIxXYYo8HnfO-Z7sc1A
---

**While we are postponing, life speeds by.**

<!-- > not used for now**Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**. -->


The most fundamental measures of time are point in time (time stamp) and intervals (fixed or variable), and the difference between them, timedelta.  These objects provide building blocks for comprehensive time series data processes.  

The most fundamental measures of time are point in time **timestamp** and **intervals** (fixed or variable), and the difference between them **timedelta**.  These objects provide building blocks for comprehensive time series data processes.    [here](https://github.com){:target="_blank"}.

### Timestamp

Pandas <span class="coding">Timestamp</span> is pandas' equivalent to the Python's native <span class="coding">datetime</span>  object and in many cases a pandas Timestamp is interchangeable with Python's datetime object.    Pandas Timestamp  combines the flexibility of datetime and <span class="coding">dateutil</span> and the efficiency of vectorized representation from numpy.datetime64.  


<div class="code-head"><span>code</span>Timestamp Object and Attributes.py</div>

```python
>>> import pandas as pd
>>> date1= pd.Timestamp('2020-01-02 8:30:00')
Out: Timestamp('2020-01-02 08:30:00')

>>> date1.time()
Out: datetime.time(8, 30)
>>> date1.date()
Out: datetime.date(2020, 1, 2)
>>> date1.year
Out: 2020
>>> date1.month
Out: 1
>>> date1.day
Out: 2
>>> date1.dayofweek
Out: 3

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

### Period.

While a Timestamp represents a point in time, a Period represents a time span or segment, or commonly known as interval to SAS users.   Periods are non-overlapping time segments uniform in length. 
Some might wonder why we need period if we have Timestamp, or vice versa.   The answer is that point, and period represent different perspectives on how we think of time and record data in time, which result in different attributes.  For example, we can talk about GDP produced from a period of a year, or stock price at a point of time.   Period has <span class="coding">start_time</span> and <span class="coding">end_time</span>  attributes while Timestamp does not.     Period can be used to check if a specific event occurs within a certain period.  
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

You can specify which month to end in a quarter.  The default is class="coding">freq='Q-Dec'</span>, which means that period ending time is at the end of the quarter coinciding with calendar year.   The flexibility of quarter in pandas period time span facilitates different reporting and makes it simple and convenient.   

We will look at an example: 

<div class="code-head"><span>code</span>Period freq='Q' and Options for Month Ending.py</div>

```python
>>> period1=pd.Period('2020-01', freq='Q')
[Out]: Period('2020Q1', 'Q-DEC')
>>> period1.end_time
Out : Timestamp('2020-03-31 23:59:59-999999999')
>>> period1=pd.Period('2020-01', freq='Q-Jan')
>>> period1
[Out]: Period('2020Q4', 'Q-JAN')
>>> period1.end_time
[Out]: Timestamp('2020-01-31 23:59:59-999999999')
```

* You can perform various mathematical operations on Period, such as adding or subtracting an integer, which is simpler than using the pd.offset object. 
* Adding or subtracting two periods is as simple as integer addition and subtraction, if the frequencies are the same.     Finally, you can also convert Period to different frequencies.    
* Line (2), Pariatur consectetur ut mollit in eu esse :
  * <span class="coding">[8]]</span>: Im occaecat aliquip eiusmod cupidatat in velit aute magna cupidatat
  * <span class="coding">raw</span>: Lorem ipsum ullamco est dolore magna ut pariatur exercitation ea esse anim labore.
  * <span class="coding">data</span>: specify whether <span class="coding">uniform</span> or  <span class="coding">normal</span>.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo quas ipsam, magnam vel architecto cumque deserunt inventore autem voluptatem minus molestias fuga unde corporis soluta quisquam sapiente consequatur, aut tempora labore id repellat omnis harum? Eveniet velit laboriosam, quas optio, enim iure nesciunt repudiandae hic temporibus facilis, corporis maxime qui quis esse nam? Quod, enim, odio? Sapiente blanditiis quisquam voluptatem fuga quod fugit molestiae illum dolor itaque id ipsam, quasi, quae repellendus error placeat impedit maxime qui nobis est veritatis.
