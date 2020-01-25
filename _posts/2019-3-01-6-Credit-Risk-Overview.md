---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Credit Risk Overview"
description: Thoughts on credit risk, and general wisdoms
author: Sarah Chen
image: images/posts/worldDebt.jpg
---

**At any given moment, there are hundreds of trillions of debt or credit.**


> **Credit risk** is the **uncertainty** associated with some event, where the event is specifically about whether the borrower will pay back the money borrowed.  

In a broader context, credit risk exists in every industry, and concerns every company.  

Like every business that wants to scale needs to be a **technology** company, every business that wants to scale succesfully financially needs to be a **financial** company, and in particular, on credit risk.  


The uncertainty can be examined in many ways.  One of the common measure is how likely the borrower will not pay back.  This type of question is called "probability of default", often abbreviated as 'PD'.

Credit scoring is used in every industry even though the term credit is usually associated with money borrowing.   

What is in common across different industries are the following two questions:
1.  How likely is something going to happen
2.  If it happens, what is the impact


Some examples for the first question are:
* **Lending institution** -  how likely will the borrower pay back the money on due date
* **Auto insurance** -  An auto insurer:  how likely a driver will have an accident and how likely a vehicle will be in an accident during policy period,
* **Investors** -  how likely will a portfolio have superior returns and beat the market
* **Trading firm** -  how likely will our counterparty default, whether due to internal or external causes 
* **Consumer company** -  how likely product X will produce great sales
* **Utility company** -  how likely will the customer pay bills on time
* **Everyone** -  how likely will recession happen in the year
* **Election** -  how likely will a candidate win
* **Government** -  how likely our allies will be supportive of our actions, etc.


<figure>
  <img src="{{ "/images/posts/worldDebt.jpg" | relative_url }}">
  <figcaption>Total Debt by Country- by Visual Capitalist</figcaption>
</figure>


### the Best of the Time, the Worst of Time


What this saying means is that the worst loans are often originated from the best of time.  When economy is good, even those company with strong risk management and disciplined underwriting principles cannot help relaxing their credit risk standards, as a result of tempation of profit and pressure from peers and/or shareholders.  

The knighted business person will retire or leave when or before the storm comes.  If they leave before the music stops, they get huge paybacks and lots of recognitions. 

In credit risk modeling, loan vintage, or origination time, matters.  Those loans that were given out just right before financial crisis started had the worst recovery due to the relaxed credit standard, and the stress period that followed.


### do you know what you don't know

> In insurance and credit, there is an asymmetry of information.  Insurers and lenders do not know a lot about the insured or borrower other than what have been provided, researched, and possibly some additional alternative data.   

* **Fraud** - Each year, the top 20 retail banks in the US loses $50 Billion to fraud. 
* **Bankruptcy** - about 50% of total losses of retail loans in financial institutions are from bankruptcy losses.   Why those bankrupcies happened and why they were not detected early on implies that financial institutions still do not know enough about what they don't know.


### the Only Thing that is Better than Data is More Data

> I learned this from my friend Professor David Belanger (former chief scientist at AT&T), who might have quoted somesone.  

If you look at the all the public companies that specializes in managing data and providing insights from their data, you will notice that they have all done well in the last ten years, in comparion with the rest. 

For example:
**Google** 
**Facebook**
**Moody's**
**S&P Global**
**Verisk**
**Equifax**
**Salesforce** 

Collecting more data, knowing how to manage them is the foundation to the growth.   If we can extrapolate, whether the computing power + analytics can deliver more incremental value will determine whether these companies will continue to outshine others.  

### technology matters

> Technology is how we do things.   We all know the difference in speed between walking and flying.   There is technology in analytics. 

For complex data that contains intricate interactions, and very non-linear data, traditional methodologies such as genearalized linear regression (GLM), which includes logistic regression, a staple in credit scoring for years, just do not deliver the kind of accuracy that machine learning models do.   

Of course, machine learning models predictions need to be well tested and understood before being used to make important credit decisions, especially when it is in a regulated institution.  

