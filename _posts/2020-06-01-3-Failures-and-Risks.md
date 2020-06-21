---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Credit Scoring Platforms and In-House Solutions"
description: Notes on credit scoring platforms, approaches and in-house solutions from large and very small ones
author: Sarah Chen
image: images/posts/equifax_pres.JPG
---

This post is a survey on some of the credit scoring platforms and credit scoring in-house solutions out there and what they do.  There are many opportunities for moving forward credit scoring but the competition is fierce: large banks with lots of resources, existing proprietary analytic software companies, new analytic analytics-as-a-service companies leveraging open source and cloud computing, old powerhouse credit scoring companies, and new credit scoring platforms. 

In less regulated countries like China there has been heavy use of machine learning in credit scoring and social scoring (Ali Pay, Baidu Finance, JD Finance).  

In the US that all credit scoring in regulated industries must adhere to [FCRA](https://www.ftc.gov/enforcement/rules/rulemaking-regulatory-reform-proceedings/fair-credit-reporting-act){:target="_blank"}, [ECOA](https://www.justice.gov/crt/equal-credit-opportunity-act-3){:target="_blank"}, [SCRA](https://www.justice.gov/servicemembers/servicemembers-civil-relief-act-scra){:target="_blank"} and [FHA](https://www.hud.gov/federal_housing_administration){:target="_blank"}. 

So, data security, privacy + machine learning interpretability (to ensure fairness) are pre-requisites.  

The order of the companies in the post is completely **random**.  There is *no implied superiority*.  In fact, some of them have been historical gold standards whereas some are very small start-ups. 


### Equifax Ignite

It is a hardoop platform that supposedly provide linked and ready data, along with analytics functions, and the option of using monotonicity-enforced neural network, or logistic regression. 

It promises a 30-day deployment. 


<figure>
  <img src="{{ "/images/posts/equifax_pres1.JPG" | relative_url }}">
  <figcaption>Equifax Ignite</figcaption>
</figure>

<figure>
  <img src="{{ "/images/posts/equifax_pres2.JPG" | relative_url }}">
  <figcaption>Equifax Ignite</figcaption>
</figure>

<figure>
  <img src="{{ "/images/posts/equifax_pres3.JPG" | relative_url }}">
  <figcaption>Equifax Ignite</figcaption>
</figure>



### [SAS Credit Scoring](https://www.sas.com/en_us/software/credit-scoring.html){:target="_blank"}

Well-established credit scoring historically for **in-house** development.

This is a quote from 
[SAS website](https://www.sas.com/en_us/software/credit-scoring.html){:target="_blank"}:


"Quickly develop, validate, deploy and track credit scorecards in house – while minimizing model risk and improving governance. We've combined award-winning data management, data mining and reporting capabilities in a powerful credit scoring solution that is faster, cheaper and more flexible than any outsourcing alternative."

[It](https://www.sas.com/content/dam/SAS/en_us/doc/productbrief/sas-credit-scoring-100665.pdf){:target="_blank"} promises faster, cheapter and more flexibble than outsourcing alternative on application and behavior scoring for virtually all lending products – including commercial loans, cards, installment loans and mortgages.

SAS has delivered "sustainable, auditable model development environment."

But what caught my eyes are these words:

>Access, transform, standardize and cleanse all relevant data to create a **360-degree** view of the customer.

What if the institution has disjoint databases and in different functions?

What if you need to get that 360 view really fast?  

More importantly, can the organization's different departments work together seamlessly so that that view is even possible in the first place? 

And then there is the promise of ["Fast in-house scorecard development"](https://www.sas.com/en_us/software/credit-scoring.html){:target="_blank"}--We know that only makes sense if data management, model review and approvals are fast.  


In the [white paper](https://www.sas.com/content/dam/SAS/en_us/doc/whitepaper1/infrastructure-credit-risk-model-development-108925.pdf){:target="_blank"} , SAS acurately summarizes the problems:
> issues with the activities that occur **before and after modeling**, such as **accessing data, data cleansing, getting business buy-in, recoding models, validating models, creating documentation, producing audit reports, implementing models, and other operational activities**. As a result, the entire analytics and modeling process is slow and difficult.

The **pain has been correctly identified**.  

Unfortunately not everywhere the solution has worked out well .  

In-house solution advantages can be realized only if the **people in-the-house** are working together and not working separately.  

<figure>
  <img src="{{ "/images/posts/sas_in_house_credit_scoring.JPG" | relative_url }}">
  <figcaption>SAS in-house credit scoring development process</figcaption>
</figure>


Besides SAS, other well-established commerical in-house solutions include [Matlab from mathworks](https://www.mathworks.com/discovery/credit-scoring-model.html){:target="_blank"} and others. 

### [ZestFinance](https://www.zest.ai/)
[zest](https://www.zest.ai/) has a much more sophisticated website that promises business results such as:
> x% lower charge off rate and y% increase in approval rate


Value proposition:
> ZAML® (Zest Automated Machine Learning) is a machine learning credit and risk modeling solution with *end-to-end explainability* and **compliant** and allows flexible engagements

Its target industries are across the "credit spectrum": consumer lending (include auto and mortgage), commercial lending, insurance and telecom. 

It was founded initially as an online lending platform in 2009 and after a few years changed to an underwriting software company.  

It has some large and mid-size customers and partners: Discover, Baidu, JD, Ford, Prestige(auto), and is recently working with  Freddie Mac in [testing mortgage underwriting](https://www.wsj.com/articles/freddie-mac-tests-underwriting-software-that-could-boost-mortgage-approvals-11569333848). 

Zest promises that lenders small and large (banks) can originate more loans with greater confidence by assessing borrower risk more accurately—all while remaining compliant with regulatory demands as their models use hundreds of variables and thousands of interaction effects.  

The company is based in Burbank, CA, and seems to promote a great working enviroment, with the mission "Our mission is to make fair and transparent credit available to everyone." 

<figure>
  <img src="{{ "/images/posts/zest.JPG" | relative_url }}">
  <figcaption>zest timeline</figcaption>
</figure>

I found two excellent Zest interviews:
 - [2019 FinTech Ideas Festival Douglas Merrill from ZestFinance](https://www.youtube.com/watch?v=A8_Z5GC25Ho)
 - [ZestFinance And Discover: LendIt 2019 CEO Keynote Interview](https://www.youtube.com/watch?v=3sT7KcJz7g4)


In [2019 Lendit keynote](https://youtu.be/3sT7KcJz7g4) Discover CEO Roger Hochschild talked about the challenges in **personal loans is that many of the credit losses are actually frauds**.  Due to this, **traditional credit scoring would not work well**.

One of the motivations behind the Discover and Zest partnership is *"explainability in fair lending"*.  

Zest CEO [Douglas Merrill](Douglas Merrill) [says](https://youtu.be/3sT7KcJz7g4) "if people finds that it matters to be explainable then they will find a way to explanable.  Neural network is not materially harder to explain than, say, support vector machine."

### [Scienaptic.ai](https://www.scienaptic.ai/)

[Scienaptic.ai](https://www.scienaptic.ai/) website homepage looks remarkably like [zest](https://www.zest.ai/), with the same color scheme and java-scripted moving network background, symbolic of neural network algorithm used. 

Its name "Scienaptic" is a combination of "scientifc" and ["synapse"](https://en.wikipedia.org/wiki/Synapse) 

Its desired customers are large banks. 

Value proposition:
> - Ether platform reduce friction inherent in current credit decisioning processes.
> - **fully compliant and explainable**
> - **"Nothing leaves customer's firewall."**

The proposition demonstrates that, like Equifax and ZestFinance, they understand in order for banking customers to use it, the tool needs to be interpretable.  

The Ether platform has pre-built APIs for both traditional and **alternative** credit data sources to accelerate data ingestion for sharper credit decisioning.  This seems to be a function that Equifax also has. 

Scienaptic also promises 30-day deployment, and within customer's firewall.

While Scienaptic is a late comer relative to Zest and some larger players, with the right marketing and execution, it can achieve its goal.  If they have a great product that has value to banks, they should understand how each of their potential customer's business work and what their pain points are, and how they can help them save cost and make more money, and get their business by talking to the buying decision maker.  

<figure>
  <img src="{{ "/images/posts/scienaptic.JPG" | relative_url }}">
  <figcaption>scienaptic ether</figcaption>
</figure>


### underwrite.ai

Despite a name associated with credit and insurance, the [company](http://www.underwrite.ai/){:target="_blank"} does not seem to have a focused goal as the company founder is discussing financial services and cancer at the same time in the same presentation. Let's see its collaboration with [h2o.ai](https://www.h2o.ai/company/news/underwrite-ai-leverages-h2o-ai-to-modernize-credit-with-ai/){:target="_blank"}  will bring. 

Value proposition:
> Use thousands of data points from credit bureau sources + machine learning + target profitability and customer lifetime value instead of default of individuals and SMEs.


>"If you have no portfolio data, we have models based upon massive quantities of publicly available datasets covering everything from home mortgage and automobile to peer to peer lending and cash advance."

### [Lenddo](https://www.lenddo.com/products.html#creditscore){:target="_blank"}

Its [website](https://www.lenddo.com/products.html#creditscore){:target="_blank"} has a popup ad about an event from 2017, which clearly is **outdated**.   Timelines of this company and events seem to have stopped at 2017 despite a lot of funding and publicity in early years.

Value proposition:
> "Lenddo’s patented score is a powerful predictor of an individual’s character or 'willingness to pay'"
   
It offers cloud-based alternative credit scoring and identity verification solutions on individual and SMEs, where "alternative" means social media and any digital foot print /online behavior. 

Its product is intended to be complimentary to traditional credit scoring. 

### Summary

There are a lot of activities in the space of applying new technologies (big data + machine learning) to credit scoring.  The competition is very fierce.   

The winners will need: great product + great people to execute + a viable philosophy/idea. Great execution that help customer making/saving lots of money without higher risk will be the key in building trust and opening doors to more customers.  


### After Thoughts

* **Credit scoring and Fraud** 
You cannot score credit and price it appropriately without taking into account fraud, because you cannot score credit when it not actually credit-related and **information provided are false**. Without taking into account fraud, AI models can make poorer predictions than judgement. 
It has been my experience that some teams in some large banks unfortunately don't distinguish fraud and credit losses when they build commercial lending models. This is an opportunity for improvement internally or a value proposition from outside.   
* **Customer experience**: 
combining 360 view data of customer + machine learning goes beyond credit scoring.  It can improve dramatically customer experience in every touch point. 
However, there is a caveat: it may be hard to get to 360 for personal credit in the US as there is a force or traditional value that goes aginst it: the rights to **privacy**.  This will prevent consolidating alternative data sources into a useful database. 
* **Winner takes it all** has been the rule of the game in platforms.  It will happen to credit scoring as well.  
* **Recession-proof**: The best of the time; the worst of the time.  The *worst loans tend to be originated in the best of the time* (often right before recession). In the good time, most customers seem good customer.  But when the hard time hits, many will default.  No AI magic will change that.  

So, when a company promises lowering risk while increasing credit volume, remember that the associated **loss rate for that underwriting is not a swipe-test**.   The verdict comes months or years later.   