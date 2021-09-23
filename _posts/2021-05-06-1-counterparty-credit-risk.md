---
layout: post
tag: Assesing risk factor
category: "credit risk"
title: "Counterparty Credit Risk"
description: Counterparty credit risk basics
author: Sarah Chen
image: images/posts/counterparty.jpg
---
<figure>
  <img src="{{ "/images/posts/counterparty.jpg" | relative_url }}">
  <figcaption></figcaption>
</figure>

# What is counterparty credit risk
Counterparty credit risk is a subset of credit risk.  

Specifically, for the two sides (parties) in OTC derivative contracts, counterparty credit risk is the risk that one may default on its obligations under the contracts prior to settlement and therefore causing losses to the other.  This is sometimes also referred to as "pre-settlement risk".   Note that exchange-traded contracts usually are not exposed to settlement risk.  The Dodd-Frank act authorized centralized exchanges for clearing swaps. 

Counterparty credit risk is important due to the huge increase in derivatives and that counterparty credit risk can trigger severe losses, such as credit default swaps to the 2008 Financial Crisis. 

# Difference between counterparty credit risk and credit risk from lending

There are two key factors that distinguishes it from traditional credit risk from lending:

**1.	Exposure uncertainty**.  

In traditional insurance contract, policy coverage limit caps how much an insurer will indemnify the insured in the event of covered loss.  In bank term loan contract, the amount the bank has lent to the borrower is the exposure at risk.    

Whereas the credit exposure under derivative contracts is a *function* of market conditions and other underlying risk factors.  It is much more stochastic (aka random) in nature.  

In plain words, for a particular derivative contract, a bank has counterparty credit risk **if it has something to lose** if the other side does not fulfill the contract.   

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

In most financial institutions, for a large customer, the credit officers approving counterparty limits is also responsible for approving limits for all other credit exposures relating to the customer, including loans, bonds, trade transactions and derivatives.   Credit officers monitor these limits to control maximum potential loss in case of default. 

# CVA

From the quantitative perspective, as credit risk in general, counterparty credit risk has the following components:
*	**Exposure estimation**
*	**Probability of default and credit migration estimation**
*	**Recovery rate** (or 1 – LGD)
*	**Correlation between credit events**

Credit valuation adjustment (CVA) is the difference between the risk-free portfolio value and the market value of portfolio.    In other words, CVA = market value of counterparty credit risk.

On the high level, CVA = LGD * Exposure * PD

This formula looks identical to the one from credit risk loss.  However, adue to the domain differences (loans vs derivatives), each of the components will have different calculations.  

# Exposure

In lending, exposures in revolver loans are not exactly fixed.  Customer may borrow up to what has been contractually committed. In EAD modeling, we measure the change in exposure by credit conversion factor (CCF) for defaults and facility incremental use (FIU) for performing loans.  Lending is one sided and the risk is one-sided.  

For counterparty credit risk, the exposure depends on market factors and the credit exposure (CE) = maximum (market value, 0) = maximum (f(market factors), 0).  

* **Expected exposure (EE)**: Mean market value on future target date, conditional on positive exposures
* **Potential future exposure (PFE)**: A high percentile market value of exposure, conditional on positive exposures.  It is similar to value at risk (VaR) for estimating market risk,

For example, PFE, EE and other measures are calculated using Monte Carlo simulations as illustrated.  
<figure>
  <img src="{{ "/images/posts/counterparty_exposure_simulation.PNG" | relative_url }}">
  <figcaption> exposure calculation based on Monte Carlo Simulation</figcaption>
</figure>

The required inputs to a simulation are: 
1. assumed distribution for the interest rates or an interest rate model.  
2. model the interest rates for future dates
3. compute future swap values based on future interest rates
4. run step 2 and 3 thousands of times
5. at each time point, we get a distribution of simulated exposure, from which we can calculate PEF and EE. 


# collateral

The purpose of collateral is to reduce CCP.  If there is a margin agreement, then one or both parties need to post(pay) margin (aka: deposits or collateral).
Collateral is akin to the deposit you pay when buying something such as a home.  The use of margin is like why people borrow mortgage when buying a real estate: leverage.  You can buy a lot more than what you have cash for. 

## netting
Netting is with respect to multiple contracts to the same counterparty.  For a specific counterparty, multiple contracts may have positive or negative market values at the same time. Netting agreement allows offsetting the postive values with the negative ones.  

For example, at time 1, contract a has value 100, contract b has value -90.   With netting, the exposure is 100- 90 = 10.  Without netting, the exposure is 100 + max(0, -90) = 100. 

Therefore, netting can reduce counterparty credit risk. 

We can think of it as a "diversification" benefit with some twists and turns.  Netting not only depends on linear correlation of the vectors of values at future time points, but also size of the values. 

## wrong way risk

The situations that exposure is positively correlated with credit quality of the counterparty, i.e., both PD and LGD are increasing at the same time.  we call them "wrong way risk".  

The causes of wrong way risks are either self-inflicted  or due to external factors such as macroeconomic factors. 

Applying haircut, decrease or discounted valuation apply to noncash collateral, is one of the methods to mitigate wrong way risk. 

## variation margin

Variation margin is the daily margin payment (can be more frequent) to keep exposure (market value - collateral, i.e. the unsecured portion) below certain thresholds. Margin payments must be liquid funds.  As a result of these daily variation margins, the counterparty risks are mitigated.  


## initial margin (IM)

Even when variation margin payments + existing collateral cover the entire exposure such that the net exposure is zero, there is still risk.  

The risk is somewhat opposite in concept to "float".  The "float" is the time value of money that you earn by using the time that money is in your hand.  Oppositely, things can go wrong from the last variation margin payment time and (potential) default, during which we may suddendly have a large exposure.   This time period is what is called the "**margin period of risk**" (MPR).  

Formally, it is the time period from the last exchange of collateral covering a netting set of transactions with a defaulting counterparty until that counterparty is closed out and the resulting market risk is re-hedged.

<figure>
  <img src="{{ "/images/posts/ccr_initial_margin.PNG" | relative_url }}">
  <figcaption> calculation of initial margin - photo from Tokyo Stock Exchange</figcaption>
</figure>


Because of this "exposed" period, we need something called "*initial margin*". 

Assuming only variation margin, the best-case reduction of counterparty risk can be shown to be approximately half the square root of the ratio of the maturity of the underlying portfolio to the MPR. For a five-year OTC derivatives portfolio, with a MPR of ten business days, this would lead to an approximate reduction of 0.5 × SQRT (5* 250  days /10 days) ≈ 5.6 times." (Source: Jon Gregory, The xVA Challenge: Counterparty Credit Risk, Funding, Collateral, and Capital, 3rd edition (West Sussex, UK: John Wiley & Sons, 2015))


Replacement cost (RC)
Losses due to counterparty default are quantified using *replacement cost* (RC) of defaulted derivative, which can be severe in case of large and illiquid positions. 

For trades without margin, the RC tries to capture the loss that would occur if the other party were to default and drop out of the transactions **immediately**.  The PFE represents a potential conservative increase in expsoure over a one-year time horizon from the calculation date. 

For margined trades, the RC is about the loss that would occur now or in the future, assuming the closeout and replacement of transactions occur instantaneously, which is not necessarily the case.  The PFE add-on is the potential change in value of the trades. 

RC is calculated at the netting set level (higher level).  


