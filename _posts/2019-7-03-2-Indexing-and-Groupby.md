---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Indexing and Groupby"
description: Data processing using Python and SAS.
author: Sarah Chen
# image: https://www.audubon.org/sites/default/files/styles/hero_image/public/sfw_nationalgeographic_1517960.jpg?itok=F5pikjxg
---

###Indexing and GroupBy
SAS users tend to think of indexing SAS data sets to either improve query performance or as a method to avoid dataset sorting. Another use case for using SAS indexes is to provide direct access to a specific observation in a dataset. 

For example, in order to retrieve an observation whose value for the variable <span class="coding">Name </span>is ‘Lassiter’, absent an index, SAS performs a sequential read starting with the first observation in the dataset.  SAS normally begins reading at observation one reading the dataset in sequence for <span class="coding">name =</span>‘Lassiter’ until all observations are read.  

Alternatively, if an index on the variable <span class="coding">Name </span>is present, SAS may use the index to directly access those observations containing these values without performing a sequential read of the dataset.  A SAS index stores values in ascending order for a specific variable or variables and manages information on how to locate a given observation(s) in the dataset. 

In contrast, Pandas automatically create an index structure at <span class="coding">DataFrame</span> creation time for both rows and columns.  In Chapter 3, Pandas we encountered the <span class="coding">RangeIndex</span> object used as the default row index.  These index objects are responsible for holding the axis labels and other metadata like integer-based location identifiers, axis name, etc.  

One or more columns in <span class="coding">DataFrame</span> can be used to define an index.  Assigning more than one column as an index creates a <span class="coding">MultiIndex</span> object discussed later in this chapter.  New users to Pandas often get confused about the role of an index, since most of their prior associations consider an index to be an auxiliary structure for columns. 

The way we like to think about a Pandas index is to consider it as a means for labeling <span class="coding">DataFrame</span> rows.  Recall from Chapter 3, Pandas, that at <span class="coding">DataFrame</span> creation time, the <span class="coding">RangeIndex</span> object is created as the default index similar to the automatic <span class="coding">_n_ </span>variable SAS establishes at SAS dataset creation time. 

In a <span class="coding">DataFrame</span>, the values from  a column or columns may be used as an index to supply values as row labels augmenting the default integer values assigned by the <span class="coding">RangeIndex</span> object.  Just as you are able to return SAS dataset observations using the automatic variable <span class="coding">_n_</span>, a DataFrame’s default <span class="coding">RangeIndex</span> is used to return rows using a zero-based offset.  By explicitly setting a <span class="coding">DataFrame</span> index from  column or multiple column values, you can return rows using these column values in addition to returning rows using the <span class="coding">RangeIndex</span> object. 

### Create Index
When a <span class="coding">DataFrame</span> is assigned an index, the rows remain accessible by supplying a collection of integer values as well as accessible by the row labels defined by the index. 

In the following example, Create <span class="coding">DataFrame</span> Index illustrates the <span class="coding">set_index</span> method using the <span class="coding">_N_</span> column.  In this example, the values from the <span class="coding">ID</span> column supply labels for the <span class="coding">DataFrame</span> rows.

<div class="code-head"><span>code</span Create DataFrame Index.py</div>

```python
<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> import pandas as pd
>>> df = pd.DataFrame([['0071', 'Patton'  , 17,  27],
...                    ['1001', 'Joyner'  , 13,  22],
...                    ['0091', 'Williams', 111, 121],
...                    ['0110', 'Jurat'   , 51,  55]],
...          columns = ['ID',   'Name', 'Before', 'After'])
>>> print(df)
     ID      Name  Before  After
0  0071    Patton      17     27
1  1001    Joyner      13     22
2  0091  Williams     111    121
3  0110     Jurat      51     55
>>> df.set_index('ID', inplace=True)
>>> print(df)
          Name  Before  After
ID
0071    Patton      17     27
1001    Joyner      13     22
0091  Williams     111    121
0110     Jurat      51     55
```
The <span class="coding">DataFrame</span> df is constructed using the <span class="coding">DataFrame</span> constructor method.  The first <span class="coding">print</span> function returns all of the rows labeled with the default <span class="coding">RangeIndex</span> object labeling rows starting with the integer 0 to length (axis – 1).  The syntax:

df.set_index('ID', inplace = True)
selects the <span class="coding">ID</span> column as the index and inplace = True updates the index in place rather than creating a new <span class="coding">DataFrame</span>. The default value for the <span class="coding">set_index</span> method is inplace = False.   In the case where the <span class="coding">inplace=</span>argument is <span class="coding">False</span>, you must assign the results to a new <span class="coding">DataFrame</span>.  For example,

df_idx = df.set_index('ID', inplace=False)
creates the df_idx <span class="coding">DataFrame</span> with the <span class="coding">ID</span> column as its index.  The original df <span class="coding">DataFrame</span> remains unaltered.

The second <span class="coding">print</span> function illustrates how the <span class="coding">DataFrame</span> rows are labeled with values from the <span class="coding">ID</span> column.  The overhead for creating and dropping indexes is minimal and it is not unusual to do so repetitively in a single Python program.

Next, we consider sub-setting <span class="coding">DataFrame</span>s.  Sub-setting data by rows and/or columns is an essential task for any form of data analysis.  Panda <span class="coding">DataFrame</span>s offers three choice for sub-setting operations.  They are:

1.  [  ] operator enables selection by columns or by rows.

2.  <span class="coding">.loc</span> indexer uses row and column labels for sub-setting.  A column label is the column <span class="coding">Name </span>and row labels are assigned with an index (either with the <span class="coding">index=</span> parameter at <span class="coding">DataFrame</span> creation time or with the df.<span class="coding">set_index</span> method.  
  
If no index is explicitly assigned, then the integer-based <span class="coding">RangeIndex</span> object is the default.  If no names are assigned to columns, then the <span class="coding">RangeIndex</span> object labels the columns with the first column as 0, the second column as 1, and so on.

3.  <span class="coding">.iloc</span> indexer uses integer positions (from 0 to length-1 of the axis) for sub-setting rows and columns.  This method remains available even if a user-defined index or <span class="coding">MultiIndex</span> is defined.  MultiIndexes, or hierarchical indexes are discussed later in this chapter.

Both the <span class="coding">.loc</span> and <span class="coding">.iloc</span> indexers accept Boolean logic to perform complex sub-setting.  The [ ] operator and the <span class="coding">.iloc</span> indexers can access rows using the default <span class="coding">RangeIndex</span> object, that is, integer values indicating a position along the index.  The <span class="coding">.loc</span> indexer requires a user-defined index for creating row labels in order to operate.
All three indexers return a <span class="coding">DataFrame</span>.


### Return Columns by Position
Consider the example below, <span class="coding">DataFrame</span> Default Indexes. This example constructs the i <span class="coding">DataFrame</span> using a single <span class="coding">print</span> function to display the <span class="coding">DataFrame</span> values, default row index and the default column index. The <span class="coding">‘\n’</span>  syntax inserts a new line to display the desired results.

<div class="code-head"><span>code</span> DataFrame Default Indexes.py</div>

```python
>>> i = pd.DataFrame([['Patton'   , 17,  27],
...                   ['Joyner'   , 13,  22],
...                   ['Williams' , 111, 121],
...                   ['Jurat'    , 51,  55],
...                   ['Aden'     , 71,  70]])
>>> print(i)
          0    1    2
0    Patton   17   27
1    Joyner   13   22
2  Williams  111  121
3     Jurat   51   55
4      Aden   71   70
>>>
>>> print(' Row Index:   ',    i.index, '\n', 'Column Index:', i.columns)
 Row Index:    RangeIndex(start=0, stop=5, step=1)
 Column Index: RangeIndex(start=0, stop=3, step=1)
```
We begin with sub-setting using the [  ] operator. Observe that both columns and rows in <span class="coding">DataFrame</span> i use the default <span class="coding">RangeIndex</span> as their labels.  

The default <span class="coding">RangeIndex</span> is used to select rows or columns using integers to locate their positions along the index.  Consider in the following examples, <span class="coding">DataFrame</span> Returns Column 0. 

<div class="code-head"><span>code</span> DataFrame Return Column or Row.py</div>

```python
>>> i[0]
0      Patton
1      Joyner
2    Williams
3       Jurat
4        Aden
```
The call to [ ] operator returns the first column (0) from the <span class="coding">DataFrame</span> i.  In most cases, <span class="coding">DataFrame</span> columns will have labels to return the columns of interest.

The [ ] operator also accepts a Python list of columns to return.  Recall that a Python list is a mutable data structure for holding a collection of items.   List literals are written within square brackets [ ] with commas (,) to indicate multiple items in the list.  

Consider the example below, Create df <span class="coding">DataFrame</span>.  Each of the values supplied to the <span class="coding">DataFrame</span> constructor method is a Python list as is the <span class="coding">columns= </span> argument.

<div class="code-head"><span>code</span> Create DataFrame df.py</div>

```python
>>> df = pd.DataFrame([['I','North', 'Patton', 17, 27],
...                    ['I', 'South','Joyner', 13, 22],
...                    ['I', 'East', 'Williams', 111, 121],
...                    ['I', 'West', 'Jurat', 51, 55],
...                    ['II','North', 'Aden', 71, 70],
...                    ['II', 'South', 'Tanner', 113, 122],
...                    ['II', 'East', 'Jenkins', 99, 99],
...                    ['II', 'West', 'Milner', 15, 65],
...                    ['III','North', 'Chang', 69, 101],
...                    ['III', 'South','Gupta', 11, 22],
...                    ['III', 'East', 'Haskins', 45, 41],
...                    ['III', 'West', 'LeMay', 35, 69],
...                    ['III', 'West', 'LeMay', 35, 69]],
...                    columns=['District', 'Sector', 'Name', 'Before', 'After'])
>>>
>>> df[['Name', 'After']].head(4)
       Name  After
0    Patton     27
1    Joyner     22
2  Williams    121
3     Jurat     55
```
In this example the syntax:
df[['Name', 'After']].head(4)
is a column sub-setting operation returning the columns <span class="coding">Name </span>and After.  

Notice how the Python list with <span class="coding">[' Name', 'After'] </span>inside the <span class="coding">DataFrame</span> slice operator results in a pair of square brackets [[ ]]. The outer pair is the syntax for the <span class="coding">DataFrame</span> [ ] operator while the inner pair hold the literal values to form the Python list of column names.

Clearly, using a list of column names rather than a list of column integer index positions is a more convenient method for sub-setting. The equivalent SAS program is displayed in the following example, Create df SAS dataset.  It is used in subsequent examples in this chapter.

<div class="code-head"><span>code</span> Create df SAS dataset.sas</div>

```sas
4 data df;
5 length region $ 6
6        name $ 8
7        district $ 3;
8 infile cards dlm=',';
8 input district $
10       region $
11       name $
12       before
13       after;
14 list;
15 datalines;

RULE:      ----+----1----+----2----+----3----+----4----+----5
16        I,   North, Patton,   17,  27
17        I,   South, Joyner,   13,  22
18        I,   East,  Williams, 111, 121
19        I,   West,  Jurat,    51,  55
20        II,  North, Aden,     71,  70
21        II,  South, Tanner,   113, 122
22        II,  East,  Jenkins,  99,  99
23        II,  West,  Milner,   15,  65
24        III, North, Chang,    69,  101
25        III, South, Gupta,    11,  22
26        III, East,  Haskins,  45,  41
27        III, West,  LeMay,    35,  69
28        III, West,  LeMay,    35,  69
NOTE: The data set WORK.DF has 13 observations and 5 variables.

29 ;;;;
30 proc print data = df(obs=4);
31    var name after;
32 run;
```

NOTE: There were 4 observations read from the data set WORK.DF
The output from PROC PRINT with data=df(obs=4) is displayed in Figure 4-1, Display SAS Dataset df Output.
 
Figure 4-1. Display SAS df Dataset Output

### Return Rows by Position
The general syntax for <span class="coding">DataFrame</span> row slicing (sub-setting rows) using the [ ] operator is:
df:[start : stop : step]

The start position is included in the output and the stop position is not included in the output. 
For example, consider the following example, <span class="coding">DataFrame</span> Row Slicing, Example 1.

<div class="code-head"><span>code</span> DataFrame Row Slicing, Example 1.py</div>

```python
>>> df[:3]
  District Sector      Name  Before  After
0        I  North    Patton      17     27
1        I  South    Joyner      13     22
2        I   East  Williams     111    121
```
This example returns the first three row from the df <span class="coding">DataFrame</span>.  A null value for the start position defaults to start position zero (0).  The value following the colon <span class="coding">:</span>indicates the stop position and goes up to but does not include the row in the slicing operation.  

In the following example below, <span class="coding">DataFrame</span> Row Slicing, Example 2, illustrates returning every other row from the df <span class="coding">DataFrame</span>.

<div class="code-head"><span>code</span> DataFrame Row Slicing, Example 2.py</div>

```python
>>> df[::2]
   District Sector      Name  Before  After
0         I  North    Patton      17     27
2         I   East  Williams     111    121
4        II  North      Aden      71     70
6        II   East   Jenkins      99     99
8       III  North     Chang      69    101
10      III   East   Haskins      45     41
12      III   West     LeMay      35     69
```
The start and stop positions are null causing the slice df[::2] to  default to the first and last row respectively in the <span class="coding">DataFrame</span>.  The value of two (2) for the step position returns every other row.
This same logic is displayed in the example below, <span class="coding">SELECT</span> Every Other Row.

<div class="code-head"><span>code</span> SELECT Every Other Row.py</div>

```sas
4 data df1;
5    set df;
6    if mod(_n_, 2) ^= 0 then output;
7 run;
```
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.DF1 has 7 observations and 5 variables.


The example creates the df1 dataset with a sub-setting IF statement to perform modulo division by 2 on the automatic SAS <span class="coding">_n_ </span>variable assigned to each observation. 

Modulo division by 2 on even integers returns 0 (zero).  By using the IF statement’s inequality evaluation of <span class="coding">^= 0</span> every odd <span class="coding">_n_ </span> value (1, 3, 5, etc.) evaluates true and is written to the output <span class="coding">df1</span> dataset.

### Return Rows and Columns by Label
The <span class="coding">.loc</span> indexer is a method primarily used for returning rows and columns using labels. Allowed inputs to <span class="coding">.loc</span> are:
• A single label such as 12 or ‘Name’.  Note that 12 is interpreted as the row label and not as the integer location along the index.

• A Python list of labels [‘A’, ‘B’, ‘C’]

• A slice object with labels ‘a’ : ‘z’.  Both the start, in this case ‘a’, and the stop, ‘z’ is included when present in the index.

• Conditional evaluations 
Each of these methods are illustrated.
Up to this point, the index for the df <span class="coding">DataFrame</span> relies on the default <span class="coding">RangeIndex</span> object for returning rows by an integer position along the index.  In order to retrieve rows from the df <span class="coding">DataFrame</span> by labels the <span class="coding">Name </span>column is set as the <span class="coding">DataFrame</span> index.  

This action assigns the values from the <span class="coding">Name </span>column as labels for the <span class="coding">DataFrame</span> rows.  Said another way, a <span class="coding">DataFrame</span> index maps columns values onto rows as labels.   
The syntax and default values for the <span class="coding">set_index</span> method is:
df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) 

