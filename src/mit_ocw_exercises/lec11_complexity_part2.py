# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:13:13 2016

@author: ericgrimson
"""

def bisect_search1(L, e):
    print('low: ' + str(L[0]) + '; high: ' + str(L[-1]))
    if L == []:
        return False
    elif len(L) == 1:
        return L[0] == e
    else:
        half = len(L)//2
        if L[half] > e:
            return bisect_search1(L[:half], e)
        else:
            return bisect_search1(L[half:], e)

def bisect_search2(L, e):
    def bisect_search_helper(L, e, low, high):
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bisect_search_helper(L, e, low, mid - 1)
        else:
            return bisect_search_helper(L, e, mid + 1, high)
    if len(L) == 0:
        return False
    else:
        return bisect_search_helper(L, e, 0, len(L) - 1)

testList = []
for i in range(100):
    testList.append(i)

print(bisect_search1(testList, 76))
print(bisect_search2(testList, 76))


def genSubsets(L):
    res = []
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    return smaller+new  # combine those with last element and those without



testSet = [1,2,3,4]
print(genSubsets(testSet))

print("\n--- Testing bisect_search1 ---")
print(bisect_search1([], 5))                  # False
print(bisect_search1([5], 5))                 # True
print(bisect_search1([1, 3, 5, 7, 9], 7))      # True
print(bisect_search1([1, 3, 5, 7, 9], 2))      # False
print(bisect_search1([1, 2, 3, 4, 5], 1))      # True
print(bisect_search1([1, 2, 3, 4, 5], 5))      # True

print("\n--- Testing bisect_search2 ---")
print(bisect_search2([], 5))                  # False
print(bisect_search2([5], 5))                 # True
print(bisect_search2([1, 3, 5, 7, 9], 7))      # True
print(bisect_search2([1, 3, 5, 7, 9], 2))      # False
print(bisect_search2([1, 2, 3, 4, 5], 1))      # True
print(bisect_search2([1, 2, 3, 4, 5], 5))      # True

print("\n--- Testing genSubsets ---")
print(genSubsets([]))                         # [[]]
print(genSubsets([1]))                        # [[], [1]]
print(genSubsets([1, 2]))                     # [[], [1], [2], [1, 2]]
print(genSubsets([1, 2, 3]))                  # All subsets of 3 elements
print(genSubsets([1, 2, 3, 4]))               # All subsets of 4 elements (16 subsets total)
