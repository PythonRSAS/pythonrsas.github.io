---
layout: post
tag: The art of Learning
category: education
title: "Learn recursion"
description: getting the simplest things right
author: Sarah Chen
image: images/posts/photos/IMG-0632.JPG
---
<figure> 
   <img src="{{"/images/posts/photos/IMG-0632.JPG"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 


# What is recursion

> Recursion is like brocolli (or cauliflower). 

Recursion is a function that is defined with itself.  What does that supposed to mean?  

The simplest example is the natural number sequence $$1, 2, 3, 4, 5, 6, ...$$
  

|  n   |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |
|:-----|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| f(n) |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |


<div class="code-head"><span>code</span>natural number.py</div>

```py
def f(n):
   if n == 0:
      return 1
   else:
      return f(n-1) + 1

for i in range(10):
   print(f(i))
``` 


|   n |   f(n) |
|----:|-------:|
|   0 |      0 |
|   1 |      1 |
|   2 |      2 |
|   3 |      3 |
|   4 |      4 |
|   5 |      5 |
|   6 |      6 |
|   7 |      7 |
|   8 |      8 |
|   9 |      9 |




|        |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |
|:-------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| fib(n) |   1 |   1 |   2 |   3 |   5 |   8 |  13 |  21 |  34 |  55 |


<div class="code-head"><span>code</span>fibonacci number.py</div>

```py
def fib(n):
   if (n== 0)|(n==1):
      return 1
   else:
      return fib(n -1) + fib(n-2)
for i in range(10):
   print(fib(i))


lt = []
for i in range(10):
   print(fib(i))
   lt.append(fib(i))
df = pd.DataFrame({'fib(n)':lt})
print(df.T.to_markdown())
``` 