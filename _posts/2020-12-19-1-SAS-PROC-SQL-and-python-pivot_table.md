---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "SAS PROC SQL and python df.groupby and pivot_table."
description:  On python groupby and pivot_table methods beyond SQL
author: Sarah Chen
image: images/posts/photos/IMG-0672.JPG

---
<figure> 
   <img src="{{"/images/photos/posts/IMG-0672.jpg"| relative_url}}"> 
   <figcaption>Photo by Ji Biduan</figcaption>
</figure> 


The concepts between SAS <span class="coding">PROC SQL</span>, Excel pivot table, and <span class="coding">pandas.pivot_table</span>, <span class="coding">df.groupby</span> are the same: **to get summaries on a two-way table, where the rows are the group-by and the columns are the <span class="coding">select</span>**, using SQL language.   I will not get into useful SAS procedures such as PROC MEANS, PROC SUMMARY, etc., even though the concepts are similar. 

**Columns**: select
**Rows**: groupby (also need to be in the select statement)

# Columns
Below is a simple select statement,selecting all the columns, using a where statement to filter. 
<div class="code-head"><span>code</span>select.sas</div>

```sas
SELECT * 
FROM data WHERE date > '2022-04-29'd and tempreture < 0;
```

In Python, 
```python
data[(data.date> pd.Timestamp('2022-04-29')) &(data.tempreture < 0)]
```

# Rows and columns


<div class="code-head"><span>code</span>groupby.py</div>

```python
tips= sns.load_dataset('tips')
tips.groupby(['smoker', 'day']).agg({'tip': [np.size, np.mean]})
Out: 
               tip
              size  mean
smoker day
Yes    Thur 17.000 3.030
       Fri  15.000 2.714
       Sat  42.000 2.875
       Sun  19.000 3.517
No     Thur 45.000 2.674
       Fri   4.000 2.812
       Sat  45.000 3.103
       Sun  57.000 3.168
```

Let's look at an example from a [SAS community Q &A.](https://communities.sas.com/t5/SAS-Programming/how-do-I-achieve-PIVOT-the-one-in-EXCEL-in-SQL/td-p/567311)

<div class="code-head"><span>code</span>prepare_data.sas</div>

```sas
data battlerecord ;                                                  
  input year $ com_a $ com_b $ result_of_a $ ;                       
  cards ;                                                            
2015 INTEL AMD DEFEAT                                                
2015 INTEL AMD WIN                                                   
2015 INTEL SAMSUNG WIN                                               
2016 INTEL AMD DRAW                                                  
2016 AMD SAMSUNG LOSE                                                
2016 AMD INTEL LOSE                                                  
2017 INTEL QUALCOMM WIN                                              
run ;  
```

Observation on the data:  all three columns that are involved in the query are categorical.   
Goal: we are going to group by 2 of the 3 columns and pivot the 3rd column, and get the counts of this tabulation.  

|    |   year | com_a   | com_b    | result_of_a   |
|---:|-------:|:--------|:---------|:--------------|
|  0 |   2015 | INTEL   | AMD      | DEFEAT        |
|  1 |   2015 | INTEL   | AMD      | WIN           |
|  2 |   2015 | INTEL   | SAMSUNG  | WIN           |
|  3 |   2016 | INTEL   | AMD      | DRAW          |
|  4 |   2016 | AMD     | SAMSUNG  | LOSE          |
|  5 |   2016 | AMD     | INTEL    | LOSE          |
|  6 |   2017 | INTEL   | QUALCOMM | WIN           |

**SAS**
To summarize it using SAS Proc SQL, the logic is straight forward as plain SQL.  The *tedious* part is to do <span class="coding">sum (result_of_a in ("WIN")) as</span> repeatedly. 


<div class="code-head"><span>code</span>proc sql.sas</div>

```sas
option validvarname = any ;                                          
                                                                     
proc sql ;                                                           
  create table need as                                               
  select com_a as "(com_a)"n                                         
       , year as  "(year)"n                                          
       , sum (result_of_a in ("WIN")          ) as "(# of 'WIN's)"n  
       , sum (result_of_a in ("DEFEAT","LOSE")) as "(# of 'LOSE's)"n 
       , sum (result_of_a in ("DRAW")         ) as "(# of 'DRAW's)"n 
  from   battlerecord                                                
  group  1, 2                                                        
  order  1 desc, 2                                                   
  ;                                                                  
quit ;    
```

**Python**

This can be achieved in pandas easily with <span class="coding">groupby</span> or <span class="coding">pd.pivot_table</span>.  They can produce the same summary.  

The difference between the result is that 

The difference is that in pandas we initially include the column that is to be summarized in the <span class="coding">groupby</span>, and then <span class="coding">unstack</span> it to the columns. 

> To keep missings in a group, use <span class="coding">dropna=False</span>.

<div class="code-head"><span>code</span>groupyby.py</div>

```python 
df = pd.read_excel(r".\python_SAS\Python-for-SAS-Users\data\sql_data.xlsx")
df=pd.read_excel(r".\Python-for-SAS-Users\data\battlerecord.xlsx")
summarized = df.groupby(['com_a','year','result_of_a'], dropna=False).count().\
     unstack().fillna(0).sort_index(ascending=[False,True])
summarized
```
Although the column names are not exactly the same as the questioner asked for, we have accomplished most of what’s been asked for.

