# 1 : Subarray with given sum

# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.

# If the answer does not exist return an array with a single element "-1".

# First sub-array means the sub-array for which starting index in minimum.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)

        left, right, currentSum = 0, 0, 0

        while left < n and right < n:

            if currentSum < B:
                currentSum += A[right]
                right += 1

            if currentSum > B:
                currentSum -= A[left]
                left += 1

            if currentSum == B:
                return(A[left:right])
        return [-1]
