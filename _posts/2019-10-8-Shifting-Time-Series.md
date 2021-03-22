---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Shifting Time Series"
description: Time series data processing using Python and SAS.
author: Sarah Chen
image: images/posts/paul-gilmor.jpg
---

<figure>
  <img src="{{ "/images/posts/paul-gilmor.jpg" | relative_url }}" width='800'>
  <figcaption>Photo by paul-gilmor</figcaption>
</figure>

In SAS there are multiple ways to shift time series data, i.e. to create leads and lags, including the <span class="coding">LAG</span> function or the more powerful one is <span class="coding">PROC EXPAND</span>.  In Python pandas, shifting is also called “sliding window”.    There are two main shifting methods in pandas: <span class="coding">shift()</span> and <span class="coding">tshift()</span>.  These two methods take the same parameters, where the defaults are: <span class="coding">periods=1, freq=None, axis=0</span>.
The difference between them is that <span class="coding">shift()</span> shifts the data whereas <span class="coding">tshift()</span> shift the index.   Both can take positive or negative integers to specify number of shifting periods, where positive integer results in lagging and negative number results in leading.

Under the hood, <span class="coding">tshift()</span> is reindexing the time index.  If you get error, you should check whether there are duplicates in the datetime index or whether your datetime index has a frequency.

In the following example below, we use <span class='coding'>df[~df.index.duplicated(keep='first')]</span> to remove duplicates by keeping the first.    We create two new columns by shifting data by 7 rows, and shifting time index by 7 days and plot them.
<div class="code-head"><span>code</span> Shifting Data and Index.py</div>

```python
 pd.options.mode.chained_assignment = None  #default='warn'
 df['shift7'] = df.High.shift(7)
 df = df[~df.index.duplicated(keep='first')]
 df = df.asfreq('D')  #set freq
 df['tshift7'] = df.High.tshift(7)
 plt.style.use('fivethirtyeight')
 df.loc['2018',['High','shift7',
'tshift7']].plot(title='Daily price High,
7 day shift and tshift')
```
Visually there seems to be no difference between <span class="coding">shift()</span> and <span class="coding">tshift()</span>.  In fact, the shift7 line is not even visible because it is mostly overlapped by the tshift7 line.  This is because for nearly the entire time span the datetime index has no gap and that the frequency we specified for the <span class="coding">tshift()</span> is the same as <span class="coding">shift()</span>.

However, if we look at the data in detail, we can see the subtle difference as shown in example below.

<div class="code-head"><span>code</span> Shifting Data and DatetimeIndex in pandas.py</div>

```python
 df.loc[:,['High','shift7', 'tshift7']].tail(15)
[Out]:
    High    shift7  tshift7
Date
12/21/2018  4,248   3,333   3,333
12/22/2018  4,060   3,272   3,272
12/23/2018  4,118   3,320   3,320
12/24/2018  4,303   3,640   3,640
12/25/2018  4,095   3,728   3,728
12/26/2018  3,924   3,970   3,970
12/27/2018  3,889   4,226   4,226
12/28/2018  4,008   4,248   4,248
12/29/2018  4,004   4,060   4,060
12/30/2018  3,925   4,118   4,118
12/31/2018  3,904   4,303   4,303
1/1/2020    3,939   4,095   4,095
1/2/2020    3,990   3,924   3,924
1/3/2020    3,966   3,889   3,889
1/9/2020    4,093   4,008   3,990
```

Note:
1.   <span class="coding">shift(7)</span> is equivant to SAS <span class='coding'>lag7()</span>.  <span class="coding">shift(7)</span> shifts data by 7.
2.   <span class="coding">tshift(7)</span> is shifting time index by 7 units of frequency, where unit can be specified by user.  In the output, we can see that the value in “tshift7” column and the “1/9/2020” row is “3,990”, which is identical from the value in “High” column and the “1/2/2020” row.

While less often used than lags, we should note that shifting in pandas by a negative number corresponds to leads.  For example, <span class="coding">shift(-7)</span> is the opposite of <span class="coding">shift(7)</span> and tshift(-7) is the opposite of <span class="coding">tshift(7)</span>.

Creating lags and leads  can be easily and efficiently done in <span class="coding">PROC EXPAND</span>.  While <span class="coding">ID</span>  in SAS is analogous to datetime index in pandas, however unlike pandas <span class="coding">datetimeIndex</span>, SAS <span class="coding">ID</span> requires the SAS date or time variable to be free of duplicates.

The following example below shows the use of <span class="coding">PROC EXPAND</span> to shift data forward and backward.

In this example,  <span class="coding">METHOD=NONE</span> and <span class="coding">TRANSFORMIN=(SETMISS 0)</span> are optional if we do not have any missing values.  But we use them to clarify that we are not using any interpolation for missing values, and that missing values would be set to 0 rather than interpolated.  If we do not specify <span class="coding">TRANSFORMIN=(SETMISS 0)</span>, the default interpolation in SAS <span class="coding">PROC EXPAND</span> is cubic spline. The <span class="coding">PLOTS=ALL</span> option is specified to request the plots of the input series, the transformed input series, the converted series, and the transformed output series, which are awesome for fast comparions visually.   For reference purpose,  <span class="coding">LAG</span> function from SAS <span class="coding">DATA</span> step is also included in the example below.
<div class="code-head"><span>code</span> Creating Leads and Lags in SAS.sas</div>

```sas
 ODS GRAPHICS ON;
 PROC EXPAND DATA =df METHOD=NONE
 OUT = df_shifted
 PLOTS=ALL;
 CONVERT High = lead7/TRANSFORMIN=(SETMISS 0)
 TRANSFORMOUT = (LEAD 7);
 CONVERT High = shift7/TRANSFORMIN=(SETMISS 0)
 TRANSFORMOUT = (LAG 7);
 ID date;
 RUN;
 ODS GRAPHICS OFF;

 PROC SORT DATA=df;
 BY date;
 RUN;
 DATA df_shifted;
 SET df;
 High_lag7 = lag7(High);
 RUN;
```
