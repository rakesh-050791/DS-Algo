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
            iRepetitions = (i+1) * (arrLen - i)

            iContributionInSubArraySum = (A[i] * iRepetitions)

            sumOfSubArraySum += iContributionInSubArraySum
        
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



# 5 : Counting Subarrays Easy
# Given an array A of N non-negative numbers and a non-negative number B,
# you need to find the number of subarrays in A with a sum less than B.
# We may assume that there is no overflow.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        noOfSubArrSumLessThenB = 0
       
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += A[j]

                if total < B:
                    noOfSubArrSumLessThenB += 1

        return noOfSubArrSumLessThenB


# 6 : Good Subarrays Easy
# Problem Description
# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        goodArrayCount = 0

        for i in range(n):
            subArraySum = 0
            subArrayLength = 0
            for j in range(i, n):
                subArraySum += A[j]
                subArrayLength = j - i + 1

                if (subArrayLength % 2 == 0) and  subArraySum < B:
                    goodArrayCount += 1
                elif (subArrayLength % 2 != 0) and  subArraySum > B:
                    goodArrayCount += 1
                    
        return goodArrayCount

# 7 : Alternating Subarrays Easy

# You are given an integer array A of length N comprising of 0's & 1's, and an integer B.

# You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.

# A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. 
# For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        subArrayLen = 2 * B + 1
        n = len(A)
        result = []
        noOfSubArrays = n-subArrayLen+1
        for i in range(0, noOfSubArrays):
            prev = -1
            is_alternating = 1
            for j in range(i, i+subArrayLen):
                if A[j] == prev:
                    is_alternating = 0
                    break;
                prev = A[j]
            if is_alternating == 1:
                result.append(i+B)
        return result










