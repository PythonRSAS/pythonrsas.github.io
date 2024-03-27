---
layout: post
tag : multi facet, relplot, driver analysis
category: "Python for SAS"
title: "Multiple facet plot for driver analysis"
description: analyze model score by looking at all the drivers in one single plot
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Plotting all the (important) drivers in one figure](#plotting-all-the-important-drivers-in-one-figure)
- [Reference](#reference)


# Plotting all the (important) drivers in one figure
Does my model result make sense?  We check, and usually we check both the largest (most important) companies, and we check randomly. 
Let's start with following a simple exmaple from seaborn.  As my models are on credit ratings forecast based on various point in time scenarios, I am focusing on line plots. 

!(multi facet line plot)[https://seaborn.pydata.org/_images/faceted_lineplot.png]

The "dots" dataset is a typical seabon type "long" dataset, where one of the columns is used for paneling.  If our data is wide, then we need to transform (using the `melt` function) as showned later.   

Meaning of the "dots" dataset: reactions of mice to different combinations of stimuli. The dataset includes variables such as the time the mouse spent freezing (a measure of fear), the type of stimulus the mouse was exposed to, and the mouse's genotype. 

<div class="code-head"><span>code</span>plot model driver.py</div>

```python

import seaborn as sns
sns.set_theme(style="ticks")

dots = sns.load_dataset("dots")
In [5]: dots
Out[5]:
    align choice  time  coherence  firing_rate
0    dots     T1   -80      0.000       33.190
1    dots     T1   -80      3.200       31.692
2    dots     T1   -80      6.400       34.280
3    dots     T1   -80     12.800       32.632
4    dots     T1   -80     25.600       35.060
..    ...    ...   ...        ...          ...
843  sacc     T2   300      3.200       33.282
844  sacc     T2   300      6.400       27.584
845  sacc     T2   300     12.800       28.512
846  sacc     T2   300     25.600       27.010
847  sacc     T2   300     51.200       30.959


palette = sns.color_palette("rocket_r") # Define the palette as a list to specify exact values
sns.relplot(data=dots,
    x="time", y="firing_rate",
    hue="coherence", col="align",
    kind="line",  palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)

sns.relplot(data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)
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
