# 1 : Special Subsequences "AG"
# You have given a string A having Uppercase English letters.

# You have to find how many times subsequence "AG" is there in the given string.

# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        totalNoOfG = 0 
        result = 0

        for i in range(n-1, -1, -1):
            if A[i] == 'G' :
                totalNoOfG += 1
            elif A[i] == 'A':
                result += totalNoOfG
        return(result%1000000007)


# 2 : Closest MinMax

# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

# and at least one occurrence of the minimum value of the array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        minIndex = -1
        maxIndex = -1
        result = n

        minVal = min(A)
        maxVal = max(A)

        if minVal == maxVal:
            return 1 
        
        for i in range(n - 1, -1, -1):
            if A[i] == minVal:
                minIndex = i
                if maxIndex != -1:
                    length = maxIndex - minIndex + 1
                    result = min(result, length)

            if A[i] == maxVal:
                maxIndex = i
                if minIndex != -1:
                    length = minIndex - maxIndex + 1
                    result = min(result, length)
        return result

# 3 : Bulb (Minimum no of switches required to turn on bulbs)

# A wire connects N light bulbs.

# Each bulb has a switch associated with it; however, due to faulty wiring, a switch also changes the state of all the bulbs to the right of the current bulb.

# Given an initial state of all bulbs, find the minimum number of switches you have to press to turn on all the bulbs.

# You can press the same switch multiple times.

# Note: 0 represents the bulb is off and 1 represents the bulb is on.

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        switchState = 1
        result = 0

        for i in range(len(A)):
            if switchState != A[i]:
                switchState = A[i]
                result += 1
        return result

# 4 : Leaders in an array

# Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

# An element is a leader if it is strictly greater than all the elements to its right side.

# NOTE:The rightmost element is always a leader.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        maxVal = A[n-1]
        result = []
        result.append(maxVal)

        for i in range(n-2, 0, -1):
            if A[i] > maxVal:
                maxVal = A[i]
                result.append(A[i])
        return result


# 5 :  Even Subarrays
# You are given an integer array A.

# Decide whether it is possible to divide the array into one or more subarrays of even length such that the first and last element of all subarrays will be even.

# Return "YES" if it is possible; otherwise, return "NO" (without quotes).
class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        arrLength = len(A)        
        if arrLength % 2 == 0 and A[0] % 2 == 0 and A[-1] % 2 == 0: return "YES"
        return "NO"









