---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "GroupBy Processing"
description: Data processing using Python and SAS.
author: Sarah Chen
# image: https://www.audubon.org/sites/default/files/styles/hero_image/public/sfw_nationalgeographic_1517960.jpg?itok=F5pikjxg
---
We cover the following topics:

**1.GroupBy**

**2. Iteration Over Groups**

**3. GroupBy Summary Statistics**

**4. Filtering by Group**

**5. Group by Column with Continuous Values**

**6. Transform Based on Group Statistic**

**7. Pivot**

### GroupBy
A common pattern for data analysis familiar to SAS users is BY-group processing.  SAS defines BY-group processing as:
…a method of processing observations from one or more SAS data sets that are grouped or ordered by values of one or more common variables. The most common use of BY-group processing in the <span class="coding">DATA</span> step is to combine two or more SAS data sets by using the BY statement with a <span class="coding">SET</span>, <span class="coding">MERGE</span>, <span class="coding">MODIFY</span>, or <span class="coding">UPDATE</span> statement. 

In pandas, the term groupby means the following three steps:
1. Splitting vales into groups based on some criteria
2. Applying a function to each of these groups
3. Combining the results into a data structure

Within the Apply step we often wish to do one or more of the following actions:
- Count, sums, means, max, or other statistics
- Custom functions such as:
    -  Normalizing data within the group,
    -  Replace missing values with a value derived from each group,
    -  Filter to discard some groups based on group-wise calculation.

To accomplish these types of operation the Pandas library includes a <span class='coding'>GroupBy</span> object.
When a <span class='coding'>GroupBy</span> object is created it contains instructions to map rows and columns to named groups.  

A crucial benefit for Pandas <span class='coding'>GroupBy</span> is eliminating the need to handle each of the resulting splits, or sub-groups explicitly.  Instead <span class='coding'>GroupBy</span> applies operations to the entire DataFrame often with a single pass of the data.  

The syntax for defining a GroupBy object is:
```python
DataFrame.groupby(by=None, axis=0, level=None, as_index=True, 
sort=True, group_keys=True, squeeze=False, observed=False, 
**kwargs) 
```

As an example,

<div class="code-head"><span>code</span>Create GroupBy gb.py</div>

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
The gb object is defined as a groupby object using the District column as the by = parameter.  In this case the three unique values from the District column define the groups. 

Notice a DataFrameGroupBy object is returned rather than a DataFrame.  The gb object is analagous to a SQL <span class="coding">view</span> containing instructions for executing SQL statement to materialize rows and columns when the <span class="coding">view</span> is applied.  

The SQL analogy is:
```sas
 CREATE VIEW GB as
   SELECT distinct District
                 , mean(Before)
                 , sum(After)
   FROM DF
   GROUP BY District
```

Only when the groupby object is applied are results produced.  Consider the example below:

<div class="code-head"><span>code</span> Applying sum over GroupBy.py</div>

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

Note:
* All numeric columns in the underlying df DataFrame are grouped by the unique levels from the District column and then summed within each group.  Of course, the sum method is just one possibility here.  
* ???Later in this chapter we will illustrate examples for selecting individual columns and applying different aggregation methods as well as applying nearly any valid DataFrame operation????
* The DataFrame returned after a groupby-apply operation is indexed with the by-column.  


<div class="code-head"><span>code</span> Create DataFrame from GroupBy Object.py</div>

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
The d_grby_sum DataFrame is indexed with values from the District column.  GroupBy objects also have attributes allowing examination of their keys and groups.  These groupby object attributes are illustrated in the following example, Keys and Groups for GroupBy Object.

<div class="code-head"><span>code</span> Keys and Groups for GroupBy Object.py</div>

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
The syntax  <span class="coding">gb.groups.keys()</span> returns a Python list for the keys’ values.  The syntax  gb.groups returns a Python dictionary of key/value pairs for each key, mapped to a group, along with a corresponding list of values indicating which rows compose a given group.  In this example, rows 0, 1, 2, and 3 define the groupby level for District = 'I'.

Consider the following example, Summary by District illustrates similar logic calling <span class="coding">PROC SUMMARY</span> to create a ‘grouped’ dataset summing the numeric variables by district.

<div class="code-head"><span>code</span> Summary by District.sas</div>

