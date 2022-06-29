---
layout: post
tag: The art of Learning
category: education
title: "Learn recursion"
description: getting the simplest things right
author: Sarah Chen
image: https://en.wikipedia.org/wiki/Romanesco_broccoli#/media/File:Romanesco_broccoli_(3).jpg
# image: images/posts/photos/IMG-0632.JPG
---
<!-- <figure> 
   <img src="{{"/images/posts/photos/IMG-0632.JPG"| relative_url}}"> 
   <figcaption></figcaption>
</figure>  -->


# What is recursion

> Recursion is like brocolli (or cauliflower). 

![Romanesco_broccoli](https://i0.wp.com/growingwithplants.com/wp-content/uploads/2011/10/romanesco.jpg?w=640)

Recursion is a function that is defined with itself.  $$f(n) = \text{some combination of }f(n-1)$$.   What does that supposed to mean?  

![](https://en.wikipedia.org/wiki/Recursion#/media/File:Sierpinski_triangle.svg)

The simplest example I think is the natural number sequence $$1, 2, 3, 4, 5, 6, ...$$

## Natural number
The natural numbers can be expressed as:

$$f(n)=f(n-1)+1$$, with the initial condition that the first number is $$0$$ (when $$n=0$$).  
**The initial values must be given in order for the recursion to be fully defined**. 

|  n   |   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |
|:-----|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| f(n) |  **1** |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |  10 |

Now, we translate it to code. 

> if input is equal to initial value, then return the values for initial values
> else return the mathematical function

The initial value  for natural number is $$1$$, and the value it is associated with is also
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

## Fibonacci number
The Fibonacci numbers can be expressed as:

$$f(n)=f(n-1)+ f(n-2)$$, 
with the initial condition that the first and the second numbers $$1$$ and $$1$$ (when $$n=0$$ and $$n=1$$).  Again, **the initial values must be given in order for the recursion to be fully defined**. 


|        |   **0** |   **1** |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |
|:-------|----:|----:|----:|----:|----:|----:|----:|----:|----:|----:|
| fib(n) |   **1** |   **1** |   2 |   3 |   5 |   8 |  13 |  21 |  34 |  55 |


<div class="code-head"><span>code</span>fibonacci number.py</div>

```py
def fib(n):
   if (n== 0)|(n==1):
      return 1
   else:
      return fib(n -1) + fib(n-2)
for i in range(10):
   print(fib(i))

# lt = []
# for i in range(10):
#    print(fib(i))
#    lt.append(fib(i))
# df = pd.DataFrame({'fib(n)':lt})
# print(df.T.to_markdown())
``` 

# Recipe for recursion

After working out the two simple examples successfully, we can use the same thinking process to tackle bigger recursion problems.
1. Write down the mathematical formula of recursion
2. Specify initial values correctly
3. Code it accordingly

Our recipe creation process feels like some kind of recursion too: we came up with a process (or a pattern of a process) that works and generalize it to future ones.  