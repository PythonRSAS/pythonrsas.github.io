---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Time Series"
description: Time series data process and analysis using Python and SA.
author: Sarah Chen
image: https://drive.google.com/uc?id=1crVhO4CHemFakRIxXYYo8HnfO-Z7sc1A
---

**While we are postponing, life speeds by.**

<!-- > not used for now**Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**. -->

### 1. Timestamp, Period and Timedelta 

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

```python
>>> %let start = 02Jan2020;
>>> %let end = 04Jan2020;
>>> DATA _null_;
  DO date="&start"d  to "&end"d;
    PUT date YYMMDD10.;
  END;
  RUN;

```

### Nulla proident dolor cupidatat  deserunt eiusmod eu id ex.

Lorem ipsum sint ut labore fugiat eiusmod voluptate exercitana culpa dolore sit sint enim. Lorem ipsum in velit ex laborinisi dolor laboris sed do enim sit eu <span class="coding">Odkfsdy</span> dfsdgg.

We will use the above Deep Neural Network architecture which has a **sdfsdle yutm xvwe**, **2 pire xaq**.

Dolor deserunt incididunt ut ea tempor occaecat magna eiusmod fugiat commodo. Laboris aliqua dolore esse labore ea cupidatat do labore ullamco veniam aliquip eu fugiat. Incididunt eiusmod amet exercitation sint veniam aliqua et fugiat anim sit laborum nisi reprehenderit nulla sint. Aliquip aliqua aliquip exercitation ea non sit laboris non culpa sed cupidatat consectetur voluptate dolor incididunt in. In ad tempor culpa cillum in magna est veniam in aliqua anim.

Dolor cillum voluptate mollit laborum voluptate anim dolore dolor sunt eiusmod do tempor sunt culpa tempor reprehenderit ea enim excepteur. Ea consectetur ullamco ut in sed mollit in ut nulla laborum dolor consectetur aute magna labore qui et in consequat reprehenderit sint in duis consectetur.

<div class="code-head"><span>code</span>from-doc-site.py</div>

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

* Line (1), Lorem ipsum culpa labore  <span class="coding">import</span> Est occaecat ad laboris eimodo ut exercitation culpa ex.
* Line (2), Pariatur consectetur ut mollit in eu esse :
  * <span class="coding">[8]]</span>: Im occaecat aliquip eiusmod cupidatat in velit aute magna cupidatat
  * <span class="coding">raw</span>: Lorem ipsum ullamco est dolore magna ut pariatur exercitation ea esse anim labore.
  * <span class="coding">data</span>: specify whether <span class="coding">uniform</span> or  <span class="coding">normal</span>.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo quas ipsam, magnam vel architecto cumque deserunt inventore autem voluptatem minus molestias fuga unde corporis soluta quisquam sapiente consequatur, aut tempora labore id repellat omnis harum? Eveniet velit laboriosam, quas optio, enim iure nesciunt repudiandae hic temporibus facilis, corporis maxime qui quis esse nam? Quod, enim, odio? Sapiente blanditiis quisquam voluptatem fuga quod fugit molestiae illum dolor itaque id ipsam, quasi, quae repellendus error placeat impedit maxime qui nobis est veritatis.
