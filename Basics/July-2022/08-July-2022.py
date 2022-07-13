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


# 3 : Given an array, arr[] of size N, the task is to find the count of array indices 
# such that removing an element from these indices makes the sum of even-indexed and odd-indexed 
# array elements equal.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        prefixSumEven = []
        prefixSumOdd = []

        prefixSumEven.append(A[0])
        prefixSumOdd.append(0)

        for i in range(1, n):
            if i % 2 == 0:
                prefixSumEven.append(prefixSumEven[i - 1] + A[i])
                prefixSumOdd.append(prefixSumOdd[i - 1])
            else:
                prefixSumOdd.append(prefixSumOdd[i - 1] + A[i])
                prefixSumEven.append(prefixSumEven[i - 1])

        count = 0
        for i in range(n):
            if i == 0:
                sumEven = 0 + (prefixSumOdd[n-1] - prefixSumOdd[i])
                sumOdd = 0 + (prefixSumEven[n-1] - prefixSumEven[i])
            else:
                sumEven = prefixSumEven[i-1] + (prefixSumOdd[n-1] - prefixSumOdd[i])
                sumOdd = prefixSumOdd[i-1] + (prefixSumEven[n-1] - prefixSumEven[i])
            
            if sumEven == sumOdd:
                count += 1
        return count

# 4 :Problem Description
# You are given an integer array A of size N.

# You have to pick B elements in total. Some (possibly 0) elements from left end of array A and some (possibly 0) from the right end of array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4, and array A contains 10 elements, then

# You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        curr_sum = sum(A[0:B])
        max_sum = curr_sum

        start = B - 1 
        end = - 1 
    
        for i in range(B):
            curr_sum = curr_sum - A[start] + A[end]

            if (max_sum < curr_sum):
                max_sum = curr_sum
                
            start -= 1
            end -= 1
        return max_sum

# 5 : Given an integer array A of size N. In one second, you can increase the value of one element by 1.

# Find the minimum time in seconds to make all elements of the array equal.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        minTime = 0

        maxElement = max(A)

        for i in range(len(A)):
            if A[i] != maxElement:
                minTime += (maxElement - A[i])
        return minTime





            