In the folowing example, Add Index to <span class="coding">DataFrame</span>, illustrates defining an index for an existing <span class="coding">DataFrame</span>.

<div class="code-head"><span>code</span> Add Index to DataFrame.py</div>

```python
>>> print(df)
   District Sector      Name  Before  After
0         I  North    Patton      17     27
1         I  South    Joyner      13     22
2         I   East  Williams     111    121
3         I   West     Jurat      51     55
4        II  North      Aden      71     70
5        II  South    Tanner     113    122
6        II   East   Jenkins      99     99
7        II   West    Milner      15     65
8       III  North     Chang      69    101
9       III  South     Gupta      11     22
10      III   East   Haskins      45     41
11      III   West     LeMay      35     69
12      III   West     LeMay      35     69
>>> print(df.index)
RangeIndex(start=0, stop=13, step=1)
>>>
>>> df.set_index('Name', inplace = True, drop = True)
>>> print(df.head(4))
         District Sector  Before  After
Name
Patton          I  North      17     27
Joyner          I  South      13     22
Williams        I   East     111    121
Jurat           I   West      51     55
>>> print(df.index)
Index(['Patton', 'Joyner', 'Williams', 'Jurat', 'Aden', 'Tanner', 'Jenkins','Milner', 'Chang', 'Gupta', 'Haskins', 'LeMay', 'LeMay'],
dtype='object', name='Name')
```
In this example, the first <span class="coding">print</span> function displays all rows from the df <span class="coding">DataFrame</span>.  The syntax: print(df.index) returns the default <span class="coding">RangeIndex</span> in use for the rows with integer values between 0 and 13.  The syntax: df.set_index('Name', inplace=True, drop=True) selects the values from the <span class="coding">Name </span>column label as row labels.  

The argument inplace=True updates the df <span class="coding">DataFrame</span> in place and the drop=True argument drops the <span class="coding">Name </span>column for the <span class="coding">DataFrame</span>.

With this defined index, the <span class="coding">.loc</span> indexer uses the <span class="coding">Name </span>column values to return rows rather than using row position.

Notice how the third <span class="coding">print</span>() function displays the values for the <span class="coding">Name </span>column as row labels in the left-most column of the output.  The syntax: print(df.index) returns the index values as a Python list.  

An index may have non-unique values which we illustrate with this example.  Some <span class="coding">DataFrame</span> operations require the index keys be in sorted order while others may require unique values.  

We cover the details for sorting in Chapter 5, Pandas Data Management.  Chapter 9, Time Series Analysis covers details for unique index values.
With an index in place as row labels we can slice rows using the <span class="coding">.loc</span> indexer.  As well, columns can be sliced with the <span class="coding">.loc</span> indexer since they have labels (i.e. names). 

The syntax for the <span class="coding">.loc</span> indexer is:
```python
df.loc[row selection, column selection]
```
The row selection is listed first, separated by a comma <span class="coding">,</span> followed by the column selection. For both the row or column selection a colon <span class="coding">:</span> is used to request a range of items.  

<div class="code-head"><span>code</span>Return Row Slices.py</div>

```python
>>> df.loc['Patton': 'Aden', ]
         District Sector  Before  After
Name
Patton          I  North      17     27
Joyner          I  South      13     22
Williams        I   East     111    121
Jurat           I   West      51     55
Aden           II  North      71     70
```
This example slices rows beginning with the row labeled Patton and ending with the row labeled Aden inclusive.  The empty value for the column selector, following the comma (,) implies all columns.  

The same <span class="coding">DataFrame</span> can be returned by stating the column selector explicitly with the syntax: df.loc['Patton' : 'Aden', 'District' : 'After']

The following example, Return Row and Column Slices, illustrates supplying a single label to the row selector followed by a Python list of labels as the column selector.

<div class="code-head"><span>code</span> Return Row and Column Slices.py</div>

```python
>>> df.loc['LeMay', ['Before','After']]
       Before  After
Name
LeMay      35     69
LeMay      35     69
```
Notice how the row labels are not unique.

#### Conditionals
In the example below, Return Rows Conditionally, illustrates returning rows and columns based on a Boolean comparison. 

<div class="code-head"><span>code</span>Return Rows Conditionally.py</div>

```python
>>> df.loc[(df['Sector'] == 'West') & (df['Before'] > 20)]
      District Sector  Before  After
Name
Jurat        I   West      51     55
LeMay      III   West      35     69
LeMay      III   West      35     69
```

The Boolean comparisons are enclosed with parentheses ( ) and utilize any of the Comparision operators listed on Table 2.2,  Python Comparison Operations from Chapter 2.  

In this example the Boolean comparisons contain two predicates; the first is (df['Sector'] == 'West') and the second is (df['Before'] > 20). The Boolean operator & (and) joins the predicates and therefore both must return True in order to meet the row selection criteria.

Note the sytax differences between Listing 4-11, Return Row and Column Slices and 4.12, Return Rows Conditionally.  In the former rows are sliced based on labels.  The latter uses the df['Sector'] and df['Before'] to designate column names for the conditional expression.

Suppose we wish to sub-set rows based on the last letter of the value for the <span class="coding">Name </span>column ending with the letter ‘r’.  In the following example, Conditionally Return Rows with String Manipulation combines the <span class="coding">.loc</span>() indexer with the .str.endswith attribute to satisfy the request.

<div class="code-head"><span>code</span> Conditionally Return Rows with String Manipulation.py</div>

```python
df.loc[df['Name'].str.endswith("r"), ['District', 'Sector']]
KeyError: 'the label [Name] is not in the [index]'
```
Unfortunately, this example raises a KeyError since the column <span class="coding">Name </span>was dropped when the df.index was initially created in the following example, Add Index to <span class="coding">DataFrame</span>. 

Note this error message is truncated here.  One remedy for the KeyError  is to ‘return’ the <span class="coding">Name </span>column using the .reset_index function illustrated in the example below, Drop <span class="coding">DataFrame</span> Index.

<div class="code-head"><span>code</span> Drop DataFrame Index.py</div>

```python
>>> df.reset_index(inplace = True)
>>> df.loc[df['Name'].str.endswith("r"), ['Name', 'Before', 'After']]
     Name Before  After
1  Joyner      13     22
5  Tanner     113    122
7  Milner      15     65 
```
In this example the syntax:
df.reset_index(inplace = True)
calls the .reset_index method to ‘drop’ the index and return the <span class="coding">Name </span>column as one of the columns on the df <span class="coding">DataFrame</span>.  

