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

            
