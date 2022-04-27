---
layout: post
tag: Assesing risk factor
category: "market risk"
title: "Introdution to Market Risk 市场风险"
description: Description of financial market risk and common metrics
author: Sarah Chen
image: images/posts/VaR_diagram.jpg
---

# What is market risk
[The Federal Reserve](https://www.federalreserve.gov/supervisionreg/topics/market_risk_mgmt.htm){:target="_blank"} defines market risk as "Market risk encompasses the risk of financial loss resulting from movements in market prices." 

The first factor listed by the Fed is "The sensitivity of the financial institution's earnings or the economic value of its capital to adverse changes in interest rates 利率风险, foreign exchanges rates 汇率风险, commodity prices, or equity prices 股市风险."   A more appropriate name should be "financial market risk".  In more plain terms: the risk that financial assets may lose value. 

Think of it this way, if you are a farmer, your market risk is the unpreditability of your costs of fertilizers, seeds and other costs for you to produce, that you have to pay, prices of crop that you will get at harvest time, and the weather.    

Banks are more exposed if they are heavily involved in investing in capital markets or sales and trading of financial instruments.  If a bank has a large trading department, and/or is a big market maker, then it will sustantial market risk.  There are four main types of market risk:

1. Interest rate risk: affecting bonds, swaps and other interest rate derivatives. 
2. Equity risk (stock market risk)
3. Commodity risk: commodity investments and derivatives. 
4. FX risk: currency swaps, or investments in currencies. 

Most stock and commodity prices, exchange rates and interest rates are provided and updated in real time.  But what causes rates and prices to fluctuate a lot?  There can be many reasons: economy, political, government policy, operational, industry change, competitions, and many more.  Most of them are very difficult or impossible to predict.  Let's keep that in the back of the mind when we think about market risk. 

# Measuring market risk

A commonly measure  **VaR** or [**Value at Risk**](https://en.wikipedia.org/wiki/Value_at_risk#cite_note-Jorion-1){:target="_blank"}.
 is informally defined as:

For a given portfolio, time horizon, and probability p, VaR can be defined informally as the maximum possible loss during that time horizon after we exclude all worse outcomes whose combined probability is at most p. 

A 1-day 99% Var is the 1-day maximum possible loss at >=99% probability. Informally, it is a hypothetical number that we are very sure that our 1-day loss won't go above.  Our guess would have to be higher if we wanted to be even more sure.  

This assumes mark-to-market pricing, and no trading in the portfolio.

But the assumptions are not valid:

* **mark-to-market pricing** - It is not difficult to obtain mark-to-market prices for the past, but it is impossible to measure mark-to-market pricing for the future. So banks often use book value.  This is a proxy but can be very far off. 
* **no trading in the portfolio.** - For institutions, especially the larger ones, their portfolio change often.

VaR can still provide us with some ballpark for our market risk in a "normal day".   However, normal days don't last.  

We have concluded that for various reasons it is close to impossible to predict market risk VaR.

Let's see how banks and other financial institutions achive the 'mission impossible':
<div class="note"><p>
<b>Note</b>: Many institutions often first compute 1-day VaR and then scale it up to 10-day VaR using the so-called "square root of time rule".  The jargon of "square of time" is nothing but the basic statistics that variance of a sum of n iid random variables is the variance of one of them multipled by the square root of n.  This assumption of iid ignores correlation and autocorrelation and assumes constant variance.  Obvious not correct!  See a simple explaination in <a href="https://www.bionicturtle.com/forum/threads/what’s-wrong-with-multiplying-by-the-square-root-of-time.10035/" target="_blank">Bionic Turtle </a> and <a href="https://www.sas.upenn.edu/~fdiebold/papers/paper18/dsi.pdf" target="_blank">Converting 1-Day Volatility to h-Day is Worse than You Think
</a> 
</p></div>

Regulated financial institutions only have to prove that they are conservative to the regulators.  

Since the square root of time rule has been shown empirically to be conservative, and it is simple and straighforward for regulators to manage, it is accepted.   

Below are the three most commonly used VaR calcuation methods. 

### Parametric VaR

> Advantage: easy and fast to compute.  All you need is volatility and correlation. 
Diadvantage: it is based on normal assumptions.  

### Monte Carlo Simulation

> Advantage: can build in more flexible distribution assumptions including fat-tails; actual data not required.
Disadvantage: computationally intensive, and subject to model risk. 


### Historical simulations

> Advantage: based on actual data, faster than Monte Carlo.
Diadvantage: some past data may not be relevant.

<figure>
  <img src="{{ "/images/posts/VaR_diagram.jpg" | relative_url }}">
  <figcaption>VaR diagram</figcaption>
</figure>

# Comparison with Loan Credit Risk

**Credit risk**:  When banks lend out loans, the principals are in the borrower's hands. The risk is in the borrower may not pay back the loan (in full). In addition, some borrowers may pay back early, which result in interest loss. 

Whereas market risk is not funded.  The risk is in the loss of the market values of the financial assets.  

# Comparison with counterparty Credit Risk
Counterparty credit risk arises when it is in the money for the bank because the other party may not keep its promise.  Counterparty credit is not a funded risk.  The risk is when the contract is "in the money" for the bank, i.e. the risk is only when you have something to lose.   At the initation of a contract, neither party owes anything to the other.  But as time goes on, the pendulum will be either be favorable to one side or the other.  There are two time periods that credit risk can happen:
1. Between margin call (beginning time of having something to lose) and time that the contract must be closed due to counterparty default.  This time period is one or two days
2. Between the time of closing contract to the counterparty to the unwinding of the contract (either to find another counterparty or to take over the entire contract).  This time period is unknown.  This is similar to workout period in credit risk loss given default calculation.  The workout period is unknown before it actually happens.  

Like market risk, counterpary credit risk also uses simulation to generate loss distributions: simulation => loss distribution.  A very similar concept to VaR is *PFE*, which is the 95th or other higher percentile loss. 