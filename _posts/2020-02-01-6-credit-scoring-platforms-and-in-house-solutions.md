---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Credit Scoring Platforms and In-House Solutions"
description: Notes on credit scoring platforms, approaches and in-house solutions from large and very small ones
author: Sarah Chen
image: images/posts/equifax_pres.JPG
---

This post is a survey on credit scoring platforms and credit scoring in-house solutions out there and what they do. 

Note that all credit scoring in the US must adhere to FCRA, ECOA, SCRA and FHA.  

So, data security, privacy + machine learning interpretability are pre-requisites.  

The order of the platforms in the post is completely **random**.  There is **no implied superiority**.  In fact, some of them have been the gold standard whereas some are very small start-ups. 


### Equifax Ignite

It is a hardoop data platform that supposedly provide data linked and ready, plus analytics functions, with the option of using monotonicity-enforced neural network, or logistic regression. 

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



### SAS Credit Scoring.

Well-established credit scoring historically for **in-house** development.

This is a quote from SAS website
[SAS Credit Scoring](https://www.sas.com/en_us/software/credit-scoring.html){:target="_blank"}:


"Quickly develop, validate, deploy and track credit scorecards in house – while minimizing model risk and improving governance. We've combined award-winning data management, data mining and reporting capabilities in a powerful credit scoring solution that is faster, cheaper and more flexible than any outsourcing alternative."

It promises faster, cheapter and more flexibble than outsourcing alternative on application and behavior scoring for virtually all lending products – including commercial loans, cards, installment loans and mortgages.

I know that SAS can deliver "Sustainable, auditable model development environment."

But what caught my eyes are these words:

>Access, transform, standardize and cleanse all relevant data to create a **360-degree** view of the customer.

What if you need to get that 360 view really fast?  

Can manual code do that?  

More importantly, can the organization's different departments work together seamlessly so that that view is even possible in the first place? 

And then there is the promise of ["Fast in-house scorecard development"](https://www.sas.com/en_us/software/credit-scoring.html){:target="_blank"}--We know that only makes sense if data management, model review and approvals are fast.  


In the [white paper](https://www.sas.com/content/dam/SAS/en_us/doc/whitepaper1/infrastructure-credit-risk-model-development-108925.pdf){:target="_blank"} , SAS acurately summarizes the problems:
> issues with the activities that occur before and after modeling, such as accessing data, data cleansing, getting business buy-in, recoding models, validating models, creating documentation, producing audit reports, implementing models, and other operational activities. As a result, the entire analytics and modeling process is slow and difficult. 

The **pain is correctly identified**.  

But unfortunately the solution is not working out well everywhere.  

In-house solution advantages can be realized only if the **people in-the-house** are working together and not working separately.  

<figure>
  <img src="{{ "/images/posts/sas_in_house_credit_scoring.JPG" | relative_url }}">
  <figcaption>SAS in-house credit scoring development process</figcaption>
</figure>



Here is the [product brief](https://www.sas.com/content/dam/SAS/en_us/doc/productbrief/sas-credit-scoring-100665.pdf){:target="_blank"}



Besides SAS, other commerical in-house solutions include [Matlab from mathworks](https://www.mathworks.com/discovery/credit-scoring-model.html){:target="_blank"}

### Gini Machine

Europe startup in Lithuania.  

Value proposition: machine learning platform for fast credit scoring. 

> "Traditional ways of building risk models require much time, a great deal of heavy lifting and specialised expertise. This is what GiniMacine changes."

<figure>
  <img src="{{ "/images/posts/gini-machine.JPG" | relative_url }}">
  <figcaption>gini machine</figcaption>
</figure>


But we know that these days even a teenager can write and run gradient boosting code that gives you better "performance". 

But where the key things like **model risk, interpretability, regulatory approvals, business success are missing**

<figure>
  <img src="{{ "/images/posts/gini-machine-promise.JPG" | relative_url }}">
  <figcaption>gini machine promise</figcaption>
</figure>

### underwrite.ai

Despite a name associated with credit and insurance, the [company](http://www.underwrite.ai/){:target="_blank"} does not seem to have a focused goal as the company founder is discussing financial services and cancer at the same time in the same presentation. Let's see its collaboration with [h2o.ai](https://www.h2o.ai/company/news/underwrite-ai-leverages-h2o-ai-to-modernize-credit-with-ai/){:target="_blank"}  will bring. 

Value proposition:
> Use thousands of data points from credit bureau sources + machine learning + target profitability and customer lifetime value instead of default of individuals and SMEs.


>"If you have no portfolio data, we have models based upon massive quantities of publicly available datasets covering everything from home mortgage and automobile to peer to peer lending and cash advance."



### Lenddo

[website](https://www.lenddo.com/products.html#creditscore){:target="_blank"} has a popup ad about an event from 2017, which clearly is **outdated**.   Timelines of this company and events seem to be pre-2017 and have stopped at 2017.

Value proposition:
> "Lenddo’s patented score is a powerful predictor of an individual’s character or 'willingness to pay'"

   
It offers cloud-based alternative credit scoring and identity verification solutions on individual and SMEs, where "alternative" means social media and any digital foot print /online behavior. 

Its product is intended to be complimentary to traditional credit scoring. 

### [zest](https://www.zest.ai/)
[zest](https://www.zest.ai/) has a much more sophisticated website that promises business results such as:
> x% lower charge off rate and y% increase in approval rate


Value proposition:
> ZAML® (Zest Automated Machine Learning) is a machine learning credit and risk modeling solution with *end-to-end explainability* and **compliant** and allows flexible Engagements

With Automated Machine Learning from Zest, lenders small and large are able to originate more loans with greater confidence by assessing borrower risk more accurately—all while remaining compliant with regulatory demands. hundreds of variables and thousands of interaction effects.

Its target industries are: consumer lending (include auto and mortgage), commercial lending, insurance and telecom. 

The company is based in Burbank, CA, and seems to promote a great working enviroment, with the mission "Our mission is to make fair and transparent credit available to everyone." 

<figure>
  <img src="{{ "/images/posts/zest.JPG" | relative_url }}">
  <figcaption>zest timeline</figcaption>
</figure>


### [Scienaptic.ai](https://www.scienaptic.ai/)

Is it just another platform to promise you 1 second credit decision?  [Scienaptic.ai](https://www.scienaptic.ai/) website homepage looks remarkably like [zest](https://www.zest.ai/), with the same color scheme and java-scripted moving network background, likely to be somewhat symbolic of neural network algorithm used.  


Value proposition:
> "Ether platform reduce friction inherent in current credit decisioning processes.
> Unique AI algorithms that are **fully compliant and explainable proprietary**

The proposition demonstrates that, like Equifax, they understand in order for banking customers to use it, the tool needs to be interpretable.  Like Equifax, Scienaptic also promises 30-day deployment, and within customer's firewall.


The description of a platform and the promise that **"Nothing leaves your firewall. Ever"** seem *contradictory*.  Is it **in-house or platform**? 

<figure>
  <img src="{{ "/images/posts/scienaptic.JPG" | relative_url }}">
  <figcaption>scienaptic ether</figcaption>
</figure>

The Ether platform has pre-built APIs for both traditional and **alternative** credit data sources to accelerate data ingestion for sharper credit decisioning.  This seems to be a function that Equifax also has. 

### Summary

There are a lot of activities in the space of applying new technologies (big data + machine learning) to credit scoring in financial services.  The competition is very fierce.   

The winners will need: great product + great people to execute + a viable philosophy/idea. Great execution that help customer making/saving lots of money without higher risk will be the key in building trust and opening doors to more customers.  
