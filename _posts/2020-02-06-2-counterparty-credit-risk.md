---
layout: post
tag: Assesing risk factor
category: "market risk"
title: "Counterparty Credit Risk"
description: Counterparty credit risk basics
author: Sarah Chen
image: images/posts/counterparty.JPG
---
<figure>
  <img src="{{ "/images/posts/counterparty.jpg" | relative_url }}">
  <figcaption></figcaption>
</figure>

# What is counterparty credit risk
Counterparty credit risk is a subset of credit risk.  

Specifically, for the two sides (parties) in OTC derivative contracts, counterparty credit risk is the risk that one may default on its obligations under the contracts prior to settlement and therefore causing losses to the other.  This is sometimes also referred to as "pre-settlement risk".   Note that exchange-traded contracts usually are not exposed to settlement risk.  

Counterparty credit risk is important due to the huge increase in derivatives and that counterparty credit risk can trigger severe losses, such as the 2008 Financial Crisis. 

# Difference between counterparty credit risk and credit risk from lending

There are two key factors that distinguishes it from traditional credit risk from lending:

**1.	Exposure uncertainty**.  

In traditional insurance contract, policy coverage limit caps how much an insurer will indemnify the insured in the event of covered loss.  In bank term loan contract, the amount the bank has lent to the borrower is the exposure at risk.    

Whereas the credit exposure under derivative contracts is a *function* of market conditions and other underlying risk factors.  It is much more stochastic (aka random) in nature. 

This uncertainty has two steps:
1.	Whether there is credit exposure, and 
2.	How much

In plain language, for a particular derivative contract, a bank has counterparty credit risk **if it has something to lose** if the other side does not fulfill the contract.   

Bank has credit exposure to its counterparty only if it is in the money, i.e., if the contract value is positive from the bank’s perspective.   Because the bank has to pay new counterparty money to assume the position of the defaulted old counterparty. 

**2. Counterparty credit risks are bilateral except for options**.  

For options, the credit exposure is always positive for the holder and negative for the writer.   For non-option derivatives, either party can face credit losses if the other party defaults. 

At least in theory, CCR is a subset of aggregate credit risk to any customer.  In most financial institutions, for a large customer, the credit officers approving counterparty limits is also responsible for approving limits for all other credit exposures relating to the customer, including loans, bonds, trade transactions and derivatives.   Credit officers monitor these limits to control maximum potential loss in case of default. 

## Counterparty credit risk management

Counterparty credit risks are aggregated to the customer level.  

The aggregation process involves:

-	netting
-	applying credit mitigation agreements
-	collateral management

CCR management requires combination of systems integration, efficient simulation capacities, and good pricing functionalities that are fast and accurate.  

From the quantitative perspective, as credit risk in general, CCR has the following components:
*	**Exposure estimation**
*	**Probability of default and credit migration estimation**
*	**Recovery rate** (or 1 – LGD)
*	**Correlation between credit events**

In most financial institutions, for a large customer, the credit officers approving counterparty limits is also responsible for approving limits for all other credit exposures relating to the customer, including loans, bonds, trade transactions and derivatives.   Credit officers monitor these limits to control maximum potential loss in case of default. 

Losses due to counterparty default are quantified using *replacement cost* (RC) of defaulted derivative, which can be severe in case of large and illiquid positions. 

Using credit risk terminology, it is about risk that LGD>0. 

Terminologies:
1. Replacement cost (RC)
2. Potential future exposure: this is very similar in concept to some of those in EAD modeling (credit conversion factor for defaults and incremental use for performing)
3. Margin agreement: if there is a margin agreement, then one or both parties need to post(pay) margin (aka: deposits or collateral)
4. Haircut: decrease or discounted valuation apply to noncash collateral. 

For trades without margin, the RC tries to capture the loss that would occur if the other party were to default and drop out of the transactions **immediately**.  The PFE represents a potential conservative increase in expsoure over a one-year time horizon from the calculation date. 

For margined trades, the RC is about the loss that would occur now or in the future, assuming the closeout and replacement of transactions occur instantaneously, which is not necessarily the case.  The PFE add-on is the potential change in value of the trades. 

RC is calculated at the netting set level (higher level).  

PFE add-ons are at each asset class level within a given netting set and then aggregated (lower level). 

