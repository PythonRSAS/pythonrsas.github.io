---
layout: post
tag : puzzle, algorithm
category: education
title: "Palindrome"
description: solving the longest palindrome puzzle
author: Sarah Chen
image: images/posts/photos/IMG_0869.JPG

---
Quote from [Wikipedia](https://en.wikipedia.org/wiki/Longest_palindromic_substring#:~:text=In%20computer%20science%2C%20the%20longest,bananas%22%20is%20%22anana%22.) "In computer science, the longest palindromic substring or longest symmetric factor problem is the problem of finding a maximum-length contiguous substring of a given string that is also a palindrome. For example, the longest palindromic substring of "bananas" is "anana".

Given a string, find the longest palindrome from the string. 
# Brute force
What came to my mind first is a brute force method.  

The method is like solving a very simple math problem.  
* You first _understand what does the problem exactly ask for_.
* **Put the requirements in math terms!**  
* Then _test it on one or two basic cases to really understand the problem and solution_.  Because it is hard to think only think with abstractions.  
* Work out the **generalization**. 

1. Let the length of the string be $$n$$.  Assume the longest is the entire string, check if it is palindrome. If yes, then done. 
2. If the entire string is not a palindrome, then we decrease check length by 1:  check on continuous chunks of length $$n-1$$, and iterate through them. Say the string is "abcd", then the iterations are: "abc", and "bcd". There are $$4-3+1$$ of them. We generalize the number of substrings with length $$x$$ to $$n - X +1$$.  If any of them is palindrome, then we are done.  Else continue. 
   

all(s[i] == s[~i] for i in range(len(s) // 2))


<div class="code-head"><span>code</span>palindrome_brute_force.py</div>\

```py
def checkPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
def max_Palindrome(s):
    for i in range(len(s),0,-1): # i: check length
        for j in range(0, len(s) + 1 - i): # j: starting index
            if checkPalindrome(s[j: j + i]):
                return s[j: j + i]
max_Palindrome("aba")
# "aba"
max_Palindrome("abcd")
# 'a'
```

# Clever ways

The brute force method works. Now we try to find improvements.  
1. Since palindroms are symmetric, do we really have to check the entire string if it is equal to its reverse?
   
```python
def check_Palindrome(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))
```
1. Can we loop through once instead of double loop?
2. Since we are looking for the longest, then if we find one of length m, then we can immediately go to check on m + 1 length ones

# Remove symbols and white spaces

What if the input string has white space, symbols, punctuations and has different cases? 
* **isalnum()**: Return True if the string is an alphanumeric string, False otherwise.  Note that <span class="coding">isalnum(</span> would return False on an empty string.   However, an empty string is considered a palindrome. 

A string is alphanumeric if all characters in the string are alphanumeric and there is at least one character in the string.

If s is an empty string, then l = 0 and r = -1.  This does not satisfy any of the while/if conditions.  So return <span class="coding">True</span>.

When s is not an empty string, l moves to the right and skp over any non-alphanumeric string while r does the same from the opposite end. 

Then compare <span class="coding">s[l].lower() != s[r].lower()</span>, and returns False upon the first non-equal pairs.   

<div class="code-head"><span>code</span>check palindrome in place.py</div>

```py
def checkPalindrome_in_place(s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower(): # compare if equal
            return False
        l += 1
        r -= 1
    return True
print(checkPalindrome_in_place(''))
# True
```

Below code is shorter, but it is not in-place. 

```python
def checkPalindrome_not_in_place(s):
    s = ''.join(i for i in s if i.isalnum()).lower()
    return s == s[::-1]
```
# reverse vs. reversed()
Initially I thought of using the <span class="coding">.reverse()</span function, but I am glad I did not. 

* **<span class="coding">.reverse()</span>**: reverses a list in-place.   Do not use <span class="coding">.reverse()</span> to check if a string is a palindrom.  It will always return False.  
* **<span class="coding">reversed</span>**: Return a reverse iterator over the values of the given sequence. 
  
```python
A = list('aba')
A == A.reverse()
# False
```

If we only want to iterate the list in reverse manner, reversed() is faster than slicing for long strings.   

On the other hand, although the reversed() function is faster than the slicing method, it returns an iterator. To make a reversed string, we have to use .join().

```python
reversed(A)
# <list_reverseiterator at 0x2a874f2cac8>
''.join(reversed(A))
'aba'
```
