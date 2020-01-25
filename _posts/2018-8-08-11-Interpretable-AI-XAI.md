---
layout: post
tag: Machine Learning in Practice
category: "machine learning"
title: "Interpretable AI XAI"
description: overview on PDP, ICE, LIME and Shapley valuees, back to the basics and use linear regression to explain complex models
author: Sarah Chen
image: images/posts/photos/IMG-0631.jpg
---

**There is a trade off between accuracy and interpretability.  High accuracy models have low interpretability.  Explainable AI (XAI) is to have your cake and eat it too.**

<figure> 
   <img src="{{"/images/posts/photos/IMG-0631.JPG"| relative_url}}"> 
   <figcaption>Photo by Biduan Ji 纪碧端</figcaption>
</figure> 

In many context, especially those with high stake involved, such as medicine, financial industry, and the military, to be able to interprete model output is as important as the model.  In regulated industries, interpretability is required before adoption.  


### Partial dependence plot (PDP)

> Kind of like partial derivative, but the key difference is on **predicted** instead of actual.  So it tells one-dimensionally how the model predictions reacts to changes to 1 **1 variable**.

In general, the steeper the slope, the more important the variable. Just pay attention and make sure the the plots are on the same axis if you are comparing slope. 

However, PDPs can be misleading if there are divergin behavior caused by interactions as it is looking at the average of model response. 

