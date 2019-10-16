---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Indexing and Groupby copy"
description: Data processing using Python and SAS.
author: Sarah Chen
# image: https://www.audubon.org/sites/default/files/styles/hero_image/public/sfw_nationalgeographic_1517960.jpg?itok=F5pikjxg
---

**Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia consequuntur, provident nemo soluta similique, maiores sit dicta doloremque facere laudantium [Keras](https://keras.io/){:target="_blank"} Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque neque totam voluptatem porro accusantium id.**

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit, similique minima repudiandae. Voluptate pariatur iusto quo voluptatibus eum? [Keras](https://keras.io/){:target="_blank"} Lorem ipsum dolor sit. [github](https://github.com/fchollet/keras){:target="_blank"} page.

> **Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**.

SAS users tend to think of indexing SAS data sets to either improve query performance or as a method to avoid dataset sorting. Another use case for using SAS indexes is to provide direct access to a specific observation in a dataset.  SAS datasets are already "tidy" tabular data with column names and row numbering and have the built-in capability to hold a wide range of data types. 

On the other hand, pandas is build on top of numpy arrays with extended capacility to hold multiple types of data in a column.  Pandas Series are essentially 1D numpy array + dictionary, where the dictionary keys are used to index elements of the array.   Similarly, pandas DataFrame is essentially numpy array + dictionary.  pandas automatically create an index structure at DataFrame creation time for both rows and columns.  For example, the <span class="coding">RangeIndex</span> object is used as the default row index.  

These index objects are responsible for holding the axis labels and other metadata like integer-based location identifiers, axis name, etc.  

One or more columns in DataFrame can be used to define an index.  Assigning more than one column as an index creates a <span class="coding">MultiIndex</span> object discussed later in this post.  New users to Pandas often get confused about the role of an index, since most of their prior associations consider an index to be an auxiliary structure for columns.  

The way we like to think about a Pandas index is to consider it as a means for labeling DataFrame rows.  Recall from our book "Python for SAS Users" Chapter 3, Pandas, that at DataFrame creation time, the <span class="coding">RangeIndex</span> object is created as the default index similar to the automatic <span class="coding">\_n_ </span>variable SAS establishes at SAS dataset creation time.  

In a DataFrame, the values from  a column or columns may be used as an index to supply values as row labels augmenting the default integer values assigned by the <span class="coding">RangeIndex</span> object.  Just as you are able to return SAS dataset observations using the automatic variable <span class="coding">\_n_</span>, a DataFrame’s default <span class="coding">RangeIndex</span> is used to return rows using a zero-based offset.  By explicitly setting a DataFrame index from  column or multiple column values, you can return rows using these column values in addition to returning rows using the <span class="coding">RangeIndex</span> object. 

### Create Index
When a DataFrame is assigned an index, the rows remain accessible by supplying a collection of integer values as well as accessible by the row labels defined by the index.  The example below illustrates the <span class="coding">set_index</span> method using the <span class="coding">\_N_</span> column.  In this example, the values from the <span class="coding">ID</span> column supply labels for the DataFrame rows.


<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python

# Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py
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
The DataFrame df is constructed using the DataFrame constructor method.  The first <span class="coding">print</span> function returns all of the rows labeled with the default <span class="coding">RangeIndex</span> object labeling rows starting with the integer 0 to length (axis – 1).  

The default value for the <span class="coding">set_index</span> method is inplace = False.   In the case where the <span class="coding">inplace=</span>argument is <span class="coding">False</span>, you must assign the results to a new DataFrame.  For example,

df_idx = df.set_index('ID', inplace=False)
creates the df_idx DataFrame with the <span class="coding">ID</span> column as its index.  The original df DataFrame remains unaltered.

The second <span class="coding">print</span> function illustrates how the DataFrame rows are labeled with values from the <span class="coding">ID</span> column.  The overhead for creating and dropping indexes is minimal and it is not unusual to do so repetitively in a single Python program.

#### Subsetting Using Index
Subsetting data by rows and/or columns is an essential task for any form of data analysis.  Panda DataFrames offers three choice for subsetting operations.  They are:

1.  <span class="coding">[  ]</span> operator enables selection by columns or by rows.

2.  <span class="coding">.loc</span> indexer uses row and column labels for subsetting.  A column label is the column <span class="coding">Name </span>and row labels are assigned with an index (either with the <span class="coding">index=</span> parameter at DataFrame creation time or with the df.<span class="coding">set_index</span> method.  If no index is explicitly assigned, then the integer-based <span class="coding">RangeIndex</span> object is the default.  If no names are assigned to columns, then the <span class="coding">RangeIndex</span> object labels the columns with the first column as 0, the second column as 1, and so on.

3.  <span class="coding">.iloc</span> indexer uses integer positions (from 0 to length-1 of the axis) for subsetting rows and columns.  This method remains available even if a user-defined index or <span class="coding">MultiIndex</span> is defined.  MultiIndexes, or hierarchical indexes are discussed later in this chapter.

Both the <span class="coding">.loc</span> and <span class="coding">.iloc</span> indexers accept Boolean logic to perform complex subsetting.  The <span class='coding'>[ ]</span> operator and the <span class="coding">.iloc</span> indexers can access rows using the default <span class="coding">RangeIndex</span> object, that is, integer values indicating a position along the index.  The <span class="coding">.loc</span> indexer requires a user-defined index for creating row labels in order to operate.
All three indexers return a DataFrame.


### Return Columns by Position
Consider Listing 4-2, DataFrame Default Indexes. This example constructs the i DataFrame using a single <span class="coding">print</span> function to display the DataFrame values, default row index and the default column index. The <span class="coding">‘\n’</span>  syntax inserts a new line to display the desired results.
Listing 4-2. DataFrame Default Indexes

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
We begin with subsetting using the <span class="coding">[  ]</span> operator.    Observe that both columns and rows in DataFrame i use the default <span class="coding">RangeIndex</span> as their labels.  
The default <span class="coding">RangeIndex</span> is used to select rows or columns using integers to locate their positions along the index.  

<div class="code-head"><span>code</span> DataFrame Return Column or Row.py</div>

```python
>>> i[0]
0      Patton
1      Joyner
2    Williams
3       Jurat
4        Aden
```
The call to <span class='coding'>[ ]</span> operator returns the first column (0) from the DataFrame i.  In most cases, DataFrame columns will have labels to return the columns of interest.
The <span class='coding'>[ ]</span> operator also accepts a Python list of columns to return.  Recall that a Python list is a mutable data structure for holding a collection of items.   List literals are written within square brackets <span class='coding'>[ ]</span> with commas (,) to indicate multiple items in the list. 

In the example below, each of the values supplied to the DataFrame constructor method is a Python list as is the <span class="coding">columns= </span>argument.

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

>>> df[['Name', 'After']].head(4)
       Name  After
0    Patton     27
1    Joyner     22
2  Williams    121
3     Jurat     55
```
In this example the syntax:
df[['Name', 'After']].head(4)
is a column subsetting operation returning the columns <span class="coding">Name </span>and After.  Notice how the Python list with <span class="coding">[' Name', 'After'] </span>inside the DataFrame slice operator results in a pair of square brackets [<span class='coding'>[ ]</span>]. The outer pair is the syntax for the DataFrame <span class='coding'>[ ]</span> operator while the inner pair hold the literal values to form the Python list of column names.

Clearly, using a list of column names rather than a list of column integer index positions is a more convenient method for subsetting.  

The equivalent SAS program is displayed in Listing 4-5, Create df SAS dataset.  It is used in subsequent examples in this chapter.
Listing 4-5. Create df SAS dataset

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
NOTE: There were 4 observations read from the data set WORK.DF
```


The output from PROC PRINT with data=df(obs=4) is displayed in Figure 4-1, Display SAS Dataset df Output.
 
Figure 4-1. Display SAS df Dataset Output

### Return Rows by Position
The general syntax for DataFrame row slicing (subsetting rows) using the <span class='coding'>[ ]</span> operator is:
df:[start : stop : step]
The start position is included in the output and the stop position is not included in the output. 

For example, consider Listing 4-6, DataFrame Row Slicing, Example 1.
Listing 4-6. DataFrame Row Slicing, Example 1

<div class="code-head"><span>code</span> DataFrame Row Slicing, Example 1.py</div>

```python
>>> df[:3]
  District Sector      Name  Before  After
0        I  North    Patton      17     27
1        I  South    Joyner      13     22
2        I   East  Williams     111    121
```
This example returns the first three row from the df DataFrame.  A null value for the start position defaults to start position zero (0).  The value following the colon (:) indicates the stop position and goes up to but does not include the row in the slicing operation.  

Listing 4-7, DataFrame Row Slicing, Example 2, illustrates returning every other row from the df DataFrame.
Listing 4-7. DataFrame Row Slicing, Example 2

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
The start and stop positions are null causing the slice df[::2] to  default to the first and last row respectively in the DataFrame.  The value of two (2) for the step position returns every other row.
This same logic is displayed in Listing 4-8, SELECT Every Other Row.
Listing 4-8. SELECT Every Other Row

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 data df1;
5    set df;
6    if mod(_n_, 2) ^= 0 then output;
7 run;
```
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.DF1 has 7 observations and 5 variables.


The example creates the df1 dataset with a subsetting IF statement to perform modulo division by 2 on the automatic SAS <span class="coding">_n_ </span>variable assigned to each observation.  Modulo division by 2 on even integers returns 0 (zero).  By using the IF statement’s inequality evaluation of ^= 0 every odd <span class="coding">_n_ </span> value (1, 3, 5, etc.) evaluates true and is written to the output df1 dataset. 
Calling PROC PRINT displays the output shown in Figure 4-2, Output from Every Other Row.
 
Figure 4-2. Output From SELECT Every Other Row
### Return Rows and Columns by Label
The <span class="coding">.loc</span> indexer is a method primarily used for returning rows and columns using labels.  Allowed inputs to <span class="coding">.loc</span> are:
• A single label such as 12 or ‘Name’.  Note that 12 is interpreted as the row label and not as the integer location along the index.

• A Python list of labels [‘A’, ‘B’, ‘C’]

• A slice object with labels ‘a’ : ‘z’.  Both the start, in this case ‘a’, and the stop, ‘z’ is included when present in the index.

• Conditional evaluations 
Each of these methods are illustrated.

Up to this point, the index for the df DataFrame relies on the default <span class="coding">RangeIndex</span> object for returning rows by an integer position along the index.  In order to retrieve rows from the df DataFrame by labels the <span class="coding">Name </span>column is set as the DataFrame index.  This action assigns the values from the <span class="coding">Name </span>column as labels for the DataFrame rows.  Said another way, a DataFrame index maps columns values onto rows as labels.   
The syntax and default values for the <span class="coding">set_index</span> method is:
df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False) 

Listing 4-9, Add Index to DataFrame, illustrates defining an index for an existing DataFrame.   
Listing 4-9. Add Index to DataFrame

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
In this example, the first <span class="coding">print</span> function displays all rows from the df DataFrame.  The syntax:
print(df.index)
returns the default <span class="coding">RangeIndex</span> in use for the rows with integer values between 0 and 13.  The syntax:
df.set_index('Name', inplace=True, drop=True)
selects the values from the <span class="coding">Name </span>column label as row labels.  The argument inplace=True updates the df DataFrame in place and the drop=True argument drops the <span class="coding">Name </span>column for the DataFrame.

With this defined index, the <span class="coding">.loc</span> indexer uses the <span class="coding">Name </span>column values to return rows rather than using row position.

Notice how the third <span class="coding">print</span>() function displays the values for the <span class="coding">Name </span>column as row labels in the left-most column of the output.  The syntax:
print(df.index) 
returns the index values as a Python list.  An index may have non-unique values which we illustrate with this example.  Some DataFrame operations require the index keys be in sorted order while others may require unique values.  We cover the details for sorting in Chapter 5, Pandas Data Management.  Chapter 9, Time Series Analysis covers details for unique index values.

With an index in place as row labels we can slice rows using the <span class="coding">.loc</span> indexer.  As well, columns can be sliced with the <span class="coding">.loc</span> indexer since they have labels (i.e. names). 
The syntax for the <span class="coding">.loc</span> indexer is:
df.loc[row selection, column selection]
The row selection is listed first, separated by a comma (,) followed by the column selection. For both the row or column selection a colon (:) is used to request a range of items.  Consider Listing 4-10, Return Row Slices.
Listing 4-10. Return Row Slices

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
This example slices rows beginning with the row labeled Patton and ending with the row labeled Aden inclusive.  The empty value for the column selector, following the comma (,) implies all columns.  The same DataFrame can be returned by stating the column selector explicitly with the syntax:

df.loc['Patton' : 'Aden', 'District' : 'After']
Listing 4-11, Return Row and Column Slices, illustrates supplying a single label to the row selector followed by a Python list of labels as the column selector.
Listing 4-11. Return Row and Column Slices

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df.loc['LeMay', ['Before','After']]
       Before  After
Name
LeMay      35     69
LeMay      35     69
```
Notice how the row labels are not unique.

#### Conditionals
Listing 4-12, Return Rows Conditionally, illustrates returning rows and columns based on a Boolean comparison.  
Listing 4-12. Return Rows Conditionally

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df.loc[(df['Sector'] == 'West') & (df['Before'] > 20)]
      District Sector  Before  After
Name
Jurat        I   West      51     55
LeMay      III   West      35     69
LeMay      III   West      35     69
```

The Boolean comparisons are enclosed with parentheses ( ) and utilize any of the Comparision operators listed on Table 2.2,  Python Comparison Operations from Chapter 2.  In this example the Boolean comparisons contain two predicates; the first is (df['Sector'] == 'West') and the second is (df['Before'] > 20). The Boolean operator & (and) joins the predicates and therefore both must return True in order to meet the row selection criteria.

Note the sytax differences between Listing 4-11, Return Row and Column Slices and 4.12, Return Rows Conditionally.  In the former rows are sliced based on labels.  The latter uses the df['Sector'] and df['Before'] to designate column names for the conditional expression.
Suppose we wish to sub-set rows based on the last letter of the value for the <span class="coding">Name </span>column ending with the letter ‘r’.  Listing 4-13, Conditionally Return Rows with String Manipulation combines the <span class="coding">.loc</span>() indexer with the .str.endswith attribute to satisfy the request.
Listing 4-13. Conditionally Return Rows with String Manipulation

<div class="code-head"><span>code</span> Conditionally Return Rows with String Manipulation.py</div>

```python
df.loc[df['Name'].str.endswith("r"), ['District', 'Sector']]
KeyError: 'the label [Name] is not in the [index]'
```
Unfortunately, this example raises a KeyError since the column <span class="coding">Name </span>was dropped when the df.index was initially created in Listing 4-9, Add Index to <span class="coding">DataFrame</span>.  Note this error message is truncated here.  One remedy for the KeyError  is to ‘return’ the <span class="coding">Name </span>column using the .reset_index function illustrated in Listing 4-14 Drop <span class="coding">DataFrame</span> Index.
Listing 4-14. Drop DataFrame Index

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
calls the .reset_index method to ‘drop’ the index and return the <span class="coding">Name </span>column as one of the columns on the df <span class="coding">DataFrame</span>.  The inplace = true argument performs the operation in-place.  The second line in the program chains the .str.endswith("r") attribute to the <span class="coding">Name </span>column and returns True for any value whose last letter in the sequence is ‘r’. 
The purpose of this example is to simply illustrate resetting an index with the reset_index method.  The more Pythonic remedy for the KeyError illustrated in Listing 4-13 is:
df.loc[df.index.str.endswith('r'), ['District', 'Sector']]
The analog SAS program is shown in Listing 4-15, Conditionally Return Observations with String Manipulation.
Listing 4-15. Conditionally Return Observations with String Manipulation

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
Figure 4-3, Last Name Ends with ‘r’, displays the output from PROC SQL.
 
Figure 4-3. Last Name Ends with ‘r’
Another method for conditional testing is to combine the <span class="coding">.loc</span> indexer with the isin attribute.  The isin attribute returns a Boolean indicating if elements in the <span class="coding">DataFrame</span> column are contained in a Python list of values.  As an example, consider Listing 4-16, Select Rows with isin List of Values.
Listing 4-16, Select Rows with isin List of Values

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
df.set_index('Name', inplace=True)

to enable slicing with labels using the <span class="coding">.loc</span> indexer.
Listing 4-17, SAS IN Operator illustrates the same capability using the IN operator.  The IN operator performs an implied truth test by including values from a list that match values from the sector variable.  The IN operator is also valid with an IF  statement in a Data Step.  Figure 4-4, IN Operator Results displays the subset row.  
Listing 4-17. SAS IN Operator

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
4 proc sql;
5   select *
6   from df
7 where sector in ('North', 'South');
8 quit;
```
 
Figure 4-4. IN Operator Results
#### Updating
The .loc indexer can update or set values (the term used with Pandas documentation).  Consider Listing 4.18, Set Values Matching a List of Labels.
Listing 4-18. Set Values Matching a List of Labels

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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
The first call to the <span class="coding">.loc</span> indexer supplies a Python List of <span class="coding">Name </span>labels for three individuals along with their corresponding After values and returns a Series.  Recall that a Series is analogous to a single <span class="coding">DataFrame</span> column.  The second call to the <span class="coding">.loc</span> indexer sets (updates) the After column for each of the labels in the Python list:
 ['Patton', 'Jurat', 'Gupta']

The SAS analog is illustatred in Listing 4-19, IN Operator Conditionally Select Rows.  
Listing 4-19. IN Operator Conditionally Select Rows

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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

Setting values for an entire <span class="coding">DataFrame</span> column is illustated in Listing 4-20, Set Values for a Column.
Listing 4.20. Set Values for a Column

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

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

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
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

The input dataset df uses the end = dataset option to detect the last observation reading the df dataset.  The end = dataset option initializes a variable’s value to 0 and is set to 1 when the last observation is read.  Sub-setting IF statements are used to output the first and last observation to the output dataset df1.  The output dataset is displayed in Figure 4-5, First and Last Observation.  The noobs option for PROC PRINT supresses the display of the SAS observation number contained in the automatic SAS variable <span class="coding">_n_</span>.

 
Figure 4-5. First and Last Observation
The <span class="coding">.iloc</span> indexer accomodates a Python list of integers as well as a slice object to define row and column selections.  Listing 4-23 <span class="coding">.iloc</span> Using List and Slice Object, illustrates combining these selectors.  
Listing 4-23 .iloc Using List and Slice Object

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
>>> df.reset_index(inplace = True)
>>> df.iloc[[2, 10, 12], :2]
        Name District
2   Williams        I
10   Haskins      III
12     LeMay      III
```
While it is possible to call the <span class="coding">.iloc</span> indexer with an index preset, in order to understand the effect, the <span class="coding">Name </span>index is dropped with:
df.reset_index(inplace = True)
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
