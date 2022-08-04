---
layout: post
tag : data structure, greedy algorithm, python, search, dynamic programming
category: education
title: "Dijkstra algorithm shortest path between"
description: algorithm for finding shortest (or lowest cost) between any two nodes in a graph
author: Sarah Chen
image: images/posts/photos/IMG_0868.JPG

---

# Introduction
Obviously to be able to find the shortest distance or cost between any two nodes in a graph is a very useful thing. 

Dijkstra's algorithm to find the shortest path between two points. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. 

I find it more intuitive if I think in terms of driving from one place to another. I look at the map, and compare the different routes in distance and traffic (plus toll).  I choose the route with the shortest distance (unless traffic is bad).  

<!-- When there are many routes, then I can iteratively  -->

  
# Dijkstra's algorithm
Dijkstra's method has two steps: 
1. Update estimates
2. Choose next node 

Initially all distances are labeled as $$\infinity$$, except the starting node.




# Reference
## Videos
[How Dijkstra's Algorithm Works](https://www.youtube.com/watch?v=EFg3u_E6eHU)
[Graphs: Dijkstra's Minimal Spanning Tree and Dijkstra's Shortest Path](https://www.youtube.com/watch?v=i4W8WgTuGTE&t=288s)
