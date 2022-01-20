---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "Working with Timeseries in Python and SAS"
description: Comparing and assembling dates, and parsing timeseries in Python and SAS.
author: Sarah Chen
image: images/posts/arindam-saha.jpg
---

This post covers miscellaneous tips for working with datatime in Python and SAS.

> **[1. Comparing dates        ](#Comparing-Dates)**
> **[2. Assembling](#Assembling)**
> **[3. Parsing](#Parsing)**

<figure>
  <img src="{{ "/images/posts/arindam-saha.jpg" | relative_url }}" width='800'>
  <figcaption>Photo by arindam saha</figcaption>
</figure>

<h3 id="Comparing-Dates">Comparing Dates</h3>
> **[Comparing dates](#Comparing-Dates)**

• To slice data using Date column by comparing against a date in Python when the date column is not the index

```python
df[df.Date.dt.year>2010] #comparing year
# or when you need to compare against a specific date
import datetime
df[df.Date.dt.date > datetime.date(2010,12,30)]
```
• To slice data by comparing against a date in SAS

```sas
if year(Date) > 2010;

/*or, to compare against a specific date*/

if Date > '30Dec2010'd;
/* or where Date > '30Dec2010'd;*/ 
```

• To create business date range that can incorporate custom frequency ranges, holidays and time zones

```python
pd.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, closed=None, **kwargs )
```

Example:
```python
#say you only work Mondays
weekmask = 'Mon'  
pd.bdate_range(pd.datetime(2020, 1, 1), pd.datetime(2020, 2, 1), freq='C',weekmask=weekmask)

[Out]: DatetimeIndex(['2020-01-06', '2020-01-13', '2020-01-20', '2020-01-27'], dtype='datetime64[ns]', freq='C')
```

• To create period range using period_range

```python
pd.period_range(start=None, end=None, periods=None, freq='D', name=None)
```

Example:
```python
 prng = pd.period_range('1/1/2020', '4/1/2020', freq='M')
 PeriodIndex(['2020-01', '2020-02', '2020-03', '2020-04'], dtype='period[M]',freq='M')
```

• To create Timedelta
```python
pd.to_timedelta(arg, unit='ns', box=True, errors='raise')
```
• To create Timestamp
```python
pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=None, box=True, format=None, exact=True, unit=None, infer_datetime_format=False, origin='unix', cache=False)
```
<h3 id="Assembling">Assembling</h3>

In SAS, a datetime variable can be assembled by providing the components: year, month, day, and more. This is the case for most programming languages.

In Python you can use <span class="coding">pd.to_datetime()</span> to build date or datetime objects by passing the right columns or entire dataframe as shown in the example below:
<div class="code-head"><span>code</span> Assembling Datetime Object.py</div>

```python
 df = pd.DataFrame({'year': [2020, 2020], 
'month': [1, 1],'day': [1, 2]})
 pd.to_datetime(df)
[Out]:
0   2020-01-01
1   2020-01-02
dtype: datetime64[ns]

# Or alternatively,
 pd.to_datetime(df[['year','month','day']])
[Out]:
0   2020-01-01
1   2020-01-02
dtype: datetime64[ns]
```
Note:
1.  <span class="coding">pd.to_datetime()</span> requires year, month, and day components.  Missing any of them will raise an error “ValueError: to assemble mappings requires at least that [year, month, day] be specified”.
2.  Hour, minute, etc. are optional. 
Converting
While you can always come up with your own algorithm to parse and assemble, it is likely there are readily available functions that can solve the problem. <span class="coding">pd.to_datetime()</span> is an important method to convert or parse a wide range of date, time, or datetime-like, including epochs, strings, or a combination of them to datetime.   
Or if you do not like the default datetime format from <span class="coding">pd.to_datetime()</span>, you can specify how it should be displayed by using format, the same way as you would do in SAS, as shown in the following exaple.
<div class="code-head"><span>code</span> to_datetime() Examples.py</div>

```python
 pd.to_datetime('2020/07/04', format='%Y/%m/%d').date()
[Out]: datetime.date(2020, 7, 4)

 pd.to_datetime('19/07/04', format='%y/%m/%d')
[Out]: Timestamp('2020-07-04 00:00:00')

 dates = pd.to_datetime([datetime(2020,1,15), '2020-Aug-10','12-25-2018','20181031','25th of December, 2018'])
 dates 
[Out]: DatetimeIndex(['2020-01-15', '2020-08-10', '2018-12-25', '2018-10-31'], dtype='datetime64[ns]', freq=None)
```
Note: 
1.  Anytime you only want the date part you can use date attribute so that the Timestamp or TimestampIndex object will be converted to datetime.date object, keeping only the date part.  
2.  Format specification syntax is similar to Python datetime module, where upper case letter Y denotes four digit year and lower case y denotes two digit year.  You do not need to specify format for unambiguous date-like strings, but you should specify format otherwise.   For example, without format, pd.to_datetime('19/07/04') will give you Timestamp('2004-07-19 00:00:00'), which is not correct.
3.  <span class="coding">pd.to_datetime()</span> by default takes a group of date(s) to a DatetimeIndex object; such as pd.to_datetime([datetime(2020,1,15)]), even if there is only one member in the group.
4.  Not all formats can be parsed directly.  For example, '10312020' will not work; while <span class="coding">pd.to_datetime()</span> can parse '25th of December, 2020', it will throw error message at “'twenty-fifth of December, 2020'.  
5.  Passing infer_datetime_format=True can speedup a parsing if it's not an ISO8601 format exactly, but in a regular format.
While the default pandas.to_datetime() uses unix epoch origin, which is January 1, 1970,  you can change it by providing your custom reference timestamp using the origin parameter.  Unless a unit is provided, the default unit is nanoseconds, since that is how Timestamp objects are stored internally.   This is illustrated in the example below.   
<div class="code-head"><span>code</span> Converting Number to Datetime by Specifying Origin and Unit.py</div>

```python
  pd.to_datetime(18081) #default unit in nanosecond
[Out]: Timestamp('1970-01-01 00:00:00.000018081') 

  pd.to_datetime(18081, unit='D')
[Out]: Timestamp('2020-07-04 00:00:00')

#SAS default reference date
 pd.to_datetime(18081, unit='D',  origin='1960-1-1')
[Out]: Timestamp('2009-07-03 00:00:00')
```
For reverse operation, i.e. to get the number of datetime units between two timestamps, we can apply simple arithmetic as followed:
```python
 (pd.to_datetime(18081, unit='D') - pd.Timestamp("1970-01-01")) // pd.Timedelta('1D')
[Out]: 18081
```
<h3 id="Parsing">Parsing</h3>

If your data is not in any of the formats that pandas can read readily but it has a regular pattern, then you can apply brute force string slicing to extract date, time or datetime.    Even though some of the examples are not from pandas, we list them because of context. The following example below shows an example of using dateutl.parser to parse string into datetime object.  
<div class="code-head"><span>code</span> Other Parsing Tools from dateutl.parser.py</div>

```python
 Time = "07/04/2020 19:00"
 from dateutil.parser import parse
 parse(Time)
[Out]: datetime.datetime(2020, 7, 4, 19, 0)
```
For reference, we show in the example below how a string can be converted to date variable in SAS.  
<div class="code-head"><span>code</span> SAS from String to Date.sas</div>
```sas
DATA _null_; 
   Time = '04Jul2020';
   date = INPUT(Time, DATE9-);
   PUT date = YYMMDD.;
   PUT date = YYQ.
RUN;
[Out]:
Date = 19-07-04
Date = 2020Q3
```

To convert non-datetime-value numbers to datetime, in either SAS or Python, we will need to first convert them to strings and then parse them to datetime as examples above.  
Both Python and SAS can convert number to datetime, and they operate in very similar way: first change data type to string because the number should not be read as number.  Then apply the usual procedure to convert string to date 

An example of how to convert number to datetime in Python is in the example below:
<div class="code-head"><span>code</span> Pandas from Number to Date.py</div>

```python
 Time = 20200704
 pd.to_datetime(str(Time))
[Out]: Timestamp('2020-10-31 00:00:00')
```
<div class="code-head"><span>code</span> Pandas from String to Date.py</div>

```python
 df = pd.DataFrame({
'TimeStamp': ['2020/07/01 17:14:13', '2020/09/14 17:14:14', '2020/04/27 17:14:15'], 
'Date': ['01JUL2020','14SEP2020','27APR2020']})
 print(df)
[Out]:
             TimeStamp       Date
0  2020/07/01 17:14:13  01JUL2020
1  2020/09/14 17:14:14  14SEP2020
2  2020/04/27 17:14:15  27APR2020

# method 1 Using pd.to_datetime
 df['TimeStamp'] = pd.to_datetime(df['TimeStamp']).dt.strftime('%Y%m/%d/ %H:%M:%S')
#Note:  df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%d%b%Y') will raise errors !

# method 2using apply
 df.Date.apply(lambda x: pd.to_datetime(x, format="%d%b%Y"))
 df.TimeStamp.apply(lambda x: pd.to_datetime(x, format="%Y/%m/%d %H:%M:%S"))

 df
[Out]:
             TimeStamp       Date
0  2020/07/01 17:14:13  01JUL2020
1  2020/09/14 17:14:14  14SEP2020
2  2020/04/27 17:14:15  27APR2020

#simply apply to_datetime without supplying format
 df.TimeStamp.apply(lambda x: pd.to_datetime(x))
 df.Date.apply(lambda x: pd.to_datetime(x))
```
Note:
1.  While <span class="coding">pd.to_datetime()</span> can parse some datetime formats, its ability is quite limited.  
2.  For common datetime formates that <span class="coding">pd.to_datetime()</span> cannot parse, use a syntax similar to <span class="coding">df.Date.apply(lambda x: pd.to_datetime(x, format="%d%b%Y"))</span>.    
3.  To build your custom formats for parsing, please see [Table Datetime](https://docs.python.org/3/library/datetime.html)

The example below shows how a string can be converted to date variable in SAS.  
<div class="code-head"><span>code</span> SAS from Number to Date.sas</div>

```sas
 DATA _null_; 
    Time = 20200704;
    date = INPUT(PUT(Time, 8.),YYMMDD8.);
    PUT date = YYMMDD10.;
RUN;
[Out]: date=2020-07-04
```



Now we have covered construction of datetime objects and basic cleaning, let's move on to the common types of time series operations:  shifting, rolling, expanding and aggregating in the coming sections.