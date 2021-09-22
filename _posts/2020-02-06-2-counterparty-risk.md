---
layout: post
tag: Assesing risk factor
category: "market risk"
title: "Counterparty Risk"
description: Counterparty risk analytics
author: Sarah Chen
image: images/posts/counterparty.jpeg
---
<figure>
  <img src="{{ "/images/posts/counterparty.jpeg" | relative_url }}">
  <figcaption>$200 Trillion of LIBOR-based contracts </figcaption>
</figure>
For the two sides (parties) in OTC derivative contracts, counterparty credit risk is the risk that one may default on its obligations under the contracts prior to settlement and therefore causing losses to the other.  This is sometimes also referred to as "pre-settlement risk".   Note that exchange-traded contracts usually are not exposed to settlement risk.  

Losses due to counterparty default are quantified using *replacement cost* (RC) of defaulted derivative, which can be severe in case of large and illiquid positions. 
There are two key factors that distinguishes it from traditional credit risk from lending:
1.	**Exposure uncertainty**.  In traditional insurance contract, policy coverage limit caps how much an insurer will indemnify the insured in the event of covered loss.  In bank term loan contract, the amount the bank has lent to the borrower is the exposure at risk.    Whereas the credit exposure under derivative contracts is a *function* of market conditions and other underlying risk factors.  It is much more stochastic (aka random) in nature. 

This uncertainty has two steps:
1.	Whether there is credit exposure, and 
2.	How much
In plain language, for a particular derivative contract, a bank has counterparty credit risk *if it has something to lose* if the other side does not fulfill the contract.   Bank has credit exposure to its counterparty only if it is in the money, i.e., if the contract value is positive from the bank’s perspective.   Because the bank has to pay new counterparty money to assume the position of the defaulted old counterparty. 

Counterparty credit risk is incurred by any transaction between two parties when the *replacement* cost in the event of default of one party is larger than zero to the other. 

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

