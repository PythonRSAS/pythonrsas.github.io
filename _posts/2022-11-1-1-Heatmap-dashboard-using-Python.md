---
layout: post
tag: heatmap, dashboard
category: "other risks"
title: "Heatmap dashboard using Python"
description: creating heatmap dashboards using Python for risk management
author: Sarah Chen
image: images/posts/balance_sheet_composition.PNG
---

Dashboards are important for senior risk managers.  This post is about creating heatmap dashboards using Python for risk management. 

# Determining the variables for the dashboard
First we need to select the variables for the dasbboard.  The candidates are:
1. sovereign rates for different durations and spreads between them (to observe any short-long-term rate spread inversions). 
2. Credit indices compare with volatility
3. Equity indices
4. Commodity prices
5. FX

# Heatmap

The cmap used is in a familiar format to senior managers, where red indicates high risk and green indicates low risk. 
<div class="code-head"><span>code</span>heatmap.py</div>

```py
from datetime import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
TODAY = datetime.today().strftime('%Y%m%d')
fig, ax = plt.subplots(1,1, figsize = (10,3))
data1 = df.copy()
data1[data1.index.isin(['reversed_mev'])] = float('nam')
sns.heatmap(data1, cmap = 'RdYlGn_r', cbar=False, ax=ax)
data1 = df1.copy()
data1[~data1,index.isin(['reversed_mev'])] =float('nan')
for i in data1.index:
    data2 = data1.copy()
    data2[~data2.index.isin([i])] = float('nan')
    sns.heatmap(data2, cmap = 'RdYlGn', cbar=False, ax=ax, lw = 0.01, linecolor='gray')
plt.subplots_adjust(top=0.99, bottom=0.22, right=0.99)
plt.ylabel("")
plt.xlabel("")
ax.set_xticklabels(ax.get_xticklabels(), fontsize = 7, va = 'bottom')
ax.set_yticklabels(ax.get_yticklabels(), fontsize = 7, ha = 'left')
tick_params(axis=u'both', which=u'both', length=0) # invisible tickmark
plt.draw()
yax = ax.get_yaxis()
yax.set_tick_params(pad=ypad)
xax = ax.get_xaxis()
xax.set_tick_params(pad=xpad)
plt.tight_layout()
plt.savefig("heatmap_%s"%TODAY, dpi = 600)
plt.show()
```

