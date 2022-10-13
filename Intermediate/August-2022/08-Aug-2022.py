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
# Given an array A of N integers.

# Find the largest continuous sequence in a array which sums to zero.
# Brute force approach 
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        n = len(A)
        maxLen = 0

        for i in range(n):
            total = 0 
            for j in range(i, n):
                total += A[j]

                if total == 0:
                    currentSubarrayLen = j - i +1
                    maxLen = max(maxLen, currentSubarrayLen)
        
        return maxLen

# Optimized solution using hashmap / disctionary :
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        n = len(A)
        maxLen = 0
        prefixSum = [0] * n
        prefixSum[0] = A[0]
        frequencyMap = {}
        result = []

        for i in range(n):
            prefixSum[i] = prefixSum[i-1] + A[i]

        for i in range(n):
            if prefixSum[i] == 0:
                if i + 1 > len(result):
                    result = A[:i+1]

            if prefixSum[i] in frequencyMap:
                if i - frequencyMap[prefixSum[i]] > len(result):
                    result = A[frequencyMap[prefixSum[i]] + 1: i+1]
            else:
                frequencyMap[prefixSum[i]] = i
        return result

# 4 : Sub-array with 0 sum
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        prefixSum = [0]*n
        prefixSum[0] = A[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1] + A[i]

        mySet = set((prefixSum))

        if (len(mySet) < n) or (0 in mySet):
            return 1
        else:
            return 0


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

# 6 : Colorful Number
# Given a number A, find if it is COLORFUL number or not.

# If number A is a COLORFUL number return 1 else, return 0.

# What is a COLORFUL Number:

# A number can be broken into different contiguous sub-subsequence parts. 
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

# Example Input
# Input 1: A = 23 , Input 2: A = 236

# Example Output
# Output 1: 1, Output 2: 0

# Example Explanation
# Explanation 1:

#  Possible Sub-sequences: [2, 3, 23] where
#  2 -> 2 
#  3 -> 3
#  23 -> 6  (product of digits)
#  This number is a COLORFUL number since product of every digit of a sub-sequence are different. 
# Explanation 2:

#  Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
#  2 -> 2 
#  3 -> 3
#  6 -> 6
#  23 -> 6  (product of digits)
#  36 -> 18  (product of digits)
#  236 -> 36  (product of digits)
#  This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.

class Solution:
    def colorful(self, A):
        digitsList = [] #  Split A into list  example A = 236 -> [2,3,6]
        while A :
            digitsList.append(A % 10)
            A = A // 10
        
        digitsList = list(reversed(digitsList))
        
        n = len(digitsList)
        digitsProductSet = set() #Declared set to store product of digitslist

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= digitsList[j]

                if product in digitsProductSet:
                    return 0
                else:
                    digitsProductSet.add(product)
        return 1









