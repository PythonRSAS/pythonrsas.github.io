---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Credit Risk Overview"
description: Thoughts on credit risk, and general wisdoms
author: Sarah Chen
image: images/posts/worldDebt.jpg
---

- [The credit industry](#the-credit-industry)
  - [Consumer](#consumer)
  - [Commercial](#commercial)
- [Credit cycles: the best of the time, the worst of time; vice versa](#credit-cycles-the-best-of-the-time-the-worst-of-time-vice-versa)
- [Managing credit risk](#managing-credit-risk)
  - [Qualitative insights](#qualitative-insights)
  - [Data](#data)
    - [Asymmetry of information](#asymmetry-of-information)
  - [Analytics:](#analytics)
At any given moment, there are hundreds of trillions of debt or credit.  This fantastic visualization (even though outdated) provides a sense of the scale and the relative scale of credit: [All of the World’s Money and Markets in One Visualization](https://money.visualcapitalist.com/worlds-money-markets-one-visualization-2017/)


> **Credit risk** is the **uncertainty** associated with credit, specifically about whether the borrower will pay back the money borrowed, and how much. 

In a broader context, credit risk exists in every industry, and concerns every company and individual in every industry even though the term credit is usually associated with money borrowing. Every business that wants to scale succesfully needs to have good management on their credit risk.  
# The credit industry
Debt (or credit) can be categorized in 4 groups: government, financial sector, non-financial companies, and , households, which are often loosely divided into retail (aka “consumer”) and commercial, where retail is smaller loans to individuals or small business loans, whereas commercial means lending to businesses, high net worth individuals and sovereigns.   The credit industry is very dynamic and complex, interconnected with government policy, geopolitical risk, macroeconomic enviroment, credit cycle, and idiosyncratic risks. 

Below is a summary of the different products or portfolios: 
## Consumer ###
•	Credit cards
•	Deposit/attritions
•	Auto loans
•	Student loans
•	Installment
•	Residential mortgages
## Commercial
•	Commercial and industrial (C&I)
•	Commercial real estate (CRE)
•	Land and Construction
•	Non-bank financial institution (NBFI)
•	Project finance
•	Shipping and aircraft
•	Small business
•	Banks
•	Sovereign

Below figure is from Visual Capitalist as of end of 2019, on governament debt. 
<figure>
  <img src="{{ "/images/posts/worldDebt.jpg" | relative_url }}">
  <figcaption>Total Debt by Country (government debt)- by Visual Capitalist</figcaption>
</figure>

# Credit cycles: the best of the time, the worst of time; vice versa

Credit, as part of the economic enviroment, has cycles.  When economy is booming, it is easy to borrow and start businesses.  When economy is in hard times, businesses go under and it is difficult to borrow.

The irony, due to the cycles, is that the best of the time often creates the worst of lending, and the worst time can often create new opportunites. 

Explain a bit more on the first part: what this saying means is that the worst loans are often originated from the best of time.  When economy is good, even those company with strong risk management and disciplined underwriting principles cannot help relaxing their credit risk standards, as a result of tempation of profit and pressure from peers and/or shareholders.  

The knighted businessperson will retire or leave when or before the storm comes.  If they leave before the music stops, they get huge paybacks and lots of recognitions. 

In credit risk modeling, loan vintage, or origination time, matters.  Those loans that were given out just right before financial crisis started had the worst recovery due to the relaxed credit standard, and the stress period that followed.
# Managing credit risk

Qualitative insights, techonology, analytics, and the only thing that is better than data is more data
## Qualitative insights
Qualitative insights come from knowing the business and what's happening. 
## Data
I learned this from my friend Professor David Belanger (former chief scientist at AT&T), who might have quoted someone, that "the only thing better than data is more data".

I want to emphasize that data is not limited to those existing in databases or alternative databases or social media databases.  The kind of data that resides in individual's **mental databases** are the qualitative sides that are difficult or impossible to capture in quantitative databases. 

If we look at the all the public companies that specializes in managing data and providing insights from their data, we notice that they have all done well in the last ten years, in comparison with the rest.  For example:Google, Facebook, Moody's, S&PGlobal, Verisk, Salesforce, Equifax. If we can extrapolate, whether the computing power + analytics can deliver more incremental value will determine whether these companies will continue to outshine others.  

Collecting more data (wider and longer), knowing how to organize and manage them is the foundation to the growth.   Those who ignore this mantra have been penalized heavily (check out a few on their stock performance if they are still around). 
### Asymmetry of information
Stories from insurance industry: there is often an **asymmetry of information** both in consumer space and commercial space just like in many insurance lines.  In car and homeowner insurance for example, insurance companies don't know the insured.  I was in some parts of urban area near NYC and I noticed there are more torched houses than richer neighborhoods.  Why?  I heard it is because of frausters who set fire to get insurance payments, which are usually large payements.  Unfortunately, good hardworking insured who take care of their homes have to subsidize the frausters.  Insurance companies that can detect and decline these bad people will be able to lower their costs and can offer more cost-effective insurance to the good ones who genuinely buy insurance to protect the unforeeable random events. 

Similarly, credit providers do not know a lot about the credit receivers other than what have been provided, researched, and possibly some additional alternative data.   If banks can detect and decline those frausters who open credit cards with the ***intention*** of never paying back, then they can offer better terms and services to the good. 

* **Fraud** - Each year, the top 20 retail banks in the US loses $50 Billion to fraud. 
* **Bankruptcy** - about 50% of total losses of retail loans in financial institutions are from bankruptcy losses.   Why those bankruptcies happened and why they were not detected early on implies that financial institutions still do not know enough about what they don't know.

However, intent is not easy to detect. 
## Analytics:  

The uncertainty can be examined in many ways. What is in common across different industries are the following two questions:
1.  How likely is something going to happen
2.  If it happens, what is the impact
  
For complex data that contains intricate interactions, and very non-linear data, traditional methodologies such as generalized linear regression (GLM), which includes logistic regression, a staple in credit scoring for years, just do not deliver the kind of accuracy that machine learning models do.   

Of course, machine learning models predictions need to be well tested and understood before being used to make important credit decisions, especially when it is in a regulated institution.  




