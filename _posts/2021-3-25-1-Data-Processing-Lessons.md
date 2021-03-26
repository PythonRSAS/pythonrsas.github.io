---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Data Processing Lessons"
description: Data processing tips from experiences
author: Sarah Chen
image: images/posts/IMG-0648.JPG
---

As I reviewed old code, I found some data processing to be chaotic.  Yes, I understand the process is iterative.  But if it is too chaotic it becomes inefficient.

For example, some have multiple places of unnecessary indicator variable creation manually.  Whereas it could all be done in one shot!

Need to be disciplined!
## General principles
1.	Move all data format correction code in block.
2.	Do not create indictor variables here and there.  Do it in one shot.
3.	Do not output describe until unneeded variables are mostly dropped.
4.	Plot scatterplots in one shot for all numeric variables.

Because PD and LGD are modeling labels and continuous numbers, respectively.  The visualizations and metrics will be two different sets corresponding to categorical target and continuous numeric taget, respectively. 

### PD specifically
PD by year plot: 
-	there is no such thing as boxplot, which we do for LGD. 