The <span class="coding">inplace = true</span> argument performs the operation in-place. The second line in the program chains the .str.endswith("r") attribute to the <span class="coding">Name </span>column and returns True for any value whose last letter in the sequence is ‘r’. 

The purpose of this example is to simply illustrate resetting an index with the reset_index method.  The more Pythonic remedy for the KeyError illustrated in the example below is: df.loc[df.index.str.endswith('r'), ['District', 'Sector']]The analog SAS program is shown in the following example, Conditionally Return Observations with String Manipulation.

<div class="code-head"><span>code</span> Conditionally Return Observations with String Manipulation.py</div>

```python
4  proc sql;
5    select name
6           ,before
7           ,after
8    from df
9    where substr(reverse(trim(name)),1,1) = 'r';
10 quit;
```
The nested functions in the WHERE clause work from the inside out by:
1. Calling the TRIM function to remove trailing blanks 
2. Calling the REVERSE function to reverse the letters in the variable name
3. Calling the SUBSTR (left of =) function to test if the first letter is ‘r’
Figure 4-3, Last Name Ends with ‘r’, displays the output from <span class="coding">PROC SQL</span>.
 
Figure 4-3. Last Name Ends with ‘r’
Another method for conditional testing is to combine the <span class="coding">.loc</span> indexer with the isin attribute.  The isin attribute returns a Boolean indicating if elements in the <span class="coding">DataFrame</span> column are contained in a Python list of values.

<div class="code-head"><span>code</span> Select Rows with isin List of Values.py</div>

```python
>>> df.set_index('Name', inplace=True)
>>> df.loc[df['Sector'].isin(['North', 'South'])]
       District Sector  Before  After
Name
Patton        I  North      17     27
Joyner        I  South      13     22
Aden         II  North      71     70
Tanner       II  South     113    122
Chang       III  North      69    101
Gupta       III  South      11     22
```
Because the index was ‘dropped’ in Listing 4-14 Drop <span class="coding">DataFrame</span> Index, the index is set again, this time with the syntax:
df.set_index('Name', inplace=True) to enable slicing with labels using the <span class="coding">.loc</span> indexer.

In the following example, SAS IN Operator illustrates the same capability using the IN operator. The IN operator performs an implied truth test by including values from a list that match values from the sector variable. The IN operator is also valid with an <span class="coding">IF</span>  statement in a Data Step.   

<div class="code-head"><span>code</span> SAS IN Operator.py</div>

```sas
4 proc sql;
5   select *
6   from df
7 where sector in ('North', 'South');
8 quit;
```
 
Figure 4-4. IN Operator Results
#### Updating
The .loc indexer can update or set values (the term used with Pandas documentation).  Consider the example below, Set Values Matching a List of Labels.

<div class="code-head"><span>code</span> Set Values Matching a List of Labels.py</div>

```python
>>> df.loc[['Patton', 'Jurat', 'Gupta'], 'After']
Name
Patton    27
Jurat     55
Gupta     22
Name: After, dtype: int64
>>> df.loc[['Patton', 'Jurat', 'Gupta'], ['After']] = 100
>>> df.loc[['Patton', 'Jurat', 'Gupta'], 'After']
Name
Patton    100
Jurat     100
Gupta     100
Name: After dtype: int64
```
The first call to the <span class="coding">.loc</span> indexer supplies a Python List of <span class="coding">Name </span>labels for three individuals along with their corresponding After values and returns a Series.  

Recall that a Series is analogous to a single <span class="coding">DataFrame</span> column.  The second call to the <span class="coding">.loc</span> indexer sets (updates) the After column for each of the labels in the Python list:
```python
 ['Patton', 'Jurat', 'Gupta']
```
The SAS analog is illustatred in the example below, IN Operator Conditionally Select Rows.  

<div class="code-head"><span>code</span> IN Operator Conditionally Select Rows.py</div>

```python
4  data df;
5      set df;
6  if _n_ = 1 then put
7     'Name     After';
8  if name in ('Patton', 'Jurat', 'Gupta') then do;
9     after = 100;
10     put @1 name @10 after;
11     end;
12  run;
```
OUTPUT:

Name     After
Patton   100
Jurat    100
Gupta    100

NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.DF has 13 observations and 5 variables.

This example uses the IN operator with an IF/THEN DO/END block updating the after variable conditionally.

Setting values for an entire <span class="coding">DataFrame</span> column is illustated in the following example, Set Values for a Column.

<div class="code-head"><span>code</span>Set Values for a Column.py</div>

```python
>>> df.loc[: , 'After'] = 100
>>> print(df.head(5))
         District Sector  Before  After
Name
Patton          I  North      17    100
Joyner          I  South      13    100
Williams        I   East     111    100
Jurat           I   West      51    100
Aden           II  North      71    100
```

The call to the <span class="coding">.loc</span> indexer slices all rows from the df <span class="coding">DataFrame</span> since no start and stop values are supplied indicated by a colon (:).  The column slice After is set to 100.
### Return Rows and Columns by Position
The <span class="coding">.iloc</span> indexer uses integer positions (from 0 to length-1 of the axis) for slicing rows and columns.  Allowed inputs to <span class="coding">.iloc</span> are:
• An integer, e.g. 12

• A Python list of integers [4, 2, 22]

• A slice object with integers 2 : 22.  The start, in this case 2 is inclusive and the stop position 22 is exclusive.

The stop position for the <span class="coding">.iloc</span> indexer is exclusive, meaning not included.  This is  in contrast to the <span class="coding">.loc</span> indexer which is inclusive.
The syntax for the <span class="coding">.iloc</span> indexer is:
df.iloc[row selection, column selection]

A comma (,) is used to separate the request of row slices from column slices. A colon (:) is used to request a range of items.  The absence of either a column or row selector is an implicit request for all columns or rows, respectively.

These features are illustrated below.  Listing 4-21, Return df First and Last Row, return the introduces the <span class="coding">.iloc</span> indexer.
Listing 4-21. Return df First and Last Row

<div class="code-head"><span>code</span> Return df First and Last Row
.py</div>

```python
>>> df.iloc[[0, -1]]
       District Sector    Name  Before  After
Name
Patton        I  North  Patton      17    100
LeMay       III   West   LeMay      35     69
```

In this example a Python list of row values based on their position is passed to the <span class="coding">.iloc</span> indexer.  Row 0 is the first row and row -1 is the last row in the df <span class="coding">DataFrame</span>.

The same logic for SAS is illustrated in Listing 4-22, Return First and Last Observation.
Listing 4-22. Return First and Last Observation

<div class="code-head"><span>code</span> Return First and Last Observation.py</div>

```sas
4  data df1;
5    set df end = last;
6
7  if name in ('Patton', 'Jurat', 'Gupta') then after = 100;
8  if _n_  = 1 then output;
9  if last = 1 then output;
10 run;

NOTE: There were 12 observations read from the data set WORK.DF.
NOTE: The data set WORK.DF1 has 2 observations and 5 variables.

11 proc print data = df1 noobs;  
12 run;
```
The input dataset df uses the end = dataset option to detect the last observation reading the df dataset.  The end = dataset option initializes a variable’s value to 0 and is set to 1 when the last observation is read.  

Sub-setting IF statements are used to output the first and last observation to the output dataset df1.  The output dataset is displayed in Figure 4-5, First and Last Observation.  The noobs option for PROC PRINT supresses the display of the SAS observation number contained in the automatic SAS variable <span class="coding">_n_</span>.

Figure 4-5. First and Last Observation
The <span class="coding">.iloc</span> indexer accomodates a Python list of integers as well as a slice object to define row and column selections.  Listing 4-23 <span class="coding">.iloc</span> Using List and Slice Object, illustrates combining these selectors.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df.reset_index(inplace = True)
>>> df.iloc[[2, 10, 12], :2]
        Name District
2   Williams        I
10   Haskins      III
12     LeMay      III
```
While it is possible to call the <span class="coding">.iloc</span> indexer with an index preset, in order to understand the effect, the <span class="coding">Name </span>index is dropped with: df.reset_index(inplace = True)

The row selector uses a Python list of integers selecting rows 2, 10, and 12 followed by a comma (,) to define the column slicer. The column slicer 0:2 selects two columns (column 0 and column 1).  Remember, for the <span class="coding">.iloc</span> indexer, the stop values used as slicers for row and column values goes up to but does not include the stop value.  

The syntax for selecting the first three columns and all rows in the <span class="coding">DataFrame</span> is:
df.iloc[ : , :3]

If the column slicer stop position exceeds the number of columns in the <span class="coding">DataFrame</span> then all columns are returned.  

The <span class="coding">.iloc</span> indexer accepts the value -1 value to indicate the last object in a sequence, -2 as second to last, and so on.  Listing 4-24 Return Last Row From Last Column illustrates this feature.
Listing 4-24. Return Last Row From Last Column

<div class="code-head"><span>code</span> Return Last Row From Last Column.py</div>

```python
>>> df.iloc[-1, -1]
100
```

This example returns the last row from the last column in <span class="coding">DataFrame</span> df.

### MultiIndexing
Thus far, the use of indexes involves a single column labeling <span class="coding">DataFrame</span> rows. See Listing 4-9, Add Index to <span class="coding">DataFrame</span> as an illustration.  

This section introduces MultiIndexing, also known as hierarchical indexing.  Often the data for analysis is captured at the detail level. As part of performing an exploratory analysis, a <span class="coding">MultiIndex</span> <span class="coding">DataFrame</span> provides a useful multi-dimensional ‘view’ of data.   

These actions are accomplished using the Panda’s <span class="coding">MultiIndex</span> object.  Simply put, a <span class="coding">MultiIndex</span> allow multiple index levels within a single index. Higher dimensional data can be represented by a one-dimensional Series or a two-dimensional <span class="coding">DataFrame</span>.  

In a <span class="coding">DataFrame</span>, rows and columns may have multiple levels of indices defined with a <span class="coding">MultiIndex</span> object.

Later in this chapter we will see the benefits from MutliIndexing for ‘pivoting’ <span class="coding">DataFrame</span>s much the same way an Excel spreadsheet can be pivoted.  We will also discuss ‘stacking’ data as a means for ‘flattening’ <span class="coding">DataFrame</span>s and ‘unstacking’ to perform the reverse operation.

To begin, consider Listing 4-25 <span class="coding">MultiIndex</span> Details, Part 1.  The example creates a hierarchical index for the columns in the df <span class="coding">DataFrame</span>.
Listing 4-25. MultiIndex Details, Part 1

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> import pandas as pd
>>> import numpy as np
>>> pd.options.display.float_format = '{:,.2f}'.format
>>> cols = pd.MultiIndex.from_tuples([ (x,y) for x in ['Test1','Test2','Test3'] for y in ['Pre','Post']])
>>>
>>> nl = '\n'
>>> np.random.seed(98765)
>>> df = pd.DataFrame(np.random.randn(2,6),index = ['Row 1','Row 2'],columns = cols)
>>>
>>> print(nl,
...       df)

       Test1      Test2       Test3
        Pre Post   Pre  Post   Pre  Post
Row 1 -0.65 0.85  1.08 -1.79  0.94 -0.76
Row 2  0.72 1.02  0.97 -0.04 -0.07  0.81
```

