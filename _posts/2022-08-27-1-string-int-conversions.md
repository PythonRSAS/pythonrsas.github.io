---
layout: post
tag : strings, int, ord, chr
category: education
title: "string int conversions"
description: explore string operations in Python and the ord, chr functions
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---
- [Convert string to integer](#convert-string-to-integer)
- [Convert integer to string](#convert-integer-to-string)
- [Appendix](#appendix)


It is easy to convert int to string or from string to int.  Just use the <span class="coding">int</span> and <span class="coding">str</span> functions.   

The int function not only can 
- convert a string to number
- convert using given base
- remove decimals from a floating number 
    
```python
int('10')
# 10
int('10', base = 2)
# 2
int(10.3)
# 10
```
But what if we want to implement those from scratch?  

* **ord**: Return the Unicode code point for a one-character string.
* **chr**: Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
  
Unicode and code point can seem complicated.  According to [Wikipedia](https://en.wikipedia.org/wiki/Unicode) It is formally The Unicode Standard is an information technology standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. 
  
# Convert string to integer

We can use the <span class="coding">ord</span> function, which returns the Unicode code point for a one-character string. 
```python
ord('0')
# 48

ord('1')
# 48

ord('a')
97

ord('z')
122
```

So we use <span class="coding">ord(s) - ord('0')</span> to get the integer because integer 1 - 9 can be represented by their distance to ord('0').

<div class="code-head"><span>code</span>Convert string to integer.py</div>

```py
def string_to_int(s):
    return ord(s) - ord('0')

def f(s):
    res = 0
    for i in range(len(s)):
        num = string_to_int(s[i:i+1]) * 10**(len(s) - i -1)
        res = res + num
    return res
f('12')
# 12
```
But that only takes care of positive integers.  We need to account for negative integers by checking if the first character is '-'.
If the beginning letter is the negative sign, then we need to start <span class="coding">i</span> at 1 instead of 0.  Other than that, everything stays the same. 
```python
def f(s):
    res = 0
    if s[0] == '-':
        start_index = 1
    else:
        start_index = 0
    for i in range(start_index, len(s)):
        num = string_to_int(s[i:i+1]) * 10**(len(s) - i - 1)
        res = res + num
    return -1*res if s[0] == '-' else res
print(f('12'))  
# 12  
print(f('-12'))    
# -12
```

# Convert integer to string

We need to take into account integers can be both positive and negative. 

A string is a list of characters.  We will 
- convert the least signficant digit (using <span class="coding">%10</span>) to string.  
- reduce current integer by //10 (to get the quotient 商)
- repeat the last two steps until the current integer is 0
- use .join() to glue the string together. 

Because we want to append to the left, we will use a special list <span class="coding">collections.deque</span>.  For example, for integer 12, the number 2 goes first, then 1.  If we use append, the string would be '21', the reverse of what's expected.  

And to convert a single digit integer to string, we use the <span class="coding">chr</span> function, which returns a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.

When we write the function to convert input single string character to integer, we subtract ord('0') from the Unicode of input by <span class="coding">ord(s) - ord('0')</span>.   Conversely, we need to add <span class="coding">ord('0')</span> when we want to go from Unicode to string. 

<div class="code-head"><span>code</span>Convert integer to string.py</div>

```py
from collections import deque
def single_int_to_string(x):
    return chr(ord('0') + x)

def f(num):
    s = deque()
    while num:
        s.appendleft(single_int_to_string(num % 10))
        num //= 10 
    return ''.join(s)

print(f(12))
# '12'
type(f(12))
# str
```

Initially I used <span class="coding">while num</span>.  But I think it is better to use <span class="coding">while num > 0</span> explicitly. 

Even though the code can be much shorter, but I think it is easy to understand and maintain to explicitly account for the case that input integer is zero, negative and positive. 

<div class="code-head"><span>code</span>Convert integer to string.py</div>

```py
from collections import deque
def single_int_to_string(x):
    return chr(ord('0') + x)

def f(num):
    if num == 0:
        return single_int_to_string(0)
    s = deque()
    if num < 0:
        is_negative = '-' 
        num = - num
    else:
        is_negative = ''
    while num > 0:
        s.appendleft(single_int_to_string(num % 10))
        num //= 10 
    s.appendleft(is_negative)
    return ''.join(s)

print(f(12))
# '12'
print(f(-12))
# '-12'
```

# Appendix
In SAS, to conver string to integer, we use

```sas
data new;
   char_var = '123';
   numeric_var = input(char_var, 8.);
run;

data new;
    num_var = 123456;
    char_var = put(num_var,6.);
run;
```
