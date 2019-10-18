---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Advanced Indexing"
description: Data processing using Python and SAS.
author: Sarah Chen
# image: https://www.audubon.org/sites/default/files/styles/hero_image/public/sfw_nationalgeographic_1517960.jpg?itok=F5pikjxg
---

**Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia consequuntur, provident nemo soluta similique, maiores sit dicta doloremque facere laudantium [Keras](https://keras.io/){:target="_blank"} Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque neque totam voluptatem porro accusantium id.**

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Velit, similique minima repudiandae. Voluptate pariatur iusto quo voluptatibus eum? [Keras](https://keras.io/){:target="_blank"} Lorem ipsum dolor sit. [github](https://github.com/fchollet/keras){:target="_blank"} page.

> **Update**: Lorem ipsum dolor. [end of life](https://pythonclock.org/), Aliquip ad magna laborum eu ut aute ut quis in veniam in. **Python3**.

##### Slicing Rows and Columns
Consider Listing 4-37, Slice Month 3 for all Years.   In this example we wish to return the 3rd month for each year.  Based on what we have learned about row and column slicing up to this point, it is reasonable to conclude the statement:

tickets.loc[(:,3),:]

is the appropirate syntax.  However, this syntax raises an error since it is illeagl to use a colon inside a tuple constructor.   Recall a tuple is an immutable sequence of items enclosed by parenthesis. As a convenience the Python’s built-in slice(None)function selects all the content for a level. In this case we want month level 3 for all years.  

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
The syntax slice(None) is the slicer for the Year column which includes all values for a given level, in this case, 2015 to 2018 followed by 3 to designate the level for month.  All columns are returned since no column slicer was given.
Another way to request this same sub-set is:
tickets.loc[(slice(None), slice(3,3)), :]
Consider the request for all years and months 2 and 3 as the row slicer in the following example:

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

idx_obj = ((slice(None), slice(2,3)), slice(None))
tickets.loc[idx_obj]
This syntax helps in further understanding exactly how the slicing operation is performed.  The first slice(None) requests all of the rows for the outer row label, years 2015 to 2018.  slice(2,3) returns months 2 and 3 for inner row label.  The last slice(None) requests all columns, that is, both the outer column Area and the inner column When.
Fairly quickly, however, we begin to have difficulty supplying a collection of tuples  for the slicers used by the <span class="coding">.loc</span> indexer.  Fortunately, Pandas provides the IndexSlice object to deal with this situation.  
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
The IndexSlice object provides a more natural syntax for slicing operations on MultiIndexed rows and columns.  In this case, the slice:
tickets.loc[idx[2015:2018, 2:3], :]
return years 2015:2018 inclusive on the outer level of the <span class="coding">MultiIndex</span> for the rows and months 2 and 3 inclusive on the inner level.  The colon (:) designates the start and stop positions for these row labels.  Following the row slicer is a comma (,) to designate the column slicer.  With no explicit column slices defined all columns are returned.  
Consider Listing 4-40, Slicing Rows and Columns, Example 1.


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

 

<div class="code-head"><span>code</span> Slicing Rows and Slicing Columns, Example 2.py</div>

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



<div class="code-head"><span>code</span> Conditional Slicing.py</div>

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
 

<div class="code-head"><span>code</span> DataFrame where Attribute.py</div>

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

  

<div class="code-head"><span>code</span> xs Cross Section, Example 1.py</div>

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

The the xs cross section method works along a column axis illustrated in 

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
In this example we return all rows for the level City.  The axis = 1 argument returns just the columns for the level City. 

Because the xs cross section method returns a <span class="coding">DataFrame</span> we can apply mathematical and statistical functions as attributes.  Listing 4-46, xs Cross Section, Example 3 returns the sum of all tickets issued during daylight hours in each of the three area.


<div class="code-head"><span>code</span> xs Cross Section, Example 3.py</div>

```python
>>> tickets.xs(('Day'), level='When', axis = 1).sum()
Area
City       178.0
Rural      164.0
Suburbs    178.0
```


<div class="code-head"><span>code</span> Summed Tickets Where Day over Area.py</div>

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