To control the ouput, pd.options.display.float_format displays floats two places to the right of the decimal.  There are several different constructors for defining a <span class="coding">MultiIndex</span>.  This example uses pd.MultiIndex.from_tuples to define a hierarchical index for the <span class="coding">DataFrame</span> columns.  

A Python tuple is a data structure similar to a list used to hold unlike items such as strings, ints, floats, etc. Unlike a list, tuples are immutable and are defined using a pair of parentheses ( ).   In this example the for loops are short-cuts creating the strings to populate the tuples.  Without the for loops the syntax is:

pd.MultiIndex.from_tuples([('Test1', 'Pre'), ('Test1', 'Post'), ('Test2', 'Pre'), ('Test2', 'Post'),
         ('Test3', 'Pre'), ('Test3', 'Post')])

The df <span class="coding">DataFrame</span> in this example uses the <span class="coding">DataFrame</span> constructor assigning row labels with index=['Row 1','Row 2'] and columns = col creating the <span class="coding">MultiIndex</span>ed or hierarchical columns.  

With the df <span class="coding">DataFrame</span> constructed along with its hierarchical columns and row labels, let’s examine the constituent components closely by considering Listing 4-26, Multi-Indexed Details, Part 2.
Listing 4-26. MultiIndex Details, Part 2

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> print(nl,
...       'Index:      '  , df.index,
...   nl              ,
...       'Columns:    '  , df.columns,
...   nl              ,
...       'Col Level 1:'  , df.columns.levels[0],
...   nl              ,
...       'Col Level 2:'  , df.columns.levels[1])

 Index:       Index(['Row 1', 'Row 2'], dtype='object')
 Columns:     MultiIndex(levels=[['Test1', 'Test2', 'Test3'], ['Post', 'Pre']],
           codes=[[0, 0, 1, 1, 2, 2], [1, 0, 1, 0, 1, 0]])
 Col Level 1: Index(['Test1', 'Test2', 'Test3'], dtype='object')
 Col Level 2: Index(['Post', 'Pre'], dtype='object')


```
Begin with the index.  Recall  a Pandas index is  simply a method to assign labels to rows.  In this example the statement df.index returns the row labels, 'Row1' and 'Row2'.

The statement df.columns returns the <span class="coding">DataFrame</span> column labels. In this case, a Python list of lists which are the unique levels from the <span class="coding">MultiIndex</span> assigned as columns.  The labels return a Python list of lists referencing these levels on the index.

This df <span class="coding">DataFrame</span> <span class="coding">MultiIndex</span> has two levels.  The statement: df.columns.levels[0] returns a Python list of column lables used in the outer-most level of the hierarchical index.  The statement df.columns.levels[1] returns the inner-most level of the hierarchical index.  Whether assigned to the <span class="coding">DataFrame</span> rows or columns,  a hierarchical index can have a arbitrary number of levels.

To further understand MultiIndexes we construct a more elaborate <span class="coding">DataFrame</span>. Listing 4-27, Create tickets <span class="coding">DataFrame</span>, illustrates a hierarchical index for both the <span class="coding">DataFrame</span>’s rows and columns.  

The <span class="coding">MultiIndex</span> for the columns has a depth of two with values for Area and When as levels.  The second hierarchical index on the rows has a depth of two with Year and Month values as levels. The tickets  <span class="coding">DataFrame</span> holds values for traffic-violation tickets.

Since our objective is to understand hierarchical indexes, the explanation for the Python code creating the tickets <span class="coding">DataFrame</span> is found in Appendix A, Generating the Tickets <span class="coding">DataFrame</span> at the end of this chapter.  Note, the script in Appendix A must be executed as a part of the examples in this section.

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> import pandas as pd
>>> import numpy as np
>>> np.random.seed(654321)
>>> idx = pd.MultiIndex.from_product([[2015, 2016, 2017, 2018],
...                          [1, 2, 3]],
...                  names = ['Year', 'Month'])
>>> columns=pd.MultiIndex.from_product([['City' , 'Suburbs', 'Rural'],
...                          ['Day' , 'Night']],
...                  names = ['Area', 'When'])
>>>
>>> data = np.round(np.random.randn(12, 6),2)
>>> data = abs(np.floor_divide(data[:] * 100, 5))
>>>
>>> tickets = pd.DataFrame(data, index=idx, columns = columns).sort_index().sort_index(axis=1)
>>> print(tickets)
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
Notice the output from the <span class="coding">print</span> function in Listing 4-27, Create Tickets <span class="coding">DataFrame</span>. The results display the hierarchical columns Area as the outer level and When as the inner level.  Likewise, with the hierarchical row index, where Year is the outer level and Month is the inner level.

The <span class="coding">print</span>(tickets.index) statement returns the <span class="coding">MultiIndex</span> levels and labels assigned to the rows.  To  sub-set <span class="coding">DataFrame</span> rows we refer to: [2015, 2016, 2017, 2018] as the outer level of the <span class="coding">MultiIndex</span> to indicate Year and:
[1, 2, 3] as the inner level of the <span class="coding">MultiIndex</span> to indicate Month to compose the row slices.

Similarly, to sub-set columns, we refer to:

 ['City', 'Rural', 'Suburbs']

as the outer levels of the of the <span class="coding">MultiIndex</span> to indicate Area and:

['Day', 'Night']

as the inner portion of the <span class="coding">MultiIndex</span> to indicate When for the column slices.

Together, row and column slices determine the <span class="coding">DataFrame</span> subset.

In the following example, Tickets Dataset from PROC TABULATE produces the analog tickets SAS dataset using PROC TABULATE to render output shaped like the tickets <span class="coding">DataFrame</span>.  

Since the Python code and SAS code call different random number generators the values created, while similar, differ between the <span class="coding">DataFrame</span> and the SAS dataset.

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
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
The Data Step uses nested DO/END blocks generating the class variables area, when, year, and  month.  The tickets variable is created with nested functions working from the inside out:

1.  The RAND function draws values from the normal distribution random number generator.  These values are then multiplied by 100 and the product is divided by 5.

2.  The INT function returns the integer portion of the value

3.  The ABS function returns the absolute value

Figure 4-6, PROC TABULATE OUTPUT, illustrates the TABLE statement syntax:

table year * month ,
      area=' ' * when=' ' * sum=' ' * tickets=' ';

that constructs this particular output.

The row dimension crosses (*) the month variable with the year variable.  The column dimension crosses (*) values for tickets with the area variable which in turn is crossed (*) with the when variable and together they are crossed with the summed value for the tickets variable.
 
#### Basic Sub-sets with MultiIndexes
With the tickets <span class="coding">DataFrame</span> created having hierarchical indexes for rows and columns, we can apply a range of methods for sub setting as well as applying condition-based logic as filtering criteria.

An important feature of hierarchical indexing is the ability to select data by a “partial” label identifying a subgroup in the data. Partial selection “drops” levels of the hierarchical index from the results using methods analogous to row and column slicing for regular <span class="coding">DataFrame</span>s.  
Consider the example below, Identify Subgroups with MultiIndexing, Example 1.

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets['Rural']
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
In this example the [ ] operator returns a subset of the tickets <span class="coding">DataFrame</span> from the level Rural.   In this case Rural designates one of three values from the outer level of the column hierarchical index.  Because there is no explicit row selection all rows are returned.

In the following example, Identify Subgroups with MultiIndexing, Example 2, answers the question: for each month how many tickets were issued in the city at night?

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python

>>> tickets['City', 'Night']
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

This example illustrates selecting with both levels of the column <span class="coding">MultiIndex</span>. City is from the outer-most level of the hierarchical index and Night is from the inner-most level.

Recall that most subsetting and slicing operations return a <span class="coding">DataFrame</span>. In the example below, Sum Tickets to New DataFrame <span class="coding">DataFrame</span>, illustrates creating a new <span class="coding">DataFrame</span>.  

In this example the sum function is applied to the tickets <span class="coding">DataFrame</span> elements returning the sum of all tickets by year.  These summed values create the new <span class="coding">DataFrame</span> <span class="coding">sum_tickets</span>.

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> sum_tickets = tickets.sum(level = 'Year')
>>> print(sum_tickets)
Area   City        Rural      Suburbs
When   Day  Night  Day  Night Day  Night
Year
2015  31.0  90.0  19.0  39.0  59.0  36.0
2016  27.0  57.0  35.0  53.0  32.0  45.0
2017  57.0  50.0  60.0  29.0  33.0  14.0
2018  63.0  56.0  50.0  39.0  54.0  22.0
```
Use the axis = 1 argument to apply the sum function along a column with the syntax:

sum_tickets2 = tickets.sum(level = 'Area', axis=1)
 
, PROC TABULATE Report and New Dataset illustrates PROC TABULATE to render the same report as Listing 4-29 as well as create the  sum_tickets dataset.
Listing 4-32. PROC TABULATE Report and New Dataset

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
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
```
NOTE: There were 24 observations read from the data set WORK.SUM_TICKETS.

The default statistic for PROC TABULATE is sum and is applied to the variable tickets using the VAR statement. The TABLE statement arranges the output similar to the output in Listing 4-30. The PROC TABULATE output is presented in Figure 4-7, Tickets Summed with PROC TABULATE.

 
Figure 4-7.  Tickets Summed with PROC TABULATE
In order to create the output dataset sum_tickets, the syntax
```python
ods output 
   table = sum_tickets (keep = area
                               when
                               year
                               tickets_sum);
```
opens the ODS destination sum_tickets, as an output SAS dataset with a KEEP list of variables.  This method for summarization is an alternative to calling PROC SUMMARY/MEANS or PROC SQL.

Listing 4-33, Summarizing tickets Dataset with PROC SUMMARY, illustrates the more convential method for producing the same ‘rolled-up’, or summarized dataset.
Listing 4-33  Summarizing tickets Dataset with PROC SUMMARY

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4  proc summary data = tickets
5               nway
6               noprint;
7     class area
8           when
9           year;
10     output out=sum_tickets(keep=area when year tickets_sum)
11            sum(tickets)=tickets_sum;
```
NOTE: There were 72 observations read from the data set WORK.TICKETS.
NOTE: The data set WORK.SUM_TICKETS has 24 observations and 4 variables.

The NWAY option requests a combination for all levels of variable values listed on the CLASS statement.  The sum(tickets)=tickets_sum option then sums the number of tickets for each NWAY crossing.

