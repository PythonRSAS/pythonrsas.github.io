---
layout: post
tag: binary system, bit-wise operations
category: education
title: "Bit-wise operations"
description: learning bit (binary) operations and use Python to illustrate
author: Sarah Chen
image: images/posts/photos/sf/photos/sf/IMG_0956.jpg
# image: images/posts/photos/IMG-0632.JPG
---
<figure> 
   <img src="{{"/images/posts/photos/sf/IMG_0956.jpg"| relative_url}}"> 
   <figcaption></figcaption>
</figure> 


> <span class="coding">|</span> is used to set a certain bit to $$1$$.

> <span class="coding">a&1</span> is used to test if a certain bit is $$1$$ or $$0$$.

# What is bit

> The bit represents a logical state with one of two possible values. These values are most commonly represented as either "1" or "0", true/false, yes/no, and etc..

From Wikipedia: [The bit is the most basic unit of information in computing and digital communications. The name is a portmanteau of binary digit.](https://en.wikipedia.org/wiki/Bit)

I first learned about bit-wise number system when I was a child.  It is nothing but using binary instead of decimal  

# Binary vs decimal number system
When we represent numbers in decimal number system, we use powers of 10. 

$$1 = 10^0$$

$$10 = 10^1$$

$$100 = 10^2$$

$$1000 = 10^3$$

$$16= 10^1+6*10^0$$

$$214 = 2*10^2+10^1 +4*10^0$$

In the bit-wise or binary number system, we use powers of 2.

$$1 = 2^0 => 1$$

$$16 = 2^4 => 10000$$

$$20 = 16 + 4 = 2^4 +2^2 => 10100$$

```py
print(bin(10))
# 0b1010
print(bin(10)[2:])
# 1010
bin(0xFF)
# '0b11111111'

int(bin(0xFF)[2:],2)
# 255
```
We can use any number system.  Say it is 3.  Then all numbers will be decomposed as powers of 3. 

# Bit-wise operations

The following operations should be taken *very literally*.  Please see the tables. 
 

**And** <span class="coding">a & b</span>

Returns $$1$$ only when both $$a$$ and $$b$$ are $$1$$, otherwise $$0$$. 

| And| $$0$$ | $$1$$ || Or| $$0$$ | $$1$$ || XOR| $$0$$ | $$1$$ |
| ---------|:---------:|----------|| ---------|:---------:|----------|| ---------|:---------:|----------|
| $$0$$ | $$0$$ | $$0$$ || $$0$$ | $$0$$ | $$1$$ || $$0$$ | $$0$$ | $$1$$ |
| $$1$$ | $$0$$ | $$1$$ || $$1$$ | $$1$$ | $$1$$ || $$1$$ | $$1$$ | $$0$$ |

Example, if we want the lower (least significant) 4 bits of an integer, we <span class="coding">AND</span> it with $$15$$ (binary $$1111$$) so:

$$201$$ is  $$1100 1001$$

After "and" with $$15$$, all upper bits disappear, keeping only the lower 4 bits. 

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

**Or** <span class="coding">a | b</span> is always $$1$$ except when both $$a$$ and $$b$$ are $$0$$.

<span class="coding">|</span> is used to set a certain bit to $$1$$.  

Counting from the lower and the first lower as 0, <span class="coding">x | 2</span> is used to set bit 1 of x to 1. 

```python
def setbit0_1(x):
    print(bin(x|1))
setbit0_1(4)
# 0b101
```

<span class="coding">x & 1</span> can be used to test if bit 0 of x is 1 or 0.  

**XOR** <span class="coding">a ^ b</span>

<span class="coding">^</span> stands for "bitwise exclusive or".   Do not confuse it with <span class="coding">**</span>.

It returns 1 only when $$a$$ and $$b$$ are different. 

**Not** <span class="coding">~ a</span>

Returns the complement of $$a$$.  If input is 0, then output is 1. It is the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as a - 1.

| Not| $$0$$ | $$1$$ |
| ---------|:---------:|----------|
|          | $$1$$ | $$0$$ |


**shifting** <span class="coding">a << b</span>  <span class="coding">a >> b</span>

x << 1 is doubling and x >> 1 is halving. 

```python
print(-16>>1)
-8
```

<span class="coding">a << b</span> returns a with the bits shifted to the left by b places (and new bits on the right-hand-side are zeros).  

In decimal system it is multiplying a by $$2^y$$.

<span class="coding">a >> b</span> returns a with the bits shifted to the right by b places. This is the same as <span class="coding">a//2**b</span>.

<div class="code-head"><span>code</span>bitwise operations.py</div>

```py
bin(10|2)[2:]
# 1010
bin(10) == bin(10|2)
# True
``` 

# Examples

In the first example, we count the number of 1's in a number.  <span class="coding">&1</span> removes all digits before the lowest one, and <span class="coding">x & 1</span> is simply 0 or 1 depending on weather the last digit of a number is 1 or 0. 

We can also use <span class="coding">bit_count</span> or <span class="coding">bin(n).count('1')</span> to count non-zero bits.

```python
n = 4
print(n.bit_count())
# 1
print(bin(4).count("1"))
```
<div class="code-head"><span>code</span>count bits.py</div>

```py
def count_bits(x):
    numBits = 0
    while x:
        numBits += x & 1
        x >>= 1
    return numBits

for i in range(5):
    print("\n",i, "in binary system is:", bin(i)[2:])
    print("The number of 1's or bits is", count_bits(i))

#  0 in binary system is: 0
# The number of 1's or bits is 0

#  1 in binary system is: 1
# The number of 1's or bits is 1

#  2 in binary system is: 10
# The number of 1's or bits is 1

#  3 in binary system is: 11
# The number of 1's or bits is 2

#  4 in binary system is: 100
# The number of 1's or bits is 1

```

Below example of parsing hexadecimal colours came from [stackoverflow](https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage).  

It accepts a String like #FF09BE and returns a tuple of its Red, Green and Blue values.
<div class="code-head"><span>code</span>hex to rgb.py</div>

```py
def hexToRgb(value):
    # Convert string to hexadecimal number (base 16)
    num = (int(value.lstrip("#"), 16))

    # Shift 16 bits to the right, and then binary AND to obtain 8 bits representing red
    r = ((num >> 16) & 0xFF)

    # Shift 8 bits to the right, and then binary AND to obtain 8 bits representing green
    g = ((num >> 8) & 0xFF)

    # Simply binary AND to obtain 8 bits representing blue
    b = (num & 0xFF)
    return (r, g, b)
```


# Reference

[bitwise operation and usage](https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage)
[Python operators](https://jakevdp.github.io/WhirlwindTourOfPython/04-semantics-operators.html)

