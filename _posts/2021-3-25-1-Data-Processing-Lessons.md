---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Data Processing Lessons"
description: Data processing tips from experiences
author: Sarah Chen
image: images/posts/IMG-0648.JPG
---
![](/images/posts/IMG-0648.JPG)
Although processes are iterative, it should still be organized, at least periodically.  If it becomes too chaotic, it becomes inefficient.

For example, some have multiple places of unnecessary indicator variable creation manually.  Whereas it could and should be all be done in one shot after we have finalized the set the variables!

> Need to be disciplined and organized!
# General principles
1.	Move all data format correction code in block.
2.	Do not create indictor variables here and there.  Do it in one shot.
3.	Do not output describe until unneeded variables are mostly dropped.
4.	Plot scatterplots in one shot for all numeric variables.

Because PD and LGD are modeling labels and continuous numbers, respectively.  The visualizations and metrics will be two different sets corresponding to categorical target and continuous numeric taget, respectively. 

## PD specifically
PD by year/quarter plot: 
-	Although we use boxplots routinely on LGD, there is no such thing as boxplot for binary targets.
-   However, quarterly average PD rates can be used as alternative data points. Boxplot can be used on them. 

