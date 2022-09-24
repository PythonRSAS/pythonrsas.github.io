---
layout: post
tag : puzzle, algorithm
category: education
title: "Cycle detection"
description: solving the linked list cycle detection puzzle using the fast-slow algorithm, also known as Floyd's tortoise-hare algorithm
author: Sarah Chen
image: images/posts/Tortoise_and_hare_algorithm.png

---

- [Problem statement:](#problem-statement)
- [Floyd's tortoise-hare](#floyds-tortoise-hare)
- [Implement in code](#implement-in-code)
- [Solve our puzzle](#solve-our-puzzle)
# Problem statement:

Given a linked list, if there is a cycle, return the start of the cycle.  The start of cycle is defined as the place where 2 nodes meet.  
If there is no cycle, return -1. 

![](../images/posts/linked_list_cycle.PNG)

# Floyd's tortoise-hare 
A famous solution for detecting cycles is attributed to computer scientist [Robert Floyd](https://en.wikipedia.org/wiki/Robert_W._Floyd), who also co-designed the [Floyd-Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm) for finding shortest paths in a directed weighted graph with positive or negative edge weights.  

![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Tortoise_and_hare_algorithm.svg/560px-Tortoise_and_hare_algorithm.svg.png)

From [wikipedia](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare):
The key insight in the algorithm is as follows. If there is a cycle, then, for any integers i ≥ μ and k ≥ 0, xi = xi + kλ, where λ is the length of the loop to be found, μ is the index of the first element of the cycle, and k is a whole integer representing the number of loops. 

Based on this, it can then be shown that i = kλ ≥ μ for some k if and only if xi = x2i (if xi = x2i in the cycle, then there exists some k such that 2i = i + kλ, which implies that i = kλ; and if there are some i and k such that i = kλ, then 2i = i + kλ and x2i = xi + kλ). 

Thus, the algorithm only needs to check for repeated values of this special form, one twice as far from the start of the sequence as the other, to find a period ν of a repetition that is a multiple of λ. 

Once ν is found, the algorithm retraces the sequence from its start to find the first repeated value xμ in the sequence, using the fact that λ divides ν and therefore that xμ = xμ + v. 

Finally, once the value of μ is known it is trivial to find the length λ of the shortest repeating cycle, by searching for the first position μ + λ for which xμ + λ = xμ.

# Implement in code

The algorithm thus maintains two pointers into the given sequence, one (the tortoise) at xi, and the other (the hare) at x2i. At each step of the algorithm, it increases i by one, moving the tortoise one step forward and the hare two steps forward in the sequence, and then compares the sequence values at these two pointers. The smallest value of i > 0 for which the tortoise and hare point to equal values is the desired value ν.
<div class="code-head"><span>code</span>floyd.py</div>\

```py
def floyd(f, x0):
    # Main phase of algorithm: finding a repetition x_i = x_2i.
    # The hare moves twice as quickly as the tortoise and
    # the distance between them increases by 1 at each step.
    # Eventually they will both be inside the cycle and then,
    # at some point, the distance between them will be
    # divisible by the period λ.
    tortoise = f(x0) # f(x0) is the element/node next to x0.
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
  
    # At this point the tortoise position, ν, which is also equal
    # to the distance between hare and tortoise, is divisible by
    # the period λ. So hare moving in circle one step at a time, 
    # and tortoise (reset to x0) moving towards the circle, will 
    # intersect at the beginning of the circle. Because the 
    # distance between them is constant at 2ν, a multiple of λ,
    # they will agree as soon as the tortoise reaches index μ.

    # Find the position μ of first repetition.    
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)   # Hare and tortoise move at same speed
        mu += 1
 
    # Find the length of the shortest cycle starting from x_μ
    # The hare moves one step at a time while tortoise is still.
    # lam is incremented until λ is found.
    lam = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        lam += 1
 
    return lam, mu
```

# Solve our puzzle
In code below, <span class="coding">detect_cycle_start</span> is the main function.  The trick is to define two separate movements: the slow one moves 1 step at a time.  The fast one moves two steps at a time. 

```python
    slow = slow.next
    fast = fast.next.next
```

If there is a cycle, then they will meet.  We use a helper function <span class="coding">get_cycle_length</span> to get the cycle length, and break out of the <span class="coding">while</span> loop.  

If there is no cycle, then we will eventually come out of the <span class="coding">while</span> loop as soon as <span class="coding">fast</span> exhausts all the linked nodes. 

In the end, we return None if cycle length is not updated and return the meeting node if a cycle is detected. 

The time complexity is O(n) because we do not have double loops.  We have 1 loop in the main function. 

The space complexity is O(1) because we use a few pointers only. 

<div class="code-head"><span>code</span>linked list cycle detection.py</div>\

```py
class Node:
  def __init__(self, x):
    self.val = x
    self.next = None

def get_cycle_length(head: None) -> int: # helper function
  cycle_len = 0
  target = head
  while True: # keep stepping next until it is back to its starting place
    head = head.next
    cycle_len += 1
    if head == target:
      break
  return cycle_len

def get_start_point(head: None, cycle_len: int) -> Node: # helper function
  p1, p2 = head, head
  for _ in range(cycle_len):
    p2 = p2.next
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next
  return p1 # return where p1 and p2 meet

def detect_cycle_start(head: Node) -> Node:
  if not head or not head.next:
    return None
  slow, fast = head, head
  cycle_len = -1
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      cycle_len = get_cycle_length(slow)
      break
  return None if cycle_len == -1 else get_start_point(head, cycle_len)
# testing code
h = Node(1)
h.next = Node(2)
h.next.next = Node(3)
h.next.next.next = Node(4)
h.next.next.next.next = Node(5)
h.next.next.next.next.next = Node(6)
h.next.next.next.next.next.next = Node(7)
h.next.next.next.next.next.next.next = h.next.next
result = detect_cycle_start(h)
if result:
  print(result.val)
else:
  print("None")
# 3
```

