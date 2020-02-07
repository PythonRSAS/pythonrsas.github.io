---
layout: post
tag: Assesing risk factor
category: "market risk"
title: "SOFR vs LIBOR"
description: Comparisons between SOFR and LIBOR
author: Sarah Chen
image: images/posts/all libor-based contracts.png
---

For decades, LIBOR (London interbank offered rate), the cost of large global banks can borrow from each other on wholesale markets, was the de facto benchmark for floating-rate borrowing (LIBOR + spread) around the world.  It’s calculated from a daily survey of more than 15 large banks that estimate the price to borrow from each other without collateral.

I will skip the reasons why LIBOR is being replaced. The reason should be apparent in the comparsion table.  

From New York Fed's [A User’s Guide to SOFR by The Alternative Reference Rates Committee](https://www.newyorkfed.org/medialibrary/Microsites/arrc/files/2019/Users_Guide_to_SOFR.pdf)
SOFR (Secured Overnight Financing Rate) has a number of characteristics that LIBOR and other similar rates based on wholesale term unsecured funding markets do not:   
- It is a rate produced by the Federal Reserve Bank of New York for the public good;  
- It is derived from an active and well-defined market with sufficient depth to **make it extraordinarily difficult to ever manipulate or influence**;  
- It is produced in a *transparent, direct manner* and is based on *observable transactions*, rather than being dependent on estimates, like LIBOR, or derived through models; and   
- It is derived from a market that was able to weather the global financial crisis and that the ARRC credibly believes will remain active enough in order that it can reliably be produced in a wide range of market conditions."
SOFR measures the cost of overnight borrowings through repo transactions collateralized with U.S. Treasury securities, which is the deepest and most liquid money market in the U.S."

Almost one year ago, Mr.Michael Held, Executive Vice President and General Counsel of The New York Fed in [SOFR and the Transition from LIBOR](https://www.newyorkfed.org/newsevents/speeches/2019/hel190226){:target="_blank"} made a good summary of the context, rational, challenges and motivations on the transition from LIBOR to SOFR. 

### Impact $

> Although actual transactions underlying LIBOR have diminished, its use as a benchmark has become ubiquitous.  The gross notional value of all financial products tied to U.S. dollar LIBOR is around $200 trillion—about 10 times U.S. GDP.  That includes $3.4 trillion of business loans, $1.8 trillion of floating-rate notes and bonds, another $1.8 trillion of securitizations, and $1.3 trillion of consumer loans held by about four million individual retail consumers, including around $1.2 trillion of residential mortgage loans.  The remaining 95% of exposures are derivative contracts, which we learned in the financial crisis have consequences for both Wall Street and Main Street.  

Below table reflects the numbers in Mr. Held's Feb 2019 speech:

|  Financial Products Tied to U.S. dollar LIBOR |   Notional Value ($Trillion)|
|:--------------------------------|:------|
| business loans                  |   3.4 |
| floating-rate notes and bonds   |   1.8 |
| securitizations                 |   1.8 |
| consumer - residential mortgage |   1.2 |
| consumer - non-mortgage         |   0.1 |
| derivative contracts            | 191.7 |

Visually,
<figure>
  <img src="{{ "/images/posts/all libor-based contracts.png" | relative_url }}">
  <figcaption>$200 Trillion of LIBOR-based contracts </figcaption>
</figure>

95% of the LIBOR-based contracts are derivatives, which were directly linked to the 2009 Financial crisis.

Chart below reflects the sizes of non-derivative contracts out of the $200 Trillion. 
<figure>
  <img src="{{ "/images/posts/libor-based non-derivative contracts.png" | relative_url }}">
  <figcaption>$5 Trillion of LIBOR-based non-derivative contracts </figcaption>
</figure>

### Comparions of SOFR and LIBOR

| SOFR                |    LIBOR          |
|:-------------------:|:-----------------:|
| secured	 | unsecured    |
| "backward-looking"| forward-looking    |
| calculated & published by New York Fed daily | calculated & published daily by ICE benchmark    |
| based on **actual transactions** | based on **LIBOR bank submissions & expert judgement**    |
| based on $1T daily transaction (repo markets)| based on about sum total of $1 B daily transaction in 3 month  |
|volatile, especially near quarter- and year-end| stable|

As can be seen from the time series below, SOFR is much more **volatile**.   
<figure>
  <img src="{{ "/images/posts/sofr-vs-libor.png" | relative_url }}">
  <figcaption>sofr-vs-libor, Federal Reserve Bank of New York</figcaption>
</figure>

More [technical definition of SOFR from the New York Fed](https://apps.newyorkfed.org/markets/autorates/SOFR):
> The SOFR is calculated as a volume-weighted median of transaction-level tri-party repo data collected from the Bank of New York Mellon as well as GCF Repo transaction data and data on bilateral Treasury repo transactions cleared through FICC's DVP service, which are obtained from DTCC Solutions LLC, an affiliate of the Depository Trust & Clearing Corporation. Each business day, the New York Fed publishes the SOFR on the New York Fed website at approximately 8:00 a.m.

We can get transparent interactive [data](https://apps.newyorkfed.org/markets/autorates/SOFR) including rate and volume from New York Fed as shown below:
<figure>
  <img src="{{ "/images/posts/sofr.PNG" | relative_url }}">
  <figcaption>Secured Overnight Financing Rate Chart from New York Fed</figcaption>
</figure>

### Impact to banks and insurers

A starter list of impacts to banks and insurers.
* **investment portfolios**
* **pricing models**
* **valuation of legacy positions** 
* **back-filled SOFR historical data from Var and SVaR** 
* **Impact to operations and infrastructure**