#### Advanced Indexing with MultiIndexes
Earlier in the chapter we detailed the <span class="coding">.loc</span> indexer for slicing rows and columns with indexed <span class="coding">DataFrame</span>s.  

See the section entitled, Return Rows and Columns by Label in this chapter.   Slicing rows and columns with the <span class="coding">.loc</span> indexer can be used with a MultiIndexed <span class="coding">DataFrame</span> using similar syntax.  The <span class="coding">.loc</span> indexer supports Boolean logic for filtering criteria.  

The <span class="coding">.loc</span> indexer enables partial slicing using hierarchically indexed rows and/or columns.  Begin by returning the <span class="coding">DataFrame</span> along with its index and columns information illustrated by the following example, Return Ticket Index and Column Levels.


<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> print(tickets.index)
MultiIndex(levels=[[2015, 2016, 2017, 2018], [1, 2, 3]],
           codes=[[0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]],
           names=['Year', 'Month'])
>>> print(tickets.columns)
MultiIndex(levels=[['City', 'Rural', 'Suburbs'], ['Day', 'Night']],
           codes=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
           names=['Area', 'When'])
```

The <span class="coding">.loc</span> indexer takes as arguments, slicers to determine the <span class="coding">DataFrame</span> sub-set of interest.  Consider the example below, Year Slice 2018, illustrates returning all rows for year 2018.

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets.loc[2018]
Area   City       Rural       Suburbs
When    Day Night   Day Night     Day Night
Month
1      25.0  10.0   8.0   4.0    20.0  15.0
2      35.0  14.0   9.0  14.0    10.0   1.0
3       3.0  32.0  33.0  21.0    24.0   6.0
```
In this case, the rows are sliced returning those with the <span class="coding">MultiIndex</span> level for Year equal to 2018.  And because no column slicer is provided all columns are returned.
We can slice Year level for 2018 and Month level for 3 illustrated in the following examle, Slice Year 2018 and Month 3.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets.loc[2018, 3, :]
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2018 3      3.0  32.0  33.0  21.0    24.0   6.0
```
In this example, level 2018 denotes the outer row slice and 3 denotes the inner row slice.  This subset-sets the <span class="coding">DataFrame</span> by returning month 3 for every year.  The column slice follows the second comma.  Again, with no column slice provided, denoted by the colon (:) all columns are returned.
##### Slicing Rows and Columns
Consider the following example, Slice Month 3 for all Years. In this example we wish to return the 3rd month for each year. Based on what we have learned about row and column slicing up to this point, it is reasonable to conclude the statement:
```python
tickets.loc[(:,3),:]
```
is the appropirate syntax.  However, this syntax raises an error since it is illeagl to use a colon inside a tuple constructor.   

Recall a tuple is an immutable sequence of items enclosed by parenthesis. As a convenience the Python’s built-in slice(None)function selects all the content for a level. In this case we want month level 3 for all years.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
The syntax slice(None) is the slicer for the Year column which includes all values for a given level, in this case, 2015 to 2018 followed by 3 to designate the level for month.  All columns are returned since no column slicer was given.
Another way to request this same sub-set is:
```python
tickets.loc[(slice(None), slice(3,3)), :]
```
Consider the request for all years and months 2 and 3 as the row slicer in Listing 4-38, Slice Months 2 and 3 for all Years.


<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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

idx_obj = ((slice(None), slice(2,3)), slice(None))
tickets.loc[idx_obj]
This syntax helps in further understanding exactly how the slicing operation is performed.  The first slice(None) requests all of the rows for the outer row label, years 2015 to 2018.  slice(2,3) returns months 2 and 3 for inner row label.  The last slice(None) requests all columns, that is, both the outer column Area and the inner column When.
Fairly quickly, however, we begin to have difficulty supplying a collection of tuples  for the slicers used by the <span class="coding">.loc</span> indexer.  Fortunately, Pandas provides the IndexSlice object to deal with this situation.  
Consider Listing 4-39 IndexSlice Object, as an alternative to Listing 4-39, IndexSlice Object.
Listing 4-39. IndexSlice Object

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
The IndexSlice object provides a more natural syntax for slicing operations on MultiIndexed rows and columns.  In this case, the slice:
tickets.loc[idx[2015:2018, 2:3], :]
return years 2015:2018 inclusive on the outer level of the <span class="coding">MultiIndex</span> for the rows and months 2 and 3 inclusive on the inner level.  The colon (:) designates the start and stop positions for these row labels.  Following the row slicer is a comma (,) to designate the column slicer.  With no explicit column slices defined all columns are returned.  
Consider Listing 4-40, Slicing Rows and Columns, Example 1.
Listing 4-40, Slicing Rows and Columns, Example 1

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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

Listing 4-41, Slicing Rows and Slicing Columns, Example 2, illustrates details for slicing columns.  
Listing 4-41. Slicing Rows and Slicing Columns, Example 2

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
##### Conditional Slicing
Often times we need to sub-set based on conditional criteria.  Pandas allows the <span class="coding">.loc</span> indexer to permit a Boolean mask for slicing based an criteria applied to values in the <span class="coding">DataFrame</span>.  We introduced the concept of a Boolean mask in Chapter 3, Introduction to Pandas in the section on isnull.

We can identify instances where the number of tickets relates to a given threshold by creating a Boolean mask and applying it to the <span class="coding">DataFrame</span> using the <span class="coding">.loc</span> indexer.  Specifically, we want to know when the number of tickets issued in the city during the day is greater than 25.  

Listing 4-42, Conditional Slicing, illustrates this feature.
Listing 4-42. Conditional Slicing

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> mask = tickets[('City' ,'Day' )] > 25
>>> tickets.loc[idx[mask], idx['City', 'Day']]
Year  Month
2017  3        31.0
2018  2        35.0
Name: (City, Day), dtype: float64
```
In this example we define the mask object using the column slicing syntax followed by the Boolean operator greater than (>) and 25 as the threshold value.  Rows are sliced using the conditional with the mask object.  The columns are sliced using the City level from Area and the Day level from When.   Area is the outer level of the column <span class="coding">MultiIndex</span> and When is the inner level.

Another form of conditional slicing uses the Pandas where attribute.  The where attribute returns a <span class="coding">DataFrame</span> the same size as the original whose corresponding values are returned when the condition is True.  When the condition is <span class="coding">False</span>, the default behavior is to return NaN’s.  This feature is illustrated in Listing 4-43, <span class="coding">DataFrame</span> where Attribute.  
Listing 4-43. DataFrame where Attribute

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> missing = "XXX"
>>> tickets.where(tickets> 30, other = missing)
Area       City       Rural       Suburbs
When        Day Night   Day Night     Day Night
Year Month
2015 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX   XXX   XXX   XXX      42   XXX
     3      XXX    54   XXX   XXX     XXX   XXX
2016 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX   XXX   XXX   XXX     XXX   XXX
     3      XXX   XXX    31    48     XXX   XXX
2017 1      XXX   XXX   XXX   XXX     XXX   XXX
     2      XXX    33   XXX   XXX     XXX   XXX
     3       31   XXX   XXX   XXX     XXX   XXX
2018 1      XXX   XXX   XXX   XXX     XXX   XXX
     2       35   XXX   XXX   XXX     XXX   XXX
     3      XXX    32    33   XXX     XXX   XXX
```
The other = argument assigns an arbitrary value for the False condition.  Also notice how the returned <span class="coding">DataFrame</span> is the same shape as the original.
#### Cross Sections
Pandas <span class="coding">DataFrame</span>s provision a cross section method called xs as another means for returning rows and columns from an indexed <span class="coding">DataFrame</span> or partial data in the case of a MultiIndexed <span class="coding">DataFrame</span>.  The compact syntax offered by the xs method makes it fairly easy to subset MultiIndexed <span class="coding">DataFrame</span>s.  The xs method is read only.  

Consider Listing 4-44, xs Cross Section, Example 1.  
Listing 4-44.  xs Cross Section, Example 1

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets.xs((1), level='Month')
Area  City       Rural       Suburbs
When   Day Night   Day Night     Day Night
Year
2015  15.0  18.0   9.0   3.0     3.0   3.0
2016  11.0  17.0   1.0   0.0    11.0  26.0
2017  21.0   5.0  22.0  10.0    12.0   2.0
2018  25.0  10.0   8.0   4.0    20.0  15.0
```
The xs cross section method has two agruments.  The first argument, in this example is level 1 and the second argument level = 'Month' returning the rows for  month 1 for all years with all columns.  Recall the Month column is a component of the <span class="coding">MultiIndex</span> to form the row labels.  

The the xs cross section method works along a column axis illustrated in Listing 4-45, xs Cross Section, Example 2.
Listing 4-45. xs Cross Section, Example 2

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
In this example we return all rows for the level City.  The axis = 1 argument returns just the columns for the level City. 

Because the xs cross section method returns a <span class="coding">DataFrame</span> we can apply mathematical and statistical functions as attributes.  Listing 4-46, xs Cross Section, Example 3 returns the sum of all tickets issued during daylight hours in each of the three area.
Listing 4-46. xs Cross Section, Example 3

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> tickets.xs(('Day'), level='When', axis = 1).sum()
Area
City       178.0
Rural      164.0
Suburbs    178.0
```
Listing 4-47, Summed Tickets Where Day over Area is the analog program for Listing 4-46.  
Listing 4-47. Summed Tickets Where Day over Area

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 proc sql;
5 select unique area
6      , sum(tickets) as Sum_by_Area
7 from tickets
8     where when = 'Day'
9 group by area;
10 quit;
```
The WHERE clause selects those rows for when = 'Day'.  The results from the query are displayed in Figure 4-8, Tickets Issued During Daylight for each Area.

 
Figure 4-8. Tickets Issued During Daylight for each Area
The GROUP BY clause sums the variable ticket into the unique levels for the area variable.  As we will see in the next section, grouping operations are essential for data analysis. 
### GroupBy
A common pattern for data analysis familiar to SAS users is BY-group processing.  SAS defines BY-group processing as:
…a method of processing observations from one or more SAS data sets that are grouped or ordered by values of one or more common variables. The most common use of BY-group processing in the DATA step is to combine two or more SAS data sets by using the BY statement with a SET, MERGE, MODIFY, or UPDATE statement. 
Pandas uses the term ‘Group By’ to describe the task in terms of three steps:
• Splitting vales into groups based on some criteria
• Applying a function to each of these groups
• Combining the results into a data structure
Within the Apply step we often wish to do one or more of the following actions:
• Aggregate to compute summary statistics, such as:
o Compute group sums or means
o Compute group counts

• Transform to perform group-specific calculations, such as:
o Normalizing data within the group
o Replace Missing values with a value derived from each group