```sas
data df;
 infile cards dlm = ',';
 length district $ 3
        sector   $ 5
        name     $ 8;
 input  district $
        sector   $
        name     $
        before
        after
        age;
 datalines;
 I,   North, Patton,   17,  27,  22
 I,   South, Joyner,   13,  22,  19
 I,   East,  Williams, 111, 121, 29
 I,   West,  Jurat,    51,  55,  22
 II,  North, Aden,     71,  70,  17
 II,  South, Tanner,   113, 122, 32
 II,  East,  Jenkins,  99,  99,  24
 II,  West,  Milner,   15,  65,  22
 III, North, Chang,    69,  101, 21
 III, South, Gupta,    11,  22,  21
 III, East,  Haskins,  45,  41,  19
 III, West,  LeMay,    35,  69,  20
 III, West,  LeMay,    35,  69,  20
 ;

 proc summary data=df nway;
     class district;
     var before after age;
     output out=gb_sum (drop = _TYPE_ _FREQ_)
        sum=;
  run;
```


#### Iteration Over Groups
The GroupBy object supports iterating over the defined groups.  As an example, consider the example below, Iterate Over Groups.

<div class="code-head"><span>code</span> Iterate Over Groups.sas</div>

```sas
>>> gb = df.groupby(['District'])
>>> for name, group in gb:
...     print('Group Name===> ',name)
...     print(group)
...     print('='*47)
...
[Out]:
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
Note:
* In this example a for loop iterates over the GroupBy object to produce a custom report.  As we have seen previously, iterating manually over objects can be useful.
* However the apply method is a more productive alternative for applying methods and functions.

With SAS, the same report is easily produced using the <span class='coding'>Data</span> step by group processing as shown in the example below, Iterative By Group Processing.  While we could have called <span class="coding">PROC PRINT</span> for this example, the goal for the example is to illustrate how first.district and last.district behaviors for By Group processing.

<div class="code-head"><span>code</span> Iterative By Group Processing.sas</div>

```sas
 proc sort data = df presorted;
    by district;
data _null_;
file print;
   set df;
   by district;
 if first.district then
    put 'Group Name====> ' district /
         'District Sector    Name     Pre  Post  Age';
 put @1 district @10 sector @20 name
     @29 pre @34 post @40 age;

 if last.district then
    put '=========================================';
 run;
```
In general, SAS By Group processing is established with either <span class="coding">PROC SORT</span> or an ORDER BY statement in <span class="coding">PROC SQL</span>.  For Data step processing when a BY statement is encountered, SAS creates the automatic variables first.<by_variable> and last.<by_variable> to permit truth testing to control logic by identifying observations as first or last in the by group.  The statement fragment:
if first.district then

is a truth test with an implied Boolean evaluation of 0 for false and 1 for true.  In our example, the statement above can be also be written as:

if first.distrct = 1 then 

Similarly, pandas provisions the first and last methods for the groupby object as illustrated in the following example, Return First and Last Rows from GroupBy returns the first and last row respectively for each group.

<div class="code-head"><span>code</span> Return First and Last Rows from GroupBy.py</div>

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
As mentioned earlier a GroupBy feature is the ability to accept most methods applicable to a DataFrame by applying the methods to individual groups.  Consider the example below, Summary Statistics by Group.

<div class="code-head"><span>code</span> Summary Statistics by Group.sas</div>

```sas
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
This example illustrates how methods not specifically implemented for the GroupBy object are passed through allowing groups to call the method.  Here the DataFrame’s desribe method performs the aggregration describing values for each group. Due to page width limitations, only a portion of the actual output is presented here.
We can apply different aggregation methods to different columns defined by the GroupBy object.  In the following example, Applying sum over GroupBy the sum method is applied to all numeric columns.  Consider the following example, Different Statistics Over Group Columns illustrates different statistics applied to columns.

<div class="code-head"><span>code</span> Different Statistics Over Group Columns.py</div>

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
In the following example, By Group Statistics over Different Variable illustrates the same approach using SAS.

<div class="code-head"><span>code</span> By Group Statistics over Different Variable.sas</div>

```sas
4 proc summary data=df nway;
5    class district;
6    output out=gb_sum (drop = _TYPE_ _FREQ_)
7       mean(age)       = age_mean
8       median(before)  = bfr_median
9       sum(after)      = aft_sum
10      median(after)   = aft_median
11      std(after)      = aft_std;
12 run;
```
NOTE: There were 13 observations read from the data set WORK.DF.
NOTE: The data set WORK.GB_SUM has 3 observations and 6 variables.

```sas
13 proc print data = gb_sum noobs;
14 run;
```
In the example, By Group Statistics for Different Variables Ouput illustrates the output created by <span class="coding">PROC SUMMARY</span>.

#### Filtering by Group
A common coding pattern for data analysis is applying actions to a set of data based on a group’s statistic.  As an example, consider the example below, Group By Filtering on a Statistic.

