---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Data Processing Lessons"
description: Data processing tips from experiences
author: Sarah Chen
image: images/posts/IMG-0648.JPG
---
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

## 1. Don't create (too many) unnecessary columns
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
## 2. Move all data format correction code in block
In the data discovery phase,  yes, you may need to correct data format as discovered.  Afterwards, we need to clean up the code and consolidate data format corrections.  Sometimes, you can even put them all in the input step.  
Regulatory models often use quarterly data.   Some metrics may use quarterly average.  Some just pick either start of the quarters of end of the quarters. 
For example,  to pick only March, June, September and December data.

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
df[df['date'].month.isin(3, 6, 9, 12)]
```

## Data aggregation
We routinely need aggregation by some categorical variable such as industry, product or regions, and date. 


```python
df1 = pd.concat([df.groupby[('category', 'date')]['balance'].sum(), df.groupby[('category', 'date')]['limit'].sum()], axis =1).reset_index()
df1['use'] = df['balance'] / df['limit']
```


## PD specifically
PD by year/quarter plot: 
-	Although we use boxplots routinely on LGD, there is no such thing as boxplot for binary targets.
-   However, quarterly average PD rates can be used as alternative data points. Boxplot can be used on them. 