|                 |   ('com_b', 'DEFEAT') |   ('com_b', 'DRAW') |   ('com_b', 'LOSE') |   ('com_b', 'WIN') |
|:----------------|----------------------:|--------------------:|--------------------:|-------------------:|
| ('INTEL', 2015) |                     1 |                   0 |                   0 |                  2 |
| ('INTEL', 2016) |                     0 |                   1 |                   0 |                  0 |
| ('INTEL', 2017) |                     0 |                   0 |                   0 |                  1 |
| ('AMD', 2016)   |                     0 |                   0 |                   2 |                  0 |


Note that the levels of indices start from the outer layer: column indices start from the top and row indices start from the left.  

To remove the outer layer of row or column index, we can use <span class="coding">.droplevel(0)</span>.
To remove the inner most layer of row or column index, use <span class="coding">.droplevel(-1)</span>

```python
# to drop the top level of column multiindex
summarized.columns=summarized.columns.droplevel(0)
# to get row index information as columns
summarized.reset_index(inplace=True)
```

|    | com_a   |   year |   DEFEAT |   DRAW |   LOSE |   WIN |
|---:|:--------|-------:|---------:|-------:|-------:|------:|
|  0 | INTEL   |   2015 |        1 |      0 |      0 |     2 |
|  1 | INTEL   |   2016 |        0 |      1 |      0 |     0 |
|  2 | INTEL   |   2017 |        0 |      0 |      0 |     1 |
|  3 | AMD     |   2016 |        0 |      0 |      2 |     0 |


Another way in Python is to use <span class="coding">pd.pivot_table</span>. 

This method is similar to the SQL logic in that only the <span class="coding">groupby</span> columns are in the index. The difference is that the column to be pivoted is directly assigned to the column. 

Comparing with <span class="coding">df.groupby</span>, it is more straightforward, and do not require the "trick" of unstack multiindex.

<div class="code-head"><span>code</span>pd.pivot_table.py</div>

```python
df = pd.read_excel(r".\python_SAS\Python-for-SAS-Users\data\sql_data.xlsx")
pd.pivot_table(df, columns ='result_of_a', index=['com_a','year'], aggfunc='size',
     ...:     fill_value = 0).sort_index(ascending = [False, True])
```

|                 |   DEFEAT |   DRAW |   LOSE |   WIN |
|:----------------|---------:|-------:|-------:|------:|
| ('INTEL', 2015) |        1 |      0 |      0 |     2 |
| ('INTEL', 2016) |        0 |      1 |      0 |     0 |
| ('INTEL', 2017) |        0 |      0 |      0 |     1 |
| ('AMD', 2016)   |        0 |      0 |      2 |     0 |

Again, if we are not satisfied with how the index looks, we can <span class="coding">reset_index(inplace=True)</span> to get information out of the index. 

**Conclusion**: for this problem, I think pd.pivot_table has the simplest solution because it takes only one line of code:
```python
pd.pivot_table(df, columns ='result_of_a', index=['com_a','year'], aggfunc='size',
     ...:     fill_value = 0).sort_index(ascending = [False, True]).reset_index(inplace=True)
```
However, it is not enough just to get a solution. Understanding how these methods are related to each other, and the general kind of problems that they can solve, can help us solve many more problems. 

# Treatment of missing
## Filtering rows

Task | SAS PROC SQL | python pandas
---------|----------|---------
want rows with missing | <span class="coding">SELECT * FROM df WHERE col IS NULL</span> | <span class="coding">df[df.col.isna()]</span>
don't want rows with missing | <span class="coding">SELECT * FROM df WHERE col IS NOT NULL</span> | <span class="coding">df[df.col.notna()</span>]
group by | automatically includes missing asa | use <span class="coding">dropna=False</span>

<div class="code-head"><span>code</span>select missing.sas</div>

```sas
SELECT * 
FROM data WHERE date IS NULL;
```

## In group by
SAS PROC SQL treats missing as a group unless you specify it with "where 1 is not missing".  This is a good feature. 

Whereas in Python, pd.pivot_table, using <span class="coding">dropna=False</span> will keep the missing as a row. 

## A Step Above
However, the advantage of using <span class="coding">pd.pivote_table<span> or <span class="coding">df.groupby</span> is not limited to summary tables. 

One of the use cases is to leverage datetime index in the methods.

For example, say we have a portfolio of loans to a group of customers.  After we <span class="coding">pd.pivot_table(index=datetime_colum, column = customer, aggfunc=’size’)</span>, we can immediately follow up with pandas <span class="coding">resampling</span> or <span class="coding">rolling</span> methods to perform additional statistics desired. 


# Joins

A trick that I use to remember the SQL syntax is: **S F J O W G H O**, which means
- select
- from
- join
- on
- where
- group by
- having
- order by


<div class="code-head"><span>code</span>join.sas</div>

```sas
SELECT *
FROM df1
INNER JOIN df2
  ON df1.key = df2.key;
```

```python
pd.merge(df1, df2, on='key')
```

<div class="code-head"><span>code</span>left join.sas</div>

```sas
SELECT *
FROM df1
LEFT OUTER JOIN df2
  ON df1.key = df2.key;
```

```python
pd.merge(df1, df2, on='key', how='left')
```

# Union
Union is stacking one set of data upon another, where the same columns are lined up.

<span class="coding">Union all</span> is stacking everything regardless duplicates.  Whereas <span class="coding">union</span> removes duplicates. 
## union all
<span class="coding">union all </span>

<div class="code-head"><span>code</span>union.sas</div>

```sas
SELECT city, rank
FROM df1
UNION ALL
SELECT city, rank
FROM df2;
```

<div class="code-head"><span>code</span>union.py</div>

```python
pd.concat([df1, df2])
```