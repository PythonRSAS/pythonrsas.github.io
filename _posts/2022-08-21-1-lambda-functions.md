---
layout: post
tag : lambda function, list comprehension, functions
category: "Python for SAS"
title: "lambda functions"
description: lambda function and its different uses through examples
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [What is lambda function](#what-is-lambda-function)
- [What is lambda function in Python](#what-is-lambda-function-in-python)
  - [list of lambda functions and list comprehension](#list-of-lambda-functions-and-list-comprehension)
- [Use with 2 arguments in list comprehension](#use-with-2-arguments-in-list-comprehension)
  - [Higher order function](#higher-order-function)
  - [Loan balance amortization](#loan-balance-amortization)
- [Reference](#reference)


# What is lambda function 
I never heard of lambda function when working in SAS, for a good reason: lambda are nothing but functions.  However, there are often used in Python and some other languages such as Matlab, Java, and even Excel.  

A little bit of history and very high level:

Alanzo Church, an American mathematician, invented the lambda function to address the question "what is a function from the computational perspective?"  He saw them as pure mathematical functions: a function takes an input and gives an output. 

> "A function is a rule of correspondence by which when anything is given (as argument) another thing (the value of the function for that argument) may be obtained."

For example, from page 15 his 1941 paper ["THE CALCULI OF LAMBDA-CONVERSION" (PRINCETON UNIVERSITY PRESS, reprint 1965)](https://compcalc.github.io/public/church/church_calculi_1941.pdf)

"Example: the equation $$(x^2+x)^2=(y^2+y)^2$$ expresses a relation between the natural numbers denoted by $$x$$ and
$$y$$ and its truth depends on a detennination of $$x$$ and of $$y$$/ (in fact, it is true if and only if $$x$$ and $$y$$ are determined as denoting the same natural number); but the equation $$\lambdax(x^2+x)^2=\lambday(y^2+y)^2$$ expresses a particular proposition -- namely $$\lambdax(x^2+x)^2$$ is the same function as $$\lambday(y^2+y)^2$$ -- and it is true (there is no question of a determination of $$x$$ and $$y$$)."

"Notice also that $$\lambda$, or $$\lambdax$$, is not the name of any function or other abstract object, but is an incomplete symbol --i.e., the symbol has no meaning alone, but appropriately formed expressions containing the symbol have a meaning. We call the symbol $$\lambdax$$ an **abstraction operator**, and speak of the function
which is denoted by $$(\lambdaxM)$$ as obtained from the expression $$M$$ by **abstraction**. "

Alanzon Church was the advisor of Alan Turing.  Alan Turning invented Turing machine, which captures state-based computation.  

Functional and state-based computation are equivalent.  They are just different ways of looking at things. 

# What is lambda function in Python

From [Python documentation](https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements):
> [...] Unlike lambda forms in other languages, where they add functionality, Python lambdas are only **a shorthand notation if you’re too lazy to define a function**.

Functions are already first class objects in Python, and can be declared in a local scope. Therefore **the only advantage** of using a lambda instead of a locally defined function is that *you don’t need to invent a name for the function* – but that’s just a local variable to which the function object (which is exactly the same type of object that a lambda expression yields) is assigned!

So, lambda function in Python is nothing but a function without a name!  

## list of lambda functions and list comprehension

Since lambda function in Python is simply a lazy shorthand, let's look at it together with another lazy way of doing things: list comprehension. 

List of lambda functions is different from implementing a lambda function in a list comprehension.  We compare 2 expressions.  

The first one is a list of lambda functions generated by list comprehension. 

The second one is a single lambda function, defined prior to implementing in a list comprehension. 

```python
f = [lambda x: x*x for x in range(10)]
# [<function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>,
#  <function __main__.<listcomp>.<lambda>>]
f[0](4)
# 16
f[-1](4)
# 16
```
Similarly, the example in [Python FAQ Why do lambdas defined in a loop with different values all return the same result?](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result) creates 5 identical lambda functions that computes squares. 

This happens because *x is **not local to the lambdas***, but *is defined in the outer scope*, and it is accessed when the lambda is called — not when it is defined. At the end of the loop, the value of x is 4, so all the functions now return 4**2, i.e. 16. You can also verify this by changing the value of x and see how the results of the lambdas change:

```python
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda: x**2)
squares
# [<function __main__.<lambda>>,
#  <function __main__.<lambda>>,
#  <function __main__.<lambda>>,
#  <function __main__.<lambda>>,
#  <function __main__.<lambda>>]
squares[-1]()
# 16
squares[-1]()
# 16
```

We can look at another example.  It creates a list of lambda functions, with the possible intention of a list of functions as [lamba x: x + 1, lambda x: x + 2, ..., lambda x: x + 9].  But unfortunately, in this case, lambda function holds on to the expression of $$i$$ and won't undate it until the end.  So we end up with a list of lambda functions, all of them are lamba x: x + 9

```python
incremental = [lambda x: x + i for i in range(10)]
print(incremental[0](2))
# 11
print(incremental[-1](2))
# 11
```

To avoid that, we need to save the values in variables local to the lambdas, so that they don’t rely on the value of the global x:
```python
>>> squares = []
>>> for x in range(5):
...     squares.append(lambda n=x: n**2)
>>>
>>> squares[2]()
# 4
>>> squares[4]()
# 16
```
Here, n=x creates a new variable n local to the lambda and computed when the lambda is defined so that it has the same value that x had at that point in the loop. This means that the value of n will be 0 in the first lambda, 1 in the second, 2 in the third, and so on. Therefore each lambda will now return the correct result:

Note that **this behaviour is not peculiar to lambdas, but applies to regular functions too**.

For the list comprehsension example, we can define the lambda function before list comprehension inputs the range(10) one by one into the lambda function f, and outputs the values in a list. 

```python
f = lambda x: x*x
[f(x) for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

#  Use with 2 arguments in list comprehension

## Higher order function

It is basically a function of function.

```python
f = lambda x, func: x + func(x)
f(2, lambda x: x*x)
# 6
f(2, lambda x: x*10)
# 2 + 2*10 = 22
```

## Loan balance amortization

<span class="coding">list(accumulate(A))</span> can be used to solve more complex problems. 

In the following example, the lambda takes 2 arguments, bal and pmt. 

bal is the the bal*1.05 + pmt, pmt is the 
bal = 1000
bal = bal*1.05 + pmt, where pmt = -90

<div class="code-head"><span>code</span>accumulate.py</div>

```py
# Amortize a 5% loan of 1000 with 4 annual payments of 90
>>> cashflows = [1000, -90, -90, -90, -90]
>>> list(accumulate(cashflows, lambda bal, pmt: bal*1.05 + pmt))
[1000, 960.0, 918.0, 873.9000000000001, 827.5950000000001]
```

# Reference

[Python design official documentation, why-can-t-lambda-expressions-contain-statements](https://docs.python.org/3/faq/design.html#why-can-t-lambda-expressions-contain-statements)

[Python FAQ Why do lambdas defined in a loop with different values all return the same result?](https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result)

[python accumulate official documentation](https://docs.python.org/3/library/itertools.html#itertools.accumulate)

[Excel lambda-the-ultimatae-excel-worksheet-function](https://www.microsoft.com/en-us/research/blog/lambda-the-ultimatae-excel-worksheet-function/)