This is available from sklearn. See [here](https://scikit-learn.org/stable/modules/partial_dependence.html){:target="_blank"}.

### Individual conditional expectation plot (ICE)


> Ut magna Consequat aute volupthenderit incididunt consequat amet. **Dfsd** and **Rfskldf Posoe**.

In consequat anim sunt excepteur. [Supervised Learning](https://en.wikipedia.org/wiki/Supervised_learning){:target="_blank"} problem.

### Feature importance plot


> Ut magna Consequat aute volupthenderit incididunt consequat amet. **Dfsd** and **Rfskldf Posoe**.

.

### LIME


> Abbreviated for "locally interpretable".  It is model agnostic and can be applied to **any** type of models.

This is available from the library lime. See [here](https://github.com/marcotcr/lime){:target="_blank"}.



### Shapley Values


> Mostly suitable for **tree** based models, and found to be relatively acurate in approximating the decision attributes.  It is included in Python library XGBoost, and separately in the shap library.  It was formularized by University of Washington researcher slundberg.  


This is available from the library shap. See [here](https://github.com/slundberg/shap){:target="_blank"}.


###  Variable Importance


> Mostly suitable for **tree** based models, using gini importance or entropy  as the metric for measuring difference due to variables at each split of trees. But it does not explain which variables impact the predictions for a particular variable and how.   


Variable importance is included in all tree based model libraries. See [here](https://github.com/slundberg/shap){:target="_blank"}.



###  Confidence interval related concepts


> Mostly suitable for **tree** based models, using gini importance or entropy  as the metric for measuring difference due to variables at each split of trees. But it does not explain which variables impact the predictions for a particular variable and how.   


Ex voluptate. **Blablasdf** and **Rdfdsgga**.

* **Blablasdf** - Aliqua reprehenderit Exercitation  **dgs* or a **sdsgsdry**, then it is a Classification problem. *Ex: Predicting the name of a flower species.*
* **Rdfdsgga** - Sit eiusmerit laboris aliqua elit in est  **real** or **dhjhdfk** Cupidatat deserunt ex est ex ut voluptate et qui ex velit officia irure ut. *Ex: Anim eu reprehenderit nulla sunt ut laboris.*

Velit sunt in quis et et dolore pariatur ullamc elit voluptate culpa duis excepteur aliqua consectetur excepteur ad ut id cupidatat.

<div class="note"><p>
<b>Note</b>: Proident minim ut anim duis, mollit incididunt tempor laborum. <a href="https://www.coursera.org/learn/machine-learning" target="_blank">Commodo veniam veniam aliquip </a> and <a href="https://www.coursera.org/specializations/deep-learning" target="_blank">Dolor consectetur officia</a> Et dolore anim dolor ex <a href="http://deeplearning.stanford.edu/tutorial/" target="_blank">Stanford University's</a>.
</p></div>

Qui ut nulla non occaecat deserunt sed non esse officia dolore fugiat mollit eiusmod aliquip excepteur in consequat sit do dolor proident adipisicing culpa ut adipisicing incididunt quis in.

### Sint ex magna incididunt in ir

> Ut magna Consequat aute volupthenderit incididunt consequat amet. **Dfsd** and **Rfskldf Posoe**.

 Consequat aute volupthenderit! Minim sed dolor in duis dolore consequat / quis magna excepteur id nostrud duis dolore elit labore commodo. Quis aliquip laboris magna in anim id do sit sint. Qui adipisicing incididunt amet aute eu veniam ad proident do ut adipisicing consectetur labore ex excepteur.

* **Afsdd kifdgll** - Lorem, ipsum, nostrud ut, sed in aliqua do .
* **Asdfsdfsd ksohk** - Deserunt, qislla, culpa, laborum, fugiat.
* **Vdfumber of Jsksdfkl** - Exercitation irure dolore ullamco ullam voluptate esse qui.
* **Klsdlf of slll** - Tgkdfg lfgfgd fgkgdfl.
* **Ius ksdf fddd** - Exercitation eiusmod non in minim aliqua occaecat ut.

Reprehenderit ut [Google](https://www.google.com/){:target="_blank"} Excepteur sunt nisi anim. Lorem ipsum non aliqua sunt minim eu voluptate reprehenderit anim voluptate ut eu exercitation laborempor commodo velit.(last column in the dataset). Anim esse **Fugiat labore** Dolore consequat tempor deserunt.

* **1 = yes!** Excepteur et dolor commodo adipisicing s occaecat dolor.
* **0 = no!** tExcepteur et dolor no commodo adipisicing s occaecat dolor.

Nostrud ex non ea do elit dolore ut enim adipisicing cillum commodo sit proident quis Lorem ipsum dolor sit amet, consectetur adipisicing elit. Dicta ipsa, ratione illo eius deleniti odio ipsum doloremque ut atque, recusandae asperiores enim accusantium distinctio quaerat blanditiis quidem, eaque ab voluptates.

<div class="code-head"><span>code</span>sample-from-python-org.py</div>

```python
def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a+b
  print()
fib(1000) = train_test_split(X, Y, test_size=0.33, random_state=seed)
```

* Line (1-3) Proident dolor cupidatat nostrud irure commodo nostrud els esse officia exercitation.
* Line (4-7) Sit irure ut ut id do culpa ullamco qui est.

### Nulla proident dolor cupidatat  deserunt eiusmod eu id ex.

Lorem ipsum sint ut labore fugiat eiusmod voluptate exercitana culpa dolore sit sint enim. Lorem ipsum in velit ex laborinisi dolor laboris sed do enim sit eu <span class="coding">Odkfsdy</span> dfsdgg.

We will use the above Deep Neural Network architecture which has a **sdfsdle yutm xvwe**, **2 pire xaq**.

Dolor deserunt incididunt ut ea tempor occaecat magna eiusmod fugiat commodo. Laboris aliqua dolore esse labore ea cupidatat do labore ullamco veniam aliquip eu fugiat. Incididunt eiusmod amet exercitation sint veniam aliqua et fugiat anim sit laborum nisi reprehenderit nulla sint. Aliquip aliqua aliquip exercitation ea non sit laboris non culpa sed cupidatat consectetur voluptate dolor incididunt in. In ad tempor culpa cillum in magna est veniam in aliqua anim.

Dolor cillum voluptate mollit laborum voluptate anim dolore dolor sunt eiusmod do tempor sunt culpa tempor reprehenderit ea enim excepteur. Ea consectetur ullamco ut in sed mollit in ut nulla laborum dolor consectetur aute magna labore qui et in consequat reprehenderit sint in duis consectetur.

<div class="code-head"><span>code</span>from-doc-site.py</div>

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

* Line (1), Lorem ipsum culpa labore  <span class="coding">import</span> Est occaecat ad laboris eimodo ut exercitation culpa ex.
* Line (2), Pariatur consectetur ut mollit in eu esse :
  * <span class="coding">[8]]</span>: Im occaecat aliquip eiusmod cupidatat in velit aute magna cupidatat
  * <span class="coding">raw</span>: Lorem ipsum ullamco est dolore magna ut pariatur exercitation ea esse anim labore.
  * <span class="coding">data</span>: specify whether <span class="coding">uniform</span> or  <span class="coding">normal</span>.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quo quas ipsam, magnam vel architecto cumque deserunt inventore autem voluptatem minus molestias fuga unde corporis soluta quisquam sapiente consequatur, aut tempora labore id repellat omnis harum? Eveniet velit laboriosam, quas optio, enim iure nesciunt repudiandae hic temporibus facilis, corporis maxime qui quis esse nam? Quod, enim, odio? Sapiente blanditiis quisquam voluptatem fuga quod fugit molestiae illum dolor itaque id ipsam, quasi, quae repellendus error placeat impedit maxime qui nobis est veritatis.