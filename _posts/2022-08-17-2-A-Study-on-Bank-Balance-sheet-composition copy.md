---
layout: post
tag: Accounting, banks, AFS, HTM, trading, balance sheet
category: "other risks"
title: "A Study on Bank Balance sheet composition"
description: composition of assets and liability of consolidated US commercial banks over time
author: Sarah Chen
image: images/posts/balance_sheet_composition.PNG
---

This post is a study on the bank balance sheet composition based on "Quarterly Trends for Consolidated U.S. Banking Organizations, First Quarter 2022" published by the Federal Reserve Bank of New York. The study can be used for benchmark for your own bank, and for study of what is happening to the banking industry as a whole and a glimpse of the overall US economy. 


Consolidated financial statistics for the U.S. commercial banking industry, including both bank holding companies (BHCs) and banks. Statistics are based on quarterly regulatory filings. Statistics are inclusive of BHCs' nonbank subsidiaries. 

Look at it from distribution perspective overtime:

# Q1 2022 recent trends
• **Decreased return on equity and return on assets**, from 11.06% and 1.06% in 2021:Q4 to 10.34% and 0.93% in 2022:Q1 respectively, reflecting an **increase in quarterly loan loss provisions and noninterest expense**.

• **Net interest margin remains low**, (net interest margin defined as net interest income as a percentage of interest earning assets),
remained the same as last quarter at 2.10%. The current net interest margin of 2.10% is below its post-crisis (2009:Q1 – 2022:Q1) average of 2.61%.

• **Reduced noninterest income ratio**, measured as noninterest income as a percentage of total assets, declined from 1.96% in 2021:Q4 to 1.90% in 2022:Q1, which is below its post-crisis average of 2.17%.

• **Slower asset growth** from 8.29% in 2021:Q4 to 6.26% in 2022:Q1. However, *loan growth rose from 3.99% to 4.83%*. So, which asset growth decreased the most? 

• **Significant decreased domestic deposit growth from 12.55% to 8.94%**.

• **Capital remains high by historical standards**. Common equity tier 1 (CET1) capital as a percentage of risk-weighted assets (RWA) stands at 12.41%, well above its pre-crisis (2001:Q1 – 2007:Q3) average of 8.25%.   Note that in 2015:Q1 firms commenced reporting risk weighted assets according to Basel III definitions rather than Basel I definitions.   This contributes to the **sharp increase in the ratio of risk weighted assets to total assets observed in 2015:Q1**.

# Composition of Banking Industry Assets and Liabilities

The 30-year chart shows that industry assets grew from about $4 Trillion in 1991 to over $25 Trillion in 2021. 