<div class="code-head"><span>code</span> Group By Filtering on a Statistic.py</div>

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

```python
def std_1(x):
    return x['Age'].std() < 5
```
def is used to define a Python function followed by the function’s name; in this case std_1.  Inside this function, x is a local variable holding the group passed in when called.

A new DataFrame is created by by passing the std_1 function to filter method of the GroupBy object.

Notice how no rows are returned from the District column with a value of ‘II’.
#### Group by Column with Continuous Values 
Sometimes the desire is to use columns with continuous values as a GroupBy object.  Consider the case of age where these values are continuous.  To create a meaningful GroupBy object, the first step is mapping continuous values into ‘buckets’ and applying these binned values to a GroupBy operation.  The binned values are mapped using the apply method to create the GroupBy object.  This action allows aggregations to be performed based on group values determined by bin ranges formed with the Age column.  
Here we illustrate this pattern using the Pandas cut method for segmenting and sorting data values into bins.  Consider the following example, GroupBY Column With Continuous Values.

<div class="code-head"><span>code</span> GroupBY Column With Continuous Values.py</div>

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

```python
bins = [0, 25, 50, 75, 200]
gp_labels = ['0 to 25', '26 to 50', '51 to 75', 'Over 75']
```
assigns the ‘cut-points’ to the bins object as a Python list of values representing the upper and lower bounds for the bins created with the cut method.  The gp_labels object is another Python list of values holding the labels assigned to these bins.  Both these objects are passed to the to the cut method with the syntax:

```python
df['Age_Fmt'] = pd.cut(df['Age'], bins, labels=gp_labels)
```
defining the Age_Fmt column in the df DataFrame.  This assignment creates column values by calling the cut method for the df['Age'] column (with bins and labels defined).  Note that pd.cut uses the syntax  pd to refer to the <span class="coding">Name </span>for the Pandas library that is loaded into the namespace with:

import pandas as pd

The syntax:

df['Age'].groupby(df['Age_Fmt']).apply(stats).unstack()

creates the GroupBy object using unique values from the Age_Fmt column as the group’s levels and is attached to the df['Age'] column.  The apply method calls the defined function stats applying the statistics column values within each group.  The unstack method reshapes the returned object from a stacked form (in this case a Series object) to an unstacked form (a “wide” DataFrame).   

The same logic in SAS is shown in the following example, By Group With Continuous Variable.  In this example the aggregation functions for the age variable statistics are produced with <span class="coding">PROC SQL</span>.

<div class="code-head"><span>code</span> By Group With Continuous Variable.sas</div>

```sas
proc format cntlout = groups;
   value age_fmt
       0  - 25   = '0-25'
       26 - 50   = '26-50'
       51 - 75   = '51-75'
       76 - high = 'Over 75';
proc sql;
   select fmt.label      label = 'Group'
        , count(dat.age) label = 'Count'
        , min(dat.age)   label = 'Min'
        , max(dat.age)   label = 'Max'
        , mean(dat.age)  label = 'Mean'
from
   groups as fmt 
      left join df as dat
      on fmt.label = put(dat.age, age_fmt.)
group by fmt.label;
quit;
```
<span class='coding'>PROC FORMAT</span> provides similar binning logic as the cut method in the Python example, GroupBy Continuous Column.  The cntlout = groups option outputs a dataset containing several variables including the label variable holding the value labels for the user-defined agefmt. format.  The aggregation functions are applied to the age variable using <span class="coding">PROC SQL</span>.  <span class="coding">PROC SQL</span> uses a left join to combine rows on the label column from the groups table (created with cntlout =) with rows from the aggregation functions applied to the age column from the df dataset.  The output from <span class="coding">PROC SQL</span> is displayed in the example Group By with Continuous Values.
 
#### Transform Based on Group Statistic
Up to this point the GroupBy objects return DataFrames with fewer rows than the original DataFrame.  This is to be expected since GroupBy objects are commonly used in aggregation operations.  There are cases where you wish to apply a transformation based on group statistics and merge the transformed version with the original DataFrame.  Calculating a z-score is an example illustrated in the example below Transform Based on GroupBy Statistic.

<div class="code-head"><span>code</span> Transform Based on GroupBy Statistic.py</div>

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
The logic to compute the z-score is accomplished by creating the z DataFrame with a GroupBy object using the syntax:

z = df.groupby('District').transform(lambda x: (x - x.mean()) / x.std())

