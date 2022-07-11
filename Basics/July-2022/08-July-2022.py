# 1 : You are given an array A of integers of size N.

# Your task is to find the equilibrium index of the given array

# The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

# NOTE:

# Array indexing starts from 0.
# If there is no equilibrium index then return -1.
# If there are more than one equilibrium indexes then return the minimum index.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        arrLen = len(A)
        prefixSum = [0] * arrLen
        prefixSum[0] = A[0]

        for i in range(1, arrLen):
            prefixSum[i] = prefixSum[i-1] + A[i]

        count = 0
        minIndex = 0
        for i in range(arrLen):

            if i == 0:
                leftSum = 0
            else:
                leftSum = prefixSum[i - 1]

            rightSum = prefixSum[arrLen -1] - prefixSum[i]

            if leftSum == rightSum:
                count += 1
                minIndex = i
        
        return minIndex if count > 0 else -1

# 2 : You are given an integer array A of length N.
# You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
# For each query, you have to find the sum of all elements from L to R indices in A (1 - indexed).
# More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.

# Input 1:
# A = [1, 2, 3, 4, 5]
# B = [[1, 4], [2, 3]]

class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        bLen = len(B)
        aLen = len(A)

        prefixSum = []
        prefixSum.append(A[0])

        for i in range(1, aLen):
            prefixSum.append(prefixSum[i - 1] + A[i])

        finalOutput = [0]*bLen

        for i in range(bLen):
            start = B[i][0]
            end = B[i][1]

            if start == 1:
                finalOutput[i] = prefixSum[end - 1]
            else:
                result = prefixSum[end - 1] - prefixSum[start-1-1]
                finalOutput[i]  = result
                
        return(finalOutput)

            
