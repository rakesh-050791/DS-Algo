# 1 : Max Sum Contiguous Subarray
# Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxSum = -9999
        sumOfEachSubarray = 0

        for i in range(len(A)):
            sumOfEachSubarray += A[i]

            if sumOfEachSubarray > maxSum:
                maxSum = sumOfEachSubarray
            
            if sumOfEachSubarray < 0:
                sumOfEachSubarray = 0
                
        return maxSum