In this example a lamdba expression is used to create an anonymous, or in-line function defining the z-score calculation.  Like the def function this expression creates a function, but does not provide it a name.  Hence, it is known as an anonymous function.

The transform function computes the z-score for rows within each group using the group’s computed mean and standard deviation.  The transform function returns a DataFrame the same shape as the input DataFrame making it useful for combining the two together.

Because Pandas allows the same name for multiple columns the rename attribute is applied to the z DataFrame passing a Python dictionary of key/value pairs where the key is the old column name and the value is the new column name.  The syntax:

df1 = pd.concat([df, z], axis = 1)

creates the df1 DataFrame by concatenating the df and z DataFrames along the columns with the axis = 1 argument.  We cover the details for Pandas concatenation and joins in Chapter 5, Advanced Data Management.

In the following example, Transform Based on By Group Statistic illustrates the same logic in SAS.  <span class="coding">PROC SUMMARY</span> is called to create the intermediate variables used for calculating the z-scores.  <span class="coding">PROC SORT</span> is called to sort the df dataset and the z_out dataset produced by <span class="coding">PROC SUMMARY</span> using the variable district as the sort keys. 

<div class="code-head"><span>code</span> Transform Based on By Group Statistic.sas</div>

```sas
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
14 proc sort data = df presorted;
15    by district;
16
17 proc sort data = z_out presorted;
18    by district;
19
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

31 proc print data=z_df(obs=6) noobs;
32    var name pre z_pre post z_post age z_age;
33 run;

```
The final step uses a Data step to merge the df and z_out datasets on the district sort key and performs the z-score calculations.  The indermediate variables from the z_out dataset are dropped with a DROP list.
 
### Pivot
Pandas provide the pivot_table function to create speadsheet-style pivot tables.  The pivot_table function enables aggregation of data values across row and column dimensions.   As we will see shortly, pivot_table function not only provides a multi-dimensional view of your data, but it turns out to be a convenient method to apply a <span class="coding">MultiIndex</span> to DataFrame rows and columns.

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
In order to appreciate the flexibility afforded by the pivot_table funtion, the script includes output from info method indicating the DataFrame has 2,823 rows and 10 columns.  

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
```
The argument fill_value = 0 replaces the NaN’s in the original output with zeros. The aggfunc= argument passes a Python Dictionary to associate column names (key) with a corresponding aggregation method (value).  In this example, the Amount column is aggreated using np.means and the Quantity column is aggregated using np.sum.

The pivot_table function syntax is easy to understand and provides a straight-forward solution for a variety of analysis problems.  Consider the following example Sales by Year Over Territory.  

<div class="code-head"><span>code</span> Rolling Count-based Window vs Time-based Window for Regular DatetimeIndex.py</div>

```python
pd.pivot_table(df2,values     = ['Amount'],
                   columns    = ['Territory'],
                   index      = ['Year', 'Status'],
                   fill_value = 0,
                   aggfunc    = (np.sum))
```
From, Output of Sales by Year Over Territory shows that the EMEA territory has an usually high amount of cancellations compared to the rest of the organization.  

To produce the same report with SAS requires multiple steps after the .csv file is read with <span class="coding">PROC IMPORT</span>.  The task is to summarize the amount variable and transpose the territory variable’s unique values into variables.  The steps are:

1.  Sort the sales_detail dataset created with <span class="coding">PROC IMPORT</span> by the territory variable.

2.  Summarize the sales_detail dataset by territory for the amount variable with <span class="coding">PROC SUMMARY</span>.  Output summary as sales_sum dataset.

3.  Sort the sales_sum dataset by the variables year status.

4.  Transpose the sales_sum dataset on the territory variable (<span class="coding">ID</span>) by year status with <span class="coding">PROC TRANSPOSE</span>.  Create a transposed dataset called sales_trans.

5.  Print the sales_trans dataset using the SAS-supplied dollar13.2 format.

 
### Summary

In this chapter we discussed the role for indexing and hierarchical indexing as a means for providing labels for DataFrame rows and columns.  We introduced in the three indexers along with slicers to return sub-sets from a DataFrame:

1.  [ ] operator

2.  <span class="coding">.loc</span> indexer for slicing along rows and columns using labels

3.  <span class="coding">.iloc</span> indexer for slicing along rows and columns based on a values position along an index
We examined how to apply a range of methods to the subset DataFrames to perform common data manipulation methods for analysis.  
We provide a detailed discussion on the GroupBy object for split-apply-combine operations.  We also provided a general introduction to pivot tables.  Together these examples lay the foundation for Chapter 5, Advanced Data Management where we examine joining DataFrames through concatenation and merging methods.
