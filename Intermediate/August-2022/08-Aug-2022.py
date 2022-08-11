# 1 : Common Elements
# Given two integer arrays, A and B of size N and M, respectively. 
# Your task is to find all the common elements in both the array.

# NOTE:
# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        commonElements = {}

        for i in range(len(A)):
            if A[i] in commonElements:
                commonElements[A[i]] += 1
            else:
                commonElements[A[i]] = 1

        result = []
        
        for i in range(len(B)):
            if B[i] in commonElements and commonElements[B[i]] > 0:
                result.append(B[i])
                commonElements[B[i]] -= 1
        return result


# 2 : First Repeating element

# Given an integer array A of size N, find the first repeating element in it.

# We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

# If there is no repeating element, return -1.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        repeatingElements = {}

        for i in range(len(A)):
            if repeatingElements.get(A[i]) == None:
                repeatingElements[A[i]] = 1
            else:
                repeatingElements[A[i]] += 1
        
        for i in range(len(A)):
            if repeatingElements.get(A[i]) <= 1:
                continue
            else:
                return A[i]
        return -1

# 3 : Largest Continuous Sequence Zero Sum




 
# 5 : Shaggy and distances
# Shaggy has an array A consisting of N elements. We call a pair of distinct indices 
# in that array a special if elements at those indices in the array are equal.

# Shaggy wants you to find a special pair such that the distance between that pair is minimum. 
# Distance between two indices is defined as |i-j|. 
# If there is no special pair in the array, then return -1

# Using Dictionary 

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        minDiff = 10 ** 5
        mydict = {}

        for i in A:
            mydict[i] = -1
        
        for i in range(n):
            if mydict[A[i]] != -1:
                minDiff = min(minDiff, i - mydict[A[i]])
            else:
                mydict[A[i]] = i

        if minDiff == 10 ** 5:
            return -1
        else:
            return minDiff

# Using SET 

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        alreadyPresent = set()
        minDiff = 10**5

        for i in range(n):
            if A[i] in alreadyPresent:
                if i - A.index(A[i]) < minDiff:
                    minDiff = i - A.index(A[i])
            alreadyPresent.add(A[i])
        
        if  minDiff == 10**5:
            return -1
        else:
            return minDiff