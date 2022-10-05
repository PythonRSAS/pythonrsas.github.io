---
layout: post
tag : data structure
category: education
title: "Merge 2 Sorted Lists"
description: Leetcode 21. Merge Two Sorted Lists
author: Sarah Chen
image: images/posts/merge_sorted_lists.jpg

---

# Problem
The problem is [Leetcode 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/). 

![merge_sorted_lists](../images/posts/merge_sorted_lists.jpg)
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
合併兩個已排序之連結串列（Linked List）l1 、 l2 並回傳一個新的已排序串列。新的串列應當由兩個串列之節點拼接在一起而形成。

範例：
輸入： 1->2->4, 1->3->4
輸出： 1->1->2->3->4->4

# Brute Force Stupid Method

The solution is [from a Leetcode user](https://leetcode.com/problems/merge-two-sorted-lists/discuss/2659387/python-solution).  It goes out of the way to do lots of extra work and it did not take any advantage of the fact that the two linked lists are already sorted.  But it gets the job done. 
It goes out of the way create two separate arrays, one for each linked list.  Then it concatenate the two arrays, and do the work of sorting the concatenated array.  Then it reverses it so that it is sorted in descending order.  Finally, it creates a new linked list, and moves the elements from array to the linked list. 

So, why do I bother to learn this code?  Because as inefficient as it is, I like the last part.  It initializes <span class="coding">res</span> as None.  Then it takes the elements from array (in descending order). 
```python
res = None
for i in l:
    res = ListNode(i,res)
return res
```
The first number node is 4.  Then res = ListNode(i,res) defines 3 to point at the older node 4.  The last number is defined to ListNode(1, res), effectively linking all the previous nodes. 

<div class="code-head"><span>code</span>mergeTwoLists_bf.py</div>

```py
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1, list2):
    l1 = []
    while list1 != None:
        l1.append(list1.val)
        list1 = list1.next
        
    l2 = []
    while list2 != None:
        l2.append(list2.val)
        list2 = list2.next
    l = sorted(l1+l2)[::-1]
    print(l)
    res = None
    for i in l:
        res = ListNode(i,res)
        print(res.val)
    return res
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

res = mergeTwoLists(list1, list2)
# [4, 4, 3, 2, 1, 1]
# 4
# 4
# 3
# 2
# 1
# 1
print(res.val)
print(res.next.val)
```

# O(n) Merge Sort Method
解題思維：
看哪個串列的第一個數字較小，就取該位置當作合併後的頭。接著，將以兩個指標 p1 、 p2 各自指向兩個串列目前正要看的元素。

如果 p1 指到的元素值較小，代表其值應接在新的串列之尾端（用另一個指標指向新串列的尾端元素，其後的元素就是接在該尾端的後面，形成新的尾端），然後將 p1 指到對應的下一個元素；若 p2 較小，則同理；若兩者一樣大，則隨便取一者加進去。

重複以上步驟直到 p1 或 p2 為空指標（沒有新的元素了），則將非空指標的該指標指到的元素全數接在新串列之後方。最後的新串列即為所求。

In the code below, we use two nodes: <span class="coding">fast</span> and <span class="coding">slow</span>. 

1. The merge process reminds me of Merge Sort (合併排序). 
2.  **Why do we use two nodes?** Can we just use one node?  We need 2 nodes because we need one to hold the head and the other <span class="coding">fast</span> to travel through the merged linked list.  At the end of the process, <span class="coding">fast</span> holds only the last value of the merged list. We cannot return only the last value. 
3. **Why do we return <span class="coding">slow.next</span>** as opposed to return slow? Because slow.val is zero.  And we don't want the zero head. 
<div class="code-head"><span>code</span>linkedList.py</div>
4. The one liner <span class="coding">fast = slow = ListNode()</span> is equivalent to writing as two liner: fast = ListNode(), slow = fast.  But, it is totally not the same as: fast = ListNode(), slow = ListNode(). 

<div class="code-head"><span>code</span>mergeTwoLists_mergeSort.py</div>

```py
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1, list2):
    # fast = slow = ListNode()
    fast = ListNode()
    slow = fast
    while list1 and list2:               
        if list1.val < list2.val:
            fast.next = list1
            list1, fast = list1.next, list1
        else:
            fast.next = list2
            list2, fast = list2.next, list2
    if list1:
         fast.next = list1
    if list2:
        fast.next = list2
    return slow.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

res = mergeTwoLists(list1, list2)
print(res.val)
# 1
print(res.next.next.next.val)
# 3
```

The time complexity is $$O(n)$$. 
The space complexity is $$O(1)$$. 
# Reference

[Linked List, Wikipedia](https://en.wikipedia.org/wiki/Linked_list)

[Leetcode 21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

https://home.gamer.com.tw/artwork.php?sn=4864600