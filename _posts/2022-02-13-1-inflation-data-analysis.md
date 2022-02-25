---
layout: post
tag: inflation, FRED, data analysis
category: "other risks"
title: "Inflation Data Analysis"
description: Using FRED data to assess inflation risk and magnitude
author: Sarah Chen
image: images/posts/photos/IMG-0869.JPG
---

![](/images/posts/photos/IMG-0869.jpg)

Too much inflation can cause many problems, and can even bring down a society/nation. 

Milton Frieman said that inflation is a disease, and that inflation is always everywhere a monetary phenomena, the result of too much money.  It is more complicated than just about money.  Other factors such as innovation, natural disaster, forces of nature, wars, and so on can all play important roles.  

In this post, I look at some data from FRED related to inflation.  Here is a list I compile,, and will expand in the future. 
<!-- from pandas import DataFrame -->
<!-- from tabulate import tabulate -->
<!-- print(tabulate(freq_tbl.iloc[:,:1], tablefmt="pipe", headers='keys')) -->
| MEV        | frequency   | date                |
|:-----------|:------------|:--------------------|
| M2Sl       | monthly     | first of month      |
| BASE       | bi-weekly   | 2019-12-18 00:00:00 |
| M2V        | quarterly   | first of quarter    |
| DCOILWTICO | daily       | nan                 |
| CPIAUCSL   | monthly     | first of month      |
| PPIACO     | monthly     | first of month      |
| USSTHPI    | quarterly   | first of quarter    |
| FEDFUNDS   | monthly     | first of month      |
| DGS10      | daily       | nan                 |
| TB3MS      | monthly     | first of month      |
| UNRATE     | monthly     | first of month      |
| GDP        | quarterly   | first of quarter    |
| GDPC1      | quarterly   | first of quarter    |
| STLFSI     | weekly      | nan                 |
| VIXCLS     | daily       | nan                 |

<!-- what's the cause of the disease,
how do we cure the disease?
what are the effects of the cure?
What are the side effects of it?
What if we don't cure it? -->
This post presents the data that shows too much money has inflicted inflation.  The recent trends indicates that it is likely going to stay and get worse in time.  

I use the following code to get data from FRED and plot the data. 
<div class="code-head"><span>code</span>corr.py</div> 

```python
import pandas_datareader.data as web    # pandas 0.19.x and later
from datetime import datetime
grey = "#57606c"
file_mev = 'mev_inflation.txt'
def get_series(MEV, NAME):
    df =web.DataReader(MEV, "fred", start, end)
    df.columns=[NAME]
    df[NAME] = np.where(df[NAME]==0., np.nan, df[NAME])
    df.dropna(axis=0, inplace=True)
    df.to_excel('./data/%s.xlsx'%MEV) # need index which are dates
    with open(file_mev, 'w') as f:
        f.write("%s %s"%(MEV, NAME))
        f.write("\n") 
        f.write("The max happens on %s"%df.idxmax())
        f.write("\n")
        f.write("The min happens on %s"%df.idxmin())
        f.write("\n")
    print(df.head())
    print(df.tail())
    print("The max happens on ", df.idxmax())
    print(df.loc[df.idxmax()])
    print("The min happens on ", df.idxmin())
    print(df.loc[df.idxmin()])
    return df
def plot_series(df, NAME):
    fig, axes = plt.subplots(1,2, figsize=(12,4))
    sns.histplot(data= df, x=NAME, ax=axes[0], color=blue)
    sns.lineplot(data= df, x=df.index, y=NAME, ax=axes[1], color=blue)
    axes[1].hlines(y=0, xmin=df.index[0], xmax=df.index[-1], color='k', linestyle='dashed', linewidth=0.5)
    MEAN = df[NAME].mean()
    axes[1].hlines(y=MEAN, xmin=df.index[0], xmax=df.index[-1], color='red', alpha=.5,linestyle='dashed', linewidth=0.5)
    for i in range(2):
        axes[i].tick_params(color=grey, labelcolor=grey)
        for spine in axes[i].spines.values():
            spine.set_edgecolor(grey)
    # plt.tight_layout()
    plt.show()
    plt.savefig('./images/%s'%NAME, dpi=300)
``` 
# Money Suppy
## M2 

![M2](/images/posts/m2.png)

<div class="code-head"><span>code</span>m2.py</div> 

```python
MEV = 'M2Sl'^M
NAME = "m2"^M
m2 = get_series(MEV, NAME)
# The max happens on  m2   2021-12-01
# dtype: datetime64[ns]
#                   m2
# DATE
# 2021-12-01 21638.100
# The min happens on  m2   1960-01-01
# dtype: datetime64[ns]
#                 m2
# DATE
# 1960-01-01 298.200
```

![M2 month over month change rate](/images/posts/m2_mom.png)

![M2 year over year change rate](/images/posts/m2_yoy.png)

## Money velocity

![M2 year over year change rate](/images/posts/m2_yoy.png)

```python
DATE
1960-01-01 1.817
1960-04-01 1.797
1960-07-01 1.780
1960-10-01 1.737
1961-01-01 1.723

DATE
2020-10-01 1.134
2021-01-01 1.121
2021-04-01 1.119
2021-07-01 1.115
2021-10-01 1.120

The max happens on  m2v   1997-07-01

DATE
1997-07-01 2.192

The min happens on  m2v   2020-04-01
DATE
2020-04-01 1.100
```

