---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "MultiIndexing"
description: Data processing using Python and SAS.
author: Sarah Chen
image: images/posts/tan-kaninthanond.JPG
---

<figure>
  <img src="{{ "/images/posts/tan-kaninthanond.jpg" | relative_url }}">
  <figcaption>Photo by Tan Kaninthanond</figcaption>
</figure>


### MultiIndexing
Thus far, the use of indexes involves a single column labeling DataFrame rows. See Add Index to DataFrame as an illustration.  This section introduces MultiIndexing, also known as hierarchical indexing.  

Often the data for analysis is captured at the detail level.  As part of performing an exploratory analysis, a <span class="coding">MultiIndex</span> DataFrame provides a useful multi-dimensional ‘view’ of data. 

In a DataFrame, rows and columns may have multiple levels of indices defined with a <span class="coding">MultiIndex</span> object. Later in this chapter we will see the benefits from MutliIndexing for ‘pivoting’ DataFrames much the same way an Excel spreadsheet can be pivoted.  We will also discuss ‘stacking’ data as a means for ‘flattening’ DataFrames and ‘unstacking’ to perform the reverse operation. To begin, consider MultiIndex Details.  The example creates a hierarchical index for the columns in the df DataFrame.

<div class="code-head"><span>code</span> MultiIndex Details.py</div>

```python
 import pandas as pd
 import numpy as np
 pd.options.display.float_format = '{:,.2f}'.format
 cols = pd.MultiIndex.from_tuples([ (x,y) for x in ['Test1','Test2','Test3'] for y in ['Pre','Post']])
 nl = '\n'
 np.random.seed(98765)
 df = pd.DataFrame(np.random.randn(2,6),index = ['Row 1','Row 2'],columns = cols)
 print(nl,
...       df)

       Test1      Test2       Test3
        Pre Post   Pre  Post   Pre  Post
Row 1 -0.65 0.85  1.08 -1.79  0.94 -0.76
Row 2  0.72 1.02  0.97 -0.04 -0.07  0.81
```

To control the ouput, <span class='coding'>pd.options.display.float_format</span> displays floats two places to the right of the decimal.  There are several different constructors for defining a <span class="coding">MultiIndex</span>.  This example uses <span class='coding'>pd.MultiIndex.from_tuples</span> to define a hierarchical index for the DataFrame columns.  

A Python tuple is a data structure similar to a list used to hold unlike items such as strings, ints, floats, etc. Unlike a list, tuples are immutable and are defined using a pair of parentheses ( ).   In this example the for loops are short-cuts creating the strings to populate the tuples.  

Without the for loops the syntax is:

```python
pd.MultiIndex.from_tuples([('Test1', 'Pre'), ('Test1', 'Post'), 
    ('Test2', 'Pre'), ('Test2', 'Post'),('Test3', 'Pre'), ('Test3', 'Post')])
```

The df DataFrame in this example uses the DataFrame constructor assigning row labels with <span class='coding'>index=['Row 1','Row 2']</span> and <span class='coding'>columns = col</span> creating the <span class="coding">MultiIndexed</span> or hierarchical columns.  

With the df DataFrame constructed along with its hierarchical columns and row labels, let’s examine the constituent components closely by considering Multi-Indexed Details.

<div class="code-head"><span>code</span>Multi-Indexed Details.py</div>

```python
 print(nl,
...       'Index:      '  , df.index,
...   nl              ,
...       'Columns:    '  , df.columns,
...   nl              ,
...       'Col Level 1:'  , df.columns.levels[0],
...   nl              ,
...       'Col Level 2:'  , df.columns.levels[1])

Out:
 Index:       Index(['Row 1', 'Row 2'], dtype='object')
 Columns:     MultiIndex(levels=[['Test1', 'Test2', 'Test3'], ['Post', 'Pre']],
           codes=[[0, 0, 1, 1, 2, 2], [1, 0, 1, 0, 1, 0]])
 Col Level 1: Index(['Test1', 'Test2', 'Test3'], dtype='object')
 Col Level 2: Index(['Post', 'Pre'], dtype='object')
```
Recall  a pandas index is  simply a method to assign labels to rows.  In this example statement <span class='coding'>df.columns</span> returns the DataFrame column labels. In this case, a Python list of lists which are the unique levels from the <span class="coding">MultiIndex</span> assigned as columns.  

The labels return a Python list of lists referencing these levels on the index, in this case, two levels.  The statement <span class='coding'>df.columns.levels[0] </span>
returns a Python list of column lables used in the outer-most level of the hierarchical index.  The statement <span class="coding">df.columns.levels[1]</span> returns the inner-most level of the hierarchical index.  

Whether assigned to the DataFrame rows or columns,  a hierarchical index can have a arbitrary number of levels. To further understand MultiIndexes we construct a more elaborate DataFrame. 

The following example, Create tickets DataFrame, illustrates a hierarchical index for both the DataFrame’s rows and columns.  The <span class="coding">MultiIndex</span> for the columns has a depth of two with values for "Area" and "When" as levels.  The second hierarchical index on the rows has a depth of two with "Year" and "Month" values as levels.  

<div class="code-head"><span>code</span> Create tickets DataFrame.py</div>

```python
 import pandas as pd
 import numpy as np
 np.random.seed(654321)
 idx = pd.MultiIndex.from_product([[2015, 2016, 2017, 2018],
...                          [1, 2, 3]],
...                  names = ['Year', 'Month'])
 columns=pd.MultiIndex.from_product([['City' , 'Suburbs', 'Rural'],
...                          ['Day' , 'Night']],
...                  names = ['Area', 'When'])
 data = np.round(np.random.randn(12, 6),2)
 data = abs(np.floor_divide(data[:] * 100, 5))

 tickets = pd.DataFrame(data, index=idx, columns = columns).
    sort_index().sort_index(axis=1)
 print(tickets)
Out:
Area        City       Rural       Suburbs
When         Day Night   Day Night     Day Night
Year Month
2015 1      15.0  18.0   9.0   3.0     3.0   3.0
     2      11.0  18.0   3.0  30.0    42.0  15.0
     3       5.0  54.0   7.0   6.0    14.0  18.0
2016 1      11.0  17.0   1.0   0.0    11.0  26.0
     2       7.0  23.0   3.0   5.0    19.0   2.0
     3       9.0  17.0  31.0  48.0     2.0  17.0
2017 1      21.0   5.0  22.0  10.0    12.0   2.0
     2       5.0  33.0  19.0   2.0     7.0  10.0
     3      31.0  12.0  19.0  17.0    14.0   2.0
2018 1      25.0  10.0   8.0   4.0    20.0  15.0
     2      35.0  14.0   9.0  14.0    10.0   1.0
     3       3.0  32.0  33.0  21.0    24.0   6.0
```
The <span class="coding">print(tickets.index)</span> statement returns the <span class="coding">MultiIndex</span> levels and labels assigned to the rows.  To  sub-set DataFrame rows we refer to: [2015, 2016, 2017, 2018] as the outer level of the <span class="coding">MultiIndex</span> to indicate Year and: [1, 2, 3] as the inner level of the <span class="coding">MultiIndex</span> to indicate Month to compose the row slices.  

Similarly, to sub-set columns, we refer to: ['City', 'Rural', 'Suburbs'] as the outer levels of the of the <span class="coding">MultiIndex</span> to indicate Area and: ['Day', 'Night'] as the inner portion of the <span class="coding">MultiIndex</span> to indicate When for the column slices.  Together, row and column slices determine the DataFrame subset.  

In the example below, we use <span class="coding">PROC TABULATE</span> to render output shaped like the tickets DataFrame from Python.  Since the Python code and SAS code call different random number generators the values created, while similar, differ between the DataFrame and the SAS dataset.

<div class="code-head"><span>code</span>Tickets Dataset from PROC TABULATE.sas</div>

```sas
4  data tickets;
5  length Area $ 7
6         When $  9;
7  call streaminit(123456);
8  do year = 2015, 2016, 2017, 2018;
9    do month = 1, 2, 3;
10        do area = 'City', 'Rural', 'Suburbs';
11           do when = 'Day', 'Night';
12              tickets = abs(int((rand('Normal')*100)/5));
13              output;
14         end;
15        end;
16     end;
17  end;

NOTE: The data set WORK.TICKETS has 72 observations and 5 variables.

18 proc tabulate;
19    var tickets;;
20    class area when year month;
21          table year * month ,
22                area=' ' * when=' ' * sum=' ' * tickets=' ';
23  run;
```
The Data Step uses nested <span class="coding">DO</span>/<span class="coding">END</span> blocks generating the class variables area, when, year, and  month.  The tickets variable is created with nested functions working from the inside out:

