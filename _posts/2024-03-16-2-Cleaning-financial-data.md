---
layout: post
tag : data cleaning, strings
category: "Python for SAS"
title: "Cleaning financial data"
description: getting financial data from difference sources require matching company names
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---

This is a long overdue post.

# Cleaning values

Financial data are often shown as strings in Python, although they are meant to be numbers. 
1. Remove common characters such as "$", ",", "()", which is used to express indicate negative number
2. Then use <span class='coding'>pd.to_numeric() </span> 
<span class="coding">.rstrip</span> or <span class="coding">.lstrip</span>:  Both will remove strings given from right or left, respectfully.  If nothing is given, then remove white space. 

> Note: All the string methods used below are not in-place operations.   Therefore, do not use <span class="coding">lstrip("$")</span> in example below.  Because the operations are not in place, it does not see "$" in the leftmost position. 

<span class='coding'>.replace(",", "") </span> by default will remove "," no matter how many commas there are in the string.   If the optional argument count is given, only the first count occurrences are
replaced.

<div class="code-head"><span>code</span>clean values.py</div>

```python
>>> ss = "($123,456)"
>>> ss.replace("(", "-").rstrip(")").replace("$", "").replace(",", "")
Out: '-123456'
>>> ss = "($123,456,7,8,,,,9)"
>>> pd.to_numeric(ss.replace("(", "-").rstrip(")").replace("$", "").replace(",", ""))
Out: -123456789

```

When we have a lot of data to convert, we may or may not want to do it in a hurry.  We can hurry up and convert everything in one go if we know the data well.  But the fact is that you should never assume you know the data well, unless you built that data.


<div class="code-head"><span>code</span>clean data 1.py</div>

```python

def clean_data_1(data, col_list, string):
    """
    attacking a particular string that's in your otherwise numeric data
    """
    for i in col_list:
        if data[i].dtype == 'object':
            if any("%s"%string in value for value in data[i] ):
                print("%s in %s"%(string,i))
            return
            else: data[col] = pd.to_numeric(data[col])
        else:
            continue
```

We can do it more thoroughly as shown below:

<div class="code-head"><span>code</span>clean_financial_data.py</div>

```python
def clean_financials(ss):
    if pd.isna(ss):
        return ss
    ss = str(ss).strip() # remove white space
    if ss.startswidth("(") and ss.endswidth(")"): # negative number expressed as in parenthesis
        ss = ss[1:-1] # remove first and last character
        ss = ss.replace("$", "").replace('%', '').replace('x', ''):
        ss = "-" + ss # add negative sign
    else:
        ss = ss.replace("$", "").replace('%', '').replace('x', ''):
    return ss

def clean_fiancial_data(data, col_list):
    for col in col_list:
        data[col] = data[col].apply(clean_financial_data)
        data[col] = pd.to_numeric(data[col])  # can add errors='coerce' to force remaining non-numbers to na
    return data
```

```

