---
layout: post
tag : Learning Python and SAS
category: "Python for SAS"
title: "MultiIndexing"
description: Data processing using Python and SAS.
author: Sarah Chen
image: images/posts/tan-kaninthanond.jpg
---
This post is about multiindexing in pandas and is partially based on Chapter 4 "Indexing and groupBy" of my co-authored book (from page 131) [Python for SAS Users](https://www.amazon.com/Python-SAS-Users-SAS-Oriented-Introduction/dp/1484250001/ref=sr_1_3?crid=21NME5C69YGV7&keywords=python+for+sas+users&qid=1572638715&sprefix=python+for+sas+%2Caps%2C196&sr=8-3). 

In this post we will cover:

[- MultiIndexing](#MultiIndexing)

[- Basic Sub-sets with MultiIndexes](#Basic-Sub-sets-with-MultiIndexes)

[- Advanced Indexing with MultiIndexes](#Advanced-Indexing-with-MultiIndexes)

<figure>
  <img src="{{ "/images/posts/tan-kaninthanond.jpg" | relative_url }}">
  <figcaption>Photo by Tan Kaninthanond</figcaption>
</figure>


<h3 id="MultiIndexing">MultiIndexing</h3>

This section introduces MultiIndexing, also known as hierarchical indexing.  The main advantage of MultiIndexing is to be able drill down data without the need of using <span class='coding'>groupby</span>. 

While many SAS users have not used indexing or composite indexing, all SAS users have encountered what looks like Python MultiIndex from the output of <span class="coding">PROC FREQ</span> and <span class="coding">PROC MEANS</span>, or <span class="coding">PROC TABULATE</span>.  For example, if you have used <span class="coding">PROC FREQ</span> followed by two column names in the <span class="coding">TABLES</span> statement such as TABLES a\*b, you would have seen the hierchical frequency output.  As part of data analysis, a <span class="coding">MultiIndex</span> DataFrame provides a useful multi-dimensional ‘view’ of data, the same way you find it useful to use multidimensional Excel pivot tables. 

In a DataFrame, rows and columns may have multiple levels of indices defined with a <span class="coding">MultiIndex</span> object.  Later in this chapter we will see the benefits from MutliIndexing for ‘pivoting’ DataFrames much the same way an Excel spreadsheet can be pivoted.  We will also discuss ‘stacking’ data as a means for ‘slimminging’ DataFrames and ‘unstacking’ to perform the reverse operation. 

<div class="code-head"><span>code</span> MultiIndex Details.py</div>

```python
 import pandas as pd
 import numpy as np
 pd.options.display.float_format = '{:,.2f}'.format
 cols = pd.MultiIndex.from_product([['Test1','Test2','Test3'],['Pre','Post']])
 nl = '\n'
 np.random.seed(98765)
 df = pd.DataFrame(np.random.randn(2,6),index = ['Row 1','Row 2'],columns = cols)
 print(nl,
...       df)
[Out]:
       Test1      Test2       Test3
        Pre Post   Pre  Post   Pre  Post
Row 1 -0.65 0.85  1.08 -1.79  0.94 -0.76
Row 2  0.72 1.02  0.97 -0.04 -0.07  0.81
```

NOTE:
  1. The df DataFrame in this example uses the DataFrame constructor assigning row labels with <span class='coding'>index=['Row 1','Row 2']</span> and <span class='coding'>columns = col</span> creating the <span class="coding">MultiIndexed</span> or hierarchical columns.  
  2. To control the ouput, <span class='coding'>pd.options.display.float_format</span> displays floats two places to the right of the decimal.  There are several different constructors for defining a <span class="coding">MultiIndex</span>.  This example uses <span class='coding'>pd.MultiIndex.from_tuples</span> to define a hierarchical index for the DataFrame columns.  
  3. Alternatively, we can also use <span class='coding'>pd.MultiIndex.from_tuples</span>, and the syntax is:

```python
cols = pd.MultiIndex.from_tuples([ (x,y) for x in ['Test1','Test2','Test3'] for y in ['Pre','Post']])
df = pd.DataFrame(np.random.randn(2,6),index = ['Row 1','Row 2'],columns = cols)
# or 
pd.MultiIndex.from_tuples([('Test1', 'Pre'), ('Test1', 'Post'), 
    ('Test2', 'Pre'), ('Test2', 'Post'),('Test3', 'Pre'), ('Test3', 'Post')])
```

With the df DataFrame constructed along with its hierarchical columns and row labels, let’s examine the constituent components closely by considering Multi-Indexed Details.

<div class="code-head"><span>code</span>Multi-Indexed Details.py</div>

```python
 df.index
[Out]: Index(['Row 1', 'Row 2'], dtype='object')

 df.columns
[Out]: MultiIndex(levels=[['Test1', 'Test2', 'Test3'], ['Post', 'Pre']],
           labels=[[0, 0, 1, 1, 2, 2], [1, 0, 1, 0, 1, 0]])

 df.columns.levels[0]
[Out]: Index(['Test1', 'Test2', 'Test3'], dtype='object')

 df.columns.levels[1]
[Out]:Index(['Post', 'Pre'], dtype='object')

```
Recall  a pandas index is  simply a method to assign labels to rows.  In this example statement <span class='coding'>df.columns</span> returns the DataFrame column labels. In this case, a Python list of lists which are the unique levels from the <span class="coding">MultiIndex</span> assigned as columns.  

The labels return a Python list of lists referencing these levels on the index, in this case, two levels.  

Like peeling an onion, we start from the outer layer.  

The statement <span class='coding'>df.columns.levels[0] </span> returns a Python list of column labels used in the outer-most level of the hierarchical index.  The statement <span class="coding">df.columns.levels[1]</span> returns the inner-most level of the hierarchical index.  

Whether assigned to the DataFrame rows or columns,  a hierarchical index can have a arbitrary number of levels. To further understand MultiIndexes we construct a more elaborate DataFrame. 

The following example, Create tickets DataFrame, illustrates a hierarchical index for both the DataFrame’s rows and columns.  The <span class="coding">MultiIndex</span> for the columns has a depth of two with values for "Area" and "When" as levels.  The second hierarchical index on the rows has a depth of two with "Year" and "Month" values as levels.  

<div class="code-head"><span>code</span> Create tickets DataFrame.py</div>

```python
 import pandas as pd
 import numpy as np
 np.random.seed(654321)
 idx = pd.MultiIndex.from_product([[2017, 2018, 2019, 2020],
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
The DATA step uses nested <span class="coding">DO</span>/<span class="coding">END</span> blocks generating the class variables area, when, year, and  month.  The tickets variable is created with nested functions working from the inside out:

1.  The <span class="coding">RAND</span> function draws values from the normal distribution random number generator.  These values are then multiplied by 100 and the product is divided by 5.

2.  The <span class="coding">INT</span> function returns the integer portion of the value

3.  The <span class="coding">ABS</span> function returns the absolute value

<span class="coding">PROC TABULATE</span> illustrates the <span class="coding">TABLE</span> statement syntax that constructs this particular output:
```sas
TABLE year * month ,
      area=' ' * when=' ' * sum=' ' * tickets=' ';
```
The row dimension crosses <span class='coding'>*</span> the month variable with the year variable.  The column dimension crosses <span class='coding'>*</span> values for tickets with the area variable which in turn is crossed <span class='coding'>*</span> with the when variable and together they are crossed with the summed value for the tickets variable.
 
<h3 id="Basic-Sub-sets-with-MultiIndexes">Basic Sub-sets with MultiIndexes</h3>

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
<h3 id="Advanced-Indexing-with-MultiIndexes">Advanced Indexing with MultiIndexes</h3>

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


<div class="code-head"><span>code</span>Slice Year 2018 and Month 3.py</div>

```python
 tickets.loc[2018, 3, :]
Out:
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2018 3      3.0  32.0  33.0  21.0    24.0   6.0
```
##### Slicing Rows and Columns
Consider the example below, Slice Month 3 for all Years.   In this example we wish to return the 3rd month for each year.  Based on what we have learned about row and column slicing up to this point, it is reasonable to conclude the statement:

tickets.loc[(:,3),:]

is the appropirate syntax.  However, this syntax raises an error since it is illeagl to use a colon inside a tuple constructor.   Recall a tuple is an immutable sequence of items enclosed by parenthesis. As a convenience the Python’s built-in <span class="coding">slice(None)</span> function selects all the content for a level. In this case we want month level 3 for all years.  

<div class="code-head"><span>code</span> Slice Month 3 for all Years.py</div>

```python
>>> tickets.loc[(slice(None), 3), :]
Area        City       Rural       Suburbs
When         Day Night   Day Night     Day Night
Year Month
2015 3       5.0  54.0   7.0   6.0    14.0  18.0
2016 3       9.0  17.0  31.0  48.0     2.0  17.0
2017 3      31.0  12.0  19.0  17.0    14.0   2.0
2018 3       3.0  32.0  33.0  21.0    24.0   6.0
```
The syntax <span class="coding">slice(None)</span> is the slicer for the Year column which includes all values for a given level, in this case, 2015 to 2018 followed by 3 to designate the level for month.  All columns are returned since no column slicer was given.
Another way to request this same sub-set is:

```python
tickets.loc[(slice(None), slice(3,3)), :]
```

Consider the request for all years and months 2 and 3 as the row slicer in the following example, Slice Months 2 and 3 for all Years.

<div class="code-head"><span>code</span> Slice Months 2 and 3 for all Years.py</div>

```python
>>> tickets.loc[(slice(None), slice(2,3)), :]
Area        City       Rural       Suburbs
When         Day Night   Day Night     Day Night
Year Month
2015 2      11.0  18.0   3.0  30.0    42.0  15.0
     3       5.0  54.0   7.0   6.0    14.0  18.0
2016 2       7.0  23.0   3.0   5.0    19.0   2.0
     3       9.0  17.0  31.0  48.0     2.0  17.0
2017 2       5.0  33.0  19.0   2.0     7.0  10.0
     3      31.0  12.0  19.0  17.0    14.0   2.0
2018 2      35.0  14.0   9.0  14.0    10.0   1.0
     3       3.0  32.0  33.0  21.0    24.0   6.0
```
Alternatively, the same results are accomplished with the syntax:
```python
idx_obj = ((slice(None), slice(2,3)), slice(None))
tickets.loc[idx_obj]
```

This syntax helps in further understanding exactly how the slicing operation is performed.  

1. The first <span class="coding">slice(None)</span> requests all of the rows for the outer row label, years 2015 to 2018. 
2. <span class="coding">slice(2,3) </span> returns months 2 and 3 for inner row label.  
3. The last <span class="coding">slice(None)</span> requests all columns, that is, both the outer column Area and the inner column When.
   
Fairly quickly, however, we begin to have difficulty supplying a collection of tuples  for the slicers used by the <span class="coding">.loc</span> indexer.  Fortunately, Pandas provides the <span class="coding">IndexSlice</span> object to deal with this situation.  

Consider the example below <span class="coding">IndexSlice</span> Object, as an alternative to the example, <span class="coding">IndexSlice</span> Object.

<div class="code-head"><span>code</span> IndexSlice Object.py</div>

```python
>>> idx = pd.IndexSlice
>>> tickets.loc[idx[2015:2018, 2:3], :]
>>>
Area        City       Rural       Suburbs
When         Day Night   Day Night     Day Night
Year Month
2015 2      11.0  18.0   3.0  30.0    42.0  15.0
     3       5.0  54.0   7.0   6.0    14.0  18.0
2016 2       7.0  23.0   3.0   5.0    19.0   2.0
     3       9.0  17.0  31.0  48.0     2.0  17.0
2017 2       5.0  33.0  19.0   2.0     7.0  10.0
     3      31.0  12.0  19.0  17.0    14.0   2.0
2018 2      35.0  14.0   9.0  14.0    10.0   1.0
     3       3.0  32.0  33.0  21.0    24.0   6.0
```
The <span class="coding">IndexSlice</span> object provides a more natural syntax for slicing operations on MultiIndexed rows and columns.  

In this case, the slice:
<span class="coding">tickets.loc[idx[2015:2018, 2:3], :]</span>
return years 2015:2018 inclusive on the outer level of the <span class="coding">MultiIndex</span> for the rows and months 2 and 3 inclusive on the inner level.  The colon (:) designates the start and stop positions for these row labels.  Following the row slicer is a comma (,) to designate the column slicer.  With no explicit column slices defined all columns are returned.  

Consider the following example, Slicing Rows and Columns, Example 1.

<div class="code-head"><span>code</span> Slicing Rows and Columns, Example 1.py</div>

```python
>>> idx = pd.IndexSlice
>>> tickets.loc[idx[2018:, 2:3 ], 'City' : 'Rural']
Area        City       Rural
When         Day Night   Day Night
Year Month
2018 2      35.0  14.0   9.0  14.0
     3       3.0  32.0  33.0  21.0
```
The row slicer returns levels 2018  for Year on the outer level of the <span class="coding">MultiIndex</span> and 2 and 3 from Month on the inner level.  The column slicer returns the levels City and Rural from Area on the outer level of the <span class="coding">MultiIndex</span>.  In this example, the column slicer did not slice along the inner level of the <span class="coding">MultiIndex</span> on When.

In the following example, Slicing Rows and Slicing Columns, Example 2, illustrates details for slicing columns.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> idx = pd.IndexSlice
>>> tickets.loc[idx[2018:, 2:3 ], idx['City', 'Day' : 'Night']]
Area        City
When         Day Night
Year Month
2018 2      35.0  14.0
     3       3.0  32.0
```
The row slicer returns levels 2018 for Year on the outer level of the <span class="coding">MultiIndex</span> and 2 and 3 from Month on the inner level.  The column slicer returns the levels City for Area on the outer level of the <span class="coding">MultiIndex</span> and the levels Day and Night on the inner level from When.

# Examples from work

## Reduce a dataframe to a dataframe with only numbers
When you become comfortable with multi-indexing, you will feel even more powerful at "manipulating" data.  For example, say you have a set of tables with company quarterly financials by region, department, and other categories. You can lump all the catagorical columns into one multi-index, with only financial values by quarter remaining, where the columns are "Q1", "Q2",...,"Qn". 

Since all the tables are numbers, you can first sort each of the tables by index (sorting them by index is very important otherwise the result would be wrong).  Adding checks will help ensuring this is done. 

```python
try:
     print(np.all(df1.index==df2.index))
except:
     print("index not matched")
```
You can perform interpolations, regressions, etc. directly using each table as an element in the computations. For example,

```python
3*df1+df2*df3
```

After you have achieved what you need to do with the numbers, you can then release the multi-index back to the columns using a simple <span class="coding">.reset_index(drop=False)</span> command. 

## Joining on index
If you don't want to write merge on which keys, you can put the keys in the index.  That way, all you have to do is use <span class="coding">.join()</span> in pandas and let it handle the rest. 

## Use list of tuples (multiindex) to filter a dataframe
Sometimes you have a list of idenfiers in the form of a list of tuples,say each has two elements.  The list can always be used as multiinex or obtained from multiindex.  And you have a dataframe df.  You want to get all the rows from df where two columns match the tuples. 

```python
df.merge(pd.DataFrame(tuple_list, columns=['col_1','col_2']))
```
