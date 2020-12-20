---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "SAS PROC SQL and python df.groupby and pivot_table."
description: Resampling and interpolation
author: Sarah Chen
image: images/posts/Figure 1- 5. Price and Expanding Window Average.png

---
The concepts between SAS <span class="coding">PROC SQL</span>, Excel pivot table, and <span class="coding">pandas.pivot_table</span>, <span class="coding">df.groupby</span> are more or less the same: to get summaries on a two-way table, where the rows are the group-by and the columns are the <span class="coding">select</span>, using SQL language. 

It may be better to illustrate using an example, which came from a [SAS community Q &A.](https://communities.sas.com/t5/SAS-Programming/how-do-I-achieve-PIVOT-the-one-in-EXCEL-in-SQL/td-p/567311)

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

This can be achieved in pandas easily with <span class="coding">groupby</span>. The difference is that in pandas we initially include the column that is to be summarized in the <span class="coding">groupby</span>, and then <span class="coding">unstack</span> it to the columns. 

<div class="code-head"><span>code</span>groupyby.py</div>

```python 
>>> summarized = df.groupby(['com_a','year','result_of_a']).count().unstack().fillna(0).sort_index(ascending=[False,True])
>>> summarized
```
Although the column names are not exactly the same as the questioner asked for, we have accomplished most of what’s been asked for.

|                 |   ('com_b', 'DEFEAT') |   ('com_b', 'DRAW') |   ('com_b', 'LOSE') |   ('com_b', 'WIN') |
|:----------------|----------------------:|--------------------:|--------------------:|-------------------:|
| ('INTEL', 2015) |                     1 |                   0 |                   0 |                  2 |
| ('INTEL', 2016) |                     0 |                   1 |                   0 |                  0 |
| ('INTEL', 2017) |                     0 |                   0 |                   0 |                  1 |
| ('AMD', 2016)   |                     0 |                   0 |                   2 |                  0 |


If we are not satisfied with how the index and column labels look, we can do the following:

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

This method is similar to the SQL logic in that only the <span class="coding">groupby</span> columns are in the index. The difference is that the column to be pivoted is in the column. 

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