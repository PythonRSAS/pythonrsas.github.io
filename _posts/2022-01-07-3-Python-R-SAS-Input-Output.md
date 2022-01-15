---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Data Input and Output"
description: comparing Python, R and SAS input and output, including quick loading of prepackaged data
author: Sarah Chen
image: images/posts/photos/IMG-0686.jpg

---
![](/images/posts/photos/IMG-0686.jpg)
Work in Progress.  
- [Load data that comes with IDE or libraries](#load-data-that-comes-with-ide-or-libraries)
  - [Loading pre-packaged data into Python](#loading-pre-packaged-data-into-python)
  - [Load prepackaged data to R](#load-prepackaged-data-to-r)
  - [Load SASHelp data](#load-sashelp-data)
- [External file](#external-file)
  - [Import external file to Python](#import-external-file-to-python)
    - [Overview](#overview)
    - [read() with open()](#read-with-open)
    - [pandas.read_](#pandasread_)
    - [Reading larger files in Python](#reading-larger-files-in-python)
  - [Import external file to R](#import-external-file-to-r)
    - [read.table](#readtable)
    - [data.table](#datatable)
  - [Import data in SAS](#import-data-in-sas)
- [First glance](#first-glance)
  - [Python](#python)


# Load data that comes with IDE or libraries
Loading data that comes with IDE or libraries allows me to test code and fast prototype. 

## Loading pre-packaged data into Python
Working with Python, I use Ipython shell and VSCode.  Neither of them come with any datasets. To load some well-known datasets quickly, first need to import one of those libraries that packaged with them. 
```python
# variable and target together
In [1]: import seaborn as sns
   ...: iris = sns.load_dataset("iris")
   ...: iris.head()
      sepal_length  sepal_width  petal_length  petal_width species
0         5.100        3.500         1.400        0.200  setosa
1         4.900        3.000         1.400        0.200  setosa
2         4.700        3.200         1.300        0.200  setosa
3         4.600        3.100         1.500        0.200  setosa
4         5.000        3.600         1.400        0.200  setosa
# as an array
In [2]: from sklearn.datasets import load_iris
   ...: data = load_iris()
   ...: data.target[[10, 25, 50]]
   ...:
   ...: list(data.target_names)
   ...:
Out[2]: ['setosa', 'versicolor', 'virginica']
# as a pandas DataFrame
In [5]: X,y=load_iris(return_X_y=True, as_frame=True)

In [6]: type(X)
Out[6]: pandas.core.frame.DataFrame

In [7]: X.head()
Out[7]:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
0              5.100             3.500              1.400             0.200
1              4.900             3.000              1.400             0.200
2              4.700             3.200              1.300             0.200
3              4.600             3.100              1.500             0.200
4              5.000             3.600              1.400             0.200
```
## Load prepackaged data to R
<span class="coding">data()</span> can be used to load any dataset that comes with RStudio.  This makes testing code fast and easy.  For example, <span class="coding">data("mtcars")</span> loads the cars dataset, and <span class="coding">data("iris")</span> loads the iris dataset. 

## Load SASHelp data
There are many famous datasets that comes with the sas. See [Sashelp Data Sets - SAS Support]https://support.sas.com/documentation/tools/sashelpug.pdf).  <span class="coding">data=sashelp.iris </span> will automatically load the data. 
<div class="code-head"><span>code</span>existing data.sas</div>

```sas
proc contents data=sashelp.iris varnum;
ods select position;
run;
title "The First Five Observations";
proc print data=sashelp.iris(obs=5) noobs;
run;

```

# External file

## Import external file to Python
### Overview
There are many ways to import data into Python.  Below is an overview, and is by no means exhaustive:
1. Python build-in functions <span class="coding">read()</span>, <span class="coding">readline()</span>, and <span class="coding">readlines()</span> for small files. 
2. The <span class="coding">csv </span> library, which I have never used. 
3. The <span class="coding">pandas </span> library, which I use all the time. 
4. <span class="coding">dask.dataframe()</span> splits big pandas DataFrame into many along index.
5. [datatable](https://datatable.readthedocs.io/en/latest/) for  big 2D data frames. 
### read() with open()
The basic syntax of is:
<span class="coding">open('file','mode')</span>. 
To use the <span class="coding">read()</span> function, the file first needs to be open by calling the <span class="coding">open()</span>built-in function, which has two parameters: the path to the file and an optional argument to indicate whether <span class="coding">'r'</span> (for reading) or <span class="coding">'w'</span> (for writing).

<div class="code-head"><span>code</span>read_open.py</div> 

```python
with open('df4.csv', 'r') as reader:
    # Read & print the entire file
    print(reader.read()) # print the entire file
# ,event,trial,freq
# 0,no,control,0
# 0,no,control,0
# ...
# 0,no,control,0
with open('df4.csv', 'r') as reader:
    # Read & print the first line
    print(reader.readline())
Out:,event,trial,
reader.close() # close after read to prevent unexpected errors

f=open('new.txt','w') # write to file. Creates file if not existed
f.write('hello')
f.close()
f=open('new.txt','r')
f.read()
Out: 'hello'
f=open("new.txt", "a+")^M
for i in range(2):^M
     f.write("\nAppended line %d" % (i+1))
f.close()
f=open("new.txt","r")
print(f.read())
# hello
# Appended line 1
# Appended line 2
```
### pandas.read_
Most of the time, I use the pandas library to import data.  See [Input/output](https://pandas.pydata.org/docs/reference/io.html) for a comprehensive list of functions for a wide variety of formats of data.  The read_csv, and other pandas read functions take many parameters.  Those that I have used are listed below: 
```python
pandas.read_csv(filepath, index_col=None, usecols=None, dtype=None, engine=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False,  thousands=None, decimal='.',  encoding=None,  low_memory=True, float_precision=None)

pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, dtype=None,  true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)

pandas.read_sas(filepath_or_buffer, format=None, index=None, encoding=None, chunksize=None, iterator=False)
```
The first example below reads a record every 100 rows. We can change n for higher or lower frequencies.  <span class="coding">columns=lambda x: x.strip()</span> removes proceeding and trailing blanks. 
<div class="code-head"><span>code</span>input.py</div>

```python
#  Large file sample of every 100 rows
keep = ['CUST_ID', 'ZIP_CODE', 'CUST_NAME', 'Country','Segment1','Segment2','DATE','LGD']
n=100
per_raw_head = pd.read_csv(inputFolder+'/filename.csv', header=0, skiprows=lambda i:i%n!=0, engine='python').rename(columns=lambda x: x.strip())
list(per_raw_head)
# full data
df = pd.read_csv('./data/filename.csv', low_memory=False, usecols=keep, encoding='lating-1').rename(columns=lambda x:x.strip())
# SAS file 
df0 = pd.read_sas(inputFolder+'/filename.sas7bdat', encoding='latin-1')
```

### Reading larger files in Python
Most of Python runs on memory.  To work with large files, we need to split the files one way or another, divide and conquer.

Using <span class="coding">chunksize</span> option, we can somewhat reunite the pieces after they are imported into Python. I guess there has to be some memory saving mechanism in this process.  
```python
chunks = pd.read_csv(input_file, chunksize=100000)
data = pd.concat(chunks)
```
<span class="coding">dask.dataframe()</span>: A [Dask DataFrame](https://docs.dask.org/en/stable/dataframe.html) is a large parallel DataFrame composed of many smaller pandas DataFrames, split along the index. These pandas DataFrames may live on disk for larger-than-memory computing on a single machine, or on many different machines in a cluster. One Dask DataFrame operation triggers many operations on the constituent pandas DataFrames. 

> Advantage: most functions used with pandas can also be used with dask. 
See some examples [here](https://examples.dask.org/dataframe.html).

[datatable](https://datatable.readthedocs.io/en/latest/) is made for  big 2D data frames, up to 100GB). It supports out-of-memory datasets.  The Python <span class="coding">datatable</span> tries to mimic R's <span class="coding">data.table</span>, but does not have all the functions associated with its R sister yet.   

The <span class="coding">datatable.fread()</span> method reads exactly like its counterpart in R.  It has a consice and cleaner syntax than pandas.  There is no need to type:
- file extension such as ".csv"
- .iloc,.loc
But because it is an extra work to remember these, for now I prefer stay with pandas unless I have to. 

```python

import datatable as dt
In [10]: df = dt.fread('iris') # don't include file extension

In [11]: df
Out[11]:
    | sepal_length  sepal_width  petal_length  petal_width  species
    |      float64      float64       float64      float64  str32
--- + ------------  -----------  ------------  -----------  ---------
  0 |          5.1          3.5           1.4          0.2  setosa
  … |            …            …             …            …  …
149 |          5.9          3             5.1          1.8  virginica
[150 rows x 5 columns]

In [12]: df[:2,:]
Out[12]:
   | sepal_length  sepal_width  petal_length  petal_width  species
   |      float64      float64       float64      float64  str32
-- + ------------  -----------  ------------  -----------  -------
 0 |          5.1          3.5           1.4          0.2  setosa
 1 |          4.9          3             1.4          0.2  setosa
[2 rows x 5 columns]
In [14]: from datatable import f
In [18]: df[f.sepal_length>7.5,:] # cannot omit ":"
Out[18]:
   | sepal_length  sepal_width  petal_length  petal_width  species
   |      float64      float64       float64      float64  str32
-- + ------------  -----------  ------------  -----------  ---------
 0 |          7.6          3             6.6          2.1  virginica
 1 |          7.7          3.8           6.7          2.2  virginica
```

## Import external file to R
R has different dialets.  It is versatile and but also fragmented. I mainly use two methods:
 1. [read.table](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)
 2. [data.table](https://cran.r-project.org/web/packages/data.table/vignettes/datatable-intro.html)

### read.table
<span class="coding">read.table</span> is the principal means of reading tabular data into R. 

<div class="code-head"><span>code</span>input.r</div>

```r
read.table(file, header = FALSE, sep = "", quote = "\"'",
           dec = ".", numerals = c("allow.loss", "warn.loss", "no.loss"),
           row.names, col.names, as.is = !stringsAsFactors,
           na.strings = "NA", colClasses = NA, nrows = -1,
           skip = 0, check.names = TRUE, fill = !blank.lines.skip,
           strip.white = FALSE, blank.lines.skip = TRUE,
           comment.char = "#",
           allowEscapes = FALSE, flush = FALSE,
           stringsAsFactors = default.stringsAsFactors(),
           fileEncoding = "", encoding = "unknown", text, skipNul = FALSE)
```

<div class="code-head"><span>code</span>input.r</div>

```r
read.table(file,header=TRUE) # default separator is sep=" " is any white space
read.table(file, as.is=TRUE) # as.is=TRUE prevents string values from being converted to factors
read.csv("file", ,header=TRUE) # specifically for .csv files

load("myData.rdata") # load the dataset written with save
write.table(myData, file= "c:/documents/data/myData.csv", sep=',', row.names=F)

data(x) # loads specific dataset

read_feather(path, columns=NULL)
write_feather(x, path)
```
### data.table

<span class="coding">fread</span> stands for "fast read".  The speed efficiency gain becomes more obvious as the data size gets larger. 

<div class="code-head"><span>code</span>fread_speed.r</div>

```r
set.seed(1)
N <-1000000
df<- data.frame(matrix(runif(N), nrow=N))
write.csv(df, 'df.csv', row.names=F)

system.time({df<-read.csv('df.csv)}) # time it
system.time({df<-fread('df.csv)})
```

The imported data is stored as a <span class="coding">data.table</span>object, which is, by inheritance, a <span class="coding">data.frame</span> object as well. 

Conversely, a <span class="coding">data.frame</span> object can be converted to <span class="coding">data.table</span> by:
1. <span class="coding">data.table(df)</span>, or <span class="coding">as.data.table(df)</span>
2. <span class="coding">setDT(df)</span> converts in place. 

> <span class="coding">data.table</span> does not store rownames.  We need to separately preserve the row names.    
<div class="code-head"><span>code</span>data frame to data.table.r</div>

```r
data("mtcars")
mtcars$carname <- rownames(mtcars)
mtcars_dt <- as.data.table(mtcars)
class(mtcars_dt) 
"data.table" "data.frame"
```


## Import data in SAS

For data already in SAS format, all you have to is use libname statement to reference it. For other formats, the <span class="coding">PROC IMPORT</span> imports external data.  Inline data can be created using <span class="coding">DATA</span> step.  That is about 99% of the cases already.  
<div class="code-head"><span>code</span>firstLook.sas</div>

```sas
PROC IMPORT DATAFILE='/folders/myfolders/DATA/LoanStats3a.csv'
OUT=df
     	DBMS=CSV
     	REPLACE;
	GUESSINGROWS=50000;
RUN;
```
# First glance
## Python

<div class="code-head"><span>code</span>firstLook.py</div>

```python
df.info()
df.dtypes()
df.shape
df.head()
df.columns.tolist()
```

<div class="code-head"><span>code</span>firstLook.r</div>

```r

str(df) # similar to Python df.info() and SAS proc contents
dim(df)
head(df)
tail(df)
```