• Filter to discard some groups based on group-wise calculation, such as:
o Drop data whose values are sparse
o Filter out data based on the group statistic 
To accomplish these types of operation the Pandas library includes a GroupBy object.
When a GroupBy object is created it contains instructions to map rows and columns to named groups.  A crucial benefit for Pandas GroupBy is eliminating the need to handle each of the resulting splits, or sub-groups explicitly.  Instead GroupBy applies operations to the entire <span class="coding">DataFrame</span> often with a single pass of the data.  The benefit being the user does not focus on group processing details, but instead benefits from a more-abstracted processing method.
The syntax for defining a GroupBy object is:
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, 
sort=True, group_keys=True, squeeze=False, observed=False, 
**kwargs) 
As an example, consider Listing 4-48, Create GroupBy gb
Listing 4-48. Create GroupBy gb

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> import numpy as np
>>> import pandas as pd
>>> df = pd.DataFrame(
...     [['I',  'North', 'Patton',   17,  27,  22],
...     ['I',   'South', 'Joyner',   13,  22,  19],
...     ['I',   'East',  'Williams', 111, 121, 29],
...     ['I',   'West',  'Jurat',    51,  55,  22],
...     ['II',  'North', 'Aden',     71,  70,  17],
...     ['II',  'South', 'Tanner',   113, 122, 32],
...     ['II',  'East',  'Jenkins',  99,  99,  24],
...     ['II',  'West',  'Milner',   15,  65,  22],
...     ['III', 'North', 'Chang',    69,  101, 21],
...     ['III', 'South', 'Gupta',    11,  22,  21],
...     ['III', 'East',  'Haskins',  45,  41,  19],
...     ['III', 'West',  'LeMay',    35,  69,  20],
...     ['III', 'West',  'LeMay',    35,  69,  20]],
...      columns=['District', 'Sector', 'Name', 'Before', 'After', 'Age'])
>>> gb = df.groupby(['District'])
>>> print(gb)
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002592A6A3B38>
```
The gb object is defined as a groupby object using the District column as the by = parameter.  In this case the three unique values from the District column define the groups. Notice a <span class="coding">DataFrame</span>GroupBy object is returned rather than a <span class="coding">DataFrame</span>.  The gb object is analagous to a SQL view containing instructions for executing SQL statement to materialize rows and columns when the view is applied.  

The SQL analogy is:
 CREATE VIEW GB as
   SELECT distinct District
                 , mean(Before)
                 , sum(After)
   FROM DF
   GROUP BY District
Only when the groupby object is applied are results produced.  Consider Listing 4-49, Applying sum over GroupBy.
Listing 4-49. Applying sum over GroupBy

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> d_grby_sum = df.groupby(['District']).sum()
>>> print(d_grby_sum)
          Before  After  Age
District
I            192    225   92
II           298    356   95
III          195    302  101
>>> print(d_grby_sum.index)
Index(['I', 'II', 'III'], dtype='object', name='District')
```
All numeric columns in the underlying df <span class="coding">DataFrame</span> are grouped by the unique levels from the District column and then summed within each group.  Of course, the sum method is just one possibility here.  Later in this chapter we will illustrate examples for selecting individual columns and applying different aggregation methods as well as applying nearly any valid <span class="coding">DataFrame</span> operation.
Also observe how output from the District column appears like what one sees with an indexed <span class="coding">DataFrame</span> to define row labels.  
A groupby object returns a <span class="coding">DataFrame</span>.  Observe what happens when the d_grby_sum <span class="coding">DataFrame</span> is created from the GroupBy object in Listing 4-50, Create <span class="coding">DataFrame</span> from GroupBy Object.
Listing 4-50. Create DataFrame from GroupBy Object

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> d_grby_sum = df.groupby(['District']).sum()
>>> print(d_grby_sum)
          Before  After  Age
District
I            192    225   92
II           298    356   95
III          195    302  101
>>> print(d_grby_sum.index)
Index(['I', 'II', 'III'], dtype='object', name='District')
```
The d_grby_sum <span class="coding">DataFrame</span> is indexed with values from the District column.  GroupBy objects also have attributes allowing examination of their keys and groups.  These groupby object attributes are illustrated with Listing 4-51, Keys and Groups for GroupBy Object.
Listing 4-51. Keys and Groups for GroupBy Object

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> gb = df.groupby(['District'])
>>> gb.groups.keys()
dict_keys(['I', 'II', 'III'])
>>>
>>> gb.groups
{'I': Int64Index([0, 1, 2, 3], dtype='int64'), 
'II': Int64Index([4, 5, 6, 7], dtype='int64'), 
'III': Int64Index([8, 9, 10, 11, 12], dtype='int64')}
```
The syntax  gb.groups.keys()returns a Python list for the keys’ values.  The syntax  gb.groups returns a Python dictionary of key/value pairs for each key, mapped to a group, along with a corresponding list of values indicating which rows compose a given group.  In this example, rows 0, 1, 2, and 3 define the groupby level for District = 'I'.
Listing 4-52, Summary by District illustrates similar logic calling PROC SUMMARY to create a ‘grouped’ dataset summing the numeric variables by district.
Listing 4-52. Summary by District

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 data df;
5  infile cards dlm = ',';
6  length district $ 3
7         sector   $ 5
8         name     $ 8;
9  input  district $
10        sector   $
11        name     $
12        before
13        after
14        age;
 15 list;
 16 datalines;

RULE:       ----+----1----+----2----+----3----+----4----+----
17          I,   North, Patton,   17,  27,  22
18          I,   South, Joyner,   13,  22,  19
19          I,   East,  Williams, 111, 121, 29
20          I,   West,  Jurat,    51,  55,  22
21          II,  North, Aden,     71,  70,  17
22          II,  South, Tanner,   113, 122, 32
23          II,  East,  Jenkins,  99,  99,  24
24          II,  West,  Milner,   15,  65,  22
25          III, North, Chang,    69,  101, 21
26          III, South, Gupta,    11,  22,  21
27          III, East,  Haskins,  45,  41,  19
28          III, West,  LeMay,    35,  69,  20
29          III, West,  LeMay,    35,  69,  20
NOTE: The data set WORK.DF has 13 observations and 6 variables.

30 ;;;;
31
32 proc summary data=df nway;
33     class district;
34     var before after age;
35     output out=gb_sum (drop = _TYPE_ _FREQ_)
36        sum=;
37  run;
```
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.GB_SUM has 3 observations and 4 variables.

Figure 4-9, Grouped Summary by District, displays the resulting ‘groups’ created using PROC SUMMARY.  The CLASS statement defines the unique levels for the district variable.
 
Figure 4-9. Grouped Summary by District
#### Iteration Over Groups
The GroupBy object supports iterating over the defined groups.  As an example, consider Listing 4-53, Iterate Over Groups.  
Listing 4-53. Iterate Over Groups

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> gb = df.groupby(['District'])
>>> for name, group in gb:
...     print('Group Name===> ',name)
...     print(group)
...     print('='*47)
...
Group Name===>  I
  District Sector      Name  Before  After  Age
0        I  North    Patton      17     27   22
1        I  South    Joyner      13     22   19
2        I   East  Williams     111    121   29
3        I   West     Jurat      51     55   22
===============================================
Group Name===>  II
  District Sector     Name  Before  After  Age
4       II  North     Aden      71     70   17
5       II  South   Tanner     113    122   32
6       II   East  Jenkins      99     99   24
7       II   West   Milner      15     65   22
===============================================
Group Name===>  III
   District Sector     Name  Before  After  Age
8       III  North    Chang      69    101   21
9       III  South    Gupta      11     22   21
10      III   East  Haskins      45     41   19
11      III   West    LeMay      35     69   20
12      III   West    LeMay      35     69   20
```
In this example a for loop iterates over the GroupBy object to produce a custom report.  As we have seen previously, iterating manually over objects can be useful, however the apply method discussed later in this chapter may be a more productive alternative for applying methods and functions to grouped values in a <span class="coding">DataFrame</span>.
With SAS, the same report is easily produced using the Data Step by group processing as shown in Listing 4-54 Iterative By Group Processing.  While we could have called PROC PRINT for this example, the goal for the example is to illustrate how first.district and last.district behaviors for By Group processing.
Listing 4-54. Iterative By Group Processing

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4  proc sort data = df presorted;
5     by district;
6

NOTE: Sort order of input data set has been verified.
NOTE: There were 13 observations read from the data set WORK.DF.

7 data _null_;
8 file print;
9    set df;
10   by district;
11
12 if first.district then
13    put 'Group Name====> ' district /
14         'District Sector    Name     Pre  Post  Age';
15 put @1 district @10 sector @20 name
16     @29 pre @34 post @40 age;
17
18 if last.district then
19    put '=========================================';
20 run;
NOTE: 22 lines were written to file PRINT.
```
In general, SAS By Group processing is established with either PROC SORT or an ORDER BY statement in PROC SQL.  For Data Step processing when a BY statement is encountered, SAS creates the automatic variables first.<by_variable> and last.<by_variable> to permit truth testing to control logic by identifying observations as first or last in the by group.  The statement fragment:
if first.district then

is a truth test with an implied Boolean evaluation of 0 for false and 1 for true.  In our example, the statement above can be also be written as:

if first.distrct = 1 then 

Figure 4-10, SAS By Group Processing displays the report output. 

 
Figure 4-10. SAS By Group Processing

Similarly, Pandas provisions the first and last methods for the groupby object as illustrated in Listing 4-55, Return First and Last Rows from GroupBy returns the first and last row respectively for each group.
Listing 4-55. Return First and Last Rows from GroupBy

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df.groupby('District').first()
         Sector    Name  Before  After  Age
District
I         North  Patton      17     27   22
II        North    Aden      71     70   17
III       North   Chang      69    101   21
>>> df.groupby('District').last()
         Sector    Name  Before  After  Age
District
I          West   Jurat      51     55   22
II         West  Milner      15     65   22
III        West   LeMay      35     69   20
```
#### GroupBy Summary Statistics
As mentioned earlier a GroupBy feature is the ability to accept most methods applicable to a <span class="coding">DataFrame</span> by applying the methods to individual groups.  Consider Listing 4-56, Summary Statistics by Group.
Listing 4-56. Summary Statistics by Group

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> pd.options.display.float_format = '{:,.2f}'.format
>>> gb.describe()
           Age                                           ...     
         count  mean  std   min   25%   50%   75%   max  ...   

District                                                 ...
I         4.00 23.00 4.24 19.00 21.25 22.00 23.75 29.00  ...    
II        4.00 23.75 6.24 17.00 20.75 23.00 26.00 32.00  ...    
III       5.00 20.20 0.84 19.00 20.00 20.00 21.00 21.00  ...    

