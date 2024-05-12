---
layout: post
tag : Levenshtein
category: "Python for SAS"
title: "Match company names"
description: getting financial data from difference sources require matching company names
author: Sarah Chen
image: images/posts/photos/IMG_0875.JPG

---

Often we need to match company names when our data comes from different sources.   One of the methods is to use distance (between word vectors).  


<div class="code-head"><span>code</span>match names.py</div>

```python

import Levenshtein

def match_names(column1, column2):
    matches = {}
    for name1 in column1:
        min_distance = float('inf')
        match = None
        for name2 in column2:
            distance = Levenshtein.distance(name1, name2)
            if distance < min_distance:
                min_distance = distance
                match = name2
        matches[name1] = match
    return matches

# Example usage:
column1 = ["John", "Jane", "Michael"]
column2 = ["Jon", "Janet", "Michele"]
matches = match_names(column1, column2)

for name1, match in matches.items():
    print(f"{name1} matched with {match}")

```
