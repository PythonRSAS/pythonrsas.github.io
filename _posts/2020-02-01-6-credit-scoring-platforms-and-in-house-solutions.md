---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Credit Scoring Platforms and In-House Solutions"
description: Notes on credit scoring platforms, approaches and in-house solutions from large and very small ones
author: Sarah Chen
image: images\posts\equifax_pres.JPG
---

This post is a summary on credit scoring platforms and credit scoring in-house solutions out there and what they do. 

All credit scoring in the US must adhere to FCRA, ECOA, SCRA and FHA.  So security, data privacy + machine learning interpretability are pre-requisites.  

The order of the platforms in the post is completely **random**.  There is **no implied superiority**.  In fact, some of them are very small start-ups. 


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

This is a quote from SAS website:
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

The pain is correctly identified.  

But the solution is not working out well everywhere.  

In-house solution has advantages if the people of the house is working together and not working separately.  

<figure>
  <img src="{{ "/images/posts/sas_in_house_credit_scoring.JPG" | relative_url }}">
  <figcaption>SAS in-house credit scoring development process</figcaption>
</figure>



Here is the [product brief](https://www.sas.com/content/dam/SAS/en_us/doc/productbrief/sas-credit-scoring-100665.pdf){:target="_blank"}



Besides SAS, other commerical in-house solutions include [Matlab from mathworks](https://www.mathworks.com/discovery/credit-scoring-model.html){:target="_blank"}

### Gini Machine

From a startup in Lithuania.  

Selling point: machine learning platform for fast credit scoring. 

Here is its value proposition from its website:
"Traditional ways of building risk models require much time, a great deal of heavy lifting and specialised expertise. This is what GiniMacine changes. Without a PhD in statistics and the necessity to write code, you can build, validate and deploy powerful scoring models. With its intuitive UI and a wealth of pro-level features, GiniMachine is a perfect fit for risk managers, developers and business owners alike."

<figure>
  <img src="{{ "/images/posts/gini-machine.JPG" | relative_url }}">
  <figcaption>gini machine</figcaption>
</figure>

It makes quick promises like those in the screenshot below.  

But we know that these days even a teenager can write and run gradient boosting code that gives you better "performance". 

But the key things are **missing**: **model risk**?   **interpretability**?  **regulatory approvals**? actual **business success**? 

<figure>
  <img src="{{ "/images/posts/gini-machine-promise.JPG" | relative_url }}">
  <figcaption>gini machine promise</figcaption>
</figure>

### Lenddo

Its [website](https://www.lenddo.com/products.html#creditscore) has a popup ad about an event from 2017, which clearly is **outdated**. 

Value proposition:
> "Lenddo’s patented score is a powerful predictor of an individual’s character or 'willingness to pay'"

Timelines of this company and events seem to be pre-2017 and have stopped at 2017.   

"Market leader in alternative credit scoring and identity verification solutions, allowing individuals and SMEs to use their digital footprints to unlock access to financial services with the use of cloud-based solutions."

Either the company is working on something in secrecy or has stopped existence. 


The LenddoScore can be deployed at the wide end of the funnel to prioritize applications or within an existing underwriting scorecard to reduce risk or approve more applications. The LenddoScore complements traditional underwriting tools, like credit scores, because it relies exclusively on non-traditional data derived from a customer’s social data and online behavior. When the LenddoScore is added to a traditional underwriting scorecard, it has been proven to better discriminate between good and bad borrowers. 

<div class="code-head"><span>code</span>sample-from-python-org.py</div>

```python
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
fib(1000) = train_test_split(X, Y, test_size=0.33, random_state=seed)
```

* Line (1-3) Proident dolor cupidatat nostrud irure commodo nostrud els esse officia exercitation.
* Line (4-7) Sit irure ut ut id do culpa ullamco qui est.

### Nulla proident dolor cupidatat  deserunt eiusmod eu id ex.

Lorem ipsum sint ut labore fugiat eiusmod voluptate exercitana culpa dolore sit sint enim. Lorem ipsum in velit ex laborinisi dolor laboris sed do enim sit eu <span class="coding">Odkfsdy</span> dfsdgg.

We will use the above Deep Neural Network architecture which has a **sdfsdle yutm xvwe**, **2 pire xaq**.

Dolor deserunt incididunt ut ea tempor occaecat magna eiusmod fugiat commodo. Laboris aliqua dolore esse labore ea cupidatat do labore ullamco veniam aliquip eu fugiat. Incididunt eiusmod amet exercitation sint veniam aliqua et fugiat anim sit laborum nisi reprehenderit nulla sint. Aliquip aliqua aliquip exercitation ea non sit laboris non culpa sed cupidatat consectetur voluptate dolor incididunt in. In ad tempor culpa cillum in magna est veniam in aliqua anim.

Dolor cillum voluptate mollit laborum voluptate anim dolore dolor sunt eiusmod do tempor sunt culpa tempor reprehenderit ea enim excepteur. Ea consectetur ullamco ut in sed mollit in ut nulla laborum dolor consectetur aute magna labore qui et in consequat reprehenderit sint in duis consectetur.

<div class="code-head"><span>code</span>from-doc-site.py</div>

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

* Line (1), Lorem ipsum culpa labore  <span class="coding">import</span> Est occaecat ad laboris eimodo ut exercitation culpa ex.
* Line (2), Pariatur consectetur ut mollit in eu esse :
  * <span class="coding">[8]]</span>: Im occaecat aliquip eiusmod cupidatat in velit aute magna cupidatat
  * <span class="coding">raw</span>: Lorem ipsum ullamco est dolore magna ut pariatur exercitation ea esse anim labore.
  * <span class="coding">data</span>: specify whether <span class="coding">uniform</span> or  <span class="coding">normal</span>.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo quas ipsam, magnam vel architecto cumque deserunt inventore autem voluptatem minus molestias fuga unde corporis soluta quisquam sapiente consequatur, aut tempora labore id repellat omnis harum? Eveniet velit laboriosam, quas optio, enim iure nesciunt repudiandae hic temporibus facilis, corporis maxime qui quis esse nam? Quod, enim, odio? Sapiente blanditiis quisquam voluptatem fuga quod fugit molestiae illum dolor itaque id ipsam, quasi, quae repellendus error placeat impedit maxime qui nobis est veritatis.
