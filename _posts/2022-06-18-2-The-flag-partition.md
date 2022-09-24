---
layout: post
tag : abstract data structure, python
category: education
title: "The flag partition"
description: sorting into 3 buckets that look like 3 bands in the Dutch, French, 
author: Sarah Chen
image: images/posts/tricolors.PNG

---
- [The Dutch flag partitioning problem](#the-dutch-flag-partitioning-problem)
- [Reversing an array](#reversing-an-array)
- [Rotating an array](#rotating-an-array)
- [Get missing number](#get-missing-number)
- [Get missing number](#get-missing-number-1)
- [Check for pair sum](#check-for-pair-sum)

![flag](../images/posts/tricolors.PNG) 
# The Dutch flag partitioning problem
We want to partition an array in the following fashion:
Given an element called "pivot" (or the index of it) of the array of integers,  the ones smaller than this number should be placed before this number, and the ones before than this number after. 

The following solution has time complexity $$O(n)$$ and space complexity $$O(1)$$.  I did this problem a few times.  There are 4 places I found myself making mistakes:
1. indent of the return (or forgot to return)
2. compare with the pivot, not anything else
3. the direction of the range
4. forgot to increment/decrement the pointer indices

<div class="code-head"><span>code</span>flag_partition.py</div>

```py
def flag_partition(pivot_idx, A):
    pivot = A[pivot_idx]
    N = len(A)
    small_idx = 0
    big_idx = N - 1
    print("Pivot is ",A[pivot_idx])
    # move smaller ones to the front
    for i in range(N):
        if A[i] < pivot:
            A[i], A[small_idx] = A[small_idx], A[i]
            small_idx += 1

    # move bigger ones to the front
    for i in reversed(range(N)):
        if A[i] < pivot:
            break
        if A[i] > pivot:
            A[i], A[big_idx] = A[big_idx], A[i]
            big_idx -= 1

    return A
lt = [0, 1,2,0,2,1,1]
print(flag_partition(3,lt))
```

The following code are from Github repository "Data Structure using Python". 

<div class="code-head"><span>code</span>Array.py</div>

```py
class Array(object):
    ''' sizeOfArray: denotes the total size of the array to be initialized
       arrayType: denotes the data type of the array(as all the elements of the array have same data type)
       arrayItems: values at each position of array
    '''
    def __init__(self, sizeOfArray, arrayType = int):
        self.sizeOfArray = len(list(map(arrayType, range(sizeOfArray))))
        self.arrayItems =[arrayType(0)] * sizeOfArray    # initialize array with zeroes
        self.arrayType = arrayType

    def __str__(self):
        return ' '.join([str(i) for i in self.arrayItems])

    def __len__(self):
        return len(self.arrayItems)

    # magic methods to enable indexing
    def __setitem__(self, index, data):
        self.arrayItems[index] = data

    def __getitem__(self, index):
        return self.arrayItems[index]

    # function for search
    def search(self, keyToSearch):
        for i in range(self.sizeOfArray):
            if (self.arrayItems[i] == keyToSearch):      # brute-forcing
                return i                                 # index at which element/ key was found

        return -1                                        # if key not found, return -1

    # function for inserting an element
    def insert(self, keyToInsert, position):
        if(self.sizeOfArray > position):
            for i in range(self.sizeOfArray - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = keyToInsert
        else:
            print('Array size is:', self.sizeOfArray)

    # function to delete an element
    def delete(self, keyToDelete, position):
        if(self.sizeOfArray > position):
            for i in range(position, self.sizeOfArray - 1):
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[i + 1] = self.arrayType(0)
        else:
            print('Array size is:', self.sizeOfArray)

if __name__ == '__main__':
    a = Array(10, int)
    a.insert(2, 2)
    a.insert(3, 1)
    a.insert(4,7)
    print(len(a))

```
We can use the array class we defined.  For example,

```python
# access
a = Array(100,int)
idx = a.search(0)
print("found at", idx)

a.insert(2,2)
print(a)

```

# Reversing an array

<div class="code-head"><span>code</span>a1_reverseArry.py</div>

```py
import Arrays

def  reversingAnArray(start, end, myArray):
    while(start < end):
        myArray[start], myArray[end - 1] = myArray[end - 1], myArray[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    myArray = Arrays.Array(10)
    myArray.insert(2, 2)
    myArray.insert(1, 3)
    myArray.insert(3, 1)
    print('Array before Reversing:',myArray)
    reversingAnArray(0, len(myArray), myArray)
    print('Array after Reversing:',myArray)

```

# Rotating an array

<div class="code-head"><span>code</span>a2_arrayRotation.py</div>

```py

from Arrays import Array

def rotation(rotateBy, myArray):
    for i in range(0, rotateBy):
        rotateOne(myArray)
    return myArray

def rotateOne(myArray):
    for i in range(len(myArray) - 1):
        myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]


if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    print('Before Rotation:',myArray)
    print('After Rotation:',rotation(3, myArray))

    # OUTPUT:
    # Before Rotation: 0 1 2 3 4 5 6 7 8 9
    # After Rotation: 3 4 5 6 7 8 9 0 1 2
```

# Get missing number

<div class="code-head"><span>code</span>a3_findMissing.py</div>

```py

from Arrays import Array

def findMissing(myArray, n):
    n = n - 1
    totalSum = (n * (n + 1)) // 2
    for i in range(0, n):
        totalSum -= myArray[i]

    return totalSum

if __name__ == '__main__':
    myArray = Array(10)
    for i in range(len(myArray)):
        myArray.insert(i, i)
    myArray.delete(4, 4)
    print('Original Array:',myArray)
    print('Missing Element:', findMissing(myArray, len(myArray)))

    # OUTPUT:
    # Original Array: 0 1 2 3 5 6 7 8 9 0
    # Missing Element: 4
```

# Get missing number

<div class="code-head"><span>code</span>a4_odd_number_occurance.py</div>

```py
# Given an array of positive integers. All numbers occur even number of times except one
# number which occurs odd number of times. Find the number in O(n) time & constant space.

# XOR of all elements gives us odd occurring element. Please note that XOR of two elements
# is 0 if both elements are same and XOR of a number x with 0 is x.

# NOTE: This will only work when there is only one number with odd number of occurences.

def printOddOccurences(array):
    odd = 0

    for element in array:
        # XOR with the odd number
        odd = odd ^ element

    return odd

if __name__ == '__main__':
    myArray = [3, 4, 1, 2, 4, 1, 2, 5, 6, 4, 6, 5, 3]
    print(printOddOccurences(myArray))      # 4
```
# Check for pair sum

<div class="code-head"><span>code</span>a5_CheckForPairSum.py</div>

```py
# Given an array A[] of n numbers and another number x, determines whether or not there exist two elements
# in S whose sum is exactly x.

def checkSum(array, sum):
    # sort the array in ascending order
    # new changes : made use of Python's inbuilt Merge Sort method
    # Reason for such change : Worst case Time complexity of Quick Sort is O(n^2) whereas Worst Case Complexity of Merge Sort is O(nlog(n))
    array = sorted(array)

    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex < rightIndex:
        if (array[leftIndex] + array[rightIndex] ==  sum):
            return array[leftIndex], array[rightIndex]
        elif(array[leftIndex] + array[rightIndex] < sum):
            leftIndex += 1
        else:
            rightIndex += 1

    return False, False

##def quickSort(array):
##    if len(array) <= 1:
##        return array
##    pivot = array[len(array) // 2]
##    left = [x for x in array if x < pivot]
##    middle = [x for x in array if x == pivot]
##    right = [x for x in array if x > pivot]
##    return quickSort(left) + middle + quickSort(right)

if __name__ == '__main__':
    myArray = [10, 20, 30, 40, 50]
    sum = 80

    number1, number2 = checkSum(myArray, sum)
    if(number1 and number2):
        print('Array has elements:', number1, 'and', number2, 'with sum:', sum)
    else:
        print('Array doesn\'t have elements with the sum:', sum)

```

