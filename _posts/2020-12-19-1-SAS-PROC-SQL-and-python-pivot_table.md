---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "SAS PROC SQL and python pivot_table."
description: Resampling and interpolation
author: Sarah Chen
image: images/posts/Figure 1- 5. Price and Expanding Window Average.png

---
The concepts between SAS PROC SQL, Excel pivot table, and pandas.pivot_table, df.groupby are more or less the same: to get summaries on a two-way table, where the rows are the group-by and the columns are the “select”, using SQL language. 

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

Here is how the data look slike:

|    |   year | com_a   | com_b    | result_of_a   |
|---:|-------:|:--------|:---------|:--------------|
|  0 |   2015 | INTEL   | AMD      | DEFEAT        |
|  1 |   2015 | INTEL   | AMD      | WIN           |
|  2 |   2015 | INTEL   | SAMSUNG  | WIN           |
|  3 |   2016 | INTEL   | AMD      | DRAW          |
|  4 |   2016 | AMD     | SAMSUNG  | LOSE          |
|  5 |   2016 | AMD     | INTEL    | LOSE          |
|  6 |   2017 | INTEL   | QUALCOMM | WIN           |

To summarize it using SAS Proc SQL, the logic is straight forward.  

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
In python, one way to do is to use pd.pivot_table, which is only one line of code, although the column names are not exactly the same as the questioner asked for. 

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