1.  The <span class="coding">RAND</span> function draws values from the normal distribution random number generator.  These values are then multiplied by 100 and the product is divided by 5.

2.  The <span class="coding">INT</span> function returns the integer portion of the value

3.  The <span class="coding">ABS</span> function returns the absolute value

<span class="coding">PROC TABULATE</span> illustrates the <span class="coding">TABLE</span> statement syntax that constructs this particular output:
```sas
table year * month ,
      area=' ' * when=' ' * sum=' ' * tickets=' ';
```
The row dimension crosses <span class='coding'>*</span> the month variable with the year variable.  The column dimension crosses <span class='coding'>*</span> values for tickets with the area variable which in turn is crossed <span class='coding'>*</span> with the when variable and together they are crossed with the summed value for the tickets variable.
 
#### Basic Sub-sets with MultiIndexes
With the tickets DataFrame created having hierarchical indexes for rows and columns, we can apply a range of methods for sub setting as well as applying condition-based logic as filtering criteria. 

An important feature of hierarchical indexing is the ability to select data by a “partial” label identifying a subgroup in the data. Partial selection “drops” levels of the hierarchical index from the results using methods analogous to row and column slicing for regular DataFrames.  

<div class="code-head"><span>code</span> Identify Subgroups with MultiIndexing.py</div>

```python
 tickets['Rural']
Out:
When         Day  Night
Year Month
2015 1       9.0    3.0
     2       3.0   30.0
     3       7.0    6.0
2016 1       1.0    0.0
     2       3.0    5.0
     3      31.0   48.0
2017 1      22.0   10.0
     2      19.0    2.0
     3      19.0   17.0
2018 1       8.0    4.0
     2       9.0   14.0
     3      33.0   21.0
```
In this example the <span class='coding'>[ ]</span> operator returns a subset of the tickets DataFrame from the level Rural.   In this case Rural designates one of three values from the outer level of the column hierarchical index.  Because there is no explicit row selection all rows are returned. 

In the following example, Identify Subgroups with MultiIndexing, answers the question: for each month how many tickets were issued in the city at night?

<div class="code-head"><span>code</span>Identify Subgroups with MultiIndexing.py</div>

```python
 tickets['City', 'Night']
Out:
Year  Month
2015  1        18.0
      2        18.0
      3        54.0
2016  1        17.0
      2        23.0
      3        17.0
2017  1         5.0
      2        33.0
      3        12.0
2018  1        10.0
      2        14.0
      3        32.0
```

This example illustrates selecting with both levels of the column <span class="coding">MultiIndex</span>.  City is from the outer-most level of the hierarchical index and Night is from the inner-most level.

Recall that most subsetting and slicing operations return a DataFrame.  The following example, Sum Tickets to New DataFrame, illustrates creating a new DataFrame.  In this example the sum function is applied to the tickets DataFrame elements returning the sum of all tickets by year.  These summed values create the new DataFrame sum_tickets.

<div class="code-head"><span>code</span>Sum Tickets to New DataFrame.py</div>

```python
 sum_tickets = tickets.sum(level = 'Year')
 print(sum_tickets)
Out:
Area   City        Rural      Suburbs
When   Day  Night  Day  Night Day  Night
Year
2015  31.0  90.0  19.0  39.0  59.0  36.0
2016  27.0  57.0  35.0  53.0  32.0  45.0
2017  57.0  50.0  60.0  29.0  33.0  14.0
2018  63.0  56.0  50.0  39.0  54.0  22.0
```
Use the axis = 1 argument to apply the sum function along a column with the syntax:

```python
sum_tickets2 = tickets.sum(level = 'Area', axis=1)
```
The following example illustrates using <span class='coding'>PROC TABULATE</span> to render the same report as well as create the  sum_tickets dataset.

<div class="code-head"><span>code</span>PROC TABULATE Report and New Dataset.sas</div>

```sas
4 ods output 
5     table = sum_tickets (keep = area
6                                  when
7                                  year
8                                  tickets_sum);
9 proc tabulate data=tickets;
10    var tickets;
11    class area when year;
12          table year,
13          area=' ' * when=' ' * sum=' ' * tickets=' ';run;

NOTE: The data set WORK.SUM_TICKETS has 24 observations and 4 variables.
NOTE: There were 72 observations read from the data set WORK.TICKETS.

14 ods output close;
15 proc print data = sum_tickets;
16 run;
NOTE: There were 24 observations read from the data set WORK.SUM_TICKETS.
```


