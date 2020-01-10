---
layout: post
tag: Assesing risk factor
category: "market risk"
title: "Introdution to Market Risk 市场风险"
description: Description of financial market risk and common metrics
author: Sarah Chen
image: images\posts\laptop.jpg
---


[The Federal Reserve](https://www.federalreserve.gov/supervisionreg/topics/market_risk_mgmt.htm){:target="_blank"} defines market risk as "Market risk encompasses the risk of financial loss resulting from movements in market prices." 

The first factor listed by the Fed is "The sensitivity of the financial institution's earnings or the economic value of its capital to adverse changes in interest rates 利率风险, foreign exchanges rates 汇率风险, commodity prices, or equity prices 股市风险."   A more appropriate name should be "financial market risk". 


### What causes them

Stock prices, exchange rates and interest rates are provided and updated in real time.  But what causes stock prices to fluctuate a lot?  There can be many reasons: political, operational, industry change, competitions, and many more.  Most of them are very difficult or impossible to predict. 
Let's keep them in the back of the mind when we think about market risk. 

A commonly measure  **VaR** or [**Value at Risk**](https://en.wikipedia.org/wiki/Value_at_risk#cite_note-Jorion-1){:target="_blank"}.
 is informally defined as:

For a given portfolio, time horizon, and probability p, the p VaR can be defined informally as the maximum possible loss during that time after we exclude all worse outcomes whose combined probability is at most p. 

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
