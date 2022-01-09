---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Retail Deposit and Attrition Model"
description: overall basics in retail banking deposit and attrition
author: Sarah Chen
image: images/posts/counterparty.jpg
---
<figure>
  <img src="{{ "/images/posts/counterparty.jpg" | relative_url }}">
  <figcaption></figcaption>
</figure>

The attrition model is about how many retail customers will leave the bank at a given point in time.  The target variable can be the number of accounts closed each month. 
Whereas the deposit model is about what is the average balance of customers for the leaving customers. The target variable can be the monthly growth rate of balances.   The two things together tell us how much $ leaving the institution at a given time. 

The key drivers are: 
**rate driven**
- difference of bank rate and benchmark rate (e.g. average rates from top 50 US banks)
- difference of bank rate and rival bank rate

**segmentation**
- customer characterisitics  
- size of deposits: on average, customers with very small balances and large balances have distinctly different behaviors

**event driven**
- Covid pandemic event dummy: to control for the event-based changes.  
- macroeconomic enviroments

# Models specifications
- Attritution model: Logistic regression is often used for the , to model whether a customer stays or leaves.  
- Deposit model: generalized linear model assuming normal (identity link) is used.  The growth rate of average balances by segment are often transformed so that it is approximately normally distributed. 

## Model use 

The models can be used for forecasting future total deposits leaving the bank.   In addition, depending on customer segmentation, the model results can help reveal which branch locations may be increaed or closed for better customer services and profit, as long as following regulatory guidelines.  

In both model development and model use, we need to pay attention to low income populations so that we are not fringing upon any descrimination inadvertently. 

