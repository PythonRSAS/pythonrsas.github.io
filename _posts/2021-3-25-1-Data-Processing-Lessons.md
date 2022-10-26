---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Data Processing Lessons"
description: Data processing tips from experiences
author: Sarah Chen
image: images/posts/IMG-0648.JPG
---
- [General principles](#general-principles)
  - [Don't create (too many) unnecessary columns](#dont-create-too-many-unnecessary-columns)
  - [Move all data format correction code in block](#move-all-data-format-correction-code-in-block)
  - [Data aggregation](#data-aggregation)
- [Functions](#functions)
- [Plotting](#plotting)
- [Other tips](#other-tips)
  - [Cartesian product](#cartesian-product)
  
![](/images/posts/IMG-0648.JPG)
Although processes are iterative, it should still be organized, at least periodically.  If it becomes too chaotic, it becomes inefficient.

For example, some have multiple places of unnecessary indicator variable creation manually.  Whereas it could and should be all be done in one shot after we have finalized the set the variables!

> Need to be disciplined and organized!
# General principles
1.	Don't create (too many) unnecessary columns.  
2.  Move all data format correction code in block.
3.	Do not create indictor variables here and there.  Do it in one shot.
4.	Do not output describe until unneeded variables are mostly dropped.
5.	Plot scatterplots in one shot for all numeric variables.

Because PD and LGD are modeling labels and continuous numbers, respectively.  The visualizations and metrics will be two different sets corresponding to categorical target and continuous numeric taget, respectively. 

## Don't create (too many) unnecessary columns
In the following code, it is completely unnecessary to create so many columns out of the original date columns.  It not only takes up more space by creating many new columns but is more error prone.

<div class="code-head"><span>code</span>redundant columns.py</div>

```py
df['date'] = df['original_date'].dt.strftime('%d/%m/%Y')
df['year'] = pd.DateimeIndex(df['date']).year
df['month'] = pd.DateimeIndex(df['date']).month
df['day'] = pd.DateimeIndex(df['date']).day
df['year_month'] = df['year']*10000 + df['month']*100
df['year_month_str'] = df['year_month'].astype(str)
df['year_month_day'] = df['year_month'] + df['day']
df['year_month_day_str'] = df['year_month_str'].astype(str)
df['ID_year_month_day'] = df['ID=='] + '_' +  df['ID_year_month_day']
...
...
```
If you need month, year, day, you can use the following code.  And there is no sense of creating a string type of all the dates.

```python
df.date.dt.month
df.date.dt.year
df.date.dt.day
```

If you need both year and month together, you can do the following instead of getting year and month, and then concatenate them:
```python
df.date.dt.to_period('m')
# 2020-09
# 2020-12
# 2020-09
```

## Move all data format correction code in block
In the data discovery phase,  yes, you may need to correct data format as discovered.  Afterwards, we need to clean up the code and consolidate data format corrections.  Sometimes, you can even put them all in the input step.  

<div class="code-head"><span>code</span>data formatting.py</div>

```py
cols = ['Facility_id', 'obligor_id', 'loan_balance', 'elapse_time', 'remaining_time', 'facility_type', 'industry', 'region', 'date']
data_types = {
    'Facility_id': str,
     'obligor_id': str,
     'loan_balance': float,
     'elapse_time': float,
     'remaining_time': float,
     'facility_type': str,
     'industry': str,
     'region': str
}
df = pd.read_csv(filename, usecols = cols, dtype = data_types)
df['date'] = pd.to_datetime(df['date'])
```

Regulatory models often use quarterly data.   Some metrics may use quarterly average.  Some just pick either start of the quarters or end of the quarters. 
For example,  to pick only March, June, September and December data.

```python
df[df['date'].month.isin(3, 6, 9, 12)]
```


## Data aggregation
We routinely need aggregation by some categorical variable such as industry, product or regions, and date. 
Note that in code below, the purpose of the programmer was to computer the usage column by date and some categorical variable. It is unnessarily doing two separate groupbys and reset index and set index again.  

```python
df1 = pd.concat([df.groupby[('category', 'date')]['balance'].sum(), df.groupby[('category', 'date')]['limit'].sum()], axis =1).reset_index().set_index('date')
df1['use'] = df['balance'] / df['limit']
```

Instead, it is much simpler to do the following:
```python
df[['category', 'date', 'balance', 'limit']].groupby[('category', 'date')].sum().droplevel(0)
             balance     limit
# date      
# 2020-09
# 2020-12
# 2020-09

```
# Functions
The general advice on writing functions are: keep them short, simple, single-purposed, and think about ***cohesion*** (connecting the components).  

Why keeping them short and single-purposed?  Because it makes it simplier to use and therefore more reusable.  You probably don't see contractors working with Swiis Army knifes. 

As described in Mark Lutz's "Learning Python" book, 
- **def creates an object and assigns it to a name**. 
- **lambda creates an object but returns it as a result**.  Some say lambda functions are simply functions that you don't care to give them names so that you can do it in-line. 
- **yield sends a result object back to the caller, but remembers where it left off**. Yield is often used with generator functions.  You can use it to save space. 
- **global declares *module-level* variables**.  By defult, all names assigned ina function are local to the function and exist only while the function runs.    To assign a name in the enclosing module, functions need to be listed in a <span class="coding">global</span> statement.  This is very similar to SAS. 

# Plotting

Plotting is a big topic.  We routinely need to plot historical time series together.  There are many ways to plot time series plots for multiple metrics.  Below is a simple version to get a quick view.  You can do deep dives once you notice something worth deep diving. 

<div class="code-head"><span>code</span>time series plots for multiple metrics.py</div>

```py
def ts_multi_metric(df, cate):
    temp = df[df['category'] == cate].copy()
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()

    l1 = ax1.plot(temp['metric1'], c = grey, label = 'metric1')
    l2 = ax1.plot(temp['metric2'], c = blue, label = 'metric2')
    l3 = ax2.plot(temp['metric3'], c = green, label = 'metric3', linestyle = ':')

    ax1.set_xlabel('date')
    ax1.set_ylabel('metric 1&2 unit')
    ax2.set_ylabel('metric 3 unit')

    # legend
    lines = l1 + l2 + l3
    labels = [l.get_label() for l in lines]
    plt.legend(lines, labels)
    ax1.set_title(cate)
ts_multi_metric(df, cate)
```

PD by year/quarter plot: 
-	Although we use boxplots routinely on LGD, there is no such thing as boxplot for binary targets.
-   However, quarterly average PD rates can be used as alternative data points. Boxplot can be used on them. 

# Other tips
## Cartesian product
Most of the time, we want data joins to be key-based one to one joins.  Sometimes however, we use cartesian product for data manipulation.  For example, we want to compare at obligor (or facility level) its metrics at time t and metrics before time t for all t that it exists in the data. 

For each data point in the Cartesian product, we use date0 as the anchor, and keep only those records that have date0 as historical. 

<div class="code-head"><span>code</span>use cartesian product to compare history.py</div>

```py
df_copy = df.copy()
df_copy.rename(columns = {'date': 'date0', 'balance': 'balance0', 'limit': 'limit0'})
df_cartisian = pd.merge(df, df_copy, on = 'id')
df_cartisian0 = df_cartesian[df_cartesian['date'] > df_cartesian['date0']]
```
