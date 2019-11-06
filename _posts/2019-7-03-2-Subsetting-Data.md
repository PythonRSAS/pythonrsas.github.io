---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Subsetting Data"
description: Data processing using Python and SAS.
author: Sarah Chen
# image: https://www.audubon.org/sites/default/files/styles/hero_image/public/sfw_nationalgeographic_1517960.jpg?itok=F5pikjxg
---
To be able to subset data masterfully is essential for working with data.  This post is about subsetting multiindexed DataFrame and is partially based from Chapter 4 "IndexIng and groupBy" of my co-authored book (from page 134) [Python for SAS Users](https://www.amazon.com/Python-SAS-Users-SAS-Oriented-Introduction/dp/1484250001/ref=sr_1_3?crid=21NME5C69YGV7&keywords=python+for+sas+users&qid=1572638715&sprefix=python+for+sas+%2Caps%2C196&sr=8-3). 

Recall that multiindex can be seen as array of tuples. For a review of multiindexing, please see my post on Multiindexing, which corresponds to the section starting from page 131 of the book. 

In this post, you will learn how to slice and dice multiindexed DataFrame anyway you wish, by indexing or on condition, however complex, and to make a quick selection:

[Slicing Rows and Columns by Index](#Slicing-Rows-and-Columns)

1. Use <span class='coding'>slice()</span> with the.loc index slicer.  For example, <span class='coding'>.loc[((slice(None), slice(2,3)), slice(None))]</span>
2. Use <span class='coding'>pd.IndexSlice</span> to accomplish the same thing but with simplier syntax. 

[Conditional Slicing](#Conditional-Slicing)
1. Use <span class='coding'>.loc </span> index slicer with boolean mask.
2. Use <span class='coding'>df.where()</span>. 

[Selection via Cross Sections](#Cross-Sections)
Selection with the <span class='coding'>.xs </span> method.

Let's begin.

<h3 id="Slicing-Rows-and-Columns">Slicing Rows and Columns</h3>
First, let's get a multi-indexed dummy dataset, which was similar to the one on page 134.
<div class="code-head"><span>code</span>  Create tickets DataFrame.py</div>
```python
>>> import pandas as pd 
>>> import numpy as np 
>>> np.random.seed(654321)
>>> idx = pd.MultiIndex.from_product([[2017, 2018,2019,2020], [1, 2, 3]], names = ['Year', 'Month']) 
>>> columns=pd.MultiIndex.from_product([['City' , 'Suburbs', 'Rural'],['Day' , 'Night']], names = ['Area', 'When']) 
>>> data =abs(((np.random.randn(12, 6))*100//5).astype(int))
>>> tickets = pd.DataFrame(data, index=idx, columns = columns).sort_index().sort_index(axis=1)
>>> print(tickets)
[Out]:
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2017 1       15    18     9     3       3     3
     2       11    18     3    30      42    15
     3        5    54     7     5      14    18
2018 1       11    17     1     0      11    26
     2        7    23     3     5      19     1
     3        9    17    31    48       2    17
2019 1       21     5    22    10      11     2
     2        5    33    19     2       7    10
     3       31    12    19    17      14     2
2020 1       25    10     8     4      20    15
     2       35    14     9    14      10     1
     3        3    32    33    21      24     6
```
Similarly, we create this data in SAS using a DATA step followed by <span class="code">PROC TABULATE</span>. 

<div class="code-head"><span>code</span>  Tickets Dataset from PROC TABULATE.sas</div>
```sas
DATA TICKETS; 
LENGTH area $ 7 
       when $  9; 
CALL STREAMINIT(123456); 
DO year = 2017, 2018, 2019, 2020; 
  DO month = 1, 2, 3; 
       DO area = 'city', 'rural', 'suburbs'; 
          DO when = 'day', 'night'; 
             tickets = ABS(INT((RAND('NORMAL')*100)/5)); 
             OUTPUT; 
        END; 
       END; 
    END; 
 END;
RUN;

PROC TABULATE;
VAR tickets; 
CLASS area when year month;
TABLE year * month,area=' ' * when=' ' * sum=' ' * tickets=' ';
RUN;
```

Now we are ready to slice the Tickets data. 

* **Problem 1:** Say we wish to return all the data for the 3rd month of every year.

Recall a tuple is an immutable sequence of items enclosed by parenthesis. As a convenience the Python’s built-in <span class='coding'>slice(None)</span> function selects all the content for a level. In this case we want month level 3 for all years.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets.loc[(slice(None), 3), :]
[Out]:
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2017 3        2    26     9    37      17     6
2018 3       29    12    15    15       2    17
2019 3       27    38     7     2      11    26
2020 3       11    12    10    47      27     9
```
The syntax <span class="code">slice(None)</span> is the slicer for the Year column which includes all values for a given level, in this case, 2017 to 2020 followed by 3 to designate the level for month.  All columns are returned since no column slicer was given.

Note:
- It would work the same <span class='coding'>tickets.loc[(slice(None), slice(3,3)), :]</span>
-Error would be raised if we use tickets.loc[(:,3),:] because it is illeagl to use a colon inside a tuple constructor.   

* **Problem 2:**  Now we want data from both months 2 and 3 for all years.

<div class="code-head"><span>code</span> Slice Months 2 and 3 for all Years.py</div>

```python
>>> tickets.loc[(slice(None), slice(2,3)), :]
[Out]:
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2017 2       11    18     3    30      42    15
     3        5    54     7     5      14    18
2018 2        7    23     3     5      19     1
     3        9    17    31    48       2    17
2019 2        5    33    19     2       7    10
     3       31    12    19    17      14     2
2020 2       35    14     9    14      10     1
     3        3    32    33    21      24     6
```
Note: The same results are accomplished with: <span class='coding'>tickets.loc[((slice(None), slice(2,3)), slice(None))]</span>

* **Use <span class='coding'>pd.IndexSlice</span>  to accomplish all the above with simplier syntax:** 

Pandas <span class='coding'>IndexSlice</span> object provides convenient method for slicing multi-indexed DataFrames.  We get exactly the same result as the last example with the following, without having to type "slice" everytime (though we do have to type it once in the "pd.IndexSlice")

<div class="code-head"><span>code</span> Slice Months 2 and 3 for all Years Using IndexSlice.py</div>

```python
>>> tickets.loc[pd.IndexSlice[:, 2:3 ], :]
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2017 2       11    18     3    30      42    15
     3        5    54     7     5      14    18
2018 2        7    23     3     5      19     1
     3        9    17    31    48       2    17
2019 2        5    33    19     2       7    10
     3       31    12    19    17      14     2
2020 2       35    14     9    14      10     1
     3        3    32    33    21      24     6
```

In Problem 2, the column slicer did not slice along the inner level of the <span class="coding">MultiIndex</span> on When. We will get to that in the next example. 

* **Problem 3:**  Retrieve data since 2018 for Month 2 and 3, and only for Area is 'City' for both 'Day' and 'Night' time. 

The example below, Slicing Rows and Slicing Columns, illustrates details for slicing columns.  

<div class="code-head"><span>code</span> Slicing Both Rows and Columns Using IndexSLice.py</div>

```python
>>> idx = pd.IndexSlice
>>> tickets.loc[idx[2018:, 2:3 ], idx['City', 'Day' : 'Night']]
Area       City
When        Day Night
Year Month
2018 2        7    23
     3        9    17
2019 2        5    33
     3       31    12
2020 2       35    14
     3        3    32
```
The row slicer returns levels 2018 for Year on the outer level of the <span class="coding">MultiIndex</span> and 2 and 3 from Month on the inner level.  The column slicer returns the levels City for Area on the outer level of the <span class="coding">MultiIndex</span> and the levels Day and Night on the inner level from When.

<h3 id="Conditional-Slicing">Conditional Slicing</h3>

Often times we need to sub-set based on conditional criteria on the values (as opposed to the index).  The <span class="coding">.loc</span> indexer permits a Boolean mask for slicing based an criteria applied to values in the DataFrame, such as <span class="coding">.isnull()</span>.

We can identify instances where the number of tickets relates to a given threshold by creating a Boolean mask and applying it to the DataFrame using the <span class="coding">.loc</span> indexer.  
* **Problem 4:**  Want to know when the number of tickets issued in the city during the day is greater than 25. 

<div class="code-head"><span>code</span> Conditional Slicing.py</div>

```python
>>> tickets.loc[pd.IndexSlice[tickets[('City' ,'Day' )] > 25], pd.IndexSlice['City', 'Day']]
# or more simplily
>>> tickets.loc[idx[tickets[('City' ,'Day' )] > 25], idx['City', 'Day']]
[Out]:
Year  Month
2019  3        31
2020  2        35
Name: (City, Day), dtype: int32
```
In this example we define the mask object using the column slicing syntax followed by the Boolean operator greater than (>) and 25 as the threshold value.  

Rows are sliced using the conditional with the mask object.  The columns are sliced using the City level from Area and the Day level from When.   Area is the outer level of the column <span class="coding">MultiIndex</span> and When is the inner level.

Another form of conditional slicing uses the Pandas <span class='coding'>where</span> attribute.  The <span class='coding'>where</span> attribute returns a DataFrame the same size as the original whose corresponding values are returned when the condition is True.  When the condition is <span class="coding">False</span>, the default behavior is to return NaN’s.  This feature is illustrated in the following example, DataFrame where Attribute.  

<div class="code-head"><span>code</span> DataFrame where Attribute.py</div>

```python
>>> missing = "XXX"
>>> tickets.where(tickets> 30, other = missing)
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2017 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX   XXX   XXX   XXX      42   XXX
     3      XXX    54   XXX   XXX     XXX   XXX
2018 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX   XXX   XXX   XXX     XXX   XXX
     3      XXX   XXX    31    48     XXX   XXX
2019 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX    33   XXX   XXX     XXX   XXX
     3       31   XXX   XXX   XXX     XXX   XXX
2020 1      XXX   XXX   XXX   XXX     XXX   XXX
     2       35   XXX   XXX   XXX     XXX   XXX
     3      XXX    32    33   XXX     XXX   XXX
```
The <span class='coding'>other =</span> argument assigns an arbitrary value for the False condition.  Also notice how the returned DataFrame is the same shape as the original.
<h3 id="Cross-Sections">Cross Sections</h3>

Pandas DataFrames provision a cross section method called <span class='coding'>xs</span> as another means for returning rows and columns from an indexed DataFrame or partial data in the case of a MultiIndexed DataFrame.  

The compact syntax offered by the <span class='coding'>xs</span> method makes it fairly easy to subset MultiIndexed DataFrames.  The <span class='coding'>xs</span> method is read only. Consider the following example, <span class='coding'>xs</span> Cross Section, Example 1.  

<div class="code-head"><span>code</span> xs Cross Section, Example 1.py</div>

```python
>>> tickets.xs((1), level='Month')
[Out]:
Area City       Rural       Suburbs
When  Day Night   Day Night     Day Night
Year
2017   15    18     9     3       3     3
2018   11    17     1     0      11    26
2019   21     5    22    10      11     2
2020   25    10     8     4      20    15

```
The xs cross section method has two agruments.  The first argument, in this example is level 1 and the second argument <span class="coding">level = 'Month'</span> returning the rows for  month 1 for all years with all columns.  

Recall the Month column is a component of the <span class="coding">MultiIndex</span> to form the row labels. The the xs cross section method works along a column axis illustrated in the example below, xs Cross Section, Example 2.

<div class="code-head"><span>code</span> xs Cross Section, Example 2.py</div>

```python
>> tickets.xs(('City'), level='Area', axis = 1)
When         Day  Night
Year Month
2015 1      15.0   18.0
     2      11.0   18.0
     3       5.0   54.0
2016 1      11.0   17.0
     2       7.0   23.0
     3       9.0   17.0
2017 1      21.0    5.0
     2       5.0   33.0
     3      31.0   12.0
2018 1      25.0   10.0
     2      35.0   14.0
     3       3.0   32.0
```
In this example we return all rows for the level City.  The <span class="coding">axis = 1</span> argument returns just the columns for the level City. 

Because the xs cross section method returns a DataFrame we can apply mathematical and statistical functions as attributes.  In the following example, xs Cross Section, Example 3 returns the sum of all tickets issued during daylight hours in each of the three area.

<div class="code-head"><span>code</span> xs Cross Section, Example 3.py</div>

```python
>>> tickets.xs(('Day'), level='When', axis = 1).sum()
Area
City       178
Rural      164
Suburbs    177
```

The following SAS code performs exactly the same as the above Python code, using <span class='coding'>PROC SQL</span>.   SAS <span class='coding'>PROC SQL</span> is extremely powerful and has a similar syntax as most other flavors of SQL out there. 
<div class="code-head"><span>code</span> Summed Tickets Where Day over Area.sas</div>

```sas
4 PROC SQL;
5 SELECT UNIQUE area
6      , SUM(tickets) AS sum_by_area
7 FROM tickets
8     WHERE WHEN = 'day'
9 GROUP BY area;
10 QUIT;
```
The <span class="coding">WHERE</span> clause selects those rows for when = 'Day'.  The results from the query are displayed in the example, Tickets Issued During Daylight for each Area.

 
The <span class="coding">GROUP BY</span> clause sums the variable ticket into the unique levels for the area variable.  As we will see in the next section, grouping operations are essential for data analysis. 
