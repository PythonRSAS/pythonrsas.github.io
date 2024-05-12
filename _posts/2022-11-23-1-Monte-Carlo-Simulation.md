---
layout: post
tag: Monte Carlo simulation
category: "other risks"
title: "Monte Carlo simulation"
description: Monte Carlo simulation for risk management
author: Sarah Chen
image: images/posts/balance_sheet_composition.PNG
---

- [Why Monte Carlo simulation](#why-monte-carlo-simulation)
- [Deterministic approach](#deterministic-approach)
- [Non-deterministic approach](#non-deterministic-approach)
- [Monte Carlo simulation](#monte-carlo-simulation)

# Why Monte Carlo simulation

Suppose we have an investment fund currently valued at $1,000,000, 100% invested in the S&P 500 ETF. 

We plan to take out the money in 30 years.  How much do we expect to have in the account at that time?

# Deterministic approach

The deterministc approach is the simplest (also unrealistic).  We assume an annual rate of return of 8% for the next 30 years. 

<div class="code-head"><span>code</span>deterministic_value.py</div>

```py
pv = 1000000
i = 0.08
time_horizon = 30
balance_t = 0
print("{:10s} {:15s} ".format("Year", "Ending Balance"))
print("-"*25)
for yr in range(1, time_horizon + 1):
    balance_t = pv * (1 + i)
    print("{:<10d} {:15,.0f}".format(yr, balance_t))
    pv = balance_t

```


# Non-deterministic approach

Can we rely on the fixed paramters?  It seems unrealistic to assume 8% fixed annual return.  We need to incorporate changes. 


<div class="code-head"><span>code</span>non_deterministic_value.py</div>

```py
import numpy.random as npr
stdev = 0.15
pv = 1000000
i = 0.08
time_horizon = 30
# balance_t
print("{:10s} {:15s} ".format("Year", "Ending Balance"))
print("-"*25)
for yr in range(1, time_horizon + 1):
    yr_return = npr.normal(i, stdev)
    balance_t = pv * (1 + yr_return)
    print("{:<10d} {:15,.0f}".format(yr, balance_t))
    pv = balance_t
```

We can run the above simulation many times (e.g. 100000 times) to get an idea of the possibilities. 

# Monte Carlo simulation

> <BR>
> $1,000,000 starter fund <BR>
> 8% average annual return <BR>
> 15% volatility <BR>
> 30 year time horizon <BR>
> <BR>

We run the simulation 100,000 times. 

We create a 2-dimensional array <span class="coding">np.zeros((iterations, time_horizon))</span>  to store the results. 
<div class="code-head"><span>code</span>monte_carlo_simulation.py</div>

```py
import numpy as np
import numpy.random as npr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
stdev = 0.15
pv = 1000000
i = 0.08
time_horizon = 30
iterations = 100000
returns_array = np.zeros((iterations, time_horizon))
for iteration in range(iterations):
    for yr in range(0, time_horizon ):
        returns_array[iteration][yr] = npr.normal(i, stdev)


print("{:10s} {:15s} ".format("Year", "Ending Balance"))
print("-"*25)
for yr in range(1, time_horizon + 1):
    yr_return = npr.normal(i, stdev)
    balance_t = pv * (1 + yr_return)
    print("{:<10d} {:15,.0f}".format(yr, balance_t))
    pv = balance_t
```

