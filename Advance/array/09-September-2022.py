# 1 : Max Sum Contiguous Subarray

# Find the contiguous non-empty subarray within an array, A of length N, with the largest sum.
# Example Input
# Input 1:

# A = [1, 2, 3, 4, -10] 

# Example Output
# Output 1:
# 10 

# Example Explanation
# Explanation 1:

#  The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

class Solution:
    def maxSubArray(self, A):
        n = len(A)
        currentSum = 0
        currentMax = float('-inf')

        for i in range(n):
            currentSum += A[i]
            currentMax = max(currentMax, currentSum)
            
            if currentSum < 0: currentSum = 0 
        return currentMax
