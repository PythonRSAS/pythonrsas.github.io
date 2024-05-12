---
layout: post
tag: trading
category: "market risk"
title: "Statistics Used In Stock Trading"
description: Statistics Used In Stock Trading
author: Sarah Chen
image: images/posts/photos/sf/IMG-0919.JPG
---

- [Metrics](#metrics)
- [Beta](#beta)
- [Getting Metrics](#getting-metrics)

There are hundreds if not thousands of ratios and metrics used in stock trading.  All metrics and ratios have their limitations and should be used with other metrics and qualitative analysis.  The limitations include (not comprehensive):

- metrics and ratios are based on historical data
  - historical data may not be relevant for the future
  - even if historical data is relevant, they may not be accurate or true (so we have to use them with a grain of salt)
- metrics do not include important qualitative information 

Additionally, the accuracy of the metrics depends on the reliability of estimates and assumptions used in calculation.

# Metrics

1. **short ratio:**
The short ratio, in finance, refers to the ratio of shares sold short to the total number of outstanding shares. It's a measure used by investors to gauge market sentiment, specifically to determine the level of bearishness or pessimism surrounding a particular stock.

The formula for calculating the short ratio is:

\[
\text{Short Ratio} = \frac{\text{Shares Sold Short}}{\text{Average Daily Trading Volume}}
\]

Where:
- "Shares Sold Short" represents the total number of shares that have been sold short by investors.
- "Average Daily Trading Volume" is the average volume of shares traded in the market each day over a certain period of time.

A high short ratio implies that a large proportion of investors are bearish on the stock, anticipating its price to decline. Conversely, a low short ratio suggests bullish sentiment, with fewer investors betting on the stock's decline.

Investors often use the short ratio as one of the indicators to assess market sentiment and potential future movements in stock prices. However, it's important to consider other factors and indicators in conjunction with the short ratio for a more comprehensive analysis.

A short ratio larger than 1 indicates that there are more shares sold short in the market than the average daily trading volume. Here's what it implies:

- **Bearish Sentiment**: A short ratio greater than 1 suggests a prevailing bearish sentiment towards the stock. This means that there are more investors betting on the stock's price to decline rather than rise.

- **Potential for Short Squeeze**: A high short ratio can sometimes lead to a short squeeze. If the stock's price starts to rise unexpectedly, short sellers may rush to cover their positions by buying back shares, which can further drive up the stock's price due to increased demand.

- **Market Attention**: A short ratio larger than 1 can also indicate that the stock has garnered significant attention from short sellers and investors. It may suggest that there are perceived weaknesses or concerns about the company's fundamentals, leading to a higher level of short interest.

- **Volatility**: Stocks with high short ratios tend to experience higher levels of volatility as short sellers and long investors engage in a tug-of-war over the stock's price direction.

Investors should interpret a short ratio larger than 1 cautiously and consider other factors such as company fundamentals, industry trends, and market sentiment before making investment decisions. While a high short ratio can signal potential risks, it can also present opportunities for contrarian investors or those seeking short-term trading strategies.


2. **PEG ratio:**
The PEG ratio, or Price/Earnings to Growth ratio, is a valuation metric used in finance to determine whether a stock is undervalued or overvalued based on both its earnings and its expected future growth rate. It is calculated as the ratio of a company's price-to-earnings (P/E) ratio to its earnings growth rate.

The formula for calculating the PEG ratio is:

\[
\text{PEG Ratio} = \frac{\text{Price-to-Earnings (P/E) Ratio}}{\text{Annual Earnings Growth Rate}}
\]

Where:
- "Price-to-Earnings (P/E) Ratio" is the ratio of a company's current share price to its earnings per share (EPS). It indicates how much investors are willing to pay per dollar of earnings.
- "Annual Earnings Growth Rate" is the rate at which a company's earnings are expected to grow annually over a certain period of time.

The PEG ratio helps investors understand whether a stock is overvalued or undervalued relative to its growth prospects. A PEG ratio of 1 is generally considered fair value, meaning the stock's price is in line with its expected earnings growth. A PEG ratio below 1 may indicate that the stock is undervalued, while a PEG ratio above 1 may suggest that it is overvalued.

A negative PEG ratio doesn't necessarily imply that a stock is undervalued or overvalued; it simply indicates that the relationship between the stock's price, its earnings, and its growth rate is negative. Investors need to interpret negative PEG ratios with caution and consider other factors such as the reasons behind the negative earnings or growth, the company's financial health, industry trends, and other valuation metrics before making investment decisions.

2. **Enterprise to Revenue ratio:**

The Enterprise to Revenue ratio, also known as the Enterprise Value to Revenue ratio (EV/Revenue), is a financial metric used to assess the valuation of a company relative to its revenue. It indicates how much investors are willing to pay for each unit of revenue generated by the company.

The formula to calculate the Enterprise to Revenue ratio is:

\[
\text{EV/Revenue} = \frac{\text{Enterprise Value}}{\text{Revenue}}
\]

Where:
- "Enterprise Value" (EV) represents the total value of a company, including its market capitalization, debt, and minority interest, minus its cash and cash equivalents. It is a measure of the company's total economic value.
- "Revenue" is the total income generated by the company from its primary business activities over a specific period, typically a fiscal year.

A low EV/Revenue ratio may indicate that the company is undervalued relative to its revenue, suggesting that investors are paying less for each unit of revenue generated. Conversely, a high EV/Revenue ratio may suggest that the company is overvalued compared to its revenue.

It's essential to consider other factors such as industry benchmarks, growth prospects, profitability, and future cash flow expectations when interpreting the Enterprise to Revenue ratio. Additionally, comparing the ratio with those of similar companies within the same industry can provide valuable insights into the company's valuation relative to its peers.


Metrics | Undervalued | Overvalued
---------|----------|---------
 short ratio | high when sentiment is bearish | low when sentiment is bullish
 PEG ratio | <1 | >1
 Enterprise to Revenue ratio | low | high


# Beta

Beta is a measure of a stock's volatility in relation to the overall market. It indicates how much a stock's price tends to move in relation to changes in the overall market, usually represented by a benchmark index such as the S&P 500. A beta greater than 1 indicates that the stock is more volatile than the market, while a beta less than 1 suggests that the stock is less volatile than the market.

The beta coefficient is just like the beta in OLS linear regression:

\[
\beta = \frac{{\text{Covariance}(r_{\text{stock}}, r_{\text{market}})}}{{\text{Variance}(r_{\text{market}})}}
\]

Where:
- \( r_{\text{stock}} \) is the return of the stock.
- \( r_{\text{market}} \) is the return of the market (usually represented by a benchmark index).
- Covariance(\( r_{\text{stock}} \), \( r_{\text{market}} \)) is the covariance between the stock's returns and the market returns.
- Variance(\( r_{\text{market}} \)) is the variance of the market returns.

In practice, beta is often estimated using historical price data. Here's a simplified approach to estimate beta:

1. Collect historical price data for the stock and the market index over a specified period.
2. Calculate the daily returns for both the stock and the market index.
3. Calculate the covariance between the stock returns and the market returns, as well as the variance of the market returns.
4. Use the formula above to compute the beta coefficient.

> Note: beta is a historical measure and may not necessarily predict future volatility accurately. Additionally, beta can vary depending on the time period and frequency of data used for calculation.

# Getting Metrics


<div class="code-head"><span>code</span>stock metrics from Yahoo Finance.py</div>

```py

import pandas as pd
from yahoofinancials import YahooFinancials
import os
os.chdir(r"C:\Users\sache\OneDrive\Documents\python_SAS\stock")
from datetime import datetime
TODAY = datetime.today().strftime("%Y%m%d")
print(TODAY)
# ************************** just 2 companies ********************************
TICKER = 'SHEL'
yfs = YahooFinancials(TICKER)
data1 = yfs.get_key_statistics_data()
financialName = []
financialValue = []
for key, values in data1[TICKER].items():
    financialName.append(key)
    financialValue.append(values)
df1 = pd.DataFrame({'%s'%TICKER: financialValue}, index=financialName)

df1.loc['dividend_yield'] = yfs.get_dividend_yield()
df1.loc['payout_ratio'] = yfs.get_payout_ratio()
df1.loc['pe_ratio'] = yfs.get_pe_ratio()
df1.loc['current_price'] = yfs.get_current_price()
df1.loc['calculated_PB_ratio'] = df1.loc['current_price'] *  df1.loc['sharesOutstanding'] / df1.loc['bookValue']
# yfs.get_esg_score_data() # This took forever!

TICKER = 'BP'
yfs = YahooFinancials(TICKER)
data2 = yfs.get_key_statistics_data()
financialName = []
financialValue = []
for key, values in data2[TICKER].items():
    financialName.append(key)
    financialValue.append(values)
df2 = pd.DataFrame({'%s'%TICKER: financialValue}, index=financialName)
df2.loc['dividend_yield'] = yfs.get_dividend_yield()
df2.loc['payout_ratio'] = yfs.get_payout_ratio()
df2.loc['pe_ratio'] = yfs.get_pe_ratio()
df2.loc['current_price'] = yfs.get_current_price()

result = df2.join(df1)
result.dropna(how='all',axis=0,inplace=True)
result.index.tolist()

drop_idx = ['maxAge',  'priceHint',
 'enterpriseValue', 
 'trailingEps',
 'forwardEps',
  'floatShares', # portion of outstanding shares available for trading in the open market
 'lastDividendDate',  'sharesShortPreviousMonthDate', 'lastDividendValue', 'lastSplitDate']


result.drop(drop_idx, inplace=True)

result.loc['dateShortInterest'] = pd.to_datetime(result.loc['dateShortInterest'], unit='s')
result.loc['lastFiscalYearEnd'] = pd.to_datetime(result.loc['lastFiscalYearEnd'], unit='s')
result.loc['nextFiscalYearEnd'] = pd.to_datetime(result.loc['nextFiscalYearEnd'], unit='s')
result.loc['mostRecentQuarter'] = pd.to_datetime(result.loc['mostRecentQuarter'], unit='s')

idx = result.index.tolist()
for x in idx:
    print("\n")
    print(result.loc[x,:])

result.to_excel("compare_BP_Shell_%s.xlsx"%TODAY)
```


