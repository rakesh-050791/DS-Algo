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