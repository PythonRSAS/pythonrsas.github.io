---
layout: post
tag : Learning Python and SAS
category: "python for sas"
title: "Xi Correlation in Python"
description: Chatterjee's Xi correlation in Python
author: Sarah Chen
image: images/posts/photos/IMG-0683.JPG

---

We want to know relationships between two things. By "things" we mean numerical variables.  Pearson, Spearman, Kendall are commonly used correlation measures.  Gini, and Gini variations also studying the relationship between 2 things.  

The "Xi" correlation is a candidate for detecting whether one thing is a function of the other, i.e. whether one is dependent on the other.  It does the job especially well when the function is not monotonic, such as a sine or cosine. 

The "Xi" correlation is actually very simple. In my view, is a variation of the Gini score, where one thing is used for ranking and the other thing is used for sorting. 


<div class="code-head"><span>code</span>xicor_implmented.py</div>

```py
def corrs(x,y, title):
    """
    input: 2 numpy arrays
    computes pearson, spearman,kendall, and xicor correlations
    implements the xicor correlation
    plot a scatterplot between x and y, and plot a barplot comparing the correlations
    returns a pandas series with the scores and function used between y and x
    """
    d = pd.DataFrame({'x':x,'y':y})
    d['y_rank'] = d.y.rank()
    d.sort_values(by='x',inplace=True)
    pearson = d[['x','y']].corr().iloc[1,0]
    spearman = d[['x','y']].corr(method='spearman').iloc[1,0]
    kendall = d[['x','y']].corr(method='kendall').iloc[1,0]
    xicor = 1-3*np.sum(np.abs(d.y_rank.diff()))/(d.shape[0]**2-1) #xicorr
    corrs = pd.Series([pearson,spearman,kendall,xicor], index=corr_lt)
    fig, ax = plt.subplots(1,2, figsize=(8,4))
    d[['x','y']].plot.scatter(x='x',y='y', ax=ax[0])
    corrs.plot(kind='bar',rot=0, ax=ax[1])
    for p in ax[1].patches:
        ax[1].annotate("{:.2f}".format(p.get_height()), (p.get_x()*1.005, p.get_height()*1.005))
    plt.suptitle(title)
    save_fig(title)
    plt.show()
    corrs['function'] = title
    return corrs
```

The following illustrates the comparisons of 4 correlations amongst various functions, where <span class="coding">x</span> is uniformly distributed random variables from 0 to 1. 

<div class="code-head"><span>code</span>correlations for straight lines.py</div>

```python
np.random.seed(1234) # use seed for replicable 

N=100 #small number for faster run
corr_lt = ['pearson','spearman','kendall','xicor']
x=2*np.random.uniform(size=N)-1
noise = np.random.normal(0,0.1,N)

y=x+noise
title="Positive Slope"
corrs0= corrs(x,y,title)

# x=2*np.random.uniform(size=N)-1
y=1- x+noise
title="Negative Slope"
corrs1 = corrs(x,y,title)
```
![positive slope](\images\_post\positive slope.png)
![negative slope](\images\_post\positive slope.png)

<div class="code-head"><span>code</span>correlations for non-straight-lines.py</div> 

```python
title="Quadratic Parabola"
# x=2*np.random.uniform(size=N)-1
y=x**2+noise
corrs2 = corrs(x,y,title)
# print("{:.2f}".format(3.1415926));

title="Sine"
# x=2*np.random.uniform(size=N)-1
y=np.sin(x*np.pi*2)+noise
corrs3 = corrs(x,y,title)

title="Cosine"
# x=2*np.random.uniform(size=N)-1
y=np.cos(x*np.pi*2)+noise
corrs4 = corrs(x,y,title)

title="Exponential"
# x=2*np.random.uniform(size=N)-1
y=np.exp(5*x)+noise
corrs5 = corrs(x,y,title)

title="Cubic Parabola"
# x=2*np.random.uniform(size=N)-1
y=x**3 +noise
corrs6 = corrs(x,y,title)

title="Cubic Root"
# x=2*np.random.uniform(size=N)-1
y=x**(1/3) +np.random.normal(0,0.1,N)
corrs7 = corrs(x,y,title)

title="Noise"
# x=2*np.random.uniform(size=N)-1
y=np.random.normal(0,0.1,N)
corrs8 = corrs(x,y,title)

summary = pd.concat([corrs1, corrs2, corrs3, corrs4, corrs5, corrs6,corrs7, corrs8], axis=1).T
#   pearson spearman kendall  xicor            function
# 0  -0.981   -0.981  -0.882  0.806      Negative Slope
# 1  -0.037    0.057   0.064   0.59  Quadratic Parabola
# 2  -0.337   -0.267  -0.169  0.767                Sine
# 3  -0.087    -0.11  -0.083   0.78              Cosine
# 4   0.676    0.986    0.93  0.874         Exponential
# 5   0.892    0.861   0.709  0.588      Cubic Parabola
# 6   0.884    0.918   0.762  0.892          Cubic Root
# 7  -0.003      0.0  -0.001 -0.054               Noise

#   pearson spearman kendall  xicor            function
# 0  -0.981   -0.981  -0.882  0.806      Negative Slope
# 1  -0.037    0.057   0.064   0.59  Quadratic Parabola
# 2  -0.337   -0.267  -0.169  0.767                Sine
# 3  -0.087    -0.11  -0.083   0.78              Cosine
# 4   0.676    0.986    0.93  0.874         Exponential
# 5   0.892    0.861   0.709  0.588      Cubic Parabola
# 6   0.884    0.918   0.762  0.892          Cubic Root
# 7  -0.003      0.0  -0.001 -0.054               Noise

```
