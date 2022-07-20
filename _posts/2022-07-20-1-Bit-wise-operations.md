---
layout: post
tag: binary system, bit-wise operations
category: education
title: "Bit-wise operations"
description: learning bit (binary) operations and use Python to illustrate
author: Sarah Chen
image: images/posts/photos/sf/photos/sf/IMG_0956.JPG
# image: images/posts/photos/IMG-0632.JPG
---
<figure> 
   <img src="{{"/images/posts/photos/sf/IMG_0956.JPG"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 

# What is bit

> The bit represents a logical state with one of two possible values. These values are most commonly represented as either "1" or "0", true/false, yes/no, and etc..

From Wikipedia: [The bit is the most basic unit of information in computing and digital communications. The name is a portmanteau of binary digit.](https://en.wikipedia.org/wiki/Bit)

I first learned about bit-wise number system when I was a child.  It is nothing but using binary instead of decimal  

# Binary number system vs decimal number system
When we represent numbers in decimal number system, we use powers of 10. 
$$1 = 10^0$$
$$10 = 10^1$$
$$100 = 10^2$$
$$1000 = 10^3$$
$$16= 10^1+6*10^0$$
$$214 = 2*10^2+10^1 +4*10^0$$

In the bit-wise or binary number system, we use powers of 2.
$$1_10 = 2^0 => 1$$
$$16_10 = 2^4 => 10000$$
$$20_10 = 16_10 + 4_10 = 2^4 +2^2 => 10100$$

We can use any number system.  Say it is 3.  Then all numbers will be decomposed as powers of 3. 

# Bit-wise operations

The following operations should be taken *very literally*.  Please see the tables. 
 
**And <span class="coding">a & b</span>**
Returns $$1$$ only when both $$a$$ and $$b$$ are $$1$$, otherwise $$0$$. 

| And| $$0$$ | $$1$$ |
| ---------|:---------:|----------|
| $$0$$ | $$0$$ | $$0$$ |
| $$1$$ | $$0$$ | $$1$$ |

Example, want the lower 4 bits of an integer.  We <span class="coding">AND</span> it with $$15$$ (binary $$1111$$) so:

    201: 1100 1001
AND  15: 0000 1111
------------------
 IS   9  0000 1001

<div class="code-head"><span>code</span>Using And.py</div>

```py
print(bin(201))
print(bin(15))
print(bin(201&15))
# 0b11001001
# 0b1111
# 0b1001
print(201&15)
# 9
``` 

Similarly, if we want to clear the lower 4 bits of the integer 201, we can do the following:
```python
int('0b11001001',2)
201
int('0b11000000',2)
192
bin(201&192)
'0b11000000'
```

**Or <span class="coding">a | b</span>**

Always $$1$$ except when both $$a$$ and $$b$$ are $$0$$.

| Or| $$0$$ | $$1$$ |
| ---------|:---------:|----------|
| $$0$$ | $$0$$ | $$1$$ |
| $$1$$ | $$1$$ | $$1$$ |

**XOR <span class="coding">a ^ b</span>**

"bitwise exclusive or".

It returns 1 only when $$a$$ and $$b$$ are different. 

| XOR| $$0$$ | $$1$$ |
| ---------|:---------:|----------|
| $$0$$ | $$0$$ | $$1$$ |
| $$1$$ | $$1$$ | $$0$$ |

**Not <span class="coding">~ a</span>**

Returns the complement of $$a$$.  If input is 0, then output is 1. It is the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as a - 1.

| Not| $$0$$ | $$1$$ |
| ---------|:---------:|----------|
|          | $$1$$ | $$0$$ |


**Shift to left <span class="coding">a << b</span>**

Returns a with the bits shifted to the left by b places (and new bits on the right-hand-side are zeros).  

In decimal system it is multiplying a by $$2^y$$.

**Shift to right <span class="coding">a >> b</span>**

Returns x with the bits shifted to the right by y places. This is the same as //'ing a by 2**y.


<div class="code-head"><span>code</span>bitwise operations.py</div>

```py
print(bin(10))
# 0b1010
print(bin(10)[2:])
# 1010
bin(10|2)[2:]
# 1010
bin(10) == bin(10|2)
# True
``` 

## Examples using bitwise operations



# Reference

[bitwise operation and usage](https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage)
[Python operators](https://jakevdp.github.io/WhirlwindTourOfPython/04-semantics-operators.html)

