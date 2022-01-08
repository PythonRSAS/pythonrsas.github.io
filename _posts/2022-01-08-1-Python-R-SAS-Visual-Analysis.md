---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Python R SAS Visual Analysis"
description: most basic plottings in Python, R and SAS
author: Sarah Chen
image: images/posts/photos/IMG-0680.JPG

---
Work in Progress.  Check back later. 

-
- [frequency barplots](#frequency-barplots)
  - [simple barplots](#simple-barplots)
  - [stacked or grouped barplots for > 1 groups](#stacked-or-grouped-barplots-for--1-groups)
- [relationship between numeric data](#relationship-between-numeric-data)
### frequency barplots

#### simple barplots 
<div class="code-head"><span>code</span>simple bar plot.py</div>

```python
# simple bar plot
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution",
   xlab="Number of Gears")

```

<div class="code-head"><span>code</span>simple bar plot.r</div>

```r
# simple bar plot
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution",
   xlab="Number of Gears")

# simple horizontal bar plot with added labels
counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", horiz=TRUE,
  names.arg=c("3 Gears", "4 Gears", "5 Gears"))
```
<div class="code-head"><span>code</span>simple bar plot.sas</div>

```sas

```
#### stacked or grouped barplots for > 1 groups
<div class="code-head"><span>code</span>stacked and grouped barplots.py</div>

```pythn
```
<div class="code-head"><span>code</span>stacked and grouped barplots.r</div>

```r
# Stacked Bar Plot with Colors and Legend
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
  xlab="Number of Gears", col=c("darkblue","red"),
  legend = rownames(counts))

# Grouped Bar Plot
counts <- table(mtcars$vs, mtcars$gear)
barplot(counts, main="Car Distribution by Gears and VS",
  xlab="Number of Gears", col=c("darkblue","red"),
  legend = rownames(counts), beside=TRUE)
```

> Bar plots need not be based on counts or frequencies. You can create bar plots that represent means, medians, standard deviations, etc. Use the <span class="coding">aggregate( )</span> function and pass the results to the <span class="coding">barplot( )</span> function.

By default, the categorical axis line is suppressed. Include the option <span class="coding">axis.lty=1</span> to draw it.

With many bars, bar labels may start to overlap. You can decrease the font size using the <span class="coding">cex.names = option</span>. Values smaller than one will shrink the size of the label. Additionally, you can use graphical parameters such as the following to help text spacing:

<div class="code-head"><span>code</span>numerica value barplot.r</div>

```r
# Fitting Labels
par(las=2) # make label text perpendicular to axis
par(mar=c(5,8,4,2)) # increase y-axis margin.

counts <- table(mtcars$gear)
barplot(counts, main="Car Distribution", horiz=TRUE, names.arg=c("3 Gears", "4 Gears", "5   Gears"), cex.names=0.8)
```

### relationship between numeric data
<div class="code-head"><span>code</span>relationship between numeric data.py</div>

```python
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(nba[["ast", "fg", "trb"]])
plt.show()
```
