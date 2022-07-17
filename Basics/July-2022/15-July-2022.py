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




# 3 : Maximum Subarray Easy
# You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
# But the sum must not exceed B.


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def maxSubarray(self, A, B, C):

        maxSum = -9999

        for i in range(A):
            
            subArraySum = 0

            for j in range(i, A):

                subArraySum += C[j]

                if (subArraySum <= B) and (subArraySum > maxSum):
                    maxSum = subArraySum
            
                if maxSum < 0:
                    maxSum = 0

        return maxSum


# 4 : Subarray with least average
# Given an array of size N, find the subarray of size K with the least average.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arrLen = len(A)
        BElementsSum = sum(A[:B]) 
        leastSum = BElementsSum
        leastAvgSubArrayIndex = 0

        for i in range(B, arrLen):
            BElementsSum = BElementsSum + A[i] - A[i-B]
   
            if BElementsSum < leastSum:
                leastSum = BElementsSum
                leastAvgSubArrayIndex = i - B + 1

        return leastAvgSubArrayIndex