![balance_sheet_composition](../images/posts/balance_sheet_composition.PNG)
Image from [New York Fed Quarterly Trends for Consolidated U.S. Banking Organizations](https://www.newyorkfed.org/research/banking_research/quarterly_trends.html)

The composition chart below shows that on the asset side:
- The *Cash & Interest Bearing Balances* category slowly decreased from 1991 until the Great Financial Crisis (GFC), and then grew significantly after the crisis. 
- The *Fed Funds Sold and Reverse Repos* category increased slowly since the 90s and remain steady as a percent of total assets.
- The *Loans* category has been shrinking over the last 30 years from about 60% to 40%.  That's a 1/3 drop. 
And from the liability side:
- Deposits were close to 80% of liability in 1991. Then it decrased over time in sync with the decreases in loans until the crisis.  These traditional banking activities increased again after the crisis.
- Two other liability categories also have moved in the same direction as deposits. 
The equities has only very mild increase in the 30 year period.

![Balance Sheet Composition Percent of Assets](../images/posts/Balance Sheet Composition Percent of Assets.PNG)

![Balance Sheet Composition, Percent of Assets Current Quarter](../images/posts/Balance Sheet Composition, Percent of Assets Current Quarter.PNG)

## Federal Funds Sold and Purchased

Both Fed Funds sold and purchased as percent of total assets have been dropping over time since 2002 when the data was available. Note: These charts begin in 2002:Q1 because data for repurchase agreements and federal funds are not consistently reported separately prior to that date. 
![Federal Funds Sold and Purchased](../images/posts/Federal Funds Sold and Purchased.PNG)

## Repurchase Agreements

Repo and reverse repo seem to be negatively correlated in a zero-sum game fashion over time since 2002 when the data was available. Note: These charts begin in 2002:Q1 because data for repurchase agreements and federal funds are not consistently reported separately prior to that date. 
![Repurchase Agreements](../images/posts/Repurchase Agreements.PNG)

## Loans
We already know that loans as % of total assets have dropped over the last 30 years.  However, looking closely, we see that the decrease mainly come from *Residential Real Estate, C&I, and consumer*.  CRE loans as % of total assets has remained more or less the same. 
![Loans](../images/posts/Loans.PNG)

### Consumer loans
Among consumer loans, it is worth taking a closer look at the breakdown between credit cards, auto and other.  It seems that *credit cards have remained more or less around 3% of total assets*.  
![consumer loans](../images/posts/consumer loans.PNG)

## Trading Assets and Liabilities
Note: The subcomponents of trading assets and liabilities in the above chart only represent banks and
BHCs that reported total trading assets of $10 million or more in any of the four preceding quarters, and
$2 million or more in average trading assets in any of the four preceding quarters prior to 2018:Q2.
![Trading Assets and Liabilities](../images/posts/Trading Assets and Liabilities.PNG)

## Securities Portfolios

Note: Chart measures debt and equity securities and excludes other types of trading assets such as whole loans and derivatives.
![Securities Portfolios](../images/posts/Securities Portfolios.PNG)

• HTM category has been growing since the GFC. 

• Steady increases in debt and equity securities held for trading purposes in the period after the repeal of the Glass-Steagall Act in 1999 (this act had largely separated investment banking and commercial banking up to that point).  During the GFC, there was a sharp decline which would have been larger if not for the conversion of two large trading firms, Goldman Sachs and Morgan Stanley, to bank holding companies in September 2008.

As [this post](https://libertystreeteconomics.newyorkfed.org/2015/02/available-for-sale-understanding-bank-securities-portfolios/) describes, the largest category of securities for both portfolio types is **agency pass-through MBS**.   These are pools of securitized mortgages with a credit guarantee from Fannie Mae, Freddie Mac, or Ginnie Mae.    Closely related, and also significant in size, are agency collateralized mortgage obligations (CMOs), which are structured securities created from agency mortgage pools.
 
Banks engage in “**swap transactions**” with the government-sponsored enterprises (GSEs) Fannie Mae and Freddie Mac to swap a pool of conforming mortgages for an MBS pool backed by the same pool of loans but that carries a credit guarantee from the GSE.   As a result, the bank is insulated against credit risk but still retains the interest rate and prepayment risk . This type of **loan-for-security swap** is attractive from the perspective of **improving regulatory capital adequacy**, since agency MBS carry lower risk weights for regulatory capital purposes than do the underlying mortgages.   Furthermore, agency MBS also have relatively little liquidity risk, since their secondary market is large and liquid compared to most loan or fixed-income markets.

### AFS
The **U.S. Treasury Securities category** within AFS has been growing since the GFC, whereas the **U.S. Government Agency Obligations** category has been dropping during the same period of time. 

When combined with the **U.S. State and Municipal Debt** category, the three together went from slighly below **5% of total assets** to slightly above 5%.  As a group they are very steady. 

**AFS as a whole decreased** the most (slope the steepest) after 2003 until the GFC.   Was it **due to rising rates** of that period?  

We expect to see reduced AFS in 2022 as the Fed has been increasing rates.  Indeed, even with 1 quarter of the data in 2022, we see that AFS has dropped. 

![AFS](../images/posts/AFS.PNG)

# 2. Earnings and PPNR

From earnings perspectively, it seems that smaller banks have better numbers especially in more recent years. Is it because smaller banks are exempt from the heavy burdens of regulations?  CCAR, DFAST, risk capital rules and stringent accounting treatments specifically targeting large banks.  These not only add significantly to the expenses of the large banks but also impact ways they do business. 

Note that PPNR is the sum of two types of net income: Net Interest Income + Net Non-Interest Income. 
**Pre-Provision Net Revenue = Net Interest Income + Non-Interest Income - Non-Interest Expenses**. 

## Return on Assets and Equity
A closer look shows that the smaller banks (Banks and BHCs <$50bn) outperform the largest banks after **2012, when the regulators introduced many regulations targeting the largest banks**.   Sadly, the mid-range banks (BHCs $50bn-750bn) have had the worst luck.  They have the lowest return on equity.  They are just about as regulated as the largest banks but may not have the scale to support the functions to meet the regulatory demands. 

• Statistics exclude financial firms that are not either commercial banks or part of a
commercial bank holding company or intermediate holding companies (IHCs). This creates discontinuities in the
time-series graphs when nonbanking firms entered or exit the industry due to acquired or sold by banks or BHCs, or when firms switch to or from a bank or BHC charter. 
For example, in **2009:Q1, Goldman Sachs, Morgan Stanley, Ally Financial, and American Express each began filing a FR Y-9C** due to the conversion of each of these firms to a **commercial banking holding company charter**. This largely accounts for
the **sharp *13%* increase in total measured industry assets in 2009:Q1**, and a corresponding discontinuous upward shift in the industry asset growth rate during 2009. 

Similarly, in **2016:Q3 (Credit Suisse Holdings, Deutsche Bank USA, UBS Americas, and Barclays US) and other firms consolidate nonbanking assets under their designated IHC over the course of 2016**. This causes industry assets to rise by approximately 4% in 2016:Q3, and
has smaller effects on industry assets in earlier quarters.

• Only 4 of the 6 BHCs in the BHCs > $750bn group exist in the data for the entire sample period from 1991:Q1 onwards: **JPMorgan Chase, Bank of America, Wells Fargo, and Citigroup**. Goldman Sachs and Morgan Stanley enter the sample in 2009:Q1.

Note: Chart measures debt and equity securities portfolios. Thus, trading portfolio excludes other types of
trading assets such as whole loans and derivatives.

![return on assets](../images/posts/return on assets.PNG)

![return on equity](../images/posts/return on equity.PNG)

## Net Interest Margin and Noninterest Income Ratio

![Net Interest Margin](../images/posts/Net Interest Margin.PNG)
![Noninterest Income Ratio](../images/posts/Noninterest Income Ratio.PNG)

Net operating revenue is defined as net interest income plus noninterest income.
![Noninterest Income Share](../images/posts/Noninterest Income Share.PNG)

# 3. Loan Performance

Note: Non-performing loans include loans that are 
(1) 90 days or more past due and still accruing,or 
(2) non-accrual. 

**The CECL factor**: The adoption of the Financial Accounting Standards Board (FASB)’s new “current expected
credit losses” (CECL) methodology for estimating allowances for credit losses may have influenced the
calculation of loan loss provisions and loan loss reserves. 

**The CARES Act Factor**: Section 4013 of the *Coronavirus Aid, Relief, and Economic Security (CARES) Act* and the Interagency Statements on Loan Modifications issued on March 22 and April 7, 2020.

**Troubled Debt Restructurings and Vintage Disclosures**:  ASU No. 2022-02, “Financial Instruments - Credit
Losses (Topic 326): Troubled Debt Restructurings and Vintage Disclosures”, issued by FASB in March 2022, may have impacted the calculation of loan loss provisions, loan loss reserves, non-performing loans and net charge-offs. 

# Reference

[Quarterly Trends for Consolidated U.S. Banking Organizations
First Quarter 2022
Federal Reserve Bank of New York](https://www.newyorkfed.org/medialibrary/media/research/banking_research/quarterlytrends2022q1.pdf?la=en)

[Available for Sale: Understanding Nank Securities Portfolios](https://libertystreeteconomics.newyorkfed.org/2015/02/available-for-sale-understanding-bank-securities-portfolios/)