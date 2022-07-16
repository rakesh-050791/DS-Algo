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


# 2 : Sum of All Subarrays


# You are given an integer array A of length N.
# You have to find the sum of all subarray sums of A.
# More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
# A subarray sum denotes the sum of all the elements of that subarray.

class Solution:
    # @param A : list of integers
     # @return an long
    def subarraySum(self, A):
        sumOfSubArraySum = 0
        arrLen = len(A)

        for i in range(arrLen):
            subArraySum = (A[i] * (i+1) * (arrLen - i))
            sumOfSubArraySum += subArraySum
        
        return sumOfSubArraySum