```python
             m2v_mom
 DATE
 1960-04-01   -1.101
 1960-07-01   -0.946
 1960-10-01   -2.416
 1961-01-01   -0.806
 1961-04-01    0.116
             m2v_mom
 DATE
 2020-10-01   -1.133
 2021-01-01   -1.146
 2021-04-01   -0.178
 2021-07-01   -0.357
 2021-10-01    0.448
 The max happens on  m2v_mom   2020-07-01
 dtype: datetime64[ns]
             m2v_mom
 DATE
 2020-07-01    4.273
 The min happens on  m2v_mom   2020-04-01
```
![Velocity of money month over month change rate](/images/posts/2v_mom.png)

```python
 m2v_yoy = level_to_yoy(m2v, NAME) 
 #             m2v_yoy
# DATE
# 1963-01-01   -6.990
# 1963-04-01   -6.789
# 1963-07-01   -5.618
# 1963-10-01   -3.742
# 1964-01-01   -2.205
# The max happens on  m2v_yoy   1995-01-01
# dtype: datetime64[ns]
#             m2v_yoy
# DATE
# 1995-01-01   14.995
# The min happens on  m2v_yoy   2021-07-01
# dtype: datetime64[ns]
 ```

[Velocity of money year over year change rate](/images/posts/m2v_yoy.png)

# Oil

<div class="code-head"><span>code</span>oil.py</div> 

```python
MEV = 'DCOILWTICO'
NAME = 'wti'
with open(file_mev, 'w') as f:
    f.write("\n") 
    f.write("**************************************") 
    f.write("WTI oil price")
wti = get_series(MEV, NAME)
plot_series(wti,NAME)
wti = daily_to_monthly(wti, NAME)
wti_yoy = level_to_yoy(wti, NAME) 
wti_mom = level_to_mom(wti, NAME) # convert to yoy and plot

```

![WTI price](/images/posts/wti.png)
![WTI month over month change rate](/images/posts/wti_mom.png)
![WTI year over year change rate](/images/posts/wti_yoy.png)

# 2. price
The CPI data is monthly, HPI quarterly, and PPI data is monthly.  
## CPI
The CPI is the most important price gauge in the US, although PPI, HPI and labor costs are important as well. 

Prices have been increasing throughout time.  Moderate inflation such as 2% annual rate has been considered as good for the economy as it encourages people to spend money (things are cheapter now than in the future) as opposed to saving and hoarding money, which happens if prices don't increase or even decrease. 

The latest CPI data as of writing is January 2022.   Figure shows that over the preceeding month, the CPI increased by 1%.  This is very significant.  Because if we annualize it, it will be 12%, much higher than the 2% target. 
![CPI](/images/posts/US cpi_20220225.png)
```python
               cpi
DATE
2021-09-01 274.214
2021-10-01 276.590
2021-11-01 278.524
2021-12-01 280.126
2022-01-01 281.933
```
**CPI Month over Month** 

The max month over month growth rate happened in 1973-08.  The rate was 1.8%, which is annualized at 21.6%!
We know that 1973 was the year of the oil embargo from OPEC to the US.  It was an "energy Pearl Harbor" per Nixon adviser. 

The min happend in 2008-11, which was -1.77%,  right after the collape of Lehman Brothers on September 15, 2008.  

![CPI Month over Month](/images/posts/US cpi_mom_20220225.png)

**CPI Year over Year** 

The YoY shown in chart has monthly resolution. For example, January 2022 CPI YoY growth rate compares January, 2022 with January of 2021.  
"1-period +6%" means that the YoY growth rate has increased by 6% in January, 2022. In other words, *inflation has sped up*. 

| DATE       |  cpi_yoy |
|-----------:|--------:|
| 2021-09-01 |   5.389 |
| 2021-10-01 |   6.236 |
| 2021-11-01 |   6.828 |
| 2021-12-01 |   7.096 |
| 2022-01-01 |   7.525 |

Note that the max cpi_mom happened on 1980-Q1, where the CPI jumped by 14.6%.  One of the triggers could be the stoppage of Iranian oil productions in the early part of 1979, and the cutback of productions of OPEC, which kept the oil prices high.  Aggrevating a situation of shorter supply is hoarding, which increases demand. 

The smallest CPI month over month growth rate happened in 3Q2009, right in the *GFC*. 

![CPI Year over Year](/images/posts/US cpi_yoy_20220225.png)

## PPI
![PPI year over year](/images/posts/US ppi_yoy_20220224.png)

## HPI
![HPI](/images/posts/ussthpi.png)
HPI month over month growth rate is sp
![HPI month over month](/images/posts/ussthpi_mom.png)

![HPI year over year](/images/posts/US hpi_yoy_20220225.png)

## PPI


# 3. RATES
## Fed funds rate
MEV = 'FEDFUNDS'
NAME = 'fedfunds'

![fedfunds](/images/posts/fedfunds.png)
![fedfunds year over year](/images/posts/fedfunds_yoy.png)

## 10-year treasury note yield

MEV = 'DGS10'
NAME = 'dgs10'

![dgs10](/images/posts/dgs10.png)
![dgs10 year over year](/images/posts/dgs10_yoy.png)

## 3-month treasury bill yield

MEV = 'TB3MS'
NAME = 'tb3ms'
![tb3ms](/images/posts/tb3ms.png)
![tb3ms year over year](/images/posts/tb3ms_yoy.png)

# 4. Economy 
## Nominal GDP
![gdp](/images/posts/gdp.png)
![gdp year over year](/images/posts/gdp_yoy.png)

## Real GDP (inflation adjusted)
![gdpc1](/images/posts/gdpc1.png)
![gdpc1 year over year](/images/posts/gdpc1_yoy.png)

# 5. Financial stress and volatility
## Financial stress
![stlfsi](/images/posts/stlfsi.png)
![stlfsi year over year](/images/posts/stlfsi_yoy.png)

## VIX
![vixcls](/images/posts/vixcls.png)
![vixcls year over year](/images/posts/vixcls_yoy.png)


# Real Estate