[3 rows x 24 columns]
```
This example illustrates how methods not specifically implemented for the GroupBy object are passed through allowing groups to call the method.  Here the <span class="coding">DataFrame</span>’s desribe method performs the aggregration describing values for each group. Due to page width limitations, only a portion of the actual output is presented here.
We can apply different aggregation methods to different columns defined by the GroupBy object.  In Listing 4-48, Applying sum over GroupBy the sum method is applied to all numeric columns.  In contrast, Listing 4-57, Different Statistics Over Group Columns illustrates different statistics applied to columns.
Listing 4-57. Different Statistics Over Group Columns

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> gb = df.groupby(['District'])
>>> gb.agg({'Age' : 'mean',
...      'Before' : 'median',
...       'After' : ['sum', 'median', 'std']
...            })
           Age Before After
          mean median   sum median   std
District
I        23.00     34   225  41.00 45.54
II       23.75     85   356  84.50 26.62
III      20.20     35   302  69.00 30.20
```
In this example the agg function is applied to the gb GroupBy object using a Python dictionary to identify aggregation methods applied to designated columns.  Recall a Python dictionary is a data structure for holding key/value pairs.  To accommodate multiple statistics for a given column, we pass a Python list of methods as the value for the dictionary.  For example, the After column has as its value a Python list of aggregation methods, sum, median, and std.
Listing 4-58, By Group Statistics over Different Variable illustrates the same approach using SAS.
Listing 4-58. By Group Statistics over Different Variable

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 proc summary data=df nway;
5    class district;
6    output out=gb_sum (drop = _TYPE_ _FREQ_)
7       mean(age)       = age_mean
8       median(before)  = bfr_median
9       sum(after)      = aft_sum
10      median(after)   = aft_median
11      std(after)      = aft_std;
12 run;

NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.GB_SUM has 3 observations and 6 variables.

13 proc print data = gb_sum noobs;
14 run;
```
Figure 4-11, By Group Statistics for Different Variables Ouput displays the output created by PROC SUMMARY.

 
Figure 4-11. By Group Statistics for Different Variables Ouput
The output out= syntax applies summary statistics to the input variables and permits the naming of the resulting output variables.
#### Filtering by Group
A common coding pattern for data analysis is applying actions to a set of data based on a group’s statistic.  As an example, consider Listing 4-59, Group By Filtering on a Statistic.
Listing 4-59. Group By Filtering on a Statistic

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> print(df)
   District Sector      Name  Before  After  Age
0         I  North    Patton      17     27   22
1         I  South    Joyner      13     22   19
2         I   East  Williams     111    121   29
3         I   West     Jurat      51     55   22
4        II  North      Aden      71     70   17
5        II  South    Tanner     113    122   32
6        II   East   Jenkins      99     99   24
7        II   West    Milner      15     65   22
8       III  North     Chang      69    101   21
9       III  South     Gupta      11     22   21
10      III   East   Haskins      45     41   19
11      III   West     LeMay      35     69   20
12      III   West     LeMay      35     69   20
>>> def std_1(x):
...    return x['Age'].std() < 5
...
>>> df.groupby(['District']).filter(std_1)
   District Sector      Name  Before  After  Age
0         I  North    Patton      17     27   22
1         I  South    Joyner      13     22   19
2         I   East  Williams     111    121   29
3         I   West     Jurat      51     55   22
8       III  North     Chang      69    101   21
9       III  South     Gupta      11     22   21
10      III   East   Haskins      45     41   19
11      III   West     LeMay      35     69   20
12      III   West     LeMay      35     69   20
```
This example removes groups with a group standard deviation for Age less than five (5).  To do this, we define the std_1 function containing the filter critera as: 
 
def std_1(x):
    return x['Age'].std() < 5

def is used to define a Python function followed by the function’s name; in this case std_1.  Inside this function, x is a local variable holding the group passed in when called.

A new <span class="coding">DataFrame</span> is created by by passing the std_1 function to filter method of the GroupBy object.

Notice how no rows are returned from the District column with a value of ‘II’.
#### Group by Column with Continuous Values 
Sometimes the desire is to use columns with continuous values as a GroupBy object.  Consider the case of age where these values are continuous.  To create a meaningful GroupBy object, the first step is mapping continuous values into ‘buckets’ and applying these binned values to a GroupBy operation.  The binned values are mapped using the apply method to create the GroupBy object.  This action allows aggregations to be performed based on group values determined by bin ranges formed with the Age column.  
Here we illustrate this pattern using the Pandas cut method for segmenting and sorting data values into bins.  Consider Listing 4-60, GroupBY Column With Continuous Values.
Listing 4-60. GroupBY Column With Continuous Values

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> def stats(group):
...     return {'count' : group.count(),
...             'min'   : group.min(),
...             'max'   : group.max(),
...             'mean'  : group.mean()}
...
>>> bins = [0, 25, 50, 75, 200]
>>> gp_labels = ['0 to 25', '26 to 50', '51 to 75', 'Over 75']
>>>
>>> df['Age_Fmt'] = pd.cut(df['Age'], bins, labels=gp_labels)
>>> df['Age'].groupby(df['Age_Fmt']).apply(stats).unstack()
>>>
          count   max  mean   min
Age_Fmt
0 to 25   11.00 24.00 20.64 17.00
26 to 50   2.00 32.00 30.50 29.00
51 to 75   0.00   nan   nan   nan
Over 75    0.00   nan   nan   nan
```
In the example we begin by defining the stats function using the def function and naming this function stats.  It simply returns a Python dictionary of aggregration methods as a convience for passing this dictionary to the apply method when creating the GroupBy object.

The syntax:

bins = [0, 25, 50, 75, 200]
gp_labels = ['0 to 25', '26 to 50', '51 to 75', 'Over 75']

assigns the ‘cut-points’ to the bins object as a Python list of values representing the upper and lower bounds for the bins created with the cut method.  The gp_labels object is another Python list of values holding the labels assigned to these bins.  Both these objects are passed to the to the cut method with the syntax:

df['Age_Fmt'] = pd.cut(df['Age'], bins, labels=gp_labels)

defining the Age_Fmt column in the df <span class="coding">DataFrame</span>.  This assignment creates column values by calling the cut method for the df['Age'] column (with bins and labels defined).  Note that pd.cut uses the syntax  pd to refer to the <span class="coding">Name </span>for the Pandas library that is loaded into the namespace with:

import pandas as pd

The syntax:

df['Age'].groupby(df['Age_Fmt']).apply(stats).unstack()

creates the GroupBy object using unique values from the Age_Fmt column as the group’s levels and is attached to the df['Age'] column.  The apply method calls the defined function stats applying the statistics column values within each group.  The unstack method reshapes the returned object from a stacked form (in this case a Series object) to an unstacked form (a “wide” <span class="coding">DataFrame</span>).   

The same logic in SAS is shown in Listing 4-61, By Group With Continuous Variable.  In this example the aggregation functions for the age variable statistics are produced with PROC SQL.
Listing 4-61. By Group With Continuous Variable

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 proc format cntlout = groups;
5     value age_fmt
6         0  - 25   = '0-25'
7         26 - 50   = '26-50'
8         51 - 75   = '51-75'
9         76 - high = 'Over 75';
NOTE: Format AGE_FMT has been output.

NOTE: The data set WORK.GROUPS has 4 observations and 21 variables.

10 proc sql;
11    select fmt.label      label = 'Group'
12         , count(dat.age) label = 'Count'
13         , min(dat.age)   label = 'Min'
14         , max(dat.age)   label = 'Max'
15         , mean(dat.age)  label = 'Mean'
16 from
17    groups as fmt 
18       left join df as dat
19       on fmt.label = put(dat.age, age_fmt.)
20 group by fmt.label;
21 quit;
```
PROC FORMAT provides similar binning logic as the cut method in the Python example Listing 4-59, GroupBy Continuous Column.  The cntlout = groups option outputs a dataset containing several variables including the label variable holding the value labels for the user-defined agefmt. format.  The aggregation functions are applied to the age variable using PROC SQL.  PROC SQL uses a left join to combine rows on the label column from the groups table (created with cntlout =) with rows from the aggregation functions applied to the age column from the df dataset.  The output from PROC SQL is displayed in Figure 4-12, Group By with Continuous Values.
 
Figure 4-12. Group By with Continuous Values
#### Transform Based on Group Statistic
Up to this point the GroupBy objects return <span class="coding">DataFrame</span>s with fewer rows than the original <span class="coding">DataFrame</span>.  This is to be expected since GroupBy objects are commonly used in aggregation operations.  There are cases where you wish to apply a transformation based on group statistics and merge the transformed version with the original <span class="coding">DataFrame</span>.  Calculating a z-score is an example illustrated in Listing 4-61 Transform Based on GroupBy Statistic.
Listing 4-61. Transform Based on GroupBy Statistic

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> z = df.groupby('District').transform(lambda x: (x - x.mean()) / x.std())
>>> z.columns
Index(['Before', 'After', 'Age'], dtype='object')
>>>
>>> z = z.rename \
...      (columns = {'Before' : 'Z_Bfr',
...                  'After'  : 'Z_Aft',
...                  'Age'    : 'Z_Age',
...                 })
>>> df1 = pd.concat([df, z], axis=1)
>>> pd.options.display.float_format = '{:,.2f}'.format
>>> print(df1[['Name', 'Before', 'Z_Bfr', 'After', 'Z_Aft', 'Age', 'Z_Age']].head(6))
       Name  Before  Z_Bfr  After  Z_Aft  Age  Z_Age
