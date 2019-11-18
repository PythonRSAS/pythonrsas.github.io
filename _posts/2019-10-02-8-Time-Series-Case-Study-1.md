---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Time Series Case Study1"
description: Import zip file, extract, manipulate, and plot CCAR 2019 Federal Reserve Macro Scenarios
author: Sarah Chen
image: http://drive.google.com/uc?export=view&id=1hXH-eJF20B6xAJvc1W5icAzePG1MwUuO

---

This post is from my upcoming book on statistical and machine learning using Python and SAS, sequal to my co-authored book [Python for SAS User](https://www.amazon.com/Sarah-Chen/e/B07ZL3Q97B?ref_=dbs_p_pbk_r00_abau_000000)


<figure>
  <img src="{{ "/images/posts/CCAR-Scenarios.png" | relative_url }}">
  <figcaption>CCAR 2019 CREPI by Scenario</figcaption>
</figure>
Let's get started.

<h4 id="Bar-line-plot">Python code</h4>


<div class="code-head"><span>code</span>Getting Data.python</div>

```python
>>> from io import BytesIO
>>> from zipfile import ZipFile
>>> import pandas
>>> import requests
>>> content = requests.get(r"https://www.federalreserve.gov/supervisionreg/files/2019-macro-scenario-tables.zip")
>>> zf = ZipFile(BytesIO(content.content))
>>> for item in zf.namelist():
>>>     print(item)
[Out]:
Table_2A_Supervisory_Baseline_Domestic.csv
Table_2B_Supervisory_Baseline_International.csv
Table_3A_Supervisory_Adverse_Domestic.csv
Table_3B_Supervisory_Adverse_International.csv
Table_4A_Supervisory_Severely_Adverse_Domestic.csv
Table_4B_Supervisory_Severely_Adverse_International.csv

>>> cols= ['Date','House Price Index (Level)','Commercial Real Estate Price Index (Level)']
>>> name_change = {'House Price Index (Level)':'HPI','Commercial Real Estate Price Index (Level)':'CREPI'}

>>> def ScenarioData(df, sffx):
>>>     df.rename(columns=name_change, inplace=True)
>>>     df[['year','qtr']]=df.Date.str.split("Q",expand=True)
>>>     df.loc[:,'year']=df.year.astype('int')
>>>     df.loc[:,'qtr']=df.qtr.astype('int')
>>>     df['month'] = df.qtr*3
>>>     df['day']= 1
>>>     df.index = pd.to_datetime(df.loc[:,['year','month','day']])
>>>     df.drop(['year','month','day','Date','qtr'], axis=1,inplace=True)
>>>     df = df.add_suffix('_%s' %sffx)
>>>     return df

>>> baseline = pd.read_csv(zf.open("Table_2A_Supervisory_Baseline_Domestic.csv"), usecols=cols)
>>> baseline =ScenarioData(baseline, "baseline")

>>> adverse = pd.read_csv(zf.open("Table_3A_Supervisory_Adverse_Domestic.csv"), usecols=cols)
>>> adverse = ScenarioData(adverse, "adverse")

>>> severe= pd.read_csv(zf.open("Table_4A_Supervisory_Severely_Adverse_Domestic.csv"), usecols=cols)
>>> severe = ScenarioData(severe,"severe")

>>> names = [baseline, adverse,severe]
>>> all_scenarios = pd.concat(names, axis=1)

>>> all_scenarios.filter(regex="CREPI").plot(style=['go-','y^:','r+-'],  title="CCAR 2019 Scenario: CREPI")
>>> plt.savefig(r"C:\Users\sache\OneDrive\Documents\python_SAS\Python-for-SAS-Users\Volume2\TimeSeries\images\CCAR Scenarios", dpi=300)
>>> plt.show()

```

**SAS** 
(to be continued)