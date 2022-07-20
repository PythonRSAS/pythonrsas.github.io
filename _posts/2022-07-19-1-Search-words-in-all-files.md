---
layout: post
tag : boring work, files
category: "Python for SAS"
title: "Search words in all files"
description: concatenate rows that contain some words from all files in data using Python
author: Sarah Chen
image: images/posts/photos/IMG_0867.JPG

---

Your very disorganized colleague needs help finding where certain data came from.  There are too many files and too many worksheets to manually go through.   

You want to help by using a little code. 

We use <span class="coding">glob.glob("*.xlsx")</span> to include all Excel files.  If the files contain some letters or numbers, we can add that to <span class="coding">glob.glob("*something*.xlsx")</span>

1. We append all sheets, except those in the no_sheet list, from all Exel files together in one single DataFrame
2. We define a helper function findWord, which finds words from DataFrame column by column because we don't know which column(s) may contain the words
3. We run the helper function on our one big DataFrame from step 1, and concatenate all results together


<div class="code-head"><span>code</span>mst_prim.py</div>

```python

import glob
import pandas as pd

# append all sheets from all Exel files together in one single DataFrame
filenames = glob.glob("*.xlsx") # all excel files
no_sheets = [] # put any sheets that are not needed for the search
d = []

for filename in filenames:
    ex1 = pd.ExcelFile(filename)
    for sheet_name in ex1.sheet_names:
        if sheet_name not in no_sheets:
            df = ex1.parse(sheet_name, index_col = None)
            d.append(df)

data = pd.concat(d, axis = 0, ignore_index = True)

# find words from DataFrame column by column
def findWord(data, words):
    '''
    append all rows containing words into lt and return lt
    '''
    lt = []
    for i in data.select_dtypes(include = ['object']).columns: # iterate through string columns
        temp = data.copy() # copy data because each time needs to drop na from the search column
        temp.dropna(subset = [i], inplace = True, how = 'any', axis = 0)
        temp = temp.reindex() # need to reindex otherwise cannot use boolean mask
        temp = temp[temp[i].str.contains(words,na = False)]
        if temp.shape[0] > 0: # if data is found then append it
            lt.append(temp)
    return lt

words = "secret | magic" # words containing either secret or magic
lt = findWord(data, words)
df_foundWord = pd.concat(lt, axis = 0, ignore_index = True)
```

We can preprocess the data a bit more: make all strings all lower case, for example, to make the search easier. 