The default statistic for <span class='coding'>PROC TABULATE</span> is sum and is applied to the variable tickets using the <span class="coding">VAR</span> statement. The <span class="coding">TABLE</span> statement arranges the output similar to the output in the following example. The <span class='coding'>PROC TABULATE</span> output is presented Tickets Summed with <span class='coding'>PROC TABULATE</span>.

Tickets Summed with <span class='coding'>PROC TABULATE</span>
In order to create the output dataset sum_tickets, the syntax

```sas
ods output 
   table = sum_tickets (keep = area
                               when
                               year
                               tickets_sum);
```

opens the ODS destination <span class="coding">sum_tickets</span>, as an output SAS dataset with a <span class="coding">KEEP</span> list of variables.  This method for summarization is an alternative to calling <span class="coding">PROC SUMMARY</span>/<span class="coding">MEANS</span> or <span class="coding">PROC SQL</span>.

In the following example, Summarizing tickets Dataset with <span class="coding">PROC SUMMARY</span>, illustrates the more convential method for producing the same ‘rolled-up’, or summarized dataset.

<div class="code-head"><span>code</span>Summarizing tickets Dataset with PROC SUMMARY.sas</div>

```sas
4  proc summary data = tickets
5               nway
6               noprint;
7     class area
8           when
9           year;
10     output out=sum_tickets(keep=area when year tickets_sum)
11            sum(tickets)=tickets_sum;
NOTE: There were 72 observations read from the data set WORK.TICKETS.
NOTE: The data set WORK.SUM_TICKETS has 24 observations and 4 variables.
```
The <span class="coding">NWAY</span> option requests a combination for all levels of variable values listed on the <span class="coding">CLASS</span> statement.  The <span class="coding">sum(tickets)=tickets_sum</span> option then sums the number of tickets for each <span class="coding">NWAY</span> crossing.
#### Advanced Indexing with MultiIndexes
Earlier in the chapter we detailed the <span class="coding">.loc</span> indexer for slicing rows and columns with indexed DataFrames.  See the section entitled, Return Rows and Columns by Label in this chapter.   Slicing rows and columns with the <span class="coding">.loc</span> indexer can be used with a MultiIndexed DataFrame using similar syntax.  The <span class="coding">.loc</span> indexer supports Boolean logic for filtering criteria.  

The <span class="coding">.loc</span> indexer enables partial slicing using hierarchically indexed rows and/or columns.  Begin by returning the DataFrame along with its index and columns information in the example below, Return Ticket Index and Column Levels.

<div class="code-head"><span>code</span>Return Ticket Index and Column Levels.py</div>

```python
 print(tickets.index)
Out:
MultiIndex(levels=[[2015, 2016, 2017, 2018], [1, 2, 3]],
           codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]],
           names=['Year', 'Month'])
 print(tickets.columns)
Out:
MultiIndex(levels=[['City', 'Rural', 'Suburbs'], ['Day', 'Night']],
           codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
           names=['Area', 'When'])
```

The <span class="coding">.loc</span> indexer takes as arguments, slicers to determine the DataFrame sub-set of interest.  In the following example, Year Slice 2018, illustrates returning all rows for year 2018.

<div class="code-head"><span>code</span>Year Slice 2018.py</div>

```python
 tickets.loc[2018]
Out:
Area   City       Rural       Suburbs
When    Day Night   Day Night     Day Night
Month
1      25.0  10.0   8.0   4.0    20.0  15.0
2      35.0  14.0   9.0  14.0    10.0   1.0
3       3.0  32.0  33.0  21.0    24.0   6.0
```
In this case, the rows are sliced returning those with the <span class="coding">MultiIndex</span> level for Year equal to 2018.  And because no column slicer is provided all columns are returned.
We can slice Year level for 2018 and Month level for 3 illustrated in the following example. 

<div class="code-head"><span>code</span>Slice Year 2018 and Month 3.py</div>

```python
 tickets.loc[2018, 3, :]
Out:
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2018 3      3.0  32.0  33.0  21.0    24.0   6.0
```
In this example, level 2018 denotes the outer row slice and 3 denotes the inner row slice.  This subset-sets the DataFrame by returning month 3 for every year.  The column slice follows the second comma.  Again, with no column slice provided, denoted by the colon <span class="coding">:</span> all columns are returned.

