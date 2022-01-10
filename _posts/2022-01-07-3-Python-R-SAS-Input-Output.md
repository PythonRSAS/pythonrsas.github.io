---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Data Input and Output"
description: comparing Python, R and SAS input and output, including quick loading of prepackaged data
author: Sarah Chen
image: images/posts/photos/IMG-0686.jpg

---
![](/images/posts/photos/IMG-0683.jpg)
Work in Progress.  Check back later. 
- [Inputting data](#inputting-data)
  - [Load data that comes with IDE or libraries](#load-data-that-comes-with-ide-or-libraries)
    - [Loading pre-packaged data into Python](#loading-pre-packaged-data-into-python)
    - [R](#r)
    - [Load SASHelp data](#load-sashelp-data)
  - [External data](#external-data)
    - [Import external data to Python](#import-external-data-to-python)
    - [Import external data to R](#import-external-data-to-r)
    - [Import data in SAS](#import-data-in-sas)
- [Take a first look at the data](#take-a-first-look-at-the-data)
  - [Python](#python)

# Inputting data
R has different dialets.  It is more versatile and fragmented than SAS and Python.  Its different "dialets" can be confusing for someone who does not use it often.  

In SAS, <span class="coding">PROC IMPORT</span> imports external data.  Inline data can be created using <span class="coding">DATA</span> step.  That is about 99% of the cases already.  

In Python, we generally use the pandas library to bring in data. 

## Load data that comes with IDE or libraries
Loading data that comes with IDE or libraries allows me to test code and fast prototype. 

### Loading pre-packaged data into Python
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
### R
<span class="coding">data(mtcars)</span> can be used to load any dataset that comes with RStudio.  This makes testing code fast and easy.  For example, <span class="coding">data("mtcars")</span> loads the cars dataset, and <span class="coding">data("iris")</span> loads the iris dataset. 

### Load SASHelp data
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

## External data
### Import external data to Python
Most of the time, I use the pandas library to import data.  See [Input/output](https://pandas.pydata.org/docs/reference/io.html) for a comprehensive list of functions for a wide variety of formats of data. 

<div class="code-head"><span>code</span>input.py</div>

```python
pandas.read_csv(filepath_or_buffer, index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False,  thousands=None, decimal='.',  encoding=None,  low_memory=True, float_precision=None)

pandas.read_excel(io, sheet_name=0, header=0, names=None, index_col=None, usecols=None, dtype=None,  true_values=None, false_values=None, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, parse_dates=False, date_parser=None, thousands=None, comment=None, skipfooter=0, convert_float=None, mangle_dupe_cols=True, storage_options=None)

pandas.read_sas(filepath_or_buffer, format=None, index=None, encoding=None, chunksize=None, iterator=False)
```
### Import external data to R
<span class="coding">read.table</span>is the principal means of reading tabular data into R. For details, please see [read.table](https://www.rdocumentation.org/packages/utils/versions/3.6.2/topics/read.table)

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
read.csv(file, header = TRUE, sep = ",", quote = "\"",
         dec = ".", fill = TRUE, comment.char = "", …)

read.csv2(file, header = TRUE, sep = ";", quote = "\"",
          dec = ",", fill = TRUE, comment.char = "", …)

read.delim(file, header = TRUE, sep = "\t", quote = "\"",
           dec = ".", fill = TRUE, comment.char = "", …)

read.delim2(file, header = TRUE, sep = "\t", quote = "\"",
            dec = ",", fill = TRUE, comment.char = "", …)
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
### Import data in SAS
<div class="code-head"><span>code</span>firstLook.sas</div>

```sas
PROC IMPORT 
```

# Take a first look at the data

After having loaded the data, we can use the following to take a quick look before further processings.
- [Inputting data](#inputting-data)
  - [Load data that comes with IDE or libraries](#load-data-that-comes-with-ide-or-libraries)
    - [Loading pre-packaged data into Python](#loading-pre-packaged-data-into-python)
    - [R](#r)
    - [Load SASHelp data](#load-sashelp-data)
  - [External data](#external-data)
    - [Import external data to Python](#import-external-data-to-python)
    - [Import external data to R](#import-external-data-to-r)
    - [Import data in SAS](#import-data-in-sas)
- [Take a first look at the data](#take-a-first-look-at-the-data)
  - [Python](#python)
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