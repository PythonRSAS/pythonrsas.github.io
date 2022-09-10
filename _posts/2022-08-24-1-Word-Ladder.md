---
layout: post
tag : puzzle, algorithm
category: education
title: "Word Ladder"
description: solving the shortest word ladder puzzle
author: Sarah Chen
image: images/posts/wordLadderBFS.PNG

---
Quote from [Wikipedia](https://en.wikipedia.org/wiki/Word_ladder) "Word ladder (also known asdoublets, word-links, change-the-word puzzles, paragrams, laddergrams, or word golf) is a word game invented by Lewis Carroll..

![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Head_to_tail_word_ladder.svg/220px-Head_to_tail_word_ladder.svg.png)

# Problem
The problem is [Leetcode 127. Word Ladder](https://leetcode.com/problems/word-ladder/).  
 
Given two words, beginWord and endWord, and a wordList, return the number of words in the **shortest**  word ladder from beginWord to endWord, or 0 if no such sequence exists.

![](../images/posts/wordLadderBFS.PNG)

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0

# Class representative hash table - adjacency dictionary
For each word in the wordList, and the beginning word, we mask one letter at a time.  For the word "hot", since it has 3 letters, there are 3 ways to mask it. \*ot, h\*t, and ho\*.

Let these masked words be class representatives (dictionary keys).  And the respective classes that they represent are lists of relatives who would be the same as each other if masked at the same position.  For example, 
*ot ['hot', 'dot', 'lot', 'cot']

h*t ['hot', 'hit']

ho* ['hot']

We first build an adjacency dictionary, where class representative is they, and the class contains words that can be represented by the representative. 

Then we traverse the graph (represented by the adjacency dictionary) using BFS, layer by layer, and check if anyone we encounter is the endWord "cog".  Each layer we visit adds 1 to the ladder. 

Each layer are the neighbors of the previously visited word.  We begin with "hit", and pop it.  Its immediate neighbors ['dot', 'lot', 'cot'] are added to the que.  We pop them one by one.  Then their immediate neighbors ['dog', 'log', 'cog'] are added to the que.   Again, we pop them one by one.  When "cog" was popped, we returen the number of layers and we are done. 

I printed out each step to explain what the code does. 
<div class="code-head"><span>code</span>word ladder.py</div>

```py
from collections import deque, defaultdict
def seqLength(A, Z, w_lt): # A=beginWord; Z=endWord
    if Z not in w_lt:
        return 0
    # build adjacency dictionary
    dd = defaultdict(list)
    w_lt.append(A) # because w_lt does not have begin word
    for word in w_lt:
        for i in range(len(word)):
            # 每个词有 ||词||个 keys, 如果词长度是3， 就有3个keys
            dd[word[:i] + "*" + word[i+1:]].append(word) 
    for k, v in dd.items(): # for explaination
        print(k, v)

    # BFS
    visit = set([A])
    # print("visit begins with: ", visit)
    que = deque()
    que.append(A)
    # print('que begins with', que)
    res = 1
    while que:
        # print("\n****************************************\n", que)
        for i in range(len(que)):
            word = que.popleft()
            # print('\npopped ', word)
            if word == Z:
                return res # exit 出口
            for j in range(len(word)):
                for value in dd[word[:j] + "*" + word[j+1:]]:
                    if value not in visit:
                        que.append(value)
                        # print("Add to que ", value)
                        visit.add(value)
            # print("i:", i)
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