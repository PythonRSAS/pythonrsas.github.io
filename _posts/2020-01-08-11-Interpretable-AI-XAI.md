---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Interpretable AI XAI"
description: There is a trade off between accuracy and interpretability.  High accuracy models have low interpretability and potential problems.  Explainable AI (XAI) is to have your cake and eat it too.
author: Sarah Chen
image: images\posts\photos\IMG-0631.jpg
---

**There is a trade off between accuracy and interpretability.  High accuracy models have low interpretability and potential problems.  Explainable AI (XAI) is to have your cake and eat it too.**

<figure> 
   <img src="{{"/images/posts/photos/IMG-0631.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 

In linear regression, there has been well-established theory and diagnostics on how a model works, such as the model statement y = a + bX, confidence interval, p-value (assuming x is not relevant what's the chance of having this kind of relationship to y) and etc.  

In linear regression and situations where linear regression are used (in neural network as well) balance of bias and variance can be strived for by using regularizers to prevent overfitting and instability due to multicollinearity. 

So, yes, machine learning is powerful leveraging computing power and data. But then, why should anyone just accept black boxes and expect less from the ML/AI models?   

For low-consequence machine learning models or those that we find to be the best option such as those used in postal code sorting, image recognition, explanation is not necessary as long as we know that the algorithms are working as demonstrated--Blackboxes are fine. 

However, in many context, especially those with high stake especially involving people, such as health care/medicine, financial industry, and the military, to be able to interprete model output is as important as the model.  

In regulated industries, interpretability is required before adoption.  

A genearal introduction from theoretical point of view on definitions of interpretability is in [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/pdf/1702.08608.pdf){:target="_blank"}.

Interpretable AI (XAI) has been a very active area in recent years, motivated by commercial reasons (to gain from the available technology) and regulatory needs. 

There are two categories of tools in both the old and latest machine learning interpretability methods and models:

* **tools for helping us to understand ML/AI models** where Linear regression is leveraged either in representation or used locally. 
* **monotonicity as regularizers** to ensure interpretability built into the models.  

Here is a quick summary of some of the old and new XAI methods and algorithms: 


###  Variable Importance and Plot


> Mostly suitable for **tree** based models, using gini importance or entropy  as the metric for measuring difference due to variables at each split of trees. But it does not explain which variables impact the predictions for a particular variable and how. 

<div class="code-head"><span>code</span>feature-importance.py</div>

```python
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
 
forest = ExtraTreesClassifier(n_estimators=250,
                              random_state=0)

forest.fit(X, y)
importances = forest.feature_importances_
feature_names = [i.split(' (', 1)[0] for i in iris.feature_names]

stdev = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)

importances_df= pd.DataFrame(zip(importances, stdev), columns=['importance','stdev'], index=feature_names)
importances_df.sort_values(by='importance',ascending=False, inplace=True)
# Print the feature ranking
print("Feature ranking:")
print(importances_df)

# Plot the feature importances of the forest
plt.figure()
plt.title("Feature importances")
plt.bar(range(X.shape[1]), importances_df.importance,
       color="g", yerr=importances_df.stdev, align="center")
plt.xticks(range(X.shape[1]), importances_df.index)
plt.xlim([-1, X.shape[1]])
plt.tight_layout()
plt.show()
```

<figure>
  <img src="{{ "/images/posts/Feature importances with error.png" | relative_url }}">
  <figcaption>Feature Importances with Stdev</figcaption>
</figure>

A side note: [A Comparison of R, SAS, and Python Implementations of Random Forests](https://digitalcommons.usu.edu/cgi/viewcontent.cgi?article=2295&=&context=gradreports&=&sei-redir=1&referer=https%253A%252F%252Fwww.bing.com%252Fsearch%253Fq%253Dvariable%252520importance%252520random%252520forest%252520R%252520python%252520sas%2526qs%253Dn%2526form%253DQBRE%2526sp%253D-1%2526pq%253Dvariable%252520importance%252520random%252520forest%252520r%252520python%252520sas%2526sc%253D0-46%2526sk%253D%2526cvid%253D333C6D25045444419A8E386D9BCA7771#search=%22variable%20importance%20random%20forest%20R%20python%20sas%22){:target="_blank"} documented comparisons on different variable importance implementation amongst Python R SAS.   


### [Tree Interpreter](https://github.com/andosa/treeinterpreter){:target="_blank"}

Tree Interpreter (formulated by Andos Saabas) is a ingenius method to represent how trees in linear regression formats.  

Since a forest is nothing but a collection of trees (average of the scores from trees), if we can explain a tree, we can explain a forest. 

Since a tree is nothing but the growth from root to leaves, if we can explain each split/step, we can explain a tree. 

In this formulation, bias corresponds to the intercept in linear regression while "contribution" of a variable is somewhat similar to beta*x.  

It is intuitive and beautiful.  One 'limitation' is that for joint contributions cases such as XOR you will need to explicitly test the joint contribution.

<div class="code-head"><span>code</span>tree-interpreter-example.py</div>

```python
from sklearn.ensemble import RandomForestClassifier
from treeinterpreter import treeinterpreter as ti
import numpy as np

from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target

rf = RandomForestClassifier(max_depth = 4)
idx = np.arange(len(iris.target))
np.random.shuffle(idx) #inplace
 
rf.fit(iris.data[idx][:100], iris.target[idx][:100])
# predict for a single instance.
instance = iris.data[idx][100:101]
print (rf.predict_proba(instance))

# Breakdown of feature contributions:
prediction, bias, contributions = ti.predict(rf, instance)
print( "Prediction", prediction)
print( "Bias (trainset prior)", bias)
print( "Feature contributions:")
for c, feature in zip(contributions[0], 
                             iris.feature_names):
    print( feature, c)
```


### Partial dependence plot (PDP)

> Kind of like partial derivative, but the key difference is on **predicted** instead of actual.  So it tells one-dimensionally how the model predictions reacts to changes to 1 **1 variable**.

In general, the steeper the slope, the more important the variable. Just pay attention and make sure the the plots are on the same axis if you are comparing slope. 

However, PDPs can be misleading if there are divergin behavior caused by interactions as it is looking at the average of model response. 

This is available from sklearn. See [here](https://scikit-learn.org/stable/modules/partial_dependence.html){:target="_blank"}.

### Individual conditional expectation plot (ICE)




### LIME

> Abbreviated for "Local Interpretable Model-Agnostic Explanations".  It is model agnostic and can be applied to any type of models.

It was formulated first by Marco Tulio Ribeiro and others in 2016.  

This is available from the library lime. See [here](https://github.com/marcotcr/lime){:target="_blank"}.



### Shapley Values


> Mostly suitable for **tree** based models, and found to be relatively acurate in approximating the decision attributes.  

It is included in Python library XGBoost, and separately in the shap library.  It was formularized by University of Washington researcher Scott Lundberg (currently senior researcher at Microsoft).                                                                                                                                       

This is available from the library shap. See [here](https://github.com/slundberg/shap){:target="_blank"}.


<div class="code-head"><span>code</span>get-started-shap.py</div>

```python
import xgboost
import shap

# load JS visualization code to notebook
shap.initjs()

# train XGBoost model
X,y = shap.datasets.boston()
model = xgboost.train({"learning_rate": 0.01}, xgboost.DMatrix(X, label=y), 100)

# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn and spark models)
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# visualize the first prediction's explanation (use matplotlib=True to avoid Javascript)
shap.force_plot(explainer.expected_value, shap_values[0,:], X.iloc[0,:])
```



###  TensorFlow Lattice


> Essentially interpolated look-up tables, TensorFlow Lattice is a library that implements constrained and interpretable lattice based models. It is an implementation of Monotonic Calibrated Interpolated Look-Up Tables in TensorFlow.

The library enables you to inject domain knowledge into the learning process through common-sense or policy-driven shape constraints. 


For an overview, see Google scientist Maya Gupta's TensorFlow Dev Summit 2019 video [TF Lattice: Control Your ML with Monotonicity](https://www.youtube.com/watch?v=ABBnNjbjv2Q&t=140s){:target="_blank"}.

Here are a few screenshots from the video. 

<figure>
  <img src="{{ "/images/posts/TF_lattice1.JPG" | relative_url }}">
  <figcaption>TF_lattice1</figcaption>
</figure>


Tree-based machine learning models and neural networks can have high accuarcy, but can be prone to fitting into random noises in the data (even with cross validation), which do not make sense, and can possibly be unethical. 

Often, how we combat "overfitting" related problems is by regularization.  

But any regularization technique will hurt the model accuracy and cannot guarantee solving the problem.  

TF Lattice hits the problem exactly by using monotonicity as the **regularizer**. 

1-d lattice is just a piecewise linear function. 

<figure>
  <img src="{{ "/images/posts/TF_lattice2.JPG" | relative_url }}">
  <figcaption>TF_lattice2</figcaption>
</figure>


Multidimensional lattice are trained using empirical risk minimization, the same as you see with DNN.

<figure>
  <img src="{{ "/images/posts/TF_lattice3.JPG" | relative_url }}">
  <figcaption>TF_lattice3</figcaption>
</figure>


<figure>
  <img src="{{ "/images/posts/TF_lattice4.JPG" | relative_url }}">
  <figcaption>TF_lattice4</figcaption>
</figure>

Recommended resources:
* **[github](https://github.com/tensorflow/lattice){:target="_blank"}**
* **[Deep Latice Networks. You et al. NIPS 2017](https://arxiv.org/abs/1709.06680){:target="_blank"}**



###  Confidence intervals


> Don't forget **resampling** techniques that make ensemble models so successful can be used to compile confidence intervals, and generate similar concepts like p-values.  