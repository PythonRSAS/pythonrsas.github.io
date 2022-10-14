---
layout: post
tag: Accounting, banks, AFS, HTM, trading, balance sheet
category: "other risks"
title: "Accounting Treatments and Reclassification"
description: bank accounting classification, treatments and reclassification
author: Sarah Chen
image: images/posts/AFS.PNG
---

- [Accounting classifications of bank assets](#accounting-classifications-of-bank-assets)
- [Why do banks own securities besides loans](#why-do-banks-own-securities-besides-loans)
- [Reclassifying](#reclassifying)
- [Unanswered questions](#unanswered-questions)
- [Reference](#reference)

Accounting is a complicated topic.  This post tries to summarize the types of accounting classifications on bank assets and impacts on reclassification. 

Image from [New York Fed Quarterly Trends for Consolidated U.S. Banking Organizations](https://www.newyorkfed.org/research/banking_research/quarterly_trends.html).  Consolidated financial statistics for the U.S. commercial banking industry, including both bank holding companies (BHCs) and banks. Statistics are based on quarterly regulatory filings. Statistics are inclusive of BHCs' nonbank subsidiaries. 

# Accounting classifications of bank assets

Below is a summary of the three accounting classifications of bank assets:

**Trading**: Securities (debt and equity) that are bought and held for the purpose of selling in the near term. They are reported at fair value.  ***Unrealized gains and losses are included in the earnings***. 

**Held to maturity (HTM)**: Debt securities that the firm has the positive intent and ability to hold until maturity. (Equities can’t be included in this category since they don’t mature.)   They are reported at ***amortized cost***.  

**Available for sale (AFS)**: A catch-all for debt and equity securities not captured by either of the above definitions. These are securities that the bank may retain for long periods but that may also be sold.  Often, they are held in the Treasury department of large banks.  The types of securities may include: US Treasury, sovereign debt, MBS, municipal bonds, corporate bonds, and so on.  They are reported at **fair value**.  However, ***non-credit related unrealized gains and losses are excluded from earnings***.    The noncredit-related component of the fair value decline is recognize in other comprehensive income (*OCI*). See [source](https://www.federalreserve.gov/supervisionreg/topics/faq-new-accounting-standards-on-financial-instruments-credit-losses-accessible.htm). 

Because of the different accounting treatments, in particular on HTM and AFS, banks have been reclassifying their assets for various purposes. 

# Why do banks own securities besides loans

To understand how and why banks classify assets, we should first know why banks hold security assets in addition to loans.

1. Banks may face an **imbalance between desposits and lendings**.   For example, there may not be enough good profitable lending opportunities.   In such cases, funding-rich banks may choose to invest in securities that reflect lending by other banks or by nonbank lenders (e.g., mortgage-backed securities issued by another lender), or direct debt issuance by nonfinancial firms (e.g., corporate bonds).

2. For risk management and to meet regulatory requirements: securities can be sold more easily and with lower price impact than loans, for which the secondary market is less active. Regulation such as the **liquidity coverage ratio** developed as part of the Basel III Capital Accord requires banks to hold enough high-quality liquid assets to meet their liquidity needs under a thirty-day liquidity stress scenario.

3. From a risk management point of view, holding securities may help the bank diversify or mitigate its risk exposures. Conversely, adjusting securities holdings can provide a straightforward way for banks to ramp up their level of risk in an effort to increase expected returns. For example, recent research argues that banks respond to expansionary monetary policy by lengthening the maturity of their securities portfolios, in an effort to boost yields.

4. Keeping an inventory of securitiesfor market-making, broker-dealers services.

5. Regulatory arbitrage:  holding securities instead of loans may reduce capital requirements.

# Reclassifying

Since AFS is a catch-all category, that means that banks can move assets in or out of the AFS to the other ones when the intent has changed.  For example, HTM to AFS and vice versa. Why?  Mostly to stablize capital adequacy ratio and to stablize earnings. 
![securities of three accounting classes](https://pythonrsas.github.io/images/posts/Securities%20Portfolios.PNG)
![AFS](../images/posts/AFS.PNG)


![HTM](../images/posts/HTM.PNG)

Notice in the chart the HTM (red) has more than doubled in size as a percentage of all bank assets over the past several years. 

A key difference between HTM and AFS is the accounting treatment of gains and losses as described at the begnning of the post.   The gains and losses in the value of HTM  that result from market movements (e.g., interest rates) aren’t recognized unless the asset is sold.   

For AFS securities, however, such shifts in value, while not affecting accounting income, do affect the measurement of regulatory capital adequacy for large banks under the Basel III framework (for so-called “advanced approaches” firms).  

On Oct 11, 2013, the [Federal Register](https://www.govinfo.gov/content/pkg/FR-2013-10-11/pdf/2013-21653.pdf), published by the Department of Treasury and the OCC, wrote "[...] consistent with Basel III, the agencies and the FDIC proposed to
require banking organizations to include
the majority of AOCI components in
common equity tier 1 capital."   Then it went on to say that they received a significant number of comments on the proposal to require banking organizations to recognize AOCI in common equity tier 1 capital.  Interestingly, the comments expressed concerns that became reality:
the change would introduce significant volatility in banking organizations’ capital ratios due in large part to
fluctuations in benchmark interest rates, and would result in many banks moving AFS securitiesinto HTM or holding additional regulatory capital solely to mitigate the volatility resultingfrom temporary unrealized gains and losses in the AFS securities portfolio.The commenters also asserted that the change would likely impair lending and negatively affect banks’ ability to manage liquidity and interest rate risk and to maintain compliance with legal lending limits. 

For example, in 2014, [Bloomberg reported](https://www.bloomberg.com/news/articles/2014-02-26/banks-averting-bond-losses-with-accounting-twist-credit-markets) that JMPC and Wells Fargo are leading a shift in how banks account for their bond investments after a $44 billion plunge in value exposed a potential drain on capital under new rules.  It also reported that The largest U.S. lenders are moving assets into HTM instead of designating them as AFS.

If you own that bond for investment purposes, and you don't have any "intent of selling it within hours or days," you have an investment loss on paper, but you get to treat it a bit more gently. (This is called "available for sale," or AFS.) The loss doesn't flow through your net income; instead it flows through a different place called "other comprehensive income," and everyone agrees to treat that as somewhat less important than net income. Everyone except Basel III bank capital regulation: Last year, regulators ungallantly decided to require you to treat those unrealized investment losses as reducing your capital.

# Unanswered questions

**AFS as a whole decreased** the most (slope the steepest) after 2003 until the GFC.   Was it **due to rising rates** of that period?  What was the accounting method before and after 2003? 

If it was due to rising rates, then we expect to see reduced AFS in 2022 as the Fed has been increasing rates.  Indeed, even with 1 quarter of the data in 2022, we see that AFS has dropped.  We will find out more when the new quarterly reports comes out.  

Transfering assets from AFS to HTM can educe the volatility of regulatory capital ratios.  However, the move will limit banks’ ability to sell those securities in the future.  What does that mean for risk management and profitability of the banks?  Would it affect negatively banks’ ability to manage liquidity and interest rate risk since banks won't be able to sell from HTM? 

# Reference

[Federal Reserve Supervisory Policy and Guidance Topics on Accounting](https://www.federalreserve.gov/supervisionreg/topics/accounting.htm)

[Federal Register / Vol. 78, No. 198 / Friday, October 11, 2013 / Rules and Regulations](https://www.govinfo.gov/content/pkg/FR-2013-10-11/pdf/2013-21653.pdf)

[Available for Sale? Understanding Bank Securities Portfolios](https://libertystreeteconomics.newyorkfed.org/2015/02/available-for-sale-understanding-bank-securities-portfolios/)

[Quarterly Trends for Consolidated U.S. Banking Organizations
First Quarter 2022 Federal Reserve Bank of New York](https://www.newyorkfed.org/medialibrary/media/research/banking_research/quarterlytrends2022q1.pdf?la=en)

[Bloomberg: Banks Averting Bond Losses With Accounting Twist: Credit Markets](https://www.bloomberg.com/news/articles/2014-02-26/banks-averting-bond-losses-with-accounting-twist-credit-markets)