0    Patton      17  -0.68     27  -0.64   22  -0.24
1    Joyner      13  -0.77     22  -0.75   19  -0.94
2  Williams     111   1.39    121   1.42   29   1.41
3     Jurat      51   0.07     55  -0.03   22  -0.24
4      Aden      71  -0.08     70  -0.71   17  -1.08
5    Tanner     113   0.89    122   1.24   32   1.32
```
The logic to compute the z-score is accomplished by creating the z <span class="coding">DataFrame</span> with a GroupBy object using the syntax:

z = df.groupby('District').transform(lambda x: (x - x.mean()) / x.std())

In this example a lamdba expression is used to create an anonymous, or in-line function defining the z-score calculation.  Like the def function this expression creates a function, but does not provide it a name.  Hence, it is known as an anonymous function.

The transform function computes the z-score for rows within each group using the group’s computed mean and standard deviation.  The transform function returns a <span class="coding">DataFrame</span> the same shape as the input <span class="coding">DataFrame</span> making it useful for combining the two together.

Because Pandas allows the same name for multiple columns the rename attribute is applied to the z <span class="coding">DataFrame</span> passing a Python dictionary of key/value pairs where the key is the old column name and the value is the new column name.  The syntax:

df1 = pd.concat([df, z], axis = 1)

creates the df1 <span class="coding">DataFrame</span> by concatenating the df and z <span class="coding">DataFrame</span>s along the columns with the axis = 1 argument.  We cover the details for Pandas concatenation and joins in Chapter 5, Advanced Data Management.

Listing 4-62 Transform Based on By Group Statistic illustrates the same logic in SAS.  PROC SUMMARY is called to create the intermediate variables used for calculating the z-scores.  PROC SORT is called to sort the df dataset and the z_out dataset produced by PROC SUMMARY using the variable district as the sort keys. 
Listing 4-62. Transform Based on By Group Statistic

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 proc summary nway data = df;
5    class district;
6    var pre post age;
7    output out=z_out (drop = _TYPE_ _FREQ_)
8       mean(age)   = age_mean
9       mean(pre)   = pre_mean
10      mean(post)  = post_mean
11      std(age)    = age_std
12      std(pre)    = pre_std
13      std(post)   = post_std;
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.Z_OUT has 3 observations and 7 variables.

14 proc sort data = df presorted;
15    by district;
16
NOTE: Sort order of input data set has been verified.
NOTE: There were 13 observations read from the data set WORK.DF.

17 proc sort data = z_out presorted;
18    by district;
19
NOTE: Sort order of input data set has been verified.
NOTE: There were 3 observations read from the data set WORK.Z_OUT.

20 data z_df (drop = age_mean pre_mean post_mean
21                   age_std pre_std post_std);
22    merge df
23          z_out;
24    by district;
25
26 z_pre  = (pre - pre_mean)   / pre_std;
27 z_post = (post - post_mean) / post_std;
28 z_age  = (age - age_mean)   / age_std;
29 format z_pre z_post z_age 8.2;
30
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: There were 3 observations read from the data set WORK.Z_OUT.
NOTE: The data set WORK.Z_DF has 13 observations and 9 variables.

31 proc print data=z_df(obs=6) noobs;
32    var name pre z_pre post z_post age z_age;
33 run;

NOTE: There were 6 observations read from the data set WORK.Z_DF.
```
The final step uses a Data Step to merge the df and z_out datasets on the district sort key and performs the z-score calculations.  The indermediate variables from the z_out dataset are dropped with a DROP list.  Figure 4-13, Transformations with By Group Statistics displays the output producted by PROC PRINT.

 
Figure 4-13. Transformations with BY Group Statistics
### Pivot
Pandas provide the pivot_table function to create speadsheet-style pivot tables.  The pivot_table function enables aggregation of data values across row and column dimensions.   As we will see shortly, pivot_table function not only provides a multi-dimensional view of your data, but it turns out to be a convenient method to apply a <span class="coding">MultiIndex</span> to <span class="coding">DataFrame</span> rows and columns.

Begin by using read_csv method to read detailed sales transaction data collected between 2016 and 2017 in Listing 4-63, Pivot Table Basics.  This input data is transaction details referred to as stacked, or long format.  There is one row per transaction.

Notice the read_csv method uses the parameter na_filter = False.  Without calling this argument the Territory column does not include rows with the value ‘NA’.  In our case, ‘NA’  denotes the value of North America and not missing values.  Later in chapter 7, Panda Readers, we explore numerous arguments to the read_csv function in detail.
Listing 4-63. Pivot Table Basics

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> url = "https://raw.githubusercontent.com/RandyBetancourt/PythonForSASUsers/master/data/Sales_Detail.csv"
>>> df2 = pd.read_csv(url, na_filter = False)
>>> df2.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2823 entries, 0 to 2822
Data columns (total 10 columns):
OrderNum       2823 non-null int64
Quantity       2823 non-null int64
Amount         2823 non-null float64
Status         2823 non-null object
ProductLine    2823 non-null object
Country        2823 non-null object
Territory      2823 non-null object
SalesAssoc     2823 non-null object
Manager        2823 non-null object
Year           2823 non-null int64
dtypes: float64(1), int64(3), object(6)
memory usage: 220.6+ KB
>>>
>>> df2.pivot_table(index =   ['Year', 'ProductLine'],
...                 columns = ['Territory'],
...                  values = ['Amount'])
                    Amount
Territory             APAC     EMEA       NA
Year ProductLine
2016 Classic Cars 3,523.60 4,099.44 4,217.20
     Motorcycles  3,749.53 3,309.57 3,298.12
     Planes       3,067.60 3,214.70 3,018.64
     Ships             nan 3,189.14 2,827.89
     Trains       1,681.35 2,708.73 2,573.10
     Trucks       3,681.24 3,709.23 3,778.57
     Vintage Cars 2,915.15 2,927.97 3,020.52
2017 Classic Cars 3,649.29 4,062.57 3,996.12
     Motorcycles  2,675.38 3,736.90 3,649.07
     Planes       2,914.59 3,047.34 3,645.51
     Ships        2,079.88 3,030.86 3,067.40
     Trains            nan 3,344.41 2,924.96
     Trucks       3,695.36 4,344.76 3,326.99
     Vintage Cars 3,399.04 2,998.96 3,662.24 
```
In order to appreciate the flexibility afforded by the pivot_table funtion, the script includes output from info method indicating the <span class="coding">DataFrame</span> has 2,823 rows and 10 columns.  

In this example the pivot_table function uses three arguments:

• index:  Containing a Python list of columns forming row lables, with Year as the outer level and ProductLine as the inner level.

• columns:  Contain a Python list of columns acting as keys to GroupBy on the pivot table columns.  Unique values from the columns argument make up the columns in the pivot tables.  In this example the Territory column has values ‘APAC’, ‘EMEA’, and ‘NA’ (for North America) with each value as the pivot table’s columns.  

• values:  the column or Python list of columns to aggregate.  In this example the Amount column.  The default aggregation method is np.mean.

Notice how row labels are formed using the Year column values as the outer level and ProductLine as the inner level.  In other words the index argument to pivot_table function creates either an index if one column is specified or a <span class="coding">MultiIndex</span> object if more than one column is specified.  The same is true for the columns = argument.  

Let’s improve the pivot table created in Listing 4-63 Pivot Table Basics.  Notice in that report NAN’s have been returned indicating missing values.  Further, we want to replace the default np.mean aggregation method for all columns by summing the values from the Quantity column.  Finally we can add row and column totals to get sub-totals and a grand-total.  These features are illustrated in Listing 4-64, Pivot Table Improvements.
Listing 4-64. Pivot Table Improvements

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
pd.pivot_table(df2,values     = ['Amount', 'Quantity'],
                   columns    = 'Territory',
                   index      = ['Year', 'ProductLine'],
                   fill_value = 0,
                   aggfunc    = {'Amount'  : np.mean,
                                'Quantity' : np.sum},
                                 margins=True)

The argument fill_value = 0 replaces the NaN’s in the original output with zeros. The aggfunc= argument passes a Python Dictionary to associate column names (key) with a corresponding aggregation method (value).  In this example, the Amount column is aggreated using np.means and the Quantity column is aggregated using np.sum. Figure 4-14, Improved Pivot Table.

 
Figure 4-14. Improved Pivot Table 
The pivot_table function syntax is easy to understand and provides a straight-forward solution for a variety of analysis problems.  Consider Listing 4-65 Sales by Year Over Territory.  
Listing 4-65. Sales by Year Over Territory

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
pd.pivot_table(df2,values     = ['Amount'],
                   columns    = ['Territory'],
                   index      = ['Year', 'Status'],
                   fill_value = 0,
                   aggfunc    = (np.sum))

From Figure 4-15, Output of Sales by Year Over Territory shows that the EMEA territory has an usually high amount of cancellations compared to the rest of the organization.  
 
Figure 4-15. Pivot Table Year Status Over Territory
To produce the same report with SAS requires multiple steps after the .csv file is read with PROC IMPORT.  The task is to summarize the amount variable and transpose the territory variable’s unique values into variables.  The steps are:

1.  Sort the sales_detail dataset created with PROC IMPORT by the territory variable.

2.  Summarize the sales_detail dataset by territory for the amount variable with PROC SUMMARY.  Output summary as sales_sum dataset.

3.  Sort the sales_sum dataset by the variables year status.

4.  Transpose the sales_sum dataset on the territory variable (<span class="coding">ID</span>) by year status with PROC TRANSPOSE.  Create a transposed dataset called sales_trans.

5.  Print the sales_trans dataset using the SAS-supplied dollar13.2 format.

Listing 4-66, SAS Year Status Over Territory illustrates this logic.
Listing 4-66.  SAS Year Status Over Territory

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4  filename git_csv temp;
5  proc http
6       url="https://raw.githubusercontent.com/RandyBetancourt/PythonForSASUsers/master/data/Sales_Detail.csv"
7     method="GET"
8     out=git_csv;
NOTE: 200 OK

9  proc import datafile = git_csv
10      dbms=csv
11      out=sales_detail
12      replace;
13 run;

NOTE: The data set WORK.SALES_DETAIL has 2823 observations and 10 variables.

14 proc sort data=sales_detail;
15    by territory;
16 run;

NOTE: There were 2823 observations read from the data set WORK.SALES_DETAIL.

17 proc summary data=sales_detail nway;
18    by territory;
19    class year status;
20    var amount;
21    output out=sales_sum (drop = _TYPE_ _FREQ_)
22       sum(amount)    = amount_sum;
23 run;

NOTE: There were 2823 observations read from the data set WORK.SALES_DETAIL.
NOTE: The data set WORK.SALES_SUM has 14 observations and 4 variables.

24 proc sort data=sales_sum;
25    by year status;
26 run;

NOTE: There were 14 observations read from the data set WORK.SALES_SUM.
NOTE: The data set WORK.SALES_SUM has 14 observations and 4 variables.

27 proc transpose data = sales_sum
28                  out = sales_trans(drop=_name_);
29                  id territory;
30 by year status;
31 run;

NOTE: There were 14 observations read from the data set WORK.SALES_SUM.
NOTE: The data set WORK.SALES_TRANS has 6 observations and 5 variables.

32 proc print data=sales_trans;
33    var apac emea na ;
34    id status year;
35 format apac emea na dollar13.2;
36 run;

The output from PROC PRINT is displayed in Figure 4-16, SAS Transpose on Territory.
 
Figure 4-16. SAS Transpose on Territory 
The key to creating this report is the call to PROC TRANSPOSE.  The territory values in the detail dataset, sales_detail, are row-oriented.  The <span class="coding">ID</span> statement maps the unique values for the territory variable into variables on the sales_trans output dataset.  And because the summarization are by the variables status and year, the call to PROC TRANSPOSE is also by status and year. 
### Summary
In this chapter we discussed the role for indexing and hierarchical indexing as a means for providing labels for <span class="coding">DataFrame</span> rows and columns.  We introduced in the three indexers along with slicers to return sub-sets from a <span class="coding">DataFrame</span>:

1.  [ ] operator

2.  <span class="coding">.loc</span> indexer for slicing along rows and columns using labels

3.  <span class="coding">.iloc</span> indexer for slicing along rows and columns based on a values position along an index
We examined how to apply a range of methods to the subset <span class="coding">DataFrame</span>s to perform common data manipulation methods for analysis.  
We provide a detailed discussion on the GroupBy object for split-apply-combine operations.  We also provided a general introduction to pivot tables.  Together these examples lay the foundation for Chapter 5, Advanced Data Management where we examine joining <span class="coding">DataFrame</span>s through concatenation and merging methods.
