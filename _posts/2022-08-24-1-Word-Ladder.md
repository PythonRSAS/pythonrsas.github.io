---
layout: post
tag : puzzle, algorithm
category: education
title: "Word Ladder"
description: solving the shortest word ladder puzzle
author: Sarah Chen
image: images/posts/Head_to_tail_word_ladder.svg.PNG

---
Quote from [Wikipedia](https://en.wikipedia.org/wiki/Word_ladder) "Word ladder (also known as Doublets, word-links, change-the-word puzzles, paragrams, laddergrams, or word golf) is a word game invented by Lewis Carroll..

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Head_to_tail_word_ladder.svg/220px-Head_to_tail_word_ladder.svg.png)


The problem is [Leetcode 127. Word Ladder](https://leetcode.com/problems/word-ladder/).  
 
Given two words, beginWord and endWord, and a wordList, return the number of words in the **shortest**  word ladder from beginWord to endWord, or 0 if no such sequence exists.

![](../images/posts/wordLadderBFS.PNG)

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
<!-- The method is like solving a very simple math problem.  
* You first _understand what does the problem exactly ask for_.
* **Put the requirements in math terms!**  
* Then _test it on one or two basic cases to really understand the problem and solution_.  Because it is hard to think only think with abstractions.  
* Work out the **generalization**. 

1. Let the length of the string be $$n$$.  Assume the longest is the entire string, check if it is palindrom. If yes, then done. 
2. If the entire string is not a palindrom, then we decrease check length by 1:  check on continuous chunks of length $$n-1$$, and iterate through them. Say the string is "abcd", then the iterations are: "abc", and "bcd". There are $$4-3+1$$ of them. We generalize the number of substrings with length $$x$$ to $$n - X +1$$.  If any of them is palindrom, then we are done.  Else continue. 
    -->

For each word in the wordList, and the beginning word, we mask one letter at a time.  For the word "hot", since it has 3 letters, there are 3 ways to mask it. \*ot, h\*t, and ho\*.

Let these masked words be class representatives (dictionary keys).  And the respective classes that they represent are lists of relatives who would be the same as each other if masked at the same position.  For example, 
*ot ['hot', 'dot', 'lot', 'cot']
h*t ['hot', 'hit']
ho* ['hot']

We first build an adjacency dictionary, where class representative is they, and the class contains words that can be represented by the representative. 

<div class="code-head"><span>code</span>word ladder.py</div>

```py
from collections import deque, defaultdict
def seqLength(A,Z, w_lt):
    if Z not in w_lt:
        return 0
    # build adjacency dictionary
    dd = defaultdict(list)
    w_lt.append(A) # because w_lt does not have begin word
    for word in w_lt:
        for i in range(len(word)):
            dd[word[:i] + "*" + word[i+1:]].append(word) # 每个词有 ||词||个 keys, 如果词长度是3， 就有3个keys
    for k, v in dd.items():
        print(k, v)

    # BFS
    visit = set([A])
    print("visit begins with: ", visit)
    que = deque()
    que.append(A)
    print('que begins with', que)
    res = 1
    while que:
        print("\n****************************************\n", que)
        for i in range(len(que)):
            word = que.popleft()
            print('\npopped ', word)
            if word == Z:
                return res # exit 出口
            for j in range(len(word)):
                for value in dd[word[:j] + "*" + word[j+1:]]:
                    if value not in visit:
                        # print("value not in visit:", value)
                        # print("to add ", value)
                        que.append(value)
                        print("Add to que ", value)
                        visit.add(value)
                        # print("visit ", visit)
            print("i:", i)
        res += 1
        print("current res is ", res)

    return 0
beginWord = "hit";  endWord = "cog";  wordList = ["hot","dot","dog","lot","log","cog", "fog", "cot"]
# beginWord = "hit";  endWord = "cog";  wordList = ["hot","dot","dog","lot","log","cog"]
print(seqLength(beginWord, endWord, wordList))
[Out]:
*ot ['hot', 'dot', 'lot', 'cot']
h*t ['hot', 'hit']
ho* ['hot']
d*t ['dot']
do* ['dot', 'dog']
*og ['dog', 'log', 'cog', 'fog']
d*g ['dog']
l*t ['lot']
lo* ['lot', 'log']
l*g ['log']
c*g ['cog']
co* ['cog', 'cot']
f*g ['fog']
fo* ['fog']
c*t ['cot']
*it ['hit']
hi* ['hit']
visit begins with:  {'hit'}
que begins with deque(['hit'])

****************************************
 deque(['hit'])

popped  hit
Add to que  hot
i: 0
current res is  2

****************************************
 deque(['hot'])

popped  hot
Add to que  dot
Add to que  lot
Add to que  cot
i: 0
current res is  3

****************************************
 deque(['dot', 'lot', 'cot'])

popped  dot
Add to que  dog
i: 0

popped  lot
Add to que  log
i: 1

popped  cot
Add to que  cog
i: 2
current res is  4

****************************************
 deque(['dog', 'log', 'cog'])

popped  dog
Add to que  fog
i: 0

popped  log
i: 1

popped  cog
4
```

# Future reading
[Wolfram.com, The Longest Word Ladder Puzzle Ever](https://blog.wolfram.com/2012/01/11/the-longest-word-ladder-puzzle-ever/)