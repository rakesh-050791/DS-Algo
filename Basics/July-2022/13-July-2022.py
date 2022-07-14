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



