---
layout: post
tag : Levenshtein
category: "Python for SAS"
title: "Match company names"
description: getting financial data from difference sources require matching company names
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Plotting all the (important) drivers in one figure](#plotting-all-the-important-drivers-in-one-figure)
- [Reference](#reference)


# Cleaning names


<div class="code-head"><span>code</span>plot model driver.py</div>

```python

import Levenshtein

def match_names(column1, column2):
    matches = {}
    for name1 in column1:
        min_distance = float('inf')
        match = None
        for name2 in column2:
            distance = Levenshtein.distance(name1, name2)
            if distance < min_distance:
                min_distance = distance
                match = name2
        matches[name1] = match
    return matches

# Example usage:
column1 = ["John", "Jane", "Michael"]
column2 = ["Jon", "Janet", "Michele"]
matches = match_names(column1, column2)

for name1, match in matches.items():
    print(f"{name1} matched with {match}")

```




!(multi facet line plot)[https://seaborn.pydata.org/_images/faceted_lineplot.png]

<div class="code-head"><span>code</span>plot model driver.py</div>
```python

>>> color_nz = ‘#2CA02C’
>>> color_cp = ‘#D62728’
>>> temp = df[drivers + [‘x’, ‘cate’]].melt(id_vars=+ [‘x’, ‘cate’]) # Reshape the data so that your data is long and can use sns.relplot.

>>> g = sns.relplot(data = temp, x=’x’, y=’value’, col=’variable’, kind = ‘line’, height=5, aspect=.75, facet_kws=dict(sharey=False), col_wrap=3, palette=[color_cp, color_nz])
>>> for ax in g.axes.flatten():
	ax.set_title(ax.get_title()[10:])
	ax.set_ylabel(“”)

>>> for ax in g.axes.flatten():
	ax.set_title(ax.get_title()[10:])
	ax.set_ylabel(“”)
>>> plt.suptitle(“%s”%company, fontweight=’bold’)
>>> plt.subplots_adjust(top=0.92, right=0.82, hspace=0.32, wspace=0.2)
>>> plt.savefig(os.path.join(“images”, “%s rating change and drivers.png”%(company))
```

We can look at another example.  It creates a list of lambda functions, with the possible intention of a list of functions as [lamba x: x + 1, lambda x: x + 2, ..., lambda x: x + 9].  But unfortunately, in this case, lambda function holds on to the expression of $$i$$ and won't undate it until the end.  So we end up with a list of lambda functions, all of them are lamba x: x + 9

```python
incremental = [lambda x: x + i for i in range(10)]
print(incremental[0](2))
# 11
print(incremental[-1](2))
# 11
```


# Reference

[Line plots on multiple facets](https://seaborn.pydata.org/examples/faceted_lineplot.html)

[Python FAQ Why do lambdas defined in a loop with different values all return the same result?](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result)

[python accumulate official documentation](https://docs.python.org/3/library/itertools.html#itertools.accumulate)

[Excel lambda-the-ultimatae-excel-worksheet-function](https://www.microsoft.com/en-us/research/blog/lambda-the-ultimatae-excel-worksheet-function/)


import Levenshtein

def match_names(column1, column2):
    matches = {}
    for name1 in column1:
        min_distance = float('inf')
        match = None
        for name2 in column2:
            distance = Levenshtein.distance(name1, name2)
            if distance < min_distance:
                min_distance = distance
                match = name2
        matches[name1] = match
    return matches

# Example usage:
column1 = ["John", "Jane", "Michael"]
column2 = ["Jon", "Janet", "Michele"]
matches = match_names(column1, column2)

for name1, match in matches.items():
    print(f"{name1} matched with {match}")
