---
layout: post
tag: inflation, FRED, data analysis
category: "other risks"
title: "US Government Interest Rates"
description: Analyze interest rates from FRED
image: images/posts/photos/IMG-0869.JPG
---

![](/images/posts/photos/IMG-0869.jpg)

Under this mighty topic of interest rate, in this post I explore interest rates from 1970s and try to understand them in more details in exact dates and actions in history. 

One of the motivation is to get a bit of crystal ball on inflation and recession.  If I have longer data, I would like to study on wars as well.  

We had lived in a world with low inflation in the US coming out of a decade of less than 2.5% YoY inflation rate.  China inflation rate is less than 4%, India 6%, and Japan only at 0.5%.  It is hard to imagine how inflation possibly could get any worse than the current +7% in the US, and 5.8% in Europe (average) in the West.  But it very well likely can.   


<!-- print(tabulate(freq_tbl.iloc[:,:1], tablefmt="pipe", headers='keys')) -->


| MEV        | frequency   | meaning                | date                |
|:-----------|:------------|:--------------------|:--------------------|
| PALLFNFINDEXQ  | quarterly     | global commodities    | first of quarter |
| CPIAUCSL   | monthly     | cpi     | first of month      |
| PPIACO     | monthly     | producers index      | first of month      |
| USSTHPI    | quarterly   | hpi   | first of quarter    |
| FEDFUNDS   | monthly     | fed funds rate      | first of month      |
| DGS10      | daily       | 10-Year Treasury rate                | nan                 |
| DGS2      | daily       | 2-Year Treasury rate                | nan                 |
| TB3MS      | monthly     | 3-month Treasury bill      | first of month      |
| UNRATE     | monthly     | unemployment rate    | first of month      |
| GDP        | quarterly   | Nominal GDP    | first of quarter    |
| GDPC1      | quarterly   | Inflation adjusted GDP   | first of quarter    |

<!-- what's the cause of the disease,
how do we cure the disease?
what are the effects of the cure?
What are the side effects of it?
What if we don't cure it? -->
<div class="code-head"><span>code</span>fred.py</div> 

```python
lt = ["FEDFUNDS","DGS10",   "DGS2",    "TB3MS",   "UNRATE",  "GDP",     "GDPC1"]
ss_lt =[]
start = pd.Timestamp('1960-1-1')
end = datetime.today()
for i in lt:
    ss =web.DataReader(i, "fred", start, end)
    ss_lt.append(ss)
df.pd.concat(ss_lt, axis=1)
